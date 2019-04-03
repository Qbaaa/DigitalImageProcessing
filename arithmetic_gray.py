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

    # dodawanie
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempSum = round((image1.imageData[i][j][0] - (image1.imageData[i][j][0] * X)) + (const - (const * X)))
            image1.imageData[i][j][0] = tempSum

            if tempSum > fmax:
                fmax = tempSum

            if tempSum < fmin:
                fmin = tempSum

    writeTiff('add_const', image1)

    # normalizacja
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


# mnozenie obrazu przez zadana stala
def multiplication_const_grayscale(image1, const=1):

    fmax = 0
    fmin = 256

    if image1.imageBitsColor[0] == 4:

        maxBitsColor = 15
        if not (0 < const <= 15):
            raise Exception("program do obrazow SZARYCH 4 bitowych moze pomnozyc liczbe z zakresu 0-15, a podana liczba "
                            "to %d." % const)
    else:
        if image1.imageBitsColor[0] == 8:

            maxBitsColor = 255
            if not (0 < const <= 255):
                raise Exception("program do obrazow SZARYCH 8 bitowych moze pomnozyc liczbe z zakresu 0-255, a podana "
                                "podana to %d." % const)
        else:
            raise Exception("program mnozy jedynie obrazy SZARE 4, 8 bitowe ze stala")

    # mnozenie
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempMult = image1.imageData[i][j][0]

            if tempMult == maxBitsColor:
                tempMult = const

            elif tempMult == 0:
                tempMult = 0

            else:
                tempMult = ceil((image1.imageData[i][j][0] * const) / maxBitsColor)

            image1.imageData[i][j][0] = tempMult

            if tempMult > fmax:
                fmax = tempMult

            if tempMult < fmin:
                fmin = tempMult

    writeTiff('multi_const', image1)

    # normalizacja
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            image1.imageData[i][j][0] = round(maxBitsColor * ((image1.imageData[i][j][0] - fmin) / (fmax - fmin)))

    writeTiff('normalization_multi_const', image1)


# mnozenie dwoch obrazow
def multiplication_two_images_grayscale(image1, image2):

    global maxBitsColor
    fmax = 0
    fmin = 256

    if image1.imageBitsColor[0] == image2.imageBitsColor[0] and (image1.imageLength == image2.imageLength) and (image1.imageWidth == image2.imageWidth):

        if image1.imageBitsColor[0] == 4:
            maxBitsColor = 15

        elif image1.imageBitsColor[0] == 8:
            maxBitsColor = 255

    else:
        raise Exception("program mnozy jedynie obrazy SZARE 4, 8 bitowe oraz obrazy musza miec takie same rozmiary.")

    # mnozenie
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempMult = image1.imageData[i][j][0]

            if tempMult == maxBitsColor:
                tempMult = image2.imageData[i][j][0]

            elif tempMult == 0:
                tempMult = 0

            else:
                tempMult = ceil((image1.imageData[i][j][0] * image2.imageData[i][j][0]) / maxBitsColor)

            image1.imageData[i][j][0] = tempMult

            if tempMult > fmax:
                fmax = tempMult

            if tempMult < fmin:
                fmin = tempMult

    writeTiff('multi_const', image1)

    # normalizacja
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            image1.imageData[i][j][0] = round(maxBitsColor * ((image1.imageData[i][j][0] - fmin) / (fmax - fmin)))

    writeTiff('normalization_multi_const', image1)


# mieszanie obrazow z okreslonym wspolczynnikiem
def mixing_images(image1, image2, scales=0.0):

    global maxBitsColor
    fmax = 0
    fmin = 256

    if image1.imageBitsColor[0] == image2.imageBitsColor[0] and (image1.imageLength == image2.imageLength) and (image1.imageWidth == image2.imageWidth):

        if not (0.0 <= scales <= 1.0):
            raise Exception("program miesza obrazy SZARE z waga z zakresu 0.0-1.0, a podana liczba "
                            "to %f." % scales)

        if image1.imageBitsColor[0] == 4:
            maxBitsColor = 15

        elif image1.imageBitsColor[0] == 8:
            maxBitsColor = 255

    else:
        raise Exception("program miesza jedynie obrazy SZARE 4, 8 bitowe oraz obrazy musza miec takie same rozmiary.")

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempMix = ceil(scales * image1.imageData[i][j][0] + (1 - scales) * image2.imageData[i][j][0])
            image1.imageData[i][j][0] = tempMix

            if tempMix > fmax:
                fmax = tempMix

            if tempMix < fmin:
                fmin = tempMix

    writeTiff('mix_two_image', image1)
    # normalizacja
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            image1.imageData[i][j][0] = round(maxBitsColor * ((image1.imageData[i][j][0] - fmin) / (fmax - fmin)))

    writeTiff('normalization_mix_two_image', image1)


# potegowanie obrazu (z zadana potega)
def pow_image(image1, p=1.0):

    global maxBitsColor
    fmax = 0
    fmin = 256
    fmaximage = 0

    if not (0.0 < p):
        raise Exception("program poteguje obraz SZARY z zadana potega z zakresu p > 0.0, a podana liczba "
                        "to %f." % p)

    if image1.imageBitsColor[0] == 4:
        maxBitsColor = 15
    elif image1.imageBitsColor[0] == 8:
        maxBitsColor = 255

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempPow = image1.imageData[i][j][0]
            if tempPow > fmaximage:
                fmaximage = tempPow

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempPow = image1.imageData[i][j][0]

            if tempPow == maxBitsColor:
                tempPow = maxBitsColor
            elif tempPow == 0:
                tempPow = 0
            else:
                tempPow = pow(image1.imageData[i][j][0] / fmaximage, p) * maxBitsColor

            image1.imageData[i][j][0] = ceil(tempPow)

            if tempPow > fmax:
                fmax = tempPow

            if tempPow < fmin:
                fmin = tempPow

    writeTiff('pow_image', image1)
    # normalizacja
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            image1.imageData[i][j][0] = round(maxBitsColor * ((image1.imageData[i][j][0] - fmin) / (fmax - fmin)))

    writeTiff('normalization_pow_image', image1)

