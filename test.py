from dotenv import find_dotenv, load_dotenv
import os

load_dotenv(find_dotenv())
t = os.getenv('DUCKLING_PATH')
print(t)
