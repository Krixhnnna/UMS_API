# UMS API

FastAPI-based REST API for University Management System.

## Features

- User Management
- Timetable Management  
- Announcements
- Hostel Management
- Placement Portal

## Installation

```bash
# Clone the repo
git clone https://github.com/Krixhnnna/UMS_API

# Go to the repository
cd UMS_API

# Install virtualenv
pip install virtualenv

# Create Virtual Env
python -m venv venv

# Activate Virtual Env [Windows]
venv\Scripts\activate

# Activate Virtual Env [Linux]
source venv/bin/activate

# Install Dependencies
pip install -r requirements.txt

# Setting Up ENV
# Rename .env.example to .env and fill the required details.

# Start server
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Access
http://localhost:8000/docs
```

## Docker

```bash
# Using Docker
docker-compose build

# Setting Up ENV
# Rename .env.example to .env.docker and fill the required details.

# Start
docker-compose --env-file ./.env.docker up

# Access
http://localhost:8000/docs
```

## Testing

```bash
# To Run Test Case
pytest tests/test.py
```

## Production

Deployed on Vercel: https://ums-au3q0at17-krishnas-projects-e779cec0.vercel.app

## Author

**Krishna** - [@Krixhnnna](https://github.com/Krixhnnna) 