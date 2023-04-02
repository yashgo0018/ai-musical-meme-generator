from . import config

from .meme_generator import combine_image_audio, generate_text_meme, combine_image_text
from .classifier import classify, load_model
from PIL import Image
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, HTTPException, UploadFile, Body
import numpy as np
import io


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

model = load_model()


@app.get("/")
def index():
    return "api is running"


@app.post("/generate-meme")
async def generate_meme(file: UploadFile, topic: str = Body()):
    if "image" not in file.content_type:
        raise HTTPException(400, detail="Invalid document type")
    request_object_content = await file.read()
    img_org = Image.open(io.BytesIO(request_object_content))
    img = np.array(img_org.resize((256, 256)).convert('RGB'))
    predictions = classify(model, img)
    emotion = predictions[0][0]
    meme = generate_text_meme(emotion, topic)
    meme_img = combine_image_text(img, meme)
    video_file_name = combine_image_audio(meme_img, emotion)
    return {"meme": meme, "video": f"/static/{video_file_name}"}
