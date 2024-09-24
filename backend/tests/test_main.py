import pytest
from fastapi.testclient import TestClient
from backend.main import app
from src.components.pipeline.inference_pipeline import InferencePipeline

# Create a TestClient instance
client = TestClient(app)


# Mock the InferencePipeline for testing
class MockInferencePipeline:
    def prediction(self, data):
        return 88.17481398582458


# Replace the real InferencePipeline with the mock
app.dependency_overrides[InferencePipeline] = MockInferencePipeline


def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Status": "Server is Live"}


def test_prediction():
    # Sample data matching the EmployeeDataStructure schema
    sample_data = {
        "Age": 20,
        "BusinessTravel": "Travel_Rarely",
        "DailyRate": 50,
        "Department": "Research & Development",
        "DistanceFromHome": 1,
        "Education": "College",
        "EducationField": "Medical",
        "EnvironmentSatisfaction": "Low",
        "Gender": "Female",
        "HourlyRate": 95,
        "JobInvolvement": "Low",
        "JobLevel": "Entry Level",
        "JobRole": "Research Scientist",
        "JobSatisfaction": "Medium",
        "MaritalStatus": "Single",
        "MonthlyIncome": 231,
        "MonthlyRate": 57,
        "NumCompaniesWorked": 2,
        "OverTime": "Yes",
        "PercentSalaryHike": 15,
        "PerformanceRating": "Excellent",
        "RelationshipSatisfaction": "Low",
        "StandardHours": 80,
        "StockOptionLevel": "No Stock Options",
        "TotalWorkingYears": 9,
        "TrainingTimesLastYear": 3,
        "WorkLifeBalance": "Bad",
        "YearsAtCompany": 1,
        "YearsInCurrentRole": 2,
        "YearsSinceLastPromotion": 1,
        "YearsWithCurrManager": 2,
    }
    response = client.post("/predict/", json=sample_data)
    assert response.status_code == 200, f"Error: {response.json()}"
    assert response.json() == {"prediction": 88.17481398582458}


if __name__ == "__main__":
    pytest.main()
