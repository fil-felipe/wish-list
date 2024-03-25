# Local application run

## run application from terminal
```bash
python .\app\manage.py runserver --settings=wish_list.settings_dev
```

## run application as local docker
``
docker-compose up -d --build
``

# Python code checks

## Black
This module verify if code style is correct
``bash
python -m black app -l 120
``

## Flake
Verify general rules of the code logic. Exceptions are covered within .flake8 file stored within app directory
``bash
python -m flake8 app
``