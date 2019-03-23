import numpy as np
from PIL import Image

from ImageUnification import unification_Grayscale_Geometric, unification_RGB_Geometric, unification_RGB_Resolution, unification_Grayscale_Resolution
from Image import Image
from ReadTiff import ReadTiff
from WriteTiff import writeTiff



if __name__ == "__main__":

    try:
        nameFIleONE = 'img/2012.tif'
        nameFileTWO = 'img/gMessi100.tif'


        #im = Image.open(nameFIleONE)
        #t = np.asarray(im)

        #print(len(t))
        #print(len(t[0]))

        #for i in range(73):
         #   print(t[2][i], end=" ")
          #   print(i+1, end=":")


        readFileOne = ReadTiff(nameFIleONE)
        imageOne = Image(readFileOne)

        #readFileTwo = ReadTiff(nameFileTWO)
        #imageTwo = Image(readFileTwo)

        #unification_Grayscale_Geometric(imageOne, imageTwo)
        #writeTiff('unifikacja_geo_1', imageOne)
        #writeTiff('unifikacja_geo_2', imageTwo)

        #unification_Grayscale_Resolution(imageOne, imageTwo)

        #writeTiff('unifikacja_res_1', imageOne)
        #writeTiff('unifikacja_res_2', imageTwo)

        writeTiff('kopia2012', imageOne)

        #print(imageOne.imageBitsColor)
        #print(imageOne.imageColor)
        #writeTiff('kopia2', imageTwo)

        #ReadTiff("results/3.tif")

    except Exception as e:
        print("BLAD %s" %e)