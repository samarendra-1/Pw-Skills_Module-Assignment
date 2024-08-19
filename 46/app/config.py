# app/config.py
import os

class Config:
    SECRET_KEY = 'your_secret_key'
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'instance/uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
