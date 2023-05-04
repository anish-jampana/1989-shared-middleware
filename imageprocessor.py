from PIL import Image as im
import numpy as np

# This is for the base image
class ImageProcessor:
    def __init__(self, image):
        self.image = image
        self.xsize = self.image.size[0]
        self.ysize = self.image.size[1]

    def mosaicSize(self, tilesAcross, tileSize):
        base_tileSize = self.xsize / tilesAcross # how much we want to render at a time from base image
        mosaicWidth = tilesAcross * tileSize 
        #mosaicHeight = (self.ysize // (self.xsize // tilesAcross)) * tileSize
        mosaicHeight = int((self.ysize // (base_tileSize)) * tileSize)
        dimensionsPixels = (mosaicWidth, mosaicHeight) # dimensions of the mosaic
        print(dimensionsPixels, base_tileSize)
        return dimensionsPixels, base_tileSize
        
    def pixels(self):
        return np.array(list(self.image.getdata()))
    
    def averageColor(self):
        pixels = self.pixels()
        return np.sum(pixels, axis=0)/len(pixels)

