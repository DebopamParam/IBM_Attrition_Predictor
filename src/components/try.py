from src.components.data_injestion import DataIngestion
from src.components.data_transformation import DataTransformation


if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()

    data_trainsformation = DataTransformation()
    train_arr, test_arr, processor_obj_path = (
        data_trainsformation.initiate_data_transformation(
            train_data_path, test_data_path
        )
    )