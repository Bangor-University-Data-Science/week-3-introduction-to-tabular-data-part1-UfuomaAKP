import pandas as pd

def display_unique_values(df: pd.Dataframe, categorical_features: list) -> dict:
    categorical_cols = df.select_dtypes (include=['object', 'category', 'boolean']).columns.to_list()
    """
    Displays unique values for each categorical feature in the DataFrame.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        categorical_features (list): List of categorical feature names.
    
    Returns:
        dict: A dictionary where keys are feature names and values are the unique values.
    """
    pass  # Implement the logic here
df = pd.DataFrame(columns=['Name', 'Sex', 'Ticket', 'Cabin', 'Embarked'])
df[['Name'], ['Sex'], ['Ticket'], ['Cabin'], ['Embarked']].unique() 