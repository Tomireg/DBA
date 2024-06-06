URL: https://dba-jxuy.onrender.com/

Description:
This is a python flask web application. The app connects to SQL to create and manage a database of users. User information can be added and then managed with the help of the app.

Deploying through render.com:
The app uses render.com to deploy from the connected github repository https://github.com/Tomireg/DBA.

Settings on render:
Set region to Frankfurt
Set an environment variable for the python version.
PYTHON VERSION 3.12.2
Set repository: https://github.com/Tomireg/DBA
Set branch to main.
Set root directory to flask.
Add build command: pip install -r requirements.txt
Add start command: gunicorn app:app
Set auto-deploy to YES.
