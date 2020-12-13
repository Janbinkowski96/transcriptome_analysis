import os
from IPython.display import display

import pandas as pd
from tqdm import tqdm

def load_from_dir(path: str, suffix: str, verbose=1) -> list:
    """Function to load all xlsx/csv files from directory"""
    list_of_files = os.listdir(path)
    
    suffix_files = [file_name for file_name in list_of_files if file_name.endswith(suffix)]
    names = [name.split(".")[0] for name in suffix_files]
    dfs = {}
    
    for file, name in tqdm(zip(suffix_files, names)):
        file_path = os.path.join(path, file)
        if suffix == "xlsx":
            df = pd.read_excel(file_path, index_col=0)
        else:
            df = pd.read_csv(file_path, index_col=0)
        if verbose:
            display(df.describe(), df.shape)
        
        dfs.update({name: df})
    
    return dfs

def save_data(dfs: list, names: list, path: str) -> None:
    for df, name in zip(dfs, names):
        file_path = os.path.join(path, name)
        df.to_csv(file_path)
