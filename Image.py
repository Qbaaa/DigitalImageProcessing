import numpy as np


class Image:

    def __init__(self, ReadTiff):

        self.oldImageLength = ReadTiff.imageLength
        self.oldImageWidth = ReadTiff.imageWidth
        self.nameImageTiff = ReadTiff.nameImage
        self.imageData = ReadTiff.imageData
        self.imageLength = ReadTiff.imageLength
        self.imageWidth = ReadTiff.imageWidth
        self.imageColor = ReadTiff.color
        self.imageBitsColor = ReadTiff.imageBitsColor
        self.imageTiffOrder = ReadTiff.tiffOrder
        self.imageRowsPerStrip = ReadTiff.imageRowsPerStrip
        self.imageDataStripByteCounts = []
        self.imageDataStripOffset = []
        self.constRowsPerStrip = ReadTiff.constRowsPerStrip

        if self.imageColor == 2:
            self.oldImageData = np.ones((self.oldImageLength, self.oldImageWidth, 3), dtype=np.uint8)

            for i in range(self.oldImageLength):
                for j in range(self.oldImageWidth):
                    for k in range(3):
                        self.oldImageData[i, j, k] = self.imageData[i][j][k]

        else:
            self.oldImageData = np.ones((self.oldImageLength, self.oldImageWidth, 3), dtype=np.uint8)

            for i in range(self.oldImageLength):
                for j in range(self.oldImageWidth):
                    self.oldImageData[i, j] = self.imageData[i][j]