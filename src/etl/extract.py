from src.paths import DATA_DIR
import pandas as pd
from os import makedirs

def extract_data(arquivo: str = "energia_solar.csv") -> pd.DataFrame:
    try:
        path_arquivo = DATA_DIR / "raw/energia_solar.csv"
        df = pd.read_csv(path_arquivo)

        colunas_esperadas = ['cidade','geracao_solar_mwh','capacidade_kw']
        if not set(colunas_esperadas).issubset(df.columns):
            colunas_faltando = set(colunas_esperadas) - set(df.columns)
            raise ValueError(f"Arquivo raw faltando as colunas: {colunas_esperadas} (recebido: {df.columns})")
        else:
            print(f"[EXTRACT] Dataframe extraido do arquivo {path_arquivo}")
            return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo nao encontrado {path_arquivo}")
    except Exception as e:
        raise RuntimeError(f"Erro ao extrair dados {e}")