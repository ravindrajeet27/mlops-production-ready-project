from dotenv import load_dotenv
import os

load_dotenv()

print("Current directory:", os.getcwd())
print("Exists:", os.path.exists(".env"))

with open(".env", "r") as f:
    print(f.read())