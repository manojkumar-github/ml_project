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

    def run_using_training_pipeline(self, training_pipeline_obj: TrainingPipeline):
        training_pipeline_obj.run()

    def run_using_inference_pipeline(self, inference_pipeline_obj: InferencePipeline):
        inference_pipeline_obj.run()

    def run_using_training_pipelines_config(self, training_config_json):
        pass

    def run_using_inference_pipelines_config(self, inference_config_json):
        pass


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Run OJ ML Automation experiment')
    parser.add_argument('--experiment-name', type=str, help='A meaningful unique experiment name')
    parser.add_argument("--use-task", type="str", choices=['training_pipeline', 'inference_pipeline',
                                                      'training_config', 'testing_config'],
                                                        help="Indicate whether the task is training "
                                                                              "or testing")
    parser.add_argument("--task-name")
    args = parser.parse_args()
    experiment_obj = Experiment(args.experiment_name)
    if args.use_task == "training_pipeline":
        training_pipeline_object = TrainingPipeline()
        experiment_obj.run_using_training_config()

    elif args.use_task == "infer":
        # covers test and validationas well
    else:
        raise MLException(f"Invalid choice {args.task} used for the argument task. Valid values are"
                          f"either 'train' or 'infer'")





