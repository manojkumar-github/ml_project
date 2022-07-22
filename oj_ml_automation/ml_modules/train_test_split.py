

def create_train_test_split(dataset, train_percent):
    """TODO: Stratified split
    Dummy code for the dataset train test split"""
    # shuffle the dataset
    dataset.sample(frac=1, inplace=True)
    train_indices = int(0.7 * dataset.shape[0])
    train_df = dataset[:train_indices]
    test_df = dataset[train_indices:]
    return train_df, test_df
