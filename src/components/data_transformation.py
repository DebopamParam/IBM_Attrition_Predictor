from dataclasses import dataclass
import logging
import numpy as np
import os, sys
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder, OrdinalEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer, KNNImputer
from src.components.fieldsinfo_dataclass import FieldsInfo
from src.exception import CustomException
from src.utils import save_object


@dataclass
class DataTransformationConfig:
    preprocessor_obj_filepath: str = os.path.join("artifacts", "preprocessor.pkl")


class DataTransformation:
    def __init__(self) -> None:
        self.config = DataTransformationConfig()

    def get_data_transformer_obj(self):
        try:
            fields_info = FieldsInfo()
            numerical_features = fields_info.numerical_columns
            categorical_features = fields_info.categorical_columns

            ordinal_feature_mappings = list(
                fields_info.ordinal_column_mappings.values()
            )
            ordinal_features = list(fields_info.ordinal_column_mappings.keys())

            numerical_pipeline = Pipeline(
                steps=[
                    ("imputer", KNNImputer(n_neighbors=10, weights="uniform")),
                    ("scaler", StandardScaler()),
                ]
            )
            categorical_pipeline = Pipeline(
                steps=[
                    ("imputer", KNNImputer(n_neighbors=10, weights="uniform")),
                    ("onehot", OneHotEncoder(handle_unknown="ignore")),
                ]
            )
            # print("Ordinal feature mappings : ", ordinal_feature_mappings)
            # print("Ordinal features : ", ordinal_features)

            ordinal_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    (
                        "ordinal",
                        OrdinalEncoder(categories=ordinal_feature_mappings),
                    ),
                ]
            )

            preprocessor = ColumnTransformer(
                transformers=[
                    ("num", numerical_pipeline, numerical_features),
                    ("cat", categorical_pipeline, categorical_features),
                    ("ord", ordinal_pipeline, ordinal_features),
                ]
            )

            return preprocessor

        except Exception as e:
            raise CustomException(e, sys) from e

    def initiate_data_transformation(
        self, train_path: str, test_path: str
    ) -> tuple["np.ndarray", "np.ndarray", "str"]:
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Read train and test data completed")

            logging.info("Obtaining preprocessing object")

            preprocessing_obj = self.get_data_transformer_obj()

            target_column = "Attrition"  # 'Attrition' is the target column
            input_features_train_df = train_df.drop(columns=[target_column], axis=1)
            target_feature_train_df = train_df[target_column]

            input_features_test_df = test_df.drop(columns=[target_column], axis=1)
            target_feature_test_df = test_df[target_column]

            # Convert the target column Yes/No to 1/0
            target_feature_train_df = np.where(target_feature_train_df == "Yes", 1, 0)
            target_feature_test_df = np.where(target_feature_test_df == "Yes", 1, 0)

            logging.info("Fitting the preprocessing object")

            ip_feature_train_arr = preprocessing_obj.fit_transform(
                input_features_train_df
            )
            ip_feature_test_arr = preprocessing_obj.transform(input_features_test_df)

            train_arr = np.c_[ip_feature_train_arr, np.array(target_feature_train_df)]
            test_arr = np.c_[ip_feature_test_arr, np.array(target_feature_test_df)]

            logging.info("Data Transformation Successful")

            save_object(
                file_path=self.config.preprocessor_obj_filepath, obj=preprocessing_obj
            )

            return (
                train_arr,
                test_arr,
                self.config.preprocessor_obj_filepath,
            )
        except Exception as e:
            raise CustomException(e, sys) from e
