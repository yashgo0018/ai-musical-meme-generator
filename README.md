# AI Emotion-based Meme Generator

[![AI Musical Meme Generator](https://img.youtube.com/vi/E4xG7E4Hug8/0.jpg)](https://www.youtube.com/watch?v=E4xG7E4Hug8)

### Table of Contents
- [AI Emotion-based Meme Generator](#ai-emotion-based-meme-generator)
    - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Model Overview](#model-overview)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

Emotions play a crucial role in our lives, and we often express them through various means, such as music, art, and memes. The AI emotion-based meme generator is a powerful tool that combines computer vision, natural language processing, and meme generation to create memes based on the emotion of an image and a topic.

This repository contains the source code for the AI emotion-based meme generator, including the deep learning model for emotion detection, the song dataset, the text generation model, and the meme generation library.

## Model Overview

The model takes two inputs: an image and a topic. The image is processed using computer vision techniques to detect the emotion of the image. Based on the emotion detected, the model searches for a song in a dataset that matches the emotion. The model then generates a meme by combining the image, the topic, and the lyrics of the song.

## Installation

To install the AI emotion-based meme generator, follow these steps:

1. Clone this repository:
```bash
git clone https://github.com/yashgo0018/ai-musical-meme-generator
```

2. Go to the `backend` folder 
```bash
cd backend
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage
To use the AI emotion-based meme generator, follow these steps:

1. Place the image you want to generate a meme for in the input folder.

Run the main.py script:

```bash
uvicorn src:app --reload
```

2. The server will start you can explore the api using `http://localhost:8000/docs`

The generated meme will be saved in the `backend/static` folder. And will accessable on `http://localhost:8000/static/{videoname}`

## Contributing

Contributions are always welcome! If you'd like to contribute to this project, please fork this repository and submit a pull request.

## License
This project is licensed under the `MIT License`.
