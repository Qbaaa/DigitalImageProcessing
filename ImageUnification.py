# ZADANIE 1

import numpy as np


# PUNKT 1 OK
def unification_Grayscale_Geometric(image1, image2):

    if (image1.imageColor == 0 or image1.imageColor == 1) and (image2.imageColor == 0 or image2.imageColor == 1):

        width1 = image1.imageWidth
        width2 = image2.imageWidth
        lenght1 = image1.imageLength
        lenght2 = image2.imageLength
        maxWidth = width1 if width1 > width2 else width2
        maxLenght = lenght1 if lenght1 > lenght2 else lenght2

        if image1.imageLength > image2.imageLength:
            print("Dlugosc obrazu 1 jest wieksza.")

            for i in range(image2.imageLength, image1.imageLength):
                image2.imageData.append([[1]])
                for j in range(image2.imageWidth-1):
                    image2.imageData[i].append([1])

            image2.imageLength = image1.imageLength

        else:
            if image1.imageLength < image2.imageLength:
                print("Dlugosc obrazu 2 jest wieksza.")

                for i in range(image1.imageLength, image2.imageLength):
                    image1.imageData.append([[1]])
                    for j in range(image1.imageWidth-1):
                        image1.imageData[i].append([1])

                image1.imageLength = image2.imageLength

            else:
                print("Dlugosc obrazu 1 i 2 jest równa.")

        if image1.imageWidth > image2.imageWidth:
            print("Szerokosc obrazu 1 jest wieksza.")

            for i in range(image2.imageLength):
                for j in range(image2.imageWidth, image1.imageWidth):
                    image2.imageData[i].append([1])

            image2.imageWidth = image1.imageWidth

        else:
            if image1.imageWidth < image2.imageWidth:
                print("Szerokosc obrazu 2 jest wieksza.")

                for i in range(image1.imageLength):
                    for j in range(image1.imageWidth, image2.imageWidth):
                        image1.imageData[i].append([1])

                image1.imageWidth = image2.imageWidth

            else:
                print("Szerokosc obrazu 1 i 2 jest równa.")

        tempImage1 = np.ones((maxLenght, maxWidth), dtype=np.uint8)
        tempImage2 = np.ones((maxLenght, maxWidth), dtype=np.uint8)

        startWidthCenter1 = int(round((maxWidth - width1) / 2))
        startLenghtCenter1 = int(round((maxLenght - lenght1) / 2))

        startWidthCenter2 = int(round((maxWidth - width2) / 2))
        startLenghtCenter2 = int(round((maxLenght - lenght2) / 2))

        for i in range(lenght1):
            for j in range(width1):
                tempImage1[i + startLenghtCenter1, j + startWidthCenter1] = image1.imageData[i][j][0]

        for i in range(lenght2):
            for j in range(width2):
                tempImage2[i + startLenghtCenter2, j + startWidthCenter2] = image2.imageData[i][j][0]

        for i in range(maxLenght):
            for j in range(maxWidth):
                image1.imageData[i][j][0] = int(tempImage1[i, j])
                image2.imageData[i][j][0] = int(tempImage2[i, j])

    else:
        raise Exception("Ta funkcja służy do ujednolicenia geometrycznie obrazów SZARYCH, a ktorys obraz jest RGB.")


# PUNKT 3 OK
def unification_RGB_Geometric(image1, image2):

    width1 = image1.imageWidth
    width2 = image2.imageWidth
    lenght1 = image1.imageLength
    lenght2 = image2.imageLength
    maxWidth = width1 if width1 > width2 else width2
    maxLenght = lenght1 if lenght1 > lenght2 else lenght2

    if image1.imageColor == 2 and image2.imageColor == 2:

        if image1.imageLength > image2.imageLength:
            print("Dlugosc obrazu 1 jest wieksza.")

            for i in range(image2.imageLength, image1.imageLength):
                image2.imageData.append([[1, 1, 1]])
                for j in range(image2.imageWidth-1):
                    image2.imageData[i].append([1, 1, 1])

            image2.imageLength = image1.imageLength

        else:
            if image1.imageLength < image2.imageLength:
                print("Dlugosc obrazu 2 jest wieksza.")

                for i in range(image1.imageLength, image2.imageLength):
                    image1.imageData.append([[1, 1, 1]])
                    for j in range(image1.imageWidth-1):
                        image1.imageData[i].append([1, 1, 1])

                image1.imageLength = image2.imageLength

            else:
                print("Dlugosc obrazu 1 i 2 jest równa.")

        if image1.imageWidth > image2.imageWidth:
            print("Szerokosc obrazu 1 jest wieksza.")

            for i in range(image2.imageLength):
                for j in range(image2.imageWidth, image1.imageWidth):
                    image2.imageData[i].append([1, 1, 1])

            image2.imageWidth = image1.imageWidth

        else:
            if image1.imageWidth < image2.imageWidth:
                print("Szerokosc obrazu 2 jest wieksza.")

                for i in range(image1.imageLength):
                    for j in range(image1.imageWidth, image2.imageWidth):
                        image1.imageData[i].append([1, 1, 1])

                image1.imageWidth = image2.imageWidth

            else:
                print("Szerokosc obrazu 1 i 2 jest równa.")

        tempImage1 = np.ones((maxLenght, maxWidth, 3), dtype=np.uint8)
        tempImage2 = np.ones((maxLenght, maxWidth, 3), dtype=np.uint8)

        startWidthCenter1 = int(round((maxWidth - width1) / 2))
        startLenghtCenter1 = int(round((maxLenght - lenght1) / 2))

        startWidthCenter2 = int(round((maxWidth - width2) / 2))
        startLenghtCenter2 = int(round((maxLenght - lenght2) / 2))

        for i in range(lenght1):
            for j in range(width1):
                tempImage1[i + startLenghtCenter1, j + startWidthCenter1] = image1.imageData[i][j]

        for i in range(lenght2):
            for j in range(width2):
                tempImage2[i + startLenghtCenter2, j + startWidthCenter2] = image2.imageData[i][j]

        for i in range(maxLenght):
            for j in range(maxWidth):
                for k in range(3):
                    image1.imageData[i][j][k] = int(tempImage1[i, j, k])
                    image2.imageData[i][j][k] = int(tempImage2[i, j, k])

    else:
        raise Exception("Ta funkcja służy do ujednolicenia geometrycznie obrazów RGB, a ktorys obraz jest SZARY.")


# PUNKT 4 OK
def unification_RGB_Resolution(image1, image2):

    if image1.imageColor == 2 and image2.imageColor == 2:

        width1 = image1.oldImageWidth
        width2 = image2.oldImageWidth
        lenght1 = image1.oldImageLength
        lenght2 = image2.oldImageLength

        if lenght1 > lenght2:
            scaleLenght1 = 1
            scaleLenght2 = lenght1/lenght2
        else:
            scaleLenght1 = lenght2/lenght1
            scaleLenght2 = 1

        if width1 > width2:
            scaleWidth1 = 1
            scaleWidth2 = width1 / width2
        else:
            scaleWidth1 = width2 / width1
            scaleWidth2 = 1

        if image1.imageBitsColor[0] != image2.imageBitsColor[0]:

            if image1.imageBitsColor[0] == 4:
                for i in range(image1.imageLength):
                    for j in range(image1.imageWidth):
                        for k in range(3):
                            image1.imageData[i][j][k] = image1.imageData[i][j][k] * 16
                for l in range(3):
                    image1.imageBitsColor[l] = 8

            else:
                if image2.imageBitsColor[0] == 4:
                    for i in range(image2.imageLength):
                        for j in range(image2.imageWidth):
                            for k in range(3):
                                image2.imageData[i][j][k] = image2.imageData[i][j][k] * 16
                    for l in range(3):
                        image2.imageBitsColor[l] = 8

                else:
                    raise Exception("programu 3")

        else:
            print("Rozdzielczosc obrazow 1 i 2 RGB jest taka sama.")

        tempImage1 = np.zeros((image1.imageLength, image1.imageWidth, 3), dtype=np.uint8)
        tempImage2 = np.zeros((image2.imageLength, image2.imageWidth, 3), dtype=np.uint8)
        temp = np.zeros((image1.imageLength, image1.imageWidth, 3), dtype=np.uint8)

        for i in range(lenght1):
            for j in range(width1):
                tempImage1[int(scaleLenght1*i), int(round(scaleWidth1*j))] = image1.oldImageData[i][j]

        for i in range(lenght2):
            for j in range(width2):
                tempImage2[int(scaleLenght2*i), int(round(scaleWidth2*j))] = image2.oldImageData[i][j]

        for i in range(image2.imageLength):
            for j in range(image2.imageWidth):
                r, g, b = 0, 0, 0
                n = 0
                temp[i, j] = tempImage2[i, j]

                if (tempImage2[i, j][0] < 1) & (tempImage2[i, j][1] < 1) & (tempImage2[i, j][2] < 1):
                    for iOff in range(-1, 2):
                        for jOff in range(-1, 2):
                            iSafe = i if ((i + iOff) > (lenght1 - 2)) | ((i + iOff) < 0) else (i + iOff)
                            jSafe = j if ((j + jOff) > (width1 - 2)) | ((j + jOff) < 0) else (j + jOff)

                            if (tempImage2[iSafe, jSafe][0] > 0) | (tempImage2[iSafe, jSafe][1] > 0) | (tempImage2[iSafe, jSafe][2] > 0):
                                r += tempImage2[iSafe, jSafe][0]
                                g += tempImage2[iSafe, jSafe][1]
                                b += tempImage2[iSafe, jSafe][2]
                                n += 1
                                temp[i, j] = (r/n, g/n, b/n)
                tempImage2[i, j] = temp[i, j]

        for i in range(image1.imageLength):
            for j in range(image1.imageWidth):
                r, g, b = 0, 0, 0
                n = 0
                temp[i, j] = tempImage1[i, j]

                if (tempImage1[i, j][0] < 1) & (tempImage1[i, j][1] < 1) & (tempImage1[i, j][2] < 1):
                    for iOff in range(-1, 2):
                        for jOff in range(-1, 2):
                            iSafe = i if ((i + iOff) > (lenght2 - 2)) | ((i + iOff) < 0) else (i + iOff)
                            jSafe = j if ((j + jOff) > (width2 - 2)) | ((j + jOff) < 0) else (j + jOff)

                            if (tempImage1[iSafe, jSafe][0] > 0) | (tempImage1[iSafe, jSafe][1] > 0) | (tempImage1[iSafe, jSafe][2] > 0):
                                r += tempImage1[iSafe, jSafe][0]
                                g += tempImage1[iSafe, jSafe][1]
                                b += tempImage1[iSafe, jSafe][2]
                                n += 1
                                temp[i, j] = (r/n, g/n, b/n)
                tempImage1[i, j] = temp[i, j]

        for i in range(image1.imageLength):
            for j in range(image1.imageWidth):
                for k in range(3):
                    image1.imageData[i][j][k] = int(tempImage1[i, j, k])
                    image2.imageData[i][j][k] = int(tempImage2[i, j, k])

    else:
        raise Exception("Ta funkcja służy do ujednolicenia rozdzielczosciowo obrazów RGB, a ktorys obraz jest SZARY.")


# PUNKT 2 OK
def unification_Grayscale_Resolution(image1, image2):
    width1 = image1.oldImageWidth
    width2 = image2.oldImageWidth
    lenght1 = image1.oldImageLength
    lenght2 = image2.oldImageLength

    if lenght1 > lenght2:
        scaleLenght1 = 1
        scaleLenght2 = lenght1/lenght2
    else:
        scaleLenght1 = lenght2/lenght1
        scaleLenght2 = 1

    if width1 > width2:
        scaleWidth1 = 1
        scaleWidth2 = width1 / width2
    else:
        scaleWidth1 = width2 / width1
        scaleWidth2 = 1

    if (image1.imageColor == 0 or image1.imageColor == 1) and (image2.imageColor == 0 or image2.imageColor == 1):

        if image1.imageBitsColor[0] != image2.imageBitsColor[0]:

            if image1.imageBitsColor[0] == 4:
                for i in range(image1.imageLength):
                    for j in range(image1.imageWidth):
                        image1.imageData[i][j][0] = image1.imageData[i][j][0] * 16
                image1.imageBitsColor[0] = 8

            else:
                if image2.imageBitsColor[0] == 4:
                    for i in range(image2.imageLength):
                        for j in range(image2.imageWidth):
                            image2.imageData[i][j][0] = image2.imageData[i][j][0] * 16
                    image2.imageBitsColor[0] = 8

                else:
                    raise Exception("programu 3")

        else:
            print("Rozdzielczosc obrazow 1 i 2 SZARYCH jest taka sama.")

        if image1.imageColor != image2.imageColor:

            if image1.imageColor == 0:
                if image1.imageBitsColor[0] == 8:
                    for i in range(image1.imageLength):
                        for j in range(image1.imageWidth):
                            image1.imageData[i][j][0] = 255 - image1.imageData[i][j][0]
                else:
                    if image1.imageBitsColor[0] == 4:
                        for i in range(image1.imageLength):
                            for j in range(image1.imageWidth):
                                image1.imageData[i][j][0] = 15 - image1.imageData[i][j][0]
                    else:
                        raise Exception("programu 4")
                image1.imageColor = 1

            else:
                if image2.imageColor == 0:
                    if image2.imageBitsColor[0] == 8:
                        for i in range(image2.imageLength):
                            for j in range(image2.imageWidth):
                                image2.imageData[i][j][0] = 255 - image2.imageData[i][j][0]
                    else:
                        if image2.imageBitsColor[0] == 4:
                            for i in range(image2.imageLength):
                                for j in range(image2.imageWidth):
                                    image2.imageData[i][j][0] = 15 - image2.imageData[i][j][0]
                        else:
                            raise Exception("programu 5")
                    image2.imageColor = 1
                else:
                    raise Exception("programu 6")

        tempImage1 = np.zeros((image1.imageLength, image1.imageWidth), dtype=np.uint8)
        tempImage2 = np.zeros((image2.imageLength, image2.imageWidth), dtype=np.uint8)
        temp = np.zeros((image1.imageLength, image1.imageWidth), dtype=np.uint8)

        for i in range(lenght1):
            for j in range(width1):
                tempImage1[int(scaleLenght1*i), int(round(scaleWidth1*j))] = image1.oldImageData[i][j][0]

        for i in range(lenght2):
            for j in range(width2):
                tempImage2[int(scaleLenght2*i), int(round(scaleWidth2*j))] = image2.oldImageData[i][j][0]

        for i in range(image2.imageLength):
            for j in range(image2.imageWidth):
                gray = 0
                n = 0
                temp[i, j] = tempImage2[i, j]

                if tempImage2[i, j] < 1:
                    for iOff in range(-1, 2):
                        for jOff in range(-1, 2):
                            iSafe = i if ((i + iOff) > (lenght1 - 2)) | ((i + iOff) < 0) else (i + iOff)
                            jSafe = j if ((j + jOff) > (width1 - 2)) | ((j + jOff) < 0) else (j + jOff)

                            if tempImage2[iSafe, jSafe] > 0:
                                gray += tempImage2[iSafe, jSafe]
                                n += 1
                                temp[i, j] = gray/n
                tempImage2[i, j] = temp[i, j]

        for i in range(image1.imageLength):
            for j in range(image1.imageWidth):
                gray = 0
                n = 0
                temp[i, j] = tempImage1[i, j]

                if tempImage1[i, j] < 1:
                    for iOff in range(-1, 2):
                        for jOff in range(-1, 2):
                            iSafe = i if ((i + iOff) > (lenght2 - 2)) | ((i + iOff) < 0) else (i + iOff)
                            jSafe = j if ((j + jOff) > (width2 - 2)) | ((j + jOff) < 0) else (j + jOff)

                            if tempImage1[iSafe, jSafe] > 0:
                                gray += tempImage1[iSafe, jSafe]
                                n += 1
                                temp[i, j] = gray/n
                tempImage1[i, j] = temp[i, j]

        for i in range(image1.imageLength):
            for j in range(image1.imageWidth):
                image1.imageData[i][j][0] = int(tempImage1[i, j])
                image2.imageData[i][j][0] = int(tempImage2[i, j])

    else:
        raise Exception("Ta funkcja służy do ujednolicenia rozdzielczosciowo obrazów SZARYCH, a ktorys obraz jest RGB.")