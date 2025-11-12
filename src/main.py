from src.etl.extract import extract_data
from src.etl.load import save_processed
from src.etl.transform import transform_data



if __name__ in "__main__":
    raw_dataframe = extract_data()
    transformed_data = transform_data(df=raw_dataframe)
    save_processed(transformed_data)

