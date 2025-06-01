"""This module will handle database Connections
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
load_dotenv()
#is used to load environment variables from a .env file into your Python program.
#Looks for a file named .env in the current working directory (or the path you specify).
# Reads the variables in that file.
# Adds them to the environment variables of your program (i.e., os.environ).
DATABASE_URL = os.getenv('DATABASE_URL') #the name  DATABASE_URL is the name where you have  .env
engine = create_engine(DATABASE_URL)
SessionLocal= sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
#fastapi dev main.py

#means that you're trying to connect to a MySQL database
#using an authentication method (sha256_password or caching_sha2_password) that requires the cryptography package.
#pip install cryptography


