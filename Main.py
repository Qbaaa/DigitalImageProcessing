from ImageUnification import ImageUnification, unificationImageGrayscaleGeometric, unificationImageRGBResolution, \
    unificationImageRGBGeometric
from Image import Image
from ReadTiff import ReadTiff
from WriteTiff import writeTiff

if __name__ == "__main__":

    try:
        nameFIleONE = 'gimage.tif'
        nameFileTWO = 'RGBLaLiga.tif'

        readFileOne = ReadTiff(nameFIleONE)
        imageOne = Image(readFileOne)

        writeTiff("kopia6", imageOne)

        #readFileTwo = ReadTiff(nameFileTWO)
        #imageTwo = Image(readFileTwo)

        #unificationImageRGBResolution(imageOne, imageTwo)
        #unificationImageRGBGeometric(imageOne, imageTwo)
        #writeTiff('kopia1', imageOne)

    except Exception as e:
        print("BLAD %s" %e)