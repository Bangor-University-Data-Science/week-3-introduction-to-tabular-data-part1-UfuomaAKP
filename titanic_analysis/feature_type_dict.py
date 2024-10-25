def create_feature_type_dict(df):
    """
    Classifies features into numerical (continuous or discrete) and categorical (nominal or ordinal).
    
    Args:
        df (pd.DataFrame): The Titanic dataset as a DataFrame.
    
    Returns:
        dict: A dictionary classifying features into numerical and categorical types.
    """
    feature_types = {
        'numerical': {
            'continuous': ['PassengerId', 'Age', 'Fare'],  # Fill with continuous numerical features
            'discrete': ['PassengerId', 'Survived', 'Sibsp', 'Parch']  # Fill with discrete numerical features
        },
        'categorical': {
            'nominal': ['Name', 'Sex']  # Fill with nominal categorical features
            'ordinal': ['Pclass']  # Fill with ordinal categorical features
        }
    }
    return feature_types
