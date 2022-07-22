

"""
Custom code to perform feature tranformation
Sometimes training feature transformer should be saved in the run path
to be reused during inference pointing to same run
"""

def create_training_features(preprocessed_train_dataset, run_path):
    """
        {'variables: []
        'values': [[], [], [], []]}

        Save feature models or TODO: save to feature store
    """
    important_columns = ['InscClaimAmtReimbursed',  'ClmAdmitDiagnosisCode',
       'DeductibleAmtPaid',  'DiagnosisGroupCode']
    # TODO: Implement the code
    return preprocessed_train_dataset[important_columns]



def create_test_inference_features(preprocessed_train_dataset, run_path):
    pass