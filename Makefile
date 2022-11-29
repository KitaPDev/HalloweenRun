all:
	python3 -m venv ./venv && source ./venv/bin/activate && pip3 install pygame

play:
	python3 main.py