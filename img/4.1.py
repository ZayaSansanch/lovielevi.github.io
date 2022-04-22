from PIL import Image

img = Image.new('RGB', [500,  500], 255)
data = img.load()

for x in range(img.size[0]):
    for y in range(img.size[1]):
        if (x > 100 and y > 100) and (x < 400 and y < 400):
            data[x, y] = (
                x % y,
                y % x,
                # 0 #4.1.2/4.png
                # (y * x) % 255 #4.1.5.png
                # ((x % y) + (y % x)) % 255 #4.1.8.png
            )

img.save('4.1.8.png')