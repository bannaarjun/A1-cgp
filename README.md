# TXT to Video Extractor

This project converts a given `.txt` file into a video, where each line or chunk of text is displayed for a certain duration.

## Features
- Converts text into video frames
- Customizable text styling and animations
- Export video in MP4 format

## Requirements
- Python 3.x
- `ffmpeg`
- `Pillow` for image processing
- `moviepy` for video creation

## Installation
1. Clone this repository:
    ```bash
    git clone https://github.com/yourusername/txt-to-video-extractor.git
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
To extract a video from a text file:

```bash
python extractor.py input.txt output.mp4
