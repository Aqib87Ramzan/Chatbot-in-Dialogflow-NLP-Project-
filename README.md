Directory structure
===================
1) backend: Contains Python FastAPI backend code
2) db: contains the dump of the database. you need to import this into your MySQL db by using MySQL workbench tool
3) dialogflow_assets: this has training phrases etc. for our intents
4) frontend: website code

Install these modules
======================

1) pip install mysql-connector
2) pip install fastapi[all]

OR just run pip install -r backend/requirements.txt to install both in one shot

To start fastapi backend server
================================
1. Go to backend directory in your command prompt
2. Run this command: uvicorn main:app --reload along with ngrok.

ngrok for https tunneling
================================
1. To install ngrok, go to https://ngrok.com/download and install ngrok version that is suitable for your OS
2. Extract the zip file and place ngrok.exe in a folder i.e backend.
3. Open windows command prompt, go to that folder and run this command: ngrok http 8000

NOTE: ngrok can timeout. you need to restart the session if you see session expired message.

Why need ngrok?
================================
For testing of our dialogflow, http request is not secure, so we need ngrok because of its https request.

