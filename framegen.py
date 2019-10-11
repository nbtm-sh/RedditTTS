from PIL import Image, ImageDraw, ImageFont
import textwrap

class Comment:
    def __init__(self, comment_object, resolution = (1920, 1080), background_color = 0xffffff):
        self.resolution = resolution

        self.image = Image.new('RGB', resolution, color = background_color)
        draw = ImageDraw.Draw(self.image)

        # Drawing and centering the text
        text = '\n'.join(textwrap.wrap(comment_object.body, width = 130))
        font = ImageFont.truetype('assets/Roboto-Regular.ttf', int(resolution[0]*0.015625))

        height = 0.015625*len(text.split('\n'))
        draw_t = resolution[1]*height
        draw_b = (resolution[1]-draw_t)/2

        draw.text(
            (resolution[0]*0.05, draw_b),
            text,
            font = font,
            fill = (0, 0, 0, 0)
        )

        # Drawing username
        font = ImageFont.truetype('assets/Roboto-Italic.ttf', int(resolution[0]*0.009375))
        draw.text(
            (resolution[0]*0.05, draw_b*0.95),
            comment_object.author,
            font = font,
            fill = (125, 125, 125, 0)
        )

class Post:
    def __init__(self, post_object, resolution = (1920, 1080), background_color = 0xffffff):
        self.resolution = resolution

        self.image = Image.new('RGB', resolution, color = background_color)
        draw = ImageDraw.Draw(self.image)

        # Drawing the title
        font = ImageFont.truetype('assets/Roboto-Bold.ttf', int(resolution[0]*0.01666666666))
        text = '\n'.join(textwrap.wrap(post_object.title, width = 120))
        lines = len(text.split('\n'))

        draw.text(
            (resolution[0]*0.05, resolution[1]*0.10),
            text,
            font = font,
            fill = (0, 0, 0, 0)
        )

        # Drawing author
        font = ImageFont.truetype('assets/Roboto-Italic.ttf', int(resolution[0]*0.01041666))
        text = post_object.author

        draw.text(
            (resolution[0]*0.05, resolution[1]*0.08),
            text,
            font = font,
            fill = (125, 125, 125, 0)
        )

        # Drawing post body
        font = ImageFont.truetype('assets/Roboto-Regular.ttf', int(resolution[0]*0.009375))
        text = textwrap.wrap(post_object.body, width = 215)

        position = (resolution[0]*0.05, ((resolution[1]*0.08)*1.5) + int(resolution[0]*0.01666666666)*lines)

        draw.text(
            position,
            '\n'.join(text),
            font = font,
            fill = (0, 0, 0, 0)
        )