import prefect
from src.etl.extract import extract_data
from src.etl.load import save_processed
from src.etl.transform import transform_data

@prefect.flow
def solar_rank_pipeline():
    raw_dataframe = extract_data()
    transformed_data = transform_data(df=raw_dataframe)
    save_processed(transformed_data)

if __name__ in "__main__":
    solar_rank_pipeline()