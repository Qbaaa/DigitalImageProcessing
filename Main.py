from ImageUnification import unification_Grayscale_Geometric, unification_RGB_Geometric, unification_RGB_Resolution, unification_Grayscale_Resolution
from Image import Image
from ReadTiff import ReadTiff
from WriteTiff import writeTiff

if __name__ == "__main__":

    try:
        nameFIleONE = 'img/gMessi.tif'
        nameFileTWO = 'img/groza.tif'

        readFileOne = ReadTiff(nameFIleONE)
        imageOne = Image(readFileOne)

        readFileTwo = ReadTiff(nameFileTWO)
        imageTwo = Image(readFileTwo)

        writeTiff('kopia1', imageOne)
        writeTiff('kopia2', imageTwo)

    except Exception as e:
        print("BLAD %s" %e)