#This is a simulation of urls.py

import os

print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
SITE_ROOT = os.path.join(BASE_DIR,'site')
print(SITE_ROOT)
