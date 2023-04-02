from moviepy.editor import AudioFileClip, ImageClip
from random import randint
import openai
import os

openai.organization = os.getenv("OPENAI_ORG_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")


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


def combine_image_text(image, text):
    return image


def combine_image_audio(image, emotion):
    audio = AudioFileClip("song.mp3")
    clip = ImageClip(image).set_duration(audio.duration)
    clip = clip.set_audio(audio)
    filename = f"{str(randint(1e7, 1e7-1))}.mp4"
    output_path = f"./static/{filename}"
    clip.write_videofile(output_path, fps=24)
    return filename
