#!/usr/bin/env python3
#@author: Manoj Kumar Putchala



from ..ml_modules.data_creation import create_dataset
from ..ml_modules.data_preprocessing import preprocess_dataset
from ..ml_modules.feature_transformer import create_training_features
from ..ml_modules.train_test_split import create_train_test_split
from ..helpers import  MLException, ml_logger
from ..ml_modules.model_training import train_model
from ..ml_modules.model_inference import infer_model
from ..ml_modules.model_evaluation import evaluate_model


class TrainingPipeline:
    """
    Current version will be functions pipelined

    In future steps can be implemented

    For now it is dataframe centric design
    """
    def __init__(self, training_percent=0.7, name: str=None):
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

    def _create_target_path(self, run_directory=None):
        """

        Returns:

        """
        if run_directory is None:
            # create pipeline directory in current working directory
            pass
        else:
            # create pipeline directory in given run directory
            pass

    def run(self, run_directory=None, acceptance_criteria:dict=None):
        target_path = self._create_target_path(run_directory=run_directory)
        dataset = create_dataset()
        preprocessed_dataset = preprocess_dataset(input_dataset=dataset)
        train_dataset, test_dataset = create_train_test_split(preprocessed_dataset, self.training_percent)
        training_features = create_training_features(train_dataset, target_path)
        testing_features = create_training_features(test_dataset, target_path)
        trained_model_saved_path = train_model(training_features, target_path)
        infer_model(trained_model_saved_path, training_features, target_path, predict_prob)
        infer_model(trained_model_saved_path, testing_features, target_path, predict_prob)
        evaluate_model(target_path, acceptance_criteria)







