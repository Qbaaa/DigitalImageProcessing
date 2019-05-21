
class Image:

    def __init__(self, ReadTiff):

        self.originalImageLength = ReadTiff.imageLength
        self.originalImageWidth = ReadTiff.imageWidth
        self.nameImageTiff = ReadTiff.nameImage
        self.imageData = ReadTiff.imageData
        #self.imageLength = ReadTiff.imageLength
        #self.imageWidth = ReadTiff.imageWidth
        self.imageLength = len(ReadTiff.imageData)
        self.imageWidth = len(ReadTiff.imageData[0])
        self.imageColor = ReadTiff.color
        self.imageBitsColor = ReadTiff.imageBitsColor
        self.imageTiffOrder = ReadTiff.tiffOrder
        self.imageRowsPerStrip = ReadTiff.imageRowsPerStrip
        self.imageDataStripByteCounts = []
        self.imageDataStripOffset = []
        self.constRowsPerStrip = ReadTiff.constRowsPerStrip
        self.originalImageData = ReadTiff.originalImageData