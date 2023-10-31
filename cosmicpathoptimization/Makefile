DOCS = docs
UML = uml

.PHONY: all check_types py_test local_test kattis_test auto_style flaker coverage create_doc_folder create_docs create_uml clean_up

all: check_types py_test local_test kattis_test auto_style flaker coverage create_doc_folder create_docs create_uml clean_up
	@echo "All done!"

check_types:
ifeq ($(shell which mypy), ) # no mypy??
	@echo "mypy not installed"
	pip install mypy
endif
	mypy main.py
	@echo "Static type check done."

auto_style:
ifeq ($(shell which autopep8), ) # no autopepe???
	@echo "autopep8 not installed"
	pip install autopep8
endif
	autopep8 --in-place --aggressive --aggressive main.py
	autopep8 --in-place --aggressive --aggressive main_test.py
	@echo "Autopep8 done."

flaker:
ifeq ($(shell which flake8), ) # no flake8??
	@echo "flake8 not installed"
	pip install flake8
endif
	flake8 main.py
	flake8 main_test.py
	@echo "Flake8 check done."

py_test:
ifeq ($(shell which pytest), ) # no pytest??
	@echo "pytest not installed"
	pip install pytest
endif
	pytest main.py main_test.py
	@echo "Local Tests using pytest done."


coverage:
ifeq ($(shell which coverage), ) # no coverage??
	@echo "coverage not installed"
	pip install coverage
endif
	coverage run -m pytest main.py main_test.py
	coverage report -m
	coverage html -d htmlcov
	@echo "coverage html generated"


local_test:
	python main.py < data/1.in > data/output.tmp
	diff data/output.tmp data/1.ans
	@echo "Local Kattis test completed"

kattis_test:
	kattis -f main.py -p cosmicpathoptimization
	@echo "Kattis test completed."

create_doc_folder:
	@mkdir -p $(DOCS)
	@echo "docs folder created"
	@mkdir -p $(UML)
	@echo "uml folder created"

create_docs: create_doc_folder
ifeq ($(shell which pdoc3), ) #no pdoc???
	@echo "pdoc3 not installed"
	pip install pdoc3
endif
	pdoc --force -o $(DOCS) main.py # creates .md docs inside docs
	pdoc --force --html -o $(DOCS) main.py  # creates html docs inside docs
	@echo "html docs created and saved in $(DOCS)"

create_uml: create_doc_folder
ifeq ($(shell which pylint), )
	@echo "pylint not installed"
	pip install pylint
endif
	pyreverse -o png -d uml main.py
	@echo "uml created"

clean_up:
	rm -rf __pycache__
	rm -rf .pytest_cache
	rm -rf .mypy_cache
	rm -rf .coverage
	@echo "clean up done"