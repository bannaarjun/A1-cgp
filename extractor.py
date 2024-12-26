import sys
from moviepy.editor import *
from PIL import Image, ImageDraw, ImageFont

def create_video_from_text(input_file, output_file, font_path='assets/font.ttf'):
    # Read the input text file
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Video settings
    width, height = 1280, 720
    fps = 30
    duration_per_line = 3  # Seconds per line of text

    clips = []

    # Create a video frame for each line of text
    for line in lines:
        # Create an image for the line of text
        img = Image.new('RGB', (width, height), color='black')
        draw = ImageDraw.Draw(img)
        font = ImageFont.truetype(font_path, 60)

        text_width, text_height = draw.textsize(line, font=font)
        position = ((width - text_width) / 2, (height - text_height) / 2)

        draw.text(position, line.strip(), font=font, fill='white')

        # Convert to MoviePy clip
        frame = ImageClip(img).set_duration(duration_per_line)
        clips.append(frame)

    # Concatenate all clips into a single video
    video = concatenate_videoclips(clips, method="compose")
    
    # Set the video fps and write the final video to a file
    video.set_fps(fps)
    video.write_videofile(output_file, codec='libx264')

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python extractor.py input.txt output.mp4")
        sys.exit(1)

    input_txt = sys.argv[1]
    output_video = sys.argv[2]

    create_video_from_text(input_txt, output_video)
  
