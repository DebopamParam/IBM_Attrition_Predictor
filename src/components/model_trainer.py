import os, sys
import numpy as np
from dataclasses import dataclass
from xgboost import XGBClassifier
from sklearn.metrics import classification_report

from src.exception import CustomException
from src.utils import save_object


@dataclass
class ModelTrainerConfig:
    model_filepath: str = os.path.join("artifacts", "model.pkl")
    model_report_filepath: str = os.path.join("artifacts", "model_report.txt")


class ModelTrainer:
    def __init__(self) -> None:
        self.config = ModelTrainerConfig()

    def initiate_model_training(self, train_arr, test_arr):
        try:

            X_train, y_train, X_test, y_test = (
                train_arr[:, :-1],
                train_arr[:, -1],
                test_arr[:, :-1],
                test_arr[:, -1],
            )
            best_hyperparameters = {
                "subsample": 0.7,
                "reg_lambda": 20,
                "reg_alpha": 3,
                "n_estimators": 300,
                "min_child_weight": 1,
                "max_depth": 3,
                "learning_rate": 0.3,
                "gamma": 0.6,
                "colsample_bytree": 0.8,
            }
            # Train the XGBoost model with the best hyperparameters
            best_xgb_model = XGBClassifier(
                **best_hyperparameters,
                eval_metric=["auc"],
            )
            best_xgb_model.fit(
                X_train,
                y_train,
                verbose=False,
            )

            save_object(
                self.config.model_filepath,
                best_xgb_model,
            )

            # Predict on the validation set
            y_test_pred = best_xgb_model.predict_proba(X_test)[:, 1]
            y_test_pred = np.where(y_test_pred > 0.3, 1, 0)
            # Generate classification report
            report = classification_report(y_test, y_test_pred)

            return report

        except Exception as e:
            raise CustomException(e, sys) from e
