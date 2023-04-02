from PIL import ImageDraw
from PIL import ImageFont
from PIL import Image
from moviepy.editor import AudioFileClip, ImageClip
from random import randint
import openai
import os
import random
import cv2
import textwrap
import numpy as np
openai.organization = os.getenv("OPENAI_ORG_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")


def put_text(img, text, x_value, y_value):
    font = cv2.FONT_HERSHEY_DUPLEX
    wrapped_text = textwrap.wrap(text, width=10)
    x, y = 200, 40
    font_size = 2
    font_thickness = 3

    for i, line in enumerate(wrapped_text):
        textsize = cv2.getTextSize(line, font, font_size, font_thickness)[0]

        gap = textsize[1] + 40
        y = y_value + i * gap
        #y = int((img.shape[0] + textsize[1]) / 2) + i * gap
        x = int((img.shape[1] - textsize[0]) / 2)
        cv2.putText(img, line, (x_value, y), font,
                    font_size,
                    (255, 255, 255),
                    font_thickness,
                    lineType=cv2.LINE_AA)


def combine_image_text(image: Image, text):

    draw = ImageDraw.Draw(image)
    (h, w, _) = np.array(image).shape

    font = ImageFont.truetype("Roboto-Black.ttf", size=25)

    draw.text((200, w-200), text, (0, 0, 0), font=font)
    return image


def generate_text_meme(emotion: str, topic: str):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"give me a {emotion} meme about '{topic}', give only text in less than 20 words\n",
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response)
    return response["choices"][0]["text"].strip()


def combine_image_audio(image, emotion):
    tunes = list(
        map(lambda x: f"./tune/{emotion}/{x}", os.listdir(f"./tune/{emotion}")))
    print(tunes)
    print(random.randint(0, len(tunes)-1))
    tune = tunes[random.randint(0, len(tunes)-1)]
    audio = AudioFileClip(tune)
    clip = ImageClip(image).set_duration(audio.duration)
    clip = clip.set_audio(audio)
    filename = f"{str(randint(1e7, 1e8-1))}.mp4"
    output_path = f"./static/{filename}"
    clip.write_videofile(output_path, fps=24)
    return filename
