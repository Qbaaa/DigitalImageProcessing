from ImageUnification import unification_Grayscale_Geometric, unification_RGB_Geometric, unification_RGB_Resolution, unification_Grayscale_Resolution
from Image import Image
from ReadTiff import ReadTiff
from WriteTiff import writeTiff
from arithmetic_gray import sum_const_grayscale, sum_two_images_grayscale, multiplication_const_grayscale, \
    multiplication_two_images_grayscale, mixing_images_grayscale, pow_image_grayscale, log_image_grayscale,\
    root_image_grayscale, division_two_iamges_grayscale, division_const_grayscale
from arithmetic_color import sum_const_RGB, sum_two_images_RGB, multiplication_const_RGB, \
    multiplication_two_images_RGB, mixing_images_RGB, pow_image_RGB, division_const_RGB, \
    division_two_iamges_RGB, root_image_RGB, log_image_RGB

if __name__ == "__main__":

    try:
        nameFIleONE = 'img/RGBLaLiga.tif'
        nameFileTWO = 'img/RGBMessi.tif'

        readFileOne = ReadTiff(nameFIleONE)
        imageOne = Image(readFileOne)

        readFileTwo = ReadTiff(nameFileTWO)
        imageTwo = Image(readFileTwo)

        unification_RGB_Geometric(imageOne, imageTwo)

        unification_RGB_Resolution(imageOne, imageTwo)

        #writeTiff("2", imageTwo)
        #sum_const_RGB(imageOne, 254)
        #sum_two_images_RGB(imageOne, imageTwo)

        #multiplication_const_RGB(imageOne, 55)
        #multiplication_two_images_RGB(imageOne, imageTwo)
        mixing_images_RGB(imageOne,imageTwo,0.3)

    except Exception as e:
        print("BLAD %s" %e)