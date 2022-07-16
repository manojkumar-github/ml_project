


import argparse
from ..experiment import Experiment

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Run OJ ML Automation experiment')
    parser.add_argument('--experiment-name', type=str, help='A meaningful unique experiment name')
    parser.add_argument("--training-pipeline-name", type="str",help='A meaningful training pipeline name.'
                                                                    'Example: RandomForest_Train70percent_Ntrees_100')
    parser.add_argument("--train-percent", type=float, help="A float value between 0.0 and 1.0. Exclude 0.0 but include"
                                                            " 1.0 i.e, in range (0.0,1.0]")
    args = parser.parse_args()
    experiment_obj = Experiment(args.experiment_name)
