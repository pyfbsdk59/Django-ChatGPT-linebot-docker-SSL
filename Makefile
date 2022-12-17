do1:
	apt-get update

	apt-get install -y docker.io

	apt-get install curl git bzip2 -y

	curl https://pyenv.run | bash
do2:
	pyenv install miniconda3-4.3.30

	pyenv global miniconda3-4.3.30

	pip install docker-compose
dcup:
    docker-compose up -d --build
do4:
	docker-compose run python sh -c "python3 manage.py makemigrations"

	docker-compose run python sh -c "python3 manage.py migrate"
	
dcdown:
    docker-compose down
    


