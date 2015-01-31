PYTHON = $(shell which python 2.7)
ENV = $(CURDIR)/env

virtual-env:
	virtualenv --python=$(PYTHON) $(ENV)

env: virtual-env
	$(ENV)/bin/pip install -r requirements/base.txt

db:
	- initdb /usr/local/var/postgres -E utf8
	- mkdir -p ~/Library/LaunchAgents
	cp /usr/local/Cellar/postgresql/9.4.0/homebrew.mxcl.postgresql.plist ~/Library/LaunchAgents/
	- launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist
	- createdb dfunct
	make migrate

kaboomdb:
	- dropdb dfunct
	make db

migrate:
	$(ENV)/bin/python manage.py makemigrations funner
	$(ENV)/bin/python manage.py migrate

run:
	$(ENV)/bin/python manage.py runserver 1337

shell:
	$(ENV)/bin/python manage.py shell

clean:
	rm -rf $(ENV)
