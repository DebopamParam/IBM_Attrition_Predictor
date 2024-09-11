from pydantic import BaseModel
from typing import Literal


class PredictionModel(BaseModel):
    prediction: float

class EmployeeDataStructure(BaseModel):
    Age: int
    BusinessTravel: Literal["Travel_Rarely", "Travel_Frequently", "Non-Travel"]
    DailyRate: int
    Department: Literal["Sales", "Research & Development", "Human Resources"]
    DistanceFromHome: int
    Education: Literal["Below College", "College", "Bachelor", "Master", "Doctor"]
    EducationField: Literal[
        "Life Sciences",
        "Other",
        "Medical",
        "Marketing",
        "Technical Degree",
        "Human Resources",
    ]
    EnvironmentSatisfaction: Literal["Low", "Medium", "High", "Very High"]
    Gender: Literal["Male", "Female"]
    HourlyRate: int
    JobInvolvement: Literal["Low", "Medium", "High", "Very High"]
    JobLevel: Literal[
        "Entry Level", "Junior Level", "Mid Level", "Senior Level", "Executive Level"
    ]
    JobRole: Literal[
        "Sales Executive",
        "Research Scientist",
        "Laboratory Technician",
        "Manufacturing Director",
        "Healthcare Representative",
        "Manager",
        "Sales Representative",
        "Research Director",
        "Human Resources",
    ]
    JobSatisfaction: Literal["Low", "Medium", "High", "Very High"]
    MaritalStatus: Literal["Single", "Married", "Divorced"]
    MonthlyIncome: int
    MonthlyRate: int
    NumCompaniesWorked: int
    OverTime: Literal["Yes", "No"]
    PercentSalaryHike: int
    PerformanceRating: Literal["Low", "Good", "Excellent", "Outstanding"]
    RelationshipSatisfaction: Literal["Low", "Medium", "High", "Very High"]
    StandardHours: int
    StockOptionLevel: Literal[
        "No Stock Options",
        "Low Stock Options",
        "Medium Stock Options",
        "High Stock Options",
    ]
    TotalWorkingYears: int
    TrainingTimesLastYear: int
    WorkLifeBalance: Literal["Bad", "Good", "Better", "Best"]
    YearsAtCompany: int
    YearsInCurrentRole: int
    YearsSinceLastPromotion: int
    YearsWithCurrManager: int


if __name__ == "__main__":
    # Example employee data dictionary
    employee_data = {
        "Age": 34,
        "BusinessTravel": "Travel_Rarely",
        "DailyRate": 629,
        "Department": "Research & Development",
        "DistanceFromHome": 27,
        "Education": "College",
        "EducationField": "Medical",
        "EnvironmentSatisfaction": "Very High",
        "Gender": "Female",
        "HourlyRate": 95,
        "JobInvolvement": "High",
        "JobLevel": "Entry Level",
        "JobRole": "Research Scientist",
        "JobSatisfaction": "Medium",
        "MaritalStatus": "Single",
        "MonthlyIncome": 2311,
        "MonthlyRate": 5711,
        "NumCompaniesWorked": 2,
        "OverTime": "No",
        "PercentSalaryHike": 15,
        "PerformanceRating": "Excellent",
        "RelationshipSatisfaction": "Very High",
        "StandardHours": 80,
        "StockOptionLevel": "No Stock Options",
        "TotalWorkingYears": 9,
        "TrainingTimesLastYear": 3,
        "WorkLifeBalance": "Better",
        "YearsAtCompany": 3,
        "YearsInCurrentRole": 2,
        "YearsSinceLastPromotion": 1,
        "YearsWithCurrManager": 2,
    }

    # Validate and parse the data
    employee = EmployeeDataStructure(**employee_data)
    print(employee.model_dump())
