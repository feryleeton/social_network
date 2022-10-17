import environ
import os

env = environ.Env()
environ.Env.read_env()

# PROJECT SETUP
SECRET_KEY = env('SECRET_KEY')
DEBUG = os.getenv("DEBUG", 'False').lower() in ('true', '1', 't')