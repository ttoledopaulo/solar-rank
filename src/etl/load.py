from src import paths
import pandas as pd
from os import makedirs
from src.etl.transform import transform_data

def save_processed(df: pd.DataFrame, nome_arquivo_processado: str = "energia_solar_processed.csv"):
    try:
        makedirs(paths.DATA_DIR / "processed", exist_ok=True)
        print("[LOAD] Diretorio processed foi criado")
        path_arquivo = paths.DATA_DIR / f"processed/{nome_arquivo_processado}"
        arquivo_processado = df.to_csv(path_arquivo, index=False)
        print(f"[LOAD] Arquivo processado salvo em: {path_arquivo}")
        return arquivo_processado
    except Exception as e:
        raise RuntimeError(f"Erro ao salvar arquivo processado: {e}")
