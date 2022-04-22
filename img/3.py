from PIL import Image

img = Image.new('RGB', [500,  500], 255)
data = img.load()

for x in range(img.size[0]):
    for y in range(img.size[1]):
        data[x, y] = (
            x % 255,
            y % 255,
            (x ** 2 - y ** 2) % 255,
        )

img.save('image1.png')