from PIL import Image, ImageDraw, ImageFont

def create_text_image(text, width, height, font_path='assets/font.ttf', font_size=60):
    # Create an image to display text
    img = Image.new('RGB', (width, height), color='black')
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype(font_path, font_size)

    text_width, text_height = draw.textsize(text, font=font)
    position = ((width - text_width) / 2, (height - text_height) / 2)

    draw.text(position, text, font=font, fill='white')
    
    return img
  
