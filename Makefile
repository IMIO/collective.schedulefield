VENV_FOLDER=.venv

.PHONY: help  # List phony targets
help:
	@cat "Makefile" | grep '^.PHONY:' | sed -e "s/^.PHONY:/- make/"

.PHONY: install  # Install development environment
install: $(VENV_FOLDER)/bin/buildout
	$(VENV_FOLDER)/bin/buildout

.PHONY: start  # Start Zope instance
start: bin/instance
	bin/instance fg

.PHONY: clean  # Clean development environment
clean:
	rm -r $(VENV_FOLDER) bin .tox .coverage .installed.cfg coverage.xml develop-eggs eggs forest.dot forest.json node_modules parts

$(VENV_FOLDER)/bin/buildout: $(VENV_FOLDER)/bin/pip
	$(VENV_FOLDER)/bin/uv pip install -r requirements.txt

$(VENV_FOLDER)/bin/pip:
	uv venv --seed -p python3.12
	$(VENV_FOLDER)/bin/pip3.12 install uv

bin/instance: $(VENV_FOLDER)/bin/buildout
	$(VENV_FOLDER)/bin/buildout
