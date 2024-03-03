import os
from secrets import choice

import aiofiles
import aiohttp
from PIL import Image, ImageDraw, ImageFont

themes = ["rrc", "hejo", "black"]


def changeImageSize(maxWidth, maxHeight, image):
    widthRatio = maxWidth / image.size[0]
    heightRatio = maxHeight / image.size[1]
    newWidth = int(widthRatio * image.size[0])
    newHeight = int(heightRatio * image.size[1])
    newImage = image.resize((newWidth, newHeight))
    return newImage


async def gen_thumb(thumbnail, title, videoid, ctitle):
    async with aiohttp.ClientSession() as session:
        async with session.get(thumbnail) as resp:
            if resp.status == 200:
                f = await aiofiles.open(
                    f"Uputt/resources/thumb{videoid}.png", mode="wb"
                )
                await f.write(await resp.read())
                await f.close()
    theme = choice(themes)
    image1 = Image.open(f"Uputt/resources/thumb{videoid}.png")
    image2 = Image.open(f"Uputt/resources/{theme}.png")
    image3 = changeImageSize(1280, 720, image1)
    image4 = changeImageSize(1280, 720, image2)
    image5 = image3.convert("RGBA")
    image6 = image4.convert("RGBA")
    Image.alpha_composite(image5, image6).save(
        f"Uputt/resources/temp{videoid}.png")
    img = Image.open(f"Uputt/resources/temp{videoid}.png")
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("Uputt/resources/Roboto-Light.ttf", 52)
    font2 = ImageFont.truetype("Uputt/resources/Roboto-Medium.ttf", 76)
    draw.text((27, 538), f"Playing on {ctitle[:15]}...", (0, 0, 0), font=font)
    draw.text((27, 612), f"{title[:20]}...", (0, 0, 0), font=font2)
    img.save(f"Uputt/resources/final{videoid}.png")
    os.remove(f"Uputt/resources/temp{videoid}.png")
    os.remove(f"Uputt/resources/thumb{videoid}.png")
    final = f"Uputt/resources/final{videoid}.png"
    return final
