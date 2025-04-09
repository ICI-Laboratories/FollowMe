# FollowMe - Daily Activity Tracker

A Streamlit web application that helps users track their daily activities, set reminders, and provide AI-powered insights - all while keeping data local and private.
---
### Features
- Google Authentication: Secure login using Google accounts
- Activity Tracking: Record and monitor your daily activities
- Privacy-Focused: All data stays on your local machine
- AI-Powered: (Coming soon) Get personalized insights and recommendations

- Prerequisites
Python 3.9 or higher
A Google Cloud account for authentication setup

### Installation
- Clone this repository:

git clone https://github.com/ICI-Laboratories/FollowMe.git
cd FollowMe

- Install the required dependencies:

pip install -r requirements.txt

Set up Google Authentication:

Go to the Google Cloud Console

Create a new project

Configure the OAuth consent screen

Create OAuth 2.0 credentials for a Web Application

Add authorized redirect URIs (e.g., http://localhost:8501/oauth2callback)

Configure your authentication credentials:

Copy .streamlit/secrets.toml.example to .streamlit/secrets.toml

Fill in the credentials from your Google Cloud Console

Generate a random cookie secret (can use Python's secrets.token_hex())

### Running the Application

Start the Streamlit server:

streamlit run app.py

The application will be available at http://localhost:8501.

Project Structure
your-repository/
├── .gitignore                # Git ignore file
├── .streamlit/
│   ├── secrets.toml          # Authentication credentials (not committed)
│   └── secrets.toml.example  # Example secrets file
├── requirements.txt          # Project dependencies
├── app.py                    # Main application entry point
├── utils/
│   └── auth_utils.py         # Authentication utilities
└── pages/
    └── dashboard.py          # Dashboard page

License
MIT License

