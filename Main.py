from ImageUnification import unification_Grayscale_Geometric, unification_RGB_Geometric, unification_RGB_Resolution, unification_Grayscale_Resolution
from Image import Image
from ReadTiff import ReadTiff
from WriteTiff import writeTiff
from arithmetic_gray import sum_const_grayscale, sum_two_images_grayscale, multiplication_const_grayscale, \
    multiplication_two_images_grayscale, mixing_images_grayscale, pow_image_grayscale, log_image_grayscale,\
    sqrt_image_grayscale, division_two_iamges_grayscale, division_const_grayscale
from arithmetic_color import sum_const_RGB, sum_two_images_RGB, multiplication_const_RGB, \
    multiplication_two_images_RGB, mixing_images_RGB, pow_image_RGB, division_const_RGB, \
    division_two_iamges_RGB, sqrt_image_RGB, log_image_RGB

if __name__ == "__main__":

    try:

        # -------SZARY-------

        nameFIleONE = 'img/gMessi.tif'
        nameFileTWO = 'img/gLaLiga.tif'

        #readFileOne = ReadTiff(nameFIleONE)
        #imageOne = Image(readFileOne)

        #readFileTwo = ReadTiff(nameFileTWO)
        #imageTwo = Image(readFileTwo)

        #unification_Grayscale_Geometric(imageOne, imageTwo)
        #writeTiff("Geometric_GRAY_1", imageOne)
        #writeTiff("Geometric_GRAY_2", imageTwo)

        #unification_Grayscale_Resolution(imageOne, imageTwo)
        #writeTiff("Resolution_GRAY_1", imageOne)
        #writeTiff("Resolution_GRAY_2", imageTwo)

        #sum_const_grayscale(imageTwo, 50)
        #sum_two_images_grayscale(imageOne, imageTwo)

        #multiplication_const_grayscale(imageTwo, 50)
        #multiplication_two_images_grayscale(imageOne, imageTwo)

        #mixing_images_grayscale(imageOne, imageTwo, 0.5)
        #pow_image_grayscale(imageTwo, 2)
        #log_image_grayscale(imageTwo)
        #sqrt_image_grayscale(imageTwo, 2)

        #division_const_grayscale(imageTwo, 15)
        #division_two_iamges_grayscale(imageOne, imageTwo)


        # --------RGB--------

        #nameFIleONE = 'img/RGBMessi.tif'
        #nameFileTWO = 'img/RGBimage.tif'

        #readFileOne = ReadTiff(nameFIleONE)
        #imageOne = Image(readFileOne)

        #readFileTwo = ReadTiff(nameFileTWO)
        #imageTwo = Image(readFileTwo)

        #unification_RGB_Geometric(imageOne, imageTwo)
        #writeTiff("Geometric_RGB_1", imageOne)
        #writeTiff("Geometric_RGB_2", imageTwo)

        #unification_RGB_Resolution(imageOne, imageTwo)
        #writeTiff("Resolution_RGB_1", imageOne)
        #writeTiff("Resolution_RGB_2", imageTwo)

        #sum_const_RGB(imageTwo, 100)
        #sum_two_images_RGB(imageOne, imageTwo)

        #multiplication_const_RGB(imageTwo, 100)
        #multiplication_two_images_RGB(imageOne, imageTwo)

        #mixing_images_RGB(imageOne, imageTwo, 0.8)
        #pow_image_RGB(imageTwo, 3)
        #log_image_RGB(imageOne)
        #sqrt_image_RGB(imageTwo, 3)

        #division_const_RGB(imageTwo, 30)
        #division_two_iamges_RGB(imageOne, imageTwo)

    except Exception as e:
        print("BLAD %s" %e)