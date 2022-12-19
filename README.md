# Django-chatgpt-linebot-docker-SSL
# 一個Django docker平台，有著SSL認證的https網址，結合chatgpt和linebot的功能的聊天機器人平台


### [English](https://github.com/pyfbsdk59/Django-ChatGPT-linebot-docker-SSL/blob/main/README_en.md)
### [日本語](https://github.com/pyfbsdk59/Django-ChatGPT-linebot-docker-SSL/blob/main/README_jp.md)


#### 1. 初次上傳專案到github，請多包涵。初版沒有設置另外的.env檔案和環境變數。之後會改正。


#### 2. 本專案參考了以下前輩的方案改成製作，只針對剛學習Python, Django或Docker的朋友來佈置linebot在VPS上：

https://github.com/howarder3/GPT-Linebot-python-flask-on-vercel

#### 3. 可使用任何VPS建制，例如DigitalOcean, Linode或是vultr。 用ssh連入主機，輸入帳密後，

---
# 環境建制（有先建制了Makefile）


### Step 0: 取得免費的轉址服務，例如 https://www.noip.com/ 。每個月只要確認一次就可以繼續用。打入VPS分配取得的ip，自己選擇可用的網址。


### Step 1: 輸入以下指令（建制docker和pyenv環境） 
   
    make do1


### Step 2: 輸入以下多行的指令。一個一個複製貼上輸入。（一共有7個指令）

echo 'export LC_ALL=C.UTF-8' >> ~/.bashrc

echo 'export LANG=C.UTF-8' >> ~/.bashrc

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc

echo 'export PATH="$PYENV_ROOT/shims:$PATH"' >> ~/.bashrc

echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc

exec $SHELL


### Step 3: 輸入以下指令 （建制python環境且安裝docker-compose）

     make do2


### Step 4: 先建制自動認證SSL機制，請參考 https://github.com/evertramos/nginx-proxy-automation 專案來建制。現在的版本，我實際跑起來有點問題。按照此專案指示，輸入以下指令。


   #### 可改用2022/10/24的版本 https://github.com/evertramos/nginx-proxy-automation/tree/5b66f76f29a58f2928e6b1092c66869466a11146
    
    
    
    git clone --recurse-submodules https://github.com/evertramos/nginx-proxy-automation.git proxy 


   
### Step 5: 輸入以下指令啟動Nginx認證SSL服務。your_email@domain部份請改成到noip網站註冊的email。成功後會有3個container執行，可打入docker ps -a指令來確認。 


    cd proxy/bin && ./fresh-start.sh --yes -e your_email@domain --skip-docker-image-check

    
    
    
   
### Step 6: 輸入 cd ~ ，到主目錄，輸入以下指令下載本專案。

    git clone https://github.com/pyfbsdk59/Django-ChatGPT-linebot-docker-SSL.git
   

### Step 7: 輸入以下指令進入本專案目錄（已建制Makefile）。根目錄應該有proxy和Django-ChatGPT-linebot-docker-SSL兩個資料夾並列。

    cd Django-ChatGPT-linebot-docker-SSL




### Step 8: 輸入以下指令，開始建制本專案的容器，完成後會有兩個container，一個是nginx，另一個是Django。（記得先用nano指令修改app/config/資料夾中的settings.py的LINE access token和channel secret部份為自己的。app/myapp/資料夾中的views.py也要修改openai的api為自己的。還有也修改資料夾中的docker-compose.yml檔案中的VIRTUAL_HOST和LETSENCRYPT_HOST部份為自己的網址，LETSENCRYPT_EMAIL改為註冊noip的email。）

    make dcup
    

### Step 9: 輸入以下指令 ，同步Django模型

    make do4


### Step 10: 到LINE developer網站，Webhook URL輸入為 https://xxxx.xxx.xxx/callback 。測試是否成功，若顯示success! ，成功就可順利運行。（openai若超過一定額度，可能要綁信用卡號才能繼續使用。）

------
### Line和openai api設置請參考： https://github.com/howarder3/GPT-Linebot-python-flask-on-vercel
