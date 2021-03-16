# KipleX Engineering Challenge Solution
The following repository contains code for a demo fo kiplex challenge with backend and frontend implementations

It is currently still work in progress with the following elements to be implemented:

- Average Loop calculation & API (backend)
- Filtering of track section data by track type (frontend)

## Prerequistes
- Python 3.7
- Mysql

## Installation

### Frontend
- Navigate to frontend folder : `cd frontend`
- Run : `npm install`
- Start frontend server : `npm run start`

### Backend
- Navigate to backend folder : `cd backend`
- Setup python virtualenv (Optional) : `python -m venv venv`
- Use virtualenv (Optional) : `source ./venv/Scripts/activate`
- Install python requirements : `pip install -r requirements.txt`
- Set configurations in [config file](/./backend/config.py)
- Start flask server : `flask run`