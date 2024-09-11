import sys
import yaml
import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from src.exception import CustomException
from src.utils import load_object


class InferenceConfig:
    def __init__(self) -> None:
        config_path = "config/config.yaml"
        try:
            with open(config_path, "r") as file:
                self.config_yaml = yaml.safe_load(file)
            self.preprocessor_path = self.config_yaml["data_transformation"][
                "processor_obj_path"
            ]
            self.model_path = self.config_yaml["model"]["model_path"]
        except Exception as e:
            raise CustomException(e, sys) from e

    def get_preprocessor(self) -> ColumnTransformer:
        try:
            preprocessor = load_object(self.preprocessor_path)
            return (
                preprocessor  # Type hinting ensures it's treated as ColumnTransformer
            )
        except Exception as e:
            raise CustomException(e, sys) from e

    def get_model(self):
        try:
            model = load_object(self.model_path)
            return model
        except Exception as e:
            raise CustomException(e, sys) from e


class InferencePipeline:
    def __init__(self):
        self.config = InferenceConfig()
        self.preprocessor = self.config.get_preprocessor()
        self.model = self.config.get_model()

    def predict(self, data: dict) -> np.ndarray:
        try:
            data = pd.DataFrame.from_dict(data)
            transformed_data = self.preprocessor.transform(data)
            prediction = self.model.predict_proba(transformed_data)[0,1]
            return prediction * 100
        except Exception as e:
            raise CustomException(e, sys) from e
