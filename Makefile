init:
	pip install -r requirements.txt

create_user_db:
	docker exec --user postgres cafe_db /bin/sh -c "createuser cafe -s && createdb -U cafe cafe"

create_cache_table:
	docker exec cafe_py /bin/sh -c "python manage.py createcachetable" 

migrate_db:
	docker exec cafe_py /bin/sh -c 'python manage.py makemigrations'
	docker exec cafe_py /bin/sh -c 'python manage.py migrate'

cov_test:
	coverage run manage.py test

cov_report:
	coverage report

build:
	docker-compose build

build_no_cache:
	docker-compose build --no-cache

create_proxy:
	docker network create proxy

up:
	docker-compose up -d

up_no_d:
	docker-compose up

restart:
	docker-compose restart

collectstatic:
	docker exec cafe_py /bin/sh -c "python manage.py collectstatic --noinput"

frontend_prod:
	cd ~/cafe_programmation/frontend && yarn build && cd .. && $(MAKE) collectstatic

bash_nginx:
	docker exec -ti cafe_nginx bash

bash_web:
	docker exec -ti cafe_py bash

bash_db:
	docker exec -ti cafe_db bash

npm_build:
	cd frontend
	npm run build

freeze:
	pip freeze > requirements.txt