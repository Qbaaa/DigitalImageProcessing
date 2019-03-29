from math import ceil
import numpy as np
from ImageUnification import unification_Grayscale_Geometric, unification_RGB_Geometric, unification_RGB_Resolution, unification_Grayscale_Resolution
from Image import Image
from ReadTiff import ReadTiff
from WriteTiff import writeTiff
from arithmetic_gray import sum_const_grayscale, sum_two_images_grayscale, multiplication_const_grayscale, multiplication_two_images_grayscale

if __name__ == "__main__":

    try:
        nameFIleONE = 'img/gMessi100.tif'
        nameFileTWO = 'img/groza.tif'

        readFileOne = ReadTiff(nameFIleONE)
        imageOne = Image(readFileOne)

        readFileTwo = ReadTiff(nameFileTWO)
        imageTwo = Image(readFileTwo)

        unification_Grayscale_Geometric(imageOne, imageTwo)
        writeTiff("unf_geo", imageOne)

        unification_Grayscale_Resolution(imageOne, imageTwo)
        writeTiff("unf_res", imageOne)

        #multiplication_two_images_grayscale(imageOne, imageTwo)

    except Exception as e:
        print("BLAD %s" %e)