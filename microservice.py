from app import create_app
from flask import Flask
import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.flaskenv')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

flask_app: Flask = create_app(os.getenv('FLASK_ENV') or 'default')
