import os


SECRET_KEY = os.getenv('SECRET_KEY', 'replace with generated key here')

SQLALCHEMY_DATABASE_URI = "sqlite:///project.db"

