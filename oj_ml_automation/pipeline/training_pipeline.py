#!/usr/bin/env python3
#@author: Manoj Kumar Putchala


#import sys
#sys.path.append("../")
from oj_ml_automation.ml_modules.data_creation import create_candidate_dataset
from oj_ml_automation.ml_modules.data_preprocessing import preprocess_dataset
from oj_ml_automation.ml_modules.feature_transformer import create_training_features
from oj_ml_automation.ml_modules.feature_transformer import create_test_inference_features
from oj_ml_automation.ml_modules.train_test_split import create_train_test_split
from oj_ml_automation.helpers import  MLException, ml_logger
from oj_ml_automation.ml_modules.model_training import train_model
from oj_ml_automation.ml_modules.model_inference import infer_model
from oj_ml_automation.ml_modules.model_evaluation import evaluate_model


class TrainingPipeline:
    """
    Current version will be functions pipelined

    In future steps can be implemented

    For now it is dataframe centric design
    """
    def __init__(self, name: str=None, training_percent=0.7, acceptance_criteria=None):
        """

        Args:
            name:
        """
        self.pipeline_name = name
        self.training_percent = training_percent
        if self.pipeline_name is None:
            # create a dummy pipeline name
            ml_logger.info("Creating dummy pipeline name")
            # TODO:
        if self.training_percent > 0.0 and self.training_percent<= 1.0:
            ml_logger.info(f"Valid value {self.training_percent} passed for training_percent"
                           f" in training pipeline")
        else:
            raise MLException(f"Invalid value {self.training_percent} passed for training_percent."
                              f"Allowed values are in (0.0, 1.0]")

    def run(self, run_directory:str, acceptance_criteria:dict=None):
        dataset = create_candidate_dataset()
        preprocessed_dataset = preprocess_dataset(input_dataset=dataset)
        target_column_name = 'target_class'
        train_dataset, test_dataset = create_train_test_split(preprocessed_dataset, self.training_percent)
        training_features = create_training_features(train_dataset, run_directory)
        testing_features = create_training_features(test_dataset, run_directory)
        trained_model_saved_path = train_model(training_features, target_column_name, run_directory)
        # save both train and test predictions
        infer_model(trained_model_saved_path, training_features, run_directory)
        infer_model(trained_model_saved_path, testing_features, run_directory)
        evaluate_model(run_directory, acceptance_criteria)







