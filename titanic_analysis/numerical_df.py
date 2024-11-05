import pandas as pd

def get_numerical_df(df: pd.DataFrame, numerical_features: list) -> pd.DataFrame:
    """
    Creates a DataFrame containing only numerical features.
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
        numerical_features (list): List of numerical feature names.
    
    Returns:
        pd.DataFrame: DataFrame containing only numerical features.
    """
    pass  # Implement the logic here
df = pd.DataFrame
numerical_cols = df.select_dtypes (include= ['int', 'float']).columns.to_list()