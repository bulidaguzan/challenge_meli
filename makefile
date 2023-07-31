builder: 
	python3 -m pip install --upgrade pip
	python3 -m venv challenge_meli_env
	. challenge_meli_env/bin/activate
	pip3 install -r requirements.txt

deploy:builder
	

run:
	. challenge_meli_env/bin/activate
	uvicorn scripts.api.api:app --reload
 
