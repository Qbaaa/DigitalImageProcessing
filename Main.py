from math import floor, ceil

from ImageUnification import unification_Grayscale_Geometric, unification_RGB_Geometric, unification_RGB_Resolution, unification_Grayscale_Resolution
from Image import Image
from ReadTiff import ReadTiff
from WriteTiff import writeTiff


if __name__ == "__main__":

    try:
        nameFIleONE = 'img/KBn.tif'
        nameFileTWO = 'img/groza.tif'


        readFileOne = ReadTiff(nameFIleONE)
        imageOne = Image(readFileOne)


        #readFileTwo = ReadTiff(nameFileTWO)
        #imageTwo = Image(readFileTwo)

        writeTiff('kopia1', imageOne)
        #writeTiff('kopia2', imageTwo)

        #ReadTiff("results/20190321_212251_kopia1.tif")

    except Exception as e:
        print("BLAD %s" %e)