"""
Experiment runs
"""

import os
import re
from datetime import datetime
from helpers import ml_logger, MLException
from ml_project.ml_project.oj_ml_automation.pipeline.training_pipeline import TrainingPipeline
from ml_project.ml_project.oj_ml_automation.pipeline.inference_pipeline import InferencePipeline


class Experiment:

    def __init__(self, name: str):
        self.experiment_name, self.experiment_dir = \
            self._check_and_create_experiement(exp_name=name)
        self.run_dir = self._create_run_dir()


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
        return exp_name, experiment_dir

    def _generate_run_name(self):
        """Run Name Date timestamp
            TODO: sha id
        """
        return datetime.now().strftime("%m_%d_%Y_%H_%M_%S")

    def _create_run_dir(self):
        run_name = self._generate_run_name()
        run_dir_name = f"{run_name}_{self.experiment_name}"
        run_dir = os.path.join(self.experiment_dir, run_dir_name)
        if not os.path.isdir(run_dir):
            ml_logger.info(f"{run_dir} run directory does not exist. Creating")
            os.mkdir(run_dir)
        else:
            raise MLException(f"{run_dir} run directory already exists. Aborting."
                              f"This cannot happen. Perhaps a minor bug in the framework."
                              f"Rerun the experiment to resolve this exception")
        return run_dir

    def run(self, pipeline_obj: [TrainingPipeline, InferencePipeline]):
        pipeline_obj.run(run_directory=run_dir)

    def run_config(self, config: dict):
        pass





