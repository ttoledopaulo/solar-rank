from src import paths
import pandas as pd
import numpy as np
from src.etl.extract import extract_data

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    try: 
        df['eficiencia'] = df['geracao_solar_mwh'] / df['capacidade_kw']
        df['prioritaria'] = np.where(df['eficiencia'] > 0.12, "S", "N")
        print(f"[TRANSFORM] Dados transformados e colunas de métricas criadas.")
        return df
    
    except Exception as e:
        raise RuntimeError(f"Erro ao transformar os dados: {e}")