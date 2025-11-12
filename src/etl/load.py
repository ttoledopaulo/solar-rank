from src import paths
import pandas as pd
from os import makedirs
from src.etl.transform import transform_data
from prefect import task, get_run_logger

@task
def save_processed(df: pd.DataFrame, nome_arquivo_processado: str = "energia_solar_processed.csv") -> bool:
    try:
        logger = get_run_logger()
        makedirs(paths.DATA_DIR / "processed", exist_ok=True)
        logger.info("[LOAD] Diretorio processed foi criado")
        path_arquivo = paths.DATA_DIR / f"processed/{nome_arquivo_processado}"
        arquivo_processado = df.to_csv(path_arquivo, index=False)
        logger.info(f"[LOAD] Arquivo processado salvo em: {path_arquivo}")
        return True
    except Exception as e:
        logger.error(f"Erro ao salvar arquivo processado: {e}")
        raise RuntimeError(f"Erro ao salvar arquivo processado: {e}")
