import pandas as pd

def generate_statistics(df: pd.DataFrame) -> dict:
    """ 
    Generate profiling statistics for each colomn

    Returns:
        dict: column_name -> metrics
    """
    profile = {}
    total_rows = len(df)
    
    for column in df.columns:
        col_data = df[column]
        
        profile[column] = {
            "data_type": str(col_data.dtype)
        }