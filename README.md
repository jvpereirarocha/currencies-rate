## About the project
This project get data from an API that handle with currencies rate tax with specified intervals of date from those data

## Project Technologies
### Backend
- Python 3.11
- Django 4.2
- SQLite
- Pydantic


### Instructions to execute
1. Create a new virtualenv with Python 3.11.
2. Use the command `python -m venv <folder_path>/<env_name>` if you're using Linux. If you're using Windows, see [this link](https://python.land/virtual-environments/virtualenv)
3. After create, run the activate command to active the virtualenv. In Linux the command is `source <folder_path>/<env_name>/bin/activate`. Check the link below if you're using Windows
4. Create a new `.env` file in the project root (See the env_example file and change with your configs)
5. In the project root, run the command `pip install -r requirements.txt`. This command will install all of the project requirements
6. Now, just run the command `python manage.py runserver <your_allowed_host>`. Ex: My ALLOWED_HOST in the .env file is `http://localhost:8080` so I'm running `python manage.py runserver 0.0.0.0:8080`. Check yours and just play with the API :)
