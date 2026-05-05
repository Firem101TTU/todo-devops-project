install:
	python3 -m pip install -r requirements.txt

test:
	python3 -m pytest

run:
	python3 todo.py

docker-build:
	docker build -t todo-devops-project .

docker-run:
	docker run -it --rm todo-devops-project
