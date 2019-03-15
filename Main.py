from ImageUnification import ImageUnification, unificationImageGrayscaleGeometric, unificationImageRGBResolution
from Image import Image
from ReadTiff import ReadTiff
from datetime import datetime


if __name__ == "__main__":

    try:
        nameFIleONE = 'RGBimage.tif'
        nameFileTWO = 'RGBLaLiga.tif'

        readFileOne = ReadTiff(nameFIleONE)
        imageOne = Image(readFileOne)
        print(imageOne.nameImageTiff)

        readFileTwo = ReadTiff(nameFileTWO)
        imageTwo = Image(readFileTwo)
        print(imageTwo.nameImageTiff)

        unificationImageRGBResolution(imageOne, imageTwo)
    #    unificationImageGrayscaleGeometric(imageOne, imageTwo)
    #    print()



        s1 = datetime.now().strftime("%Y%m%d_%H%M%S")
        print(s1)
        print(type(s1))

    except Exception as e:
        print("BLAD %s" %e)


#print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@2")
#plik2 = open('czarny.tif', 'rb')
#bytest = plik2.read(2)
#bytest = plik2.read(2)
#image = int.from_bytes(bytest, byteorder="little")
#print(bytest)
#print(image)

#image =512
#test = image.to_bytes(4, byteorder="little")
#print(test)
#print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@2")



#plik.seek(214)
#qw = 0
#test = qw.to_bytes(1, byteorder=self.tiffOrder)
#print(test)
#plik.write(s=test)