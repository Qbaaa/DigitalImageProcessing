from ImageUnification import unification_Grayscale_Geometric, unification_RGB_Geometric, unification_RGB_Resolution, unification_Grayscale_Resolution
from Image import Image
from ReadTiff import ReadTiff
from WriteTiff import writeTiff
from arithmetic_gray import sum_const_grayscale, sum_two_images_grayscale, multiplication_const_grayscale, multiplication_two_images_grayscale

if __name__ == "__main__":

    try:
        nameFIleONE = 'img/RGBMessi.tif'
        nameFileTWO = 'img/RGBimage.tif'

        readFileOne = ReadTiff(nameFIleONE)
        imageOne = Image(readFileOne)

        readFileTwo = ReadTiff(nameFileTWO)
        imageTwo = Image(readFileTwo)

        unification_RGB_Geometric(imageOne, imageTwo)

        unification_RGB_Resolution(imageOne, imageTwo)
        writeTiff("1", imageOne)
        writeTiff("2", imageTwo)

    except Exception as e:
        print("BLAD %s" %e)