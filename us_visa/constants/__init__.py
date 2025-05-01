# We need this file becuas ewe will use constant names in entire project and value of these constants can be changed form this file

import os 
from datetime import date

DATABASE_NAME = "US_VISA"
COLLECTION_NAME = "visa_data"

# import urllib.parse
# encoded_username = urllib.parse.quote_plus("kshitijdegg")
# encoded_password = urllib.parse.quote_plus("Welcome@2021")
# MONGODB_URL_KEY= f'mongodb+srv://{encoded_username}:{encoded_password}@cluster0.u3wbf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

MONGODB_URL_KEY = "MONGODB_URL"     # Set MONGODB_URL in environment variables - "export MONGODB_URL="mongodb+srv://kshitijdegg:Welcome%402021@cluster0.u3wbf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0""

PIPELINE_NAME:str = "usvisa"
ARTIFACTS_DIR:str = "artifact"
FILE_NAME="usvisa.csv"
TRAIN_FILE_NAME="train.csv"
TEST_FILE_NAME="test.csv"

MODEL_FILE_NAME:str = "model.pkl"


"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"     # inside artifact folder, we will create data_ingestion folder where data from MongoDB will be stored
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2      # 80% for train; 20% for test


