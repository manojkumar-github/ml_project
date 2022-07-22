
"""
Module to have preprocessing related code like
dropping rows with NaN values
Duplicate values
Application related preprocessing activities
"""

def preprocess_dataset(input_dataset):
    # dummy code to drop empty
    input_dataset.dropna(inplace=True)
    print(input_dataset.shape)
    return input_dataset