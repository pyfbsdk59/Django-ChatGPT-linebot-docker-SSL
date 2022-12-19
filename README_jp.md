# Django-chatgpt-linebot-docker-SSL
#SSL付けのURLとChatGPTとlinebotの機能を組み合わせた Django docker プラットフォーム



#### 1. ここにプロジェクトをアップロードするのはこれが初めてです。バグでごめんなさい。環境変数が .env ファイルやその他の場所に設定されていません。これは将来修正される予定です

------
#### 2. このプロジェクトは、Python、Django、Docker の初心者向け、DigitalOcean、Linode、Vultr などの VPS にラインボットを展開できるようにすることを目的としています。

https://github.com/howarder3/GPT-Linebot-python-flask-on-vercel
------
#### 3. ssh経由でVPSサーバーにアクセスしてから、アカウント/パスワードを入力すると、次のことがします...

------
# Makefileを含む環境構築

------
### Step 0: noip のような無料のDNSホスト名サービスを利用できます。サインアップ後、VPS の IP を入力し、独自の URL アドレスを選択するだけで、わずか 1 か月の確認のみで済みます。


------
### Step 1: 次のコマンドを入力して、Docker と pyenv をインストールしてください
    
    make do1

------
### Step 2: 次の 7 つのコマンドをコピーして貼り付け、ターミナルで 1 つずつ ENTER を押してください

echo 'export LC_ALL=C.UTF-8' >> ~/.bashrc

echo 'export LANG=C.UTF-8' >> ~/.bashrc

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc

echo 'export PATH="$PYENV_ROOT/shims:$PATH"' >> ~/.bashrc

echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init -)"\nfi' >> ~/.bashrc

exec $SHELL

------
### Step 3: 次のコマンドを入力して Python 環境を構築し、docker-compose をインストールします

     make do2

------
### Step 4: まず、https://github.com/evertramos/nginx-proxy-automation の指示に従って Auto-SSL Nginx サービスを構築します。ただし、現在のコミットには問題があるため、2022/10/24 のバージョンを使用できます。


   #### 可改用2022/10/24的版本 https://github.com/evertramos/nginx-proxy-automation/tree/5b66f76f29a58f2928e6b1092c66869466a11146
    
    
    
    git clone --recurse-submodules https://github.com/evertramos/nginx-proxy-automation.git proxy 


------    
### Step 5: 以下のコマンドでSSL認定サービスを開始してください。 noip などの Web サイトで your_email@domain を登録済みのメール アドレスに変更してください。その後、3 つのコンテナーが実行されます。 docker ps -a と入力して確認できます。


    cd proxy/bin && ./fresh-start.sh --yes -e your_email@domain --skip-docker-image-check

    
    
    
------    
### Step 6: cd ~ と入力し、ルート フォルダーに戻ります。次のコマンドを入力して、プロジェクトをダウンロードします。

    git clone https://github.com/pyfbsdk59/Django-ChatGPT-linebot-docker-SSL.git
   
------   
### Step 7: 次のコマンドを入力して、Makefile を含むこのプロジェクトのフォルダーに入ります。 「proxy」と「Django-ChatGPT-linebot-docker-SSL」という 2 つのフォルダーがあるはずです。

    cd Django-ChatGPT-linebot-docker-SSL



------
### Step 8: 次のコマンドを入力して、プロジェクトのコンテナーのビルドを開始してください。 Nginx と Django サービスを表す 2 つのコンテナーが実行されます。 app/config/ フォルダー内の settings.py を編集することを忘れないでください。ファイルにLINEアクセストークンとチャンネルシークレットを追加してください。また、app/myapp/ フォルダー内の views.py を編集し、OPENAPI サービスの API を追加する必要があります。 docker-compose.yml ファイルも編集する必要があります。 VIRTUAL_HOST と LETSENCRYPT_HOST は、ラインボット サービスの URL になります。 LETSENCRYPT_EMAIL は、noip 登録済みメールのような DNS サービスになります。

    make dcup
    
    
------
### Step 9: 次のコマンドを入力して、Djangoのappとmodelを同期させてください。
    make do4

------
### Step 10: LINE 開発者の Web サイトにアクセスし、Webhook URLに https://xxxx.xxx.xxx/callback を入力します。これをテストして、「success!」と表示されれば、django Web サイトは正常に動作しています。 OPRNAPIを一定時間使用した後、クレジットカード番号をOPENAIアカウントに追加する必要がある場合があります。

------
### LINE developerの設定方法とOPENAI apiの取得方法はこちらで確認できます。 https://github.com/howarder3/GPT-Linebot-python-flask-on-vercel
