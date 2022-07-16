"""
Experiment runs
"""

import os
import argparse
from helpers import ml_logger, MLException
from training_pipeline import TrainingPipeline
from inference_pipeline import InferencePipeline


class Experiment:

    def __init__(self, name: str):
        self.experiment_name = self._check_and_create_experiement(exp_name=name)

    @staticmethod
    def _check_and_create_experiement(exp_name: str):
        """

        Args:
            exp_name:

        Returns:

        """
        ml_logger.info(f"\n\nValidating if the {exp_name} already exists\n\n")
        current_dir = os.path.abspath(os.getcwd())
        ml_logger.info(f"Current directory = {current_dir}")
        # handle if user inputs experiment name with spaces
        exp_name = "_".join(exp_name.split(" "))
        experiment_dir = os.path.join(os.path.join(current_dir, "experiment_runs"), exp_name)
        if not os.path.isdir(experiment_dir):
            ml_logger.info(f"{exp_name} experiment does not exist. Initiating it for the first time")
            os.mkdir(experiment_dir)
        else:
            ml_logger.info(f"{exp_name} already exists. Skipping the experiment run directory creation")
        return exp_name

    def run(self, pipeline_obj: [TrainingPipeline, InferencePipeline]):
        pipeline_obj.run()

    def run_config(self, config: dict):
        pass






