
class Image:

    def __init__(self, ReadTiff):

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