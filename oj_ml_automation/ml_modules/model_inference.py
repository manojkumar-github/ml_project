"""
load saved model

predict_prob()
"""


import joblib

def infer_model(model_saved_path:str, input_features, target_path:str):
    """
    jsons and all in one sheet
    Returns:
    Compute both predict and predict_prob
    Compute metrics
    Loads save model
    """
    reloaded_model = joblib.load(model_saved_path)
    integer_predictions = reloaded_model.predict(input_features)
    float_predictions = reloaded_model.predict_prob(input_features)
    # save integer and float predictions to target path
    return None