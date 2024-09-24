# Local application run

## run application in dev mode
```bash
python manage.py runserver --settings=wish_list.settings.dev
```



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