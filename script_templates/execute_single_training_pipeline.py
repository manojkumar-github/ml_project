
import sys
sys.path.append("../")

import argparse
from oj_ml_automation.experiment import Experiment
from oj_ml_automation.pipeline import TrainingPipeline, InferencePipeline


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Run OJ ML Automation experiment')
    parser.add_argument('--experiment-name', type=str, help='A meaningful unique experiment name')
    parser.add_argument("--version", type=float, help='Valid float version of experiment. Examples "1.0" or "1.1"')
    #parser.add_argument("--training-pipeline-name", type="str",help='A meaningful training pipeline name.'
     #                                                               'Example: RandomForest_Train70percent_Ntrees_100')
    parser.add_argument("--train-percent", type=float, help="A float value between 0.0 and 1.0. Exclude 0.0 but include"
                                                            " 1.0 i.e, in range (0.0,1.0]")
    parser.add_argument("--acceptance-criteria-file-path", type=str, help="Provide acceptance criteria json file path."
                                                                     "Refer to config_templates/acceptance_criteria.json")
    args = parser.parse_args()
    experiment_obj = Experiment(name=args.experiment_name, version=args.version)
    training_pipeline_obj = TrainingPipeline(name=args.training_pipeline_name, training_percent=args.train_percent,
                                             acceptance_criteria=args.acceptance_criteria_file_path)
    #experiment_obj.run(training_pipeline_obj)
    # --experiment_name TestTrainingExperiment1 --version 1.0 --training_pipeline_name RandomForest --train_percent 0.7 --acceptance_criteria_path "foo"