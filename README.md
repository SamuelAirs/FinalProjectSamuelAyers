### INF601 - Advanced Programming in Python
### Samuel Ayers
### Final Project


# Project Title

TaskFlows

## Description

This project create a simple reminder application using Django. Users are able to register for an account, and once they log in to their account, 
it is easy to create, edit, and send emails for your detailed reminders. This project was completed as part of Advanced Programming in Python, 
but I initially conceptualized the idea in and entrepreneurship class, and I worked on a prototype in my introduction to programming class.

## Getting Started

### PIP install instructions

`pip install -r requirements.txt`

### Setting up the API

1. [Create a Google Cloud project](https://developers.google.com/workspace/guides/create-project)
2. [Enable the gmail API](https://console.cloud.google.com/flows/enableapi?apiid=gmail.googleapis.com)
3. Configure the OAuth consent screen and add yourself as a test user.
*  In the Google Cloud console, go to Menu menu > APIs & Services > OAuth consent screen.
*  For User type select Internal, then click Create.
*  Complete the app registration form, then click Save and Continue.
4. Authorize Credentials for a desktop application
* In the Google Cloud console, go to Menu menu > APIs & Services > Credentials.
* Click Create Credentials > OAuth client ID.
* Click Application type > Desktop app.
* In the Name field, type a name for the credential. This name is only shown in the Google Cloud console.
* Click Create. The OAuth client created screen appears, showing your new Client ID and Client secret.
* Click OK. The newly created credential appears under OAuth 2.0 Client IDs.
* Save the downloaded JSON file as credentials.json, and move the file to the FinalProjectSamuelAyers/taskFlows directory.
  
### How to run
`python quickstart.py`
* This will open up a window that will allow you to grant permission for the application to send reminders via your gmail.

`cd taskflows`

`python manage.py migrate`

`python manage.py runserver`
  
## Authors
Samuel Ayers

## Sources/Inspiration
* ChatGPT
* [Gmail API Quickstart](https://developers.google.com/gmail/api/quickstart/python)
* [Django Registration Tutorial](https://learndjango.com/tutorials/django-login-and-logout-tutorial)
## Version History
* 0.1 (Initial Release)



