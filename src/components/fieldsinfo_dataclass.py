from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class FieldsInfo:

    target_column: str = "Attrition"

    categorical_columns: List[str] = field(
        default_factory=lambda: [
            "BusinessTravel",
            "Department",
            "EducationField",
            "Gender",
            "JobRole",
            "MaritalStatus",
            "OverTime",
        ]
    )
    numerical_columns: List[str] = field(
        default_factory=lambda: [
            "Age",
            "DailyRate",
            "DistanceFromHome",
            "HourlyRate",
            "MonthlyIncome",
            "MonthlyRate",
            "PercentSalaryHike",
            "StandardHours",
            "TotalWorkingYears",
            "TrainingTimesLastYear",
            "YearsAtCompany",
            "YearsInCurrentRole",
            "YearsSinceLastPromotion",
            "YearsWithCurrManager",
        ]
    )
    ordinal_columns: List[str] = field(
        default_factory=lambda: [
            "Education",
            "EnvironmentSatisfaction",
            "JobInvolvement",
            "JobLevel",
            "JobSatisfaction",
            "NumCompaniesWorked",
            "PerformanceRating",
            "RelationshipSatisfaction",
            "StockOptionLevel",
            "WorkLifeBalance",
        ]
    )

    # Define the custom mappings for each column as key-value pairs
    ordinal_column_mappings: Dict[str, List[str]] = field(
        default_factory=lambda: {
            "Education": ["Below College", "College", "Bachelor", "Master", "Doctor"],
            "EnvironmentSatisfaction": ["Low", "Medium", "High", "Very High"],
            "JobInvolvement": ["Low", "Medium", "High", "Very High"],
            "JobLevel": [
                "Entry Level",
                "Junior Level",
                "Mid Level",
                "Senior Level",
                "Executive Level",
            ],
            "JobSatisfaction": ["Low", "Medium", "High", "Very High"],
            "PerformanceRating": ["Low", "Good", "Excellent", "Outstanding"],
            "RelationshipSatisfaction": ["Low", "Medium", "High", "Very High"],
            "WorkLifeBalance": ["Bad", "Good", "Better", "Best"],
            "StockOptionLevel": [
                "No Stock Options",
                "Low Stock Options",
                "Medium Stock Options",
                "High Stock Options",
            ],
        }
    )

    useless_columns: List[str] = field(
        default_factory=lambda: [
            "EmployeeCount",
            "EmployeeNumber",
            "Over18",
            "StandardHours",
        ]
    )


# Example usage
fields_info = FieldsInfo()
# print(fields_info.categorical_columns)
# print(fields_info.numerical_columns)
# print(fields_info.ordinal_columns)
print(list(fields_info.ordinal_column_mappings.values()))
