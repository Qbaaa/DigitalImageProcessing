# ZADANIE 3

from math import ceil, log
from WriteTiff import writeTiff


# sumowanie obrazu ze stala
def sum_const_RGB(image1, const=0):

    if image1.imageBitsColor[0] == 4:

        maxBitsColor = 15
        if not (0 <= const <= 15):
            raise Exception("program do obrazow RGB 4 bitowych mozne dodac liczbe z zakresu 0-15, a podana liczba "
                            "to %d." % const)
    else:
        if image1.imageBitsColor[0] == 8:

            maxBitsColor = 255
            if not (0 <= const <= 255):
                raise Exception("program do obrazow RGB 8 bitowych mozne dodac liczbe z zakresu 0-255, a podana "
                                "podana to %d." % const)
        else:
            raise Exception("program dodaje jedynie obrazy RGB 4, 8 bitowe ze stala")

    Qmax = 0
    Dmax = 0
    X = 0
    fmax = 0
    fmin = 256

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempR = image1.imageData[i][j][0] + const
            tempG = image1.imageData[i][j][1] + const
            tempB = image1.imageData[i][j][2] + const

            if max([tempR, tempG, tempB]) > Qmax:
                Qmax = max([tempR, tempG, tempB])

    if Qmax > maxBitsColor:
        Dmax = Qmax - maxBitsColor
        X = round(Dmax/maxBitsColor, 2)

    if X == 1.0:
        X = 0.99

    print(X)
    # dodawanie
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempSumR = ceil((image1.imageData[i][j][0] - (image1.imageData[i][j][0] * X)) + (const - (const * X)))
            tempSumG = ceil((image1.imageData[i][j][1] - (image1.imageData[i][j][1] * X)) + (const - (const * X)))
            tempSumB = ceil((image1.imageData[i][j][2] - (image1.imageData[i][j][2] * X)) + (const - (const * X)))

            image1.imageData[i][j][0] = tempSumR
            image1.imageData[i][j][1] = tempSumG
            image1.imageData[i][j][2] = tempSumB

            if max([tempSumR, tempSumG, tempSumB]) > fmax:
                fmax = max([tempSumR, tempSumG, tempSumB])

            if min([tempSumR, tempSumG, tempSumB]) < fmin:
                fmin = min([tempSumR, tempSumG, tempSumB])

    writeTiff('add_const_RGB', image1)

    # normalizacja
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            image1.imageData[i][j][0] = ceil(maxBitsColor * ((image1.imageData[i][j][0] - fmin) / (fmax - fmin)))
            image1.imageData[i][j][1] = ceil(maxBitsColor * ((image1.imageData[i][j][1] - fmin) / (fmax - fmin)))
            image1.imageData[i][j][2] = ceil(maxBitsColor * ((image1.imageData[i][j][2] - fmin) / (fmax - fmin)))
    writeTiff('normalization_add_const_RGB', image1)


# sumowanie dwoch obrazow
def sum_two_images_RGB(image1, image2):

    global maxBitsColor
    if image1.imageBitsColor[0] == image2.imageBitsColor[0] and (image1.imageLength == image2.imageLength) and (image1.imageWidth == image2.imageWidth):

        if image1.imageBitsColor[0] == 4:
            maxBitsColor = 15

        else:
            if image1.imageBitsColor[0] == 8:
                maxBitsColor = 255

    else:
        raise Exception("program dodaje jedynie obrazy RGB 4, 8 bitowe oraz obrazy musza miec takie same rozmiary.")

    Qmax = 0
    Dmax = 0
    X = 0
    fmax = 0
    fmin = 256

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempR = image1.imageData[i][j][0] + image2.imageData[i][j][0]
            tempG = image1.imageData[i][j][1] + image2.imageData[i][j][1]
            tempB = image1.imageData[i][j][2] + image2.imageData[i][j][2]

            if max([tempR, tempG, tempB]) > Qmax:
                Qmax = max([tempR, tempG, tempB])

    if Qmax > maxBitsColor:
        Dmax = Qmax - maxBitsColor
        X = round(Dmax/maxBitsColor, 2)

    if X == 1.0:
        X = 0.99

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempSumR = ceil((image1.imageData[i][j][0] - (image1.imageData[i][j][0] * X)) + (image2.imageData[i][j][0] - (image2.imageData[i][j][0] * X)))

            image1.imageData[i][j][0] = tempSumR

            tempSumG = ceil((image1.imageData[i][j][1] - (image1.imageData[i][j][1] * X)) + (image2.imageData[i][j][1] - (image2.imageData[i][j][1] * X)))
            image1.imageData[i][j][1] = tempSumG

            tempSumB = ceil((image1.imageData[i][j][2] - (image1.imageData[i][j][2] * X)) + (image2.imageData[i][j][2] - (image2.imageData[i][j][2] * X)))
            image1.imageData[i][j][2] = tempSumB

            if max([tempSumR, tempSumG, tempSumB]) > fmax:
                fmax = max([tempSumR, tempSumG, tempSumB])

            if min([tempSumR, tempSumG, tempSumB]) < fmin:
                fmin = min([tempSumR, tempSumG, tempSumB])

    writeTiff('add_two_image_RGB', image1)

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            image1.imageData[i][j][0] = ceil(maxBitsColor * ((image1.imageData[i][j][0] - fmin) / (fmax - fmin)))
            image1.imageData[i][j][1] = ceil(maxBitsColor * ((image1.imageData[i][j][1] - fmin) / (fmax - fmin)))
            image1.imageData[i][j][2] = ceil(maxBitsColor * ((image1.imageData[i][j][2] - fmin) / (fmax - fmin)))

    writeTiff('normalization_add_two_image_RGB', image1)


# mnozenie obrazu przez zadana stala
def multiplication_const_RGB(image1, const=1):

    fmax = 0
    fmin = 256

    if image1.imageBitsColor[0] == 4:

        maxBitsColor = 15
        if not (0 < const <= 15):
            raise Exception("program do obrazow RGB 4 bitowych moze pomnozyc liczbe z zakresu 0-15, a podana liczba "
                            "to %d." % const)
    else:
        if image1.imageBitsColor[0] == 8:

            maxBitsColor = 255
            if not (0 < const <= 255):
                raise Exception("program do obrazow RGB 8 bitowych moze pomnozyc liczbe z zakresu 0-255, a podana "
                                "podana to %d." % const)
        else:
            raise Exception("program mnozy jedynie obrazy RGB 4, 8 bitowe ze stala")

    # mnozenie
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempMultR = image1.imageData[i][j][0]
            tempMultG = image1.imageData[i][j][1]
            tempMultB = image1.imageData[i][j][2]

            if tempMultR == maxBitsColor:
                tempMultR = const
            elif tempMultR == 0:
                tempMultR = 0
            else:
                tempMultR = ceil((image1.imageData[i][j][0] * const) / maxBitsColor)

            if tempMultG == maxBitsColor:
                tempMultG = const
            elif tempMultG == 0:
                tempMultG = 0
            else:
                tempMultG = ceil((image1.imageData[i][j][1] * const) / maxBitsColor)

            if tempMultB == maxBitsColor:
                tempMultB = const
            elif tempMultB == 0:
                tempMultB = 0
            else:
                tempMultB = ceil((image1.imageData[i][j][2] * const) / maxBitsColor)

            image1.imageData[i][j][0] = tempMultR
            image1.imageData[i][j][1] = tempMultG
            image1.imageData[i][j][2] = tempMultB

            if max([tempMultR, tempMultG, tempMultB]) > fmax:
                fmax = max([tempMultR, tempMultG, tempMultB])

            if min([tempMultR, tempMultG, tempMultB]) < fmin:
                fmin = min([tempMultR, tempMultG, tempMultB])

    writeTiff('multi_const_RGB', image1)

    # normalizacja
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            image1.imageData[i][j][0] = round(maxBitsColor * ((image1.imageData[i][j][0] - fmin) / (fmax - fmin)))
            image1.imageData[i][j][1] = round(maxBitsColor * ((image1.imageData[i][j][1] - fmin) / (fmax - fmin)))
            image1.imageData[i][j][2] = round(maxBitsColor * ((image1.imageData[i][j][2] - fmin) / (fmax - fmin)))

    writeTiff('normalization_multi_const_RGB', image1)


# mnozenie dwoch obrazow
def multiplication_two_images_RGB(image1, image2):

    global maxBitsColor
    fmax = 0
    fmin = 256

    if image1.imageBitsColor[0] == image2.imageBitsColor[0] and (image1.imageLength == image2.imageLength) and (image1.imageWidth == image2.imageWidth):

        if image1.imageBitsColor[0] == 4:
            maxBitsColor = 15

        elif image1.imageBitsColor[0] == 8:
            maxBitsColor = 255

    else:
        raise Exception("program mnozy jedynie obrazy RGB 4, 8 bitowe oraz obrazy musza miec takie same rozmiary.")

    # mnozenie
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempMultR = image1.imageData[i][j][0]
            tempMultG = image1.imageData[i][j][1]
            tempMultB = image1.imageData[i][j][2]

            if tempMultR == maxBitsColor:
                tempMultR = image2.imageData[i][j][0]
            elif tempMultR == 0:
                tempMultR = 0
            else:
                tempMultR = ceil((image1.imageData[i][j][0] * image2.imageData[i][j][0]) / maxBitsColor)

            if tempMultG == maxBitsColor:
                tempMultG = image2.imageData[i][j][1]
            elif tempMultG == 0:
                tempMultG = 0
            else:
                tempMultG = ceil((image1.imageData[i][j][1] * image2.imageData[i][j][1]) / maxBitsColor)

            if tempMultB == maxBitsColor:
                tempMultB = image2.imageData[i][j][2]
            elif tempMultB == 0:
                tempMultB = 0
            else:
                tempMultB = ceil((image1.imageData[i][j][2] * image2.imageData[i][j][2]) / maxBitsColor)

            image1.imageData[i][j][0] = tempMultR
            image1.imageData[i][j][1] = tempMultG
            image1.imageData[i][j][2] = tempMultB

            if max([tempMultR, tempMultG, tempMultB]) > fmax:
                fmax = max([tempMultR, tempMultG, tempMultB])

            if min([tempMultR, tempMultG, tempMultB]) < fmin:
                fmin = min([tempMultR, tempMultG, tempMultB])

    writeTiff('multi_two_images_RGB', image1)

    # normalizacja
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            image1.imageData[i][j][0] = round(maxBitsColor * ((image1.imageData[i][j][0] - fmin) / (fmax - fmin)))
            image1.imageData[i][j][1] = round(maxBitsColor * ((image1.imageData[i][j][1] - fmin) / (fmax - fmin)))
            image1.imageData[i][j][2] = round(maxBitsColor * ((image1.imageData[i][j][2] - fmin) / (fmax - fmin)))

    writeTiff('normalization_multi_two_images_RGB', image1)


# mieszanie obrazow z okreslonym wspolczynnikiem
def mixing_images_RGB(image1, image2, scales=0.0):

    global maxBitsColor
    fmax = 0
    fmin = 256

    if image1.imageBitsColor[0] == image2.imageBitsColor[0] and (image1.imageLength == image2.imageLength) and (image1.imageWidth == image2.imageWidth):

        if not (0.0 <= scales <= 1.0):
            raise Exception("program miesza obrazy RGB z waga z zakresu 0.0-1.0, a podana liczba "
                            "to %f." % scales)

        if image1.imageBitsColor[0] == 4:
            maxBitsColor = 15

        elif image1.imageBitsColor[0] == 8:
            maxBitsColor = 255

    else:
        raise Exception("program miesza jedynie obrazy RGB 4, 8 bitowe oraz obrazy musza miec takie same rozmiary.")

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempMixR = ceil(scales * image1.imageData[i][j][0] + (1 - scales) * image2.imageData[i][j][0])
            tempMixG = ceil(scales * image1.imageData[i][j][1] + (1 - scales) * image2.imageData[i][j][1])
            tempMixB = ceil(scales * image1.imageData[i][j][2] + (1 - scales) * image2.imageData[i][j][2])

            image1.imageData[i][j][0] = tempMixR
            image1.imageData[i][j][1] = tempMixG
            image1.imageData[i][j][2] = tempMixB

            if max([tempMixR, tempMixG, tempMixB]) > fmax:
                fmax = max([tempMixR, tempMixG, tempMixB])

            if min([tempMixR, tempMixG, tempMixB]) < fmin:
                fmin = min([tempMixR, tempMixG, tempMixB])

    writeTiff('mix_two_image_RGB', image1)
    # normalizacja
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            image1.imageData[i][j][0] = round(maxBitsColor * ((image1.imageData[i][j][0] - fmin) / (fmax - fmin)))
            image1.imageData[i][j][1] = round(maxBitsColor * ((image1.imageData[i][j][1] - fmin) / (fmax - fmin)))
            image1.imageData[i][j][2] = round(maxBitsColor * ((image1.imageData[i][j][2] - fmin) / (fmax - fmin)))

    writeTiff('normalization_mix_two_image_RGB', image1)


# potegowanie obrazu (z zadana potega)
def pow_image_RGB(image1, p=1):

    global maxBitsColor
    fmax = 0
    fmin = 256
    fmaximage = 0

    if not (0 < p):
        raise Exception("program poteguje obraz SZARY z zadana potega z zakresu p > 0, a podana liczba "
                        "to %d." % p)

    if image1.imageBitsColor[0] == 4:
        maxBitsColor = 15
    elif image1.imageBitsColor[0] == 8:
        maxBitsColor = 255

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempPowR = image1.imageData[i][j][0]
            tempPowG = image1.imageData[i][j][1]
            tempPowB = image1.imageData[i][j][2]

            if max([tempPowR, tempPowG, tempPowB]) > fmaximage:
                fmaximage = max([tempPowR, tempPowG, tempPowB])

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempPowR = image1.imageData[i][j][0]
            tempPowG = image1.imageData[i][j][1]
            tempPowB = image1.imageData[i][j][2]

            if tempPowR == maxBitsColor:
                tempPowR = maxBitsColor
            elif tempPowR == 0:
                tempPowR = 0
            else:
                tempPowR = ceil(pow(image1.imageData[i][j][0] / fmaximage, p) * maxBitsColor)

            if tempPowG == maxBitsColor:
                tempPowG = maxBitsColor
            elif tempPowG == 0:
                tempPowG = 0
            else:
                tempPowG = ceil(pow(image1.imageData[i][j][1] / fmaximage, p) * maxBitsColor)

            if tempPowB == maxBitsColor:
                tempPowB = maxBitsColor
            elif tempPowB == 0:
                tempPowB = 0
            else:
                tempPowB = ceil(pow(image1.imageData[i][j][2] / fmaximage, p) * maxBitsColor)

            image1.imageData[i][j][0] = tempPowR
            image1.imageData[i][j][1] = tempPowG
            image1.imageData[i][j][2] = tempPowB

            if max([tempPowR, tempPowG, tempPowB]) > fmax:
                fmax = max([tempPowR, tempPowG, tempPowB])

            if min([tempPowR, tempPowG, tempPowB]) < fmin:
                fmin = min([tempPowR, tempPowG, tempPowB])

    writeTiff('pow_image_RGB', image1)
    # normalizacja
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            image1.imageData[i][j][0] = round(maxBitsColor * ((image1.imageData[i][j][0] - fmin) / (fmax - fmin)))
            image1.imageData[i][j][1] = round(maxBitsColor * ((image1.imageData[i][j][1] - fmin) / (fmax - fmin)))
            image1.imageData[i][j][2] = round(maxBitsColor * ((image1.imageData[i][j][2] - fmin) / (fmax - fmin)))

    writeTiff('normalization_pow_image_RGB', image1)


# dzielenie obrazu przez (zadana) liczbe
def division_const_RGB(image1, const=1):

    Qmax = 0
    fmax = 0
    fmin = 256

    if image1.imageBitsColor[0] == 4:

        maxBitsColor = 15
        if not (0 < const <= 15):
            raise Exception("program do obrazow RGB 4 bitowych moze dzielic liczbe z zakresu 0-15, a podana liczba "
                            "to %d." % const)
    elif image1.imageBitsColor[0] == 8:

        maxBitsColor = 255
        if not (0 < const <= 255):
            raise Exception("program do obrazow RGB 8 bitowych moze dzielic liczbe z zakresu 0-255, a podana "
                            "podana to %d." % const)
    else:
        raise Exception("program dzieli jedynie obrazy RGB 4, 8 bitowe ze stala")

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempDivR = image1.imageData[i][j][0] + const
            tempDivG = image1.imageData[i][j][1] + const
            tempDivB = image1.imageData[i][j][2] + const

            if Qmax < max([tempDivR, tempDivG, tempDivB]):
                Qmax = max([tempDivR, tempDivG, tempDivB])

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempDivR = image1.imageData[i][j][0] + const
            tempDivG = image1.imageData[i][j][1] + const
            tempDivB = image1.imageData[i][j][2] + const

            resultDivR = ceil((tempDivR * maxBitsColor) / Qmax)
            resultDivG = ceil((tempDivG * maxBitsColor) / Qmax)
            resultDivB = ceil((tempDivB * maxBitsColor) / Qmax)

            image1.imageData[i][j][0] = resultDivR
            image1.imageData[i][j][1] = resultDivG
            image1.imageData[i][j][2] = resultDivB


            if max([resultDivR, resultDivG, resultDivB]) > fmax:
                fmax = max([resultDivR, resultDivG, resultDivB])

            if min([resultDivR, resultDivG, resultDivB]) < fmin:
                fmin = min([resultDivR, resultDivG, resultDivB])

    writeTiff('div_image_const', image1)
    # normalizacja
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            image1.imageData[i][j][0] = round(maxBitsColor * ((image1.imageData[i][j][0] - fmin) / (fmax - fmin)))

    writeTiff('normalization_div_image_const', image1)


# dzielenie obrazu przez inny obraz
def division_two_iamges_RGB(image1, image2):

    global maxBitsColor
    fmax = 0
    fmin = 256
    Qmax = 0

    if image1.imageBitsColor[0] == image2.imageBitsColor[0] and (image1.imageLength == image2.imageLength) and (image1.imageWidth == image2.imageWidth):

        if image1.imageBitsColor[0] == 4:
            maxBitsColor = 15

        elif image1.imageBitsColor[0] == 8:
            maxBitsColor = 255

    else:
        raise Exception("program dzieli jedynie obrazy RGB 4, 8 bitowe oraz obrazy musza miec takie same rozmiary.")

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempDivR = image1.imageData[i][j][0] + image2.imageData[i][j][0]
            tempDivG = image1.imageData[i][j][1] + image2.imageData[i][j][1]
            tempDivB = image1.imageData[i][j][2] + image2.imageData[i][j][2]

            if Qmax < max([tempDivR, tempDivG, tempDivB]):
                Qmax = max([tempDivR, tempDivG, tempDivB])

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempDivR = image1.imageData[i][j][0] + image2.imageData[i][j][0]
            tempDivG = image1.imageData[i][j][1] + image2.imageData[i][j][1]
            tempDivB = image1.imageData[i][j][2] + image2.imageData[i][j][2]

            resultDivR = ceil((tempDivR * maxBitsColor) / Qmax)
            resultDivG = ceil((tempDivG * maxBitsColor) / Qmax)
            resultDivB = ceil((tempDivB * maxBitsColor) / Qmax)

            image1.imageData[i][j][0] = resultDivR
            image1.imageData[i][j][1] = resultDivG
            image1.imageData[i][j][2] = resultDivB

            if max([resultDivR, resultDivG, resultDivB]) > fmax:
                fmax = max([resultDivR, resultDivG, resultDivB])

            if min([resultDivR, resultDivG, resultDivB]) < fmin:
                fmin = min([resultDivR, resultDivG, resultDivB])

    writeTiff('div_two_images_RGB', image1)
    # normalizacja
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            image1.imageData[i][j][0] = round(maxBitsColor * ((image1.imageData[i][j][0] - fmin) / (fmax - fmin)))
            image1.imageData[i][j][1] = round(maxBitsColor * ((image1.imageData[i][j][1] - fmin) / (fmax - fmin)))
            image1.imageData[i][j][2] = round(maxBitsColor * ((image1.imageData[i][j][2] - fmin) / (fmax - fmin)))

    writeTiff('normalization_div_two_images_RGB', image1)


# pierwiastkowanie obrazu
def sqrt_image_RGB(image1, deg=1):

    global maxBitsColor
    fmax = 0
    fmin = 256
    fmaximage = 0

    p = 1/deg

    if image1.imageBitsColor[0] == 4:
        maxBitsColor = 15
    elif image1.imageBitsColor[0] == 8:
        maxBitsColor = 255

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempPowR = image1.imageData[i][j][0]
            tempPowG = image1.imageData[i][j][1]
            tempPowB = image1.imageData[i][j][2]

            if max([tempPowR, tempPowG, tempPowB]) > fmaximage:
                fmaximage = max([tempPowR, tempPowG, tempPowB])

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempPowR = image1.imageData[i][j][0]
            tempPowG = image1.imageData[i][j][1]
            tempPowB = image1.imageData[i][j][2]

            if tempPowR == maxBitsColor:
                tempPowR = maxBitsColor
            elif tempPowR == 0:
                tempPowR = 0
            else:
                tempPowR = ceil(pow(image1.imageData[i][j][0] / fmaximage, p) * maxBitsColor)

            if tempPowG == maxBitsColor:
                tempPowG = maxBitsColor
            elif tempPowG == 0:
                tempPowG = 0
            else:
                tempPowG = ceil(pow(image1.imageData[i][j][0] / fmaximage, p) * maxBitsColor)

            if tempPowB == maxBitsColor:
                tempPowB = maxBitsColor
            elif tempPowB == 0:
                tempPowB = 0
            else:
                tempPowB = ceil(pow(image1.imageData[i][j][0] / fmaximage, p) * maxBitsColor)

            image1.imageData[i][j][0] = tempPowR
            image1.imageData[i][j][1] = tempPowG
            image1.imageData[i][j][2] = tempPowB

            if max([tempPowR, tempPowG, tempPowB]) > fmax:
                fmax = max([tempPowR, tempPowG, tempPowB])

            if min([tempPowR, tempPowG, tempPowB]) < fmin:
                fmin = min([tempPowR, tempPowG, tempPowB])

    writeTiff('root_image_RGB', image1)
    # normalizacja
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            image1.imageData[i][j][0] = round(maxBitsColor * ((image1.imageData[i][j][0] - fmin) / (fmax - fmin)))
            image1.imageData[i][j][1] = round(maxBitsColor * ((image1.imageData[i][j][1] - fmin) / (fmax - fmin)))
            image1.imageData[i][j][2] = round(maxBitsColor * ((image1.imageData[i][j][2] - fmin) / (fmax - fmin)))

    writeTiff('normalization_root_image_RGB', image1)


# logarytmowanie obrazu
def log_image_RGB(image1):

    global maxBitsColor
    fmax = 0
    fmin = 256
    fmaximage = 0

    if image1.imageBitsColor[0] == 4:
        maxBitsColor = 15
    elif image1.imageBitsColor[0] == 8:
        maxBitsColor = 255

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempLogR = image1.imageData[i][j][0]
            tempLogG = image1.imageData[i][j][1]
            tempLogB = image1.imageData[i][j][2]

            if fmaximage < max([tempLogR, tempLogG, tempLogB]):
                fmaximage = max([tempLogR, tempLogG, tempLogB])

    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            tempLogR = image1.imageData[i][j][0]
            tempLogG = image1.imageData[i][j][1]
            tempLogB = image1.imageData[i][j][2]

            if tempLogR == 0:
                tempLogR = 0
            else:
                tempLogR = ceil((log(1 + tempLogR) / log(1 + fmaximage)) * maxBitsColor)

            if tempLogG == 0:
                tempLogG = 0
            else:
                tempLogG = ceil((log(1 + tempLogG) / log(1 + fmaximage)) * maxBitsColor)

            if tempLogB == 0:
                tempLogB = 0
            else:
                tempLogB = ceil((log(1 + tempLogB) / log(1 + fmaximage)) * maxBitsColor)

            image1.imageData[i][j][0] = tempLogR
            image1.imageData[i][j][1] = tempLogG
            image1.imageData[i][j][2] = tempLogB

            if max([tempLogR, tempLogG, tempLogB]) > fmax:
                fmax = max([tempLogR, tempLogG, tempLogB])

            if min([tempLogR, tempLogG, tempLogB]) < fmin:
                fmin = min([tempLogR, tempLogG, tempLogB])

    writeTiff('log_image_RGB', image1)
    # normalizacja
    for i in range(image1.imageLength):
        for j in range(image1.imageWidth):
            image1.imageData[i][j][0] = round(maxBitsColor * ((image1.imageData[i][j][0] - fmin) / (fmax - fmin)))
            image1.imageData[i][j][1] = round(maxBitsColor * ((image1.imageData[i][j][1] - fmin) / (fmax - fmin)))
            image1.imageData[i][j][2] = round(maxBitsColor * ((image1.imageData[i][j][2] - fmin) / (fmax - fmin)))

    writeTiff('normalization_log_image_RGB', image1)