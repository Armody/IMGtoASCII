from PIL import Image
import numpy as np  

GrayScale = "@%#*+=-:. "

def main():
    image = Image.open("Images/Image.jpg").convert("L")
    Width, Height = image.size
    Scale = 0.43
    Columns = 80
    Tile_Width = Width / Columns
    Tile_Height = Tile_Width / Scale
    Rows = int(Height / Tile_Height)

    output = ""
    for row in range(Rows):
        for col in range(Columns):
            tile = image.crop((col * Tile_Width, row * Tile_Height, (col + 1) * Tile_Width, (row + 1) * Tile_Height))
            avarageL = getAvarageL(tile)
            output += GrayScale[int((avarageL * 9) / 255)]

        output += "\n"

    print(output)
    #image.show()

def getAvarageL(image):
    im = np.array(image)
    Width, Height = im.shape
    return np.average(im.reshape(Width * Height))


if __name__ == "__main__":
    main()