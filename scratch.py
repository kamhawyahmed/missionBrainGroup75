# print(os.environ['auth_token'])

from dotenv import load_dotenv

load_dotenv(".env") #loads environ vars from .venv file (hidden on mac bc start with .)
import os
print(os.environ.get('auth_token')) #can interact with environ vars as usual in rest of code