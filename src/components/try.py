from src.components.data_injestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.components.pipeline.inference_pipeline import InferencePipeline


if __name__ == "__main__":
    # obj = DataIngestion()
    # train_data_path, test_data_path = obj.initiate_data_ingestion()

    # data_trainsformation = DataTransformation()
    # train_arr, test_arr, processor_obj_path = (
    #     data_trainsformation.initiate_data_transformation(
    #         train_data_path, test_data_path
    #     )
    # )
    # print(test_arr[0])
    # model = ModelTrainer()
    # model_report = model.initiate_model_training(train_arr, test_arr)
    # print(model_report)

    inference = InferencePipeline()
    data = {
        "Age": [34],
        "BusinessTravel": ["Travel_Rarely"],
        "DailyRate": [629],
        "Department": ["Research & Development"],
        "DistanceFromHome": [27],
        "Education": ["College"],
        "EducationField": ["Medical"],
        "EnvironmentSatisfaction": ["Very High"],
        "Gender": ["Female"],
        "HourlyRate": [95],
        "JobInvolvement": ["High"],
        "JobLevel": ["Entry Level"],
        "JobRole": ["Research Scientist"],
        "JobSatisfaction": ["Medium"],
        "MaritalStatus": ["Single"],
        "MonthlyIncome": [2311],
        "MonthlyRate": [5711],
        "NumCompaniesWorked": [2],
        "OverTime": ["No"],
        "PercentSalaryHike": [15],
        "PerformanceRating": ["Excellent"],
        "RelationshipSatisfaction": ["Very High"],
        "StandardHours": [80],
        "StockOptionLevel": ["No Stock Options"],
        "TotalWorkingYears": [9],
        "TrainingTimesLastYear": [3],
        "WorkLifeBalance": ["Better"],
        "YearsAtCompany": [3],
        "YearsInCurrentRole": [2],
        "YearsSinceLastPromotion": [1],
        "YearsWithCurrManager": [2],
    }
    prediction = inference.predict(data)
    print(prediction)
