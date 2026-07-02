# from us_visa.logger import logging 

# from us_visa.exception import UsvisaException   

# # logging.info("welcome to the us visa project")

# import sys

# try:
#     a = 2/0
# except Exception as e:
#     raise UsvisaException(e, sys)

import os 
mongo_db_url = os.getenv("MONGODB_URL")
print(mongo_db_url)
