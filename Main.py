from ImageUnification import unification_Grayscale_Geometric, unification_RGB_Geometric, unification_RGB_Resolution, unification_Grayscale_Resolution
from Image import Image
from ReadTiff import ReadTiff
from WriteTiff import writeTiff
from arithmetic_gray import sum_const_grayscale, sum_two_images_grayscale, multiplication_const_grayscale, \
    multiplication_two_images_grayscale, mixing_images, pow_image

if __name__ == "__main__":

    try:
        nameFIleONE = 'img/gMessi.tif'
        nameFileTWO = 'img/gimage.tif'

        readFileOne = ReadTiff(nameFIleONE)
        imageOne = Image(readFileOne)

        #readFileTwo = ReadTiff(nameFileTWO)
        #imageTwo = Image(readFileTwo)

        #unification_Grayscale_Geometric(imageOne, imageTwo)

        #unification_Grayscale_Resolution(imageOne, imageTwo)

        #mixing_images(imageOne, imageTwo, 0.6)
        pow_image(imageOne, 3)

        #writeTiff("1", imageOne)
        #writeTiff("2", imageTwo)

    except Exception as e:
        print("BLAD %s" %e)