from fastapi import FastAPI, status, HTTPException
from . import schemas
from src.components.pipeline.inference_pipeline import InferencePipeline

app = FastAPI()


@app.get("/")
def read_root():
    return {"Status": "Server is Live"}


@app.post(
    "/predict/", status_code=status.HTTP_200_OK, response_model=schemas.PredictionModel
)
async def prediction(data: schemas.EmployeeDataStructure):
    try:
        data = data.model_dump()
        data = {k: [v] if not isinstance(v, list) else v for k, v in data.items()}
        inference = InferencePipeline()
        model_prediction = inference.predict(data)
        response_model = schemas.PredictionModel(prediction=model_prediction)
        return response_model
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        ) from e
