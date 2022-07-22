

from acceptance_criteria import compute_acceptance_criteria


def evaluate_model(model_results_path: str, acceptance_criteria:dict=None):
    """
    Compute metrics and acceptance criteria
    Evaluates on both train and test
    Select best sorted based on accuracy
    Returns:
        Load train_predictions.csv
        Load test_predictions.csv

        Load accpetance_critieria.json

        For stat in acceptance critier:
            Compute stats for train and test
            dump a csv with train and test sheets
            and assign a color as well
            Columns: Pipeline Name, Train Percent, Train_Acc, Test_Acc, Train_F1, Test_F1, COLOR
        TODO: In future bundle this run for multiple pipelines
    """
    pass
