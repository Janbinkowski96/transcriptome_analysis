import pandas as pd
import os
from tqdm import tqdm

def load_from_dir(path: str, suffix: str) -> list:
    """Function to load all xlsx/csv files from directory"""
    list_of_files = os.listdir(path)
    
    suffix_files = [file_name for file_name in list_of_files if file_name.endswith(suffix)]    
    dfs = []
    
    for file in tqdm(suffix_files):
        file_path = os.path.join(path, file)
        if suffix == "xlsx":
            file = pd.read_excel(file_path, index_col=0)
        else:
            file = pd.read_csv(file_path, index_col=0)
        dfs.append(file)
        
    return dfs

def save_data(dfs: list, names: list, path: str) -> None:
    for df, name in zip(dfs, names):
        file_path = os.path.join(path, name)
        df.to_csv(file_path)
