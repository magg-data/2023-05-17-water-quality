# utils.py

# --------------------
# useful headers
# --------------------
#import pandas as pd


# --------------------
# constants
# --------------------
# original data
PATH_DATA_ORG = "input/kc_swqi.csv"
# preliminary modified data
PATH_DATA = "input/kc_swqi_md.csv"
# processed dataset
PATH_DATA_PROCESSED = "input/kc_swqi_proc.csv"


# --------------------
# find missing data ####
# --------------------
# in: df Data frame
def find_missing(df):
    # count missing values
    missing_data = df.isnull()
    # False - means is not missing
    # True - means it is missing
    for column in missing_data.columns.values.tolist():
        print(column)
        print (missing_data[column].value_counts())
        print("")    
  
# -------------------
# percentage
# -------------------
def percentage(part, whole):
  return 100 * float(part)/float(whole)
          
        


