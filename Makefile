py = python3
pip = ${py} -m pip

pyrequirements:
	cat requirements.txt | grep "#" | sed 's/# //g' | $(py) || $(pip) install -r requirements.txt

test: pyrequirements
	$(py) -m mypy ina
	$(py) -m pytest .

format: pyrequirements
	$(py) -m black ina
	$(py) -m isort ina
