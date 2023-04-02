from fastapi import FastAPI, UploadFile, HTTPException
from .classifier import load_model, classify
from PIL import Image
import numpy as np
import io

app = FastAPI()
model = load_model()


@app.get("/")
def index():
    return "api is running"


@app.post("/generate-meme")
async def generate_meme(file: UploadFile):
    if "image" not in file.content_type:
        raise HTTPException(400, detail="Invalid document type")
    request_object_content = await file.read()
    img = Image.open(io.BytesIO(request_object_content))
    img = np.array(img.resize((256, 256)).convert('RGB'))
    predictions = classify(model, img)
    return {"prediction": predictions}
