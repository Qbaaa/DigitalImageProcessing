# ZADANIE 2
from math import ceil
from WriteTiff import writeTiff


# suowanie obrazu ze stala
def sum_const_grayscale(image1, const=0):
    if image1.imageBitsColor[0] == 4:

        maxBitsColor = 15
        if not (0 <= const <= 15):
            raise Exception("program do obrazow SZARYCH 4 bitowych mozne dodac liczbe z zakresu 0-15, a podana liczba "
                            "to %d." % const)
    else:
        if image1.imageBitsColor[0] == 8:

            maxBitsColor = 255
            if not (0 <= const <= 255):
                raise Exception("program do obrazow SZARYCH 8 bitowych mozne dodac liczbe z zakresu 0-255, a podana "
                                "podana to %d." % const)
        else:
            raise Exception("program dodaje jedynie obrazy SZARE 4, 8 bitowe ze stala")

    Qmax = 0
    Dmax = 0
    X = 0
    fmax = 0
    fmin = 256

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            temp = image1.imageData[i][j][0] + const

            if temp > Qmax:
                Qmax = temp

    if Qmax > maxBitsColor:
        Dmax = Qmax - maxBitsColor
        x = ceil((Dmax/maxBitsColor)*100)
        X = x / 100

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempSum = round((image1.imageData[i][j][0] - (image1.imageData[i][j][0] * X)) + (const - (const * X)))
            image1.imageData[i][j][0] = tempSum

            if tempSum > fmax:
                fmax = tempSum

            if tempSum < fmin:
                fmin = tempSum

    writeTiff('add_const', image1)
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            image1.imageData[i][j][0] = round(maxBitsColor * ((image1.imageData[i][j][0] - fmin) / (fmax - fmin)))
    writeTiff('normalization_add_const', image1)


# sumowanie dwoch obrazow
def sum_two_images_grayscale(image1, image2):

    global maxBitsColor
    if image1.imageBitsColor[0] == image2.imageBitsColor[0] and (image1.imageLength == image2.imageLength) and (image1.imageWidth == image2.imageWidth):

        if image1.imageBitsColor[0] == 4:
            maxBitsColor = 15

        else:
            if image1.imageBitsColor[0] == 8:
                maxBitsColor = 255

    else:
        raise Exception("program dodaje jedynie obrazy SZARE 4, 8 bitowe oraz obrazy musza miec takie same rozmiary.")

    Qmax = 0
    Dmax = 0
    X = 0
    fmax = 0
    fmin = 256

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            temp = image1.imageData[i][j][0] + image2.imageData[i][j][0]

            if temp > Qmax:
                Qmax = temp

    if Qmax > maxBitsColor:
        Dmax = Qmax - maxBitsColor
        x = ceil((Dmax/maxBitsColor)*100)
        X = x / 100

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempSum = round((image1.imageData[i][j][0] - (image1.imageData[i][j][0] * X)) + (image2.imageData[i][j][0] - (image2.imageData[i][j][0] * X)))
            image1.imageData[i][j][0] = tempSum

            if tempSum > fmax:
                fmax = tempSum

            if tempSum < fmin:
                fmin = tempSum

    writeTiff('add_two_image', image1)
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            image1.imageData[i][j][0] = round(maxBitsColor * ((image1.imageData[i][j][0] - fmin) / (fmax - fmin)))
    writeTiff('normalization_add_two_image', image1)