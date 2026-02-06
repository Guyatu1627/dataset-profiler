import pandas as pd

def load_dataset(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas Dataframe
    
    Why this function exists:
    - Keep data ingestion separeted from the business logic
    - Makes the pipleline easier to test and extend
    """
    
    try:
        df = pd.read_csv(file_path)
        return df
    
    except Exception as e:
        # Data engineering prefer loud errors over silent corruption 
        raise RuntimeError(f"Failed to load dataset: {e}")
        