
"""
Module to load data from databases and create a one candidate dataset

This is just a sample code

Application specific dataset creation code should be written here
"""

import sys
sys.path.append("../")
import pandas as pd
import numpy as np
from helpers import ml_logger

def _load_dataset():
    return pd.read_csv("dummy_dataset/Train_Inpatientdata-1542865627584.csv")

def create_candidate_dataset():
    df = _load_dataset()
    ml_logger.info(f"Dataframe shape: {df.shape}")
    ml_logger.info(f"Dataframe columns: {df.columns}")
    # add a dummy target column for demo
    df['target_class'] = pd.Series(np.random.choice(a=[0,1],size=df.shape[0], replace=True))
    print(df.columns)
    return df

if __name__=="__main__":
    create_candidate_dataset()