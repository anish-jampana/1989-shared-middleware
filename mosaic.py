from imageprocessor import ImageProcessor
from PIL import Image as im
from scipy import spatial
import numpy as np
import os
from tqdm import tqdm

def genMosaic(input_image, folder, tilesAcross, tileSize):
    print("Started.")
    base_image = ImageProcessor(input_image)
    dimensionsPixels, base_tileSize = base_image.mosaicSize(tilesAcross, tileSize)

    # resize every tile image to tile size and get average color
    average_colors = []
    files = os.listdir(folder)
    for file in tqdm(files):
        # resizing
        image = im.open(f'{folder}/' + file)
        new_image = image.resize((tileSize, tileSize))
        new_image.save(f'{folder}-resized/' + file)

        # getting average color
        new_image = ImageProcessor(new_image)
        average_colors.append(new_image.averageColor())

    average_colors = np.array(average_colors)
    # use kd tree on list of colors
    tree = spatial.KDTree(average_colors)

    # go through each tile sized piece of base image and find closest average color
    k = 0
    output = im.new('RGB', dimensionsPixels)
    for i in np.arange(0, base_image.xsize, base_tileSize):
        for j in np.arange(0, base_image.ysize, base_tileSize):
            area = base_image.image.crop((i, j, i+base_tileSize, j+base_tileSize))
            cropped_image = ImageProcessor(area)
            color = cropped_image.averageColor()
            distance, index = tree.query(color)

            closest_file = files[index]
            image = im.open(f'{folder}-resized/' + closest_file)
            paste_x = round(i / base_tileSize) * tileSize
            paste_y = round(j / base_tileSize) * tileSize
            output.paste(image, (paste_x, paste_y))
    print("Done.")
    output.save("output.png")