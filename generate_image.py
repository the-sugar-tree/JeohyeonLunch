from PIL import Image, ImageDraw, ImageFont


def make_image(message, file_name):
    print(f"이미지 생성중... | img/{file_name}.png | {message.split('\n')}")

    W = 1080
    H = 1920
    bg_color = 'rgb(214, 230, 245)'

    font = ImageFont.truetype('fonts/NanumGothic.ttf', size=80)
    font_color = 'rgb(0, 0, 0)'

    image = Image.new('RGB', (W, H), color=bg_color)
    draw = ImageDraw.Draw(image)

    lines = message.split('\n')

    x_text = 50
    y_text = 600

    for line in lines:
        _, _, width, height = font.getbbox(line)
        draw.text((x_text, y_text), line, font=font, fill=font_color)
        y_text += height + 10

    image.save('img/{}.png'.format(file_name))


if __name__ == '__main__':
    make_image('Hello, World!', '240529')
