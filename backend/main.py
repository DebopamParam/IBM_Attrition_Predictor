from fastapi import FastAPI, status, HTTPException
from . import schemas
from src.components.pipeline.inference_pipeline import InferencePipeline
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allowing CORS for all origins for now (you can restrict this to your specific front-end domain later)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins, you can specify your Flutter Web URL here
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods like GET, POST, etc.
    allow_headers=["*"],  # Allows all headers
)

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
