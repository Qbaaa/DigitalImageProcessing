from ImageUnification import unification_Grayscale_Geometric, unification_RGB_Geometric, unification_RGB_Resolution, \
    unification_Grayscale_Resolution, unification_Grayscale_one_image, unification_RGB_one_image
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

        # -------SZARY TEST 1-------

        nameFIleONE = 'img/gae.tif'
        nameFileTWO = 'img/gMessi.tif'

        readFileOne = ReadTiff(nameFIleONE)
        imageOne = Image(readFileOne)

        readFileTwo = ReadTiff(nameFileTWO)
        imageTwo = Image(readFileTwo)

        unification_Grayscale_Geometric(imageOne, imageTwo)
        writeTiff("Geometric_GRAY_1", imageOne)
        writeTiff("Geometric_GRAY_2", imageTwo)

        unification_Grayscale_Resolution(imageOne, imageTwo)
        writeTiff("Resolution_GRAY_3", imageOne)
        writeTiff("Resolution_GRAY_4", imageTwo)

        #sum_const_grayscale(imageTwo, 50)
        #sum_two_images_grayscale(imageOne, imageTwo)

        #multiplication_const_grayscale(imageTwo, 50)
        #multiplication_two_images_grayscale(imageOne, imageTwo)

        #mixing_images_grayscale(imageOne, imageTwo, 0.5)
        #pow_image_grayscale(imageTwo, 3)
        #log_image_grayscale(imageTwo)
        #sqrt_image_grayscale(imageTwo, 2)

        #division_const_grayscale(imageTwo, 15)
        #division_two_iamges_grayscale(imageOne, imageTwo)

        # -------SZARY TEST 2------------

        #nameFIleTHREE = 'img/gLU.tif'
        #nameFileFOUR = 'img/groza.tif'

        #readFileThree = ReadTiff(nameFIleTHREE)
        #imageThree = Image(readFileThree)

        #readFileFour = ReadTiff(nameFileFOUR)
        #imageFour = Image(readFileFour)

        #unification_Grayscale_Geometric(imageThree, imageFour)
        #writeTiff("Geometric_GRAY_3", imageThree)
        #writeTiff("Geometric_GRAY_4", imageFour)

        #unification_Grayscale_Resolution(imageThree, imageFour)
        #writeTiff("Resolution_GRAY_3", imageThree)
        #writeTiff("Resolution_GRAY_4", imageFour)

        #sum_const_grayscale(imageThree, 100)
        #sum_two_images_grayscale(imageThree,imageFour)

        #multiplication_const_grayscale(imageThree, 100)
        #multiplication_two_images_grayscale(imageThree, imageFour)

        #mixing_images_grayscale(imageThree, imageFour, 0.8)
        #pow_image_grayscale(imageThree, 3)

        #division_const_grayscale(imageThree, 3)
        #division_two_iamges_grayscale(imageThree, imageFour)

        #log_image_grayscale(imageThree)
        #sqrt_image_grayscale(imageThree, 3)
        #log_image_grayscale(imageThree)


        # --------RGB Test 1--------

        #nameFIleONE = 'img/RGBMessi.tif'
        #nameFileTWO = 'img/RGBLL.tif'
        #
        #readFileOne = ReadTiff(nameFIleONE)
        #imageOne = Image(readFileOne)
        #
        #readFileTwo = ReadTiff(nameFileTWO)
        #imageTwo = Image(readFileTwo)
        #
        #unification_RGB_Geometric(imageOne, imageTwo)
        # writeTiff("Geometric_RGB_1", imageOne)
        # writeTiff("Geometric_RGB_2", imageTwo)
        #
        #unification_RGB_Resolution(imageOne, imageTwo)
        # writeTiff("Resolution_RGB_1", imageOne)
        # writeTiff("Resolution_RGB_2", imageTwo)

        #sum_const_RGB(imageOne, 50)
        #sum_two_images_RGB(imageOne, imageTwo)

        #multiplication_const_RGB(imageOne, 50)
        #multiplication_two_images_RGB(imageOne, imageTwo)

        #mixing_images_RGB(imageOne, imageTwo, 0.5)
        #pow_image_RGB(imageOne, 2)
        #log_image_RGB(imageOne)
        #sqrt_image_RGB(imageOne, 2)

        #division_const_RGB(imageOne, 15)
        #division_two_iamges_RGB(imageOne, imageTwo)

        # --------RGB Test 2--------

        #nameFIleTHREE = 'img/RGBkamel.tif'
        #nameFileFOUR = 'img/RGBkulki.tif'

        #readFileThree = ReadTiff(nameFIleTHREE)
        #imageThree = Image(readFileThree)

        #readFileFour = ReadTiff(nameFileFOUR)
        #imageFour = Image(readFileFour)

        #unification_RGB_Geometric(imageThree, imageFour)
        #writeTiff("Geometric_RGB_3", imageThree)
        #writeTiff("Geometric_RGB_4", imageFour)

        #unification_RGB_Resolution(imageThree, imageFour)
        #writeTiff("Resolution_RGB_3", imageThree)
        #writeTiff("Resolution_RGB_4", imageFour)

        #sum_const_RGB(imageFour, 100)
        #sum_two_images_RGB(imageThree, imageFour)

        #multiplication_const_RGB(imageFour, 100)
        #multiplication_two_images_RGB(imageThree, imageFour)

        #mixing_images_RGB(imageThree, imageFour, 0.8)
        #pow_image_RGB(imageFour, 3)

        #division_const_RGB(imageFour, 3)
        #division_two_iamges_RGB(imageThree, imageFour)

        #sqrt_image_RGB(imageFour, 3)
        #log_image_RGB(imageFour)

    except Exception as e:
        print("BLAD %s" %e)