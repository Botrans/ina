py = python3
pip = ${py} -m pip

pyrequirements:
	cat requirements.txt | grep "#" | sed 's/# //g' | $(py) || $(pip) install -r requirements.txt

test: pyrequirements
	# $(py) -m mypy risu --ignore-missing-imports
	$(py) -m pytest .

format: pyrequirements
	$(py) -m black risu
	$(py) -m isort risu
