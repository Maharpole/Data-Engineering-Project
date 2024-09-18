# import libraries
import pandas as pd
import configparser
from sqlalchemy import create_engine, text 

#set up configparser
config = configparser.ConfigParser()
config.read('config.ini')
user = config.get('database', 'username')
password = config.get('database', 'password')

# define postgres connection
# connection_string  = f'postgresql://{user}:{password}@localhost/postgres'

# #create engine that connects to db 
# engine = create_engine(connection_string)
# connection = engine.connect() 

#determine csv file path
#csv_file_path = <csv_file_path>