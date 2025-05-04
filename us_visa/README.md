## Workflow -
Pipeline: 
After running data_ingestion(1st component), output is train.csv and test.csv, which are my artifacts
These train.csv and test.csv are passed as input to 2nd component (Data_validation)
Output of Data_Validation is sent to Data_Transformation
Output of Data_Transformation is sent to Model_Training
Output of Model_Training is sent to Model_Evaluation
Output of Model_Evaluation is sent to Model_Pusher

config_entity will manipulate constants; 

Data ingestion -  
## Workflow - 
1) constants - us_visa/constants folder has __init.py__ constructor file 
2) entity - us_visa/config_entity (to manipulate us_visa/constants)
3) components
4) pipeline

Set 'export MONGODB_URL="mongodb+srv://kshitijdegg:Welcome%402021@cluster0.u3wbf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"' environment variable before running code.


|artifact
    - TIMESTAMP
       | -data_ingestion - 
            - ingested-
                | - train.csv
                | - test.csv
            - feature_store-
                | - usvisa.csv


DataValidation - 
## Workflow - 
1) constants - us_visa/constants folder has __init.py__ constructor file 
2) entity - us_visa/config_entity (to manipulate us_visa/constants)
3) components
4) pipeline
5) Main file
