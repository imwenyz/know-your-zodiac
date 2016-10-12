# Statement for enabling the development environment
DEBUG = True

# Place your own mysql
MYSQL_URL = 'mysql+pymysql://zodiac:unsafepwd@94.237.28.44/zodiac'

# Alternative database, SQLite
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLITE_URL = 'sqlite:///' + os.path.join(BASE_DIR, 'deploy/database.db')

# Define the database
SQLALCHEMY_DATABASE_URI = SQLITE_URL
SQLALCHEMY_TRACK_MODIFICATIONS = True
DATABASE_CONNECT_OPTIONS = {}
