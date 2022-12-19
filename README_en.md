# Django-chatgpt-linebot-docker-SSL
# A Django docker platform combined with SSL URL function and ChatGPT linebot function<br> 


#### 1. This is the first time to upload a project here. Sorry for the bugs. Environment variables are not set in .env file or other places, which will be fixed in the future.

------
#### 2. This project is aimed to help beginners of Python, Django or Docker to deploy their linebot on any VPS like DigitalOcean, Linode, or Vultr according to several people.

https://github.com/howarder3/GPT-Linebot-python-flask-on-vercel
------
#### 3. You can access your VPS server with ssh. After you enter your account/password, you can...

------
#Environment Building with Makefile included

------
### Step 0: You can get free DNS hostname service like noip. After signing up, you just type in your VPS ip and choose your own URL address with only one-month confirmation.


------
### Step 1: Please type in the following word to install Docker and pyenv.
    
    make do1

------
### Step 2: Please copy and paste the following 7 commands and press ENTER one by one in you terminal.

echo 'export LC_ALL=C.UTF-8' >> ~/.bashrc

echo 'export LANG=C.UTF-8' >> ~/.bashrc

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc

echo 'export PATH="$PYENV_ROOT/shims:$PATH"' >> ~/.bashrc

echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc

exec $SHELL

------
### Step 3: Type in the following command to build Python environment and install docker-compose.

     make do2

------
### Step 4: Build Auto-SSL Nginx service according to  https://github.com/evertramos/nginx-proxy-automation 。However, there is something wrong with the current commit, so you can use the version of 2022/10/24 commit. 


   #### 2022/10/24 https://github.com/evertramos/nginx-proxy-automation/tree/5b66f76f29a58f2928e6b1092c66869466a11146
    
    
    
    git clone --recurse-submodules https://github.com/evertramos/nginx-proxy-automation.git proxy 


------    
### Step 5:  Please start the certified SSL service with the following command. Please change your_email@domain into your registered email on websites like noip. After that, there will be three containers running. You can type in docker ps -a to confirm that.


    cd proxy/bin && ./fresh-start.sh --yes -e your_email@domain --skip-docker-image-check

    
    
    
------    
### Step 6: type in cd ~ , and go back to the root folder. Type in the following command to download the project.

    git clone https://github.com/pyfbsdk59/Django-ChatGPT-linebot-docker-SSL.git
   
------   
### Step 7: Type in the following command to get into the folder of this project, which contains a Makefile. There should be two folders called "proxy" and "Django-ChatGPT-linebot-docker-SSL".

    cd Django-ChatGPT-linebot-docker-SSL



------
### Step 8: Please type in the following command and start to build the containers of the project. There will be two containers running which represent Nginx and Django service. Remember to edit the settings.py inside the folder of app/config/. Please add your LINE access token and channel secret to the file. You should also edit the views.py inside the folder of app/myapp/ and add the api of OPENAPI service. The docker-compose.yml file should also be edited. VIRTUAL_HOST and LETSENCRYPT_HOST will be your linebot service URL. LETSENCRYPT_EMAIL will be your DNS service like noip registered email.

    make dcup
    
    
------
### Step 9: Please type in the following command, and make Django app and model sync.
    make do4

------
### Step 10: Go to LINE developer website, and you type in https://xxxx.xxx.xxx/callback in your Webhook URL. You can test it, and if it shows "success!", your django website is working fine. You may have to add your CREDIT CARD number to your OPENAI account after you use the api for certain time.

------
### You can see how to set up line and get OPENAI api here. https://github.com/howarder3/GPT-Linebot-python-flask-on-vercel
