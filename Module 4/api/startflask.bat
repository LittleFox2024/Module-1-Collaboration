@ECHO OFF

REM Make sure you are in the right dir before starting this!
REM Use "cd <dir>"

REM Env. Variables
set FLASK_APP=application.py
set FLASK_ENV=development

REM Start the server...
ECHO Starting Flask...
flask run