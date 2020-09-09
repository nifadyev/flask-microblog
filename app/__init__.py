from flask import Flask

app = Flask(__name__)

# Importing here is workaround to circular imports
from app import routes
