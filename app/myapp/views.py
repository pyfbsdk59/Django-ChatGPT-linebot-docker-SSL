from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextMessage




from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction

import openai


line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)

from django.conf import settings
	
openai.api_key = "" #引號中填入你的open ai的api key
#os.getenv("OPENAI_API_KEY")


#import os
	
chat_language = "zh" #os.getenv("INIT_LANGUAGE", default = "zh")
	
MSG_LIST_LIMIT = 20 #int(os.getenv("MSG_LIST_LIMIT", default = 20))
LANGUAGE_TABLE = {
	  "zh": "哈囉！",
	  "en": "Hello!"
	}
class Prompt:
	    def __init__(self):
	        self.msg_list = []
	        self.msg_list.append(f"AI:{LANGUAGE_TABLE[chat_language]}")
	    
	    def add_msg(self, new_msg):
	        if len(self.msg_list) >= MSG_LIST_LIMIT:
	            self.remove_msg()
	        self.msg_list.append(new_msg)
	
	    def remove_msg(self):
	        self.msg_list.pop(0)
	
	    def generate_prompt(self):
	        return '\n'.join(self.msg_list)	
	
class ChatGPT:
    def __init__(self):
        self.prompt = Prompt()
        self.model = "text-davinci-003" #os.getenv("OPENAI_MODEL", default = "text-davinci-003")
        self.temperature = 0.9 #float(os.getenv("OPENAI_TEMPERATURE", default = 0))
        self.frequency_penalty = 0 #float(os.getenv("OPENAI_FREQUENCY_PENALTY", default = 0))
        self.presence_penalty = 0.6 #float(os.getenv("OPENAI_PRESENCE_PENALTY", default = 0.6))
        self.max_tokens = 240 #int(os.getenv("OPENAI_MAX_TOKENS", default = 240))
	
    def get_response(self):
        response = openai.Completion.create(
	            model=self.model,
	            prompt=self.prompt.generate_prompt(),
	            temperature=self.temperature,
	            frequency_penalty=self.frequency_penalty,
	            presence_penalty=self.presence_penalty,
	            max_tokens=self.max_tokens
	        )
        print(response['choices'][0]['text'].strip())
        print(response)
        return response['choices'][0]['text'].strip()
	
    def add_msg(self, text):
        self.prompt.add_msg(text)

chatgpt = ChatGPT()

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
            ##############3
                    user_message = event.message.text        
                    chatgpt.add_msg(f"HUMAN:{user_message}?\n")

                    
            
                    print(user_message)
                    #response = chatbot.get_chat_response((user_message), output="text")
                    reply_msg = chatgpt.get_response() #.replace("AI:", "", 1)
                    #chatgpt.add_msg(f"AI:{reply_msg}\n")
                    
                    
                    print(reply_msg) 
                    # Get opengpt's response
                    #openai_response = response["message"]
                    # Send response to user
                    line_bot_api.reply_message(
                        event.reply_token,
                        TextSendMessage(text=reply_msg)
                        )
            ##########################

                     
                                              
                
        return HttpResponse()

    else:
        return HttpResponseBadRequest()


