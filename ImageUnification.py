# ZADANIE 1

import numpy as np


# PUNKT 1 OK
def unification_Grayscale_Geometric(image1, image2):

    if (image1.imageColor == 0 or image1.imageColor == 1) and (image2.imageColor == 0 or image2.imageColor == 1):

        # Wybranie największej szerokości i wysokości z dwóch obrazów
        #width1 = image1.imageWidth
        #width2 = image2.imageWidth
        #lenght1 = image1.imageLength
        #lenght2 = image2.imageLength
        #maxWidth = width1 if width1 > width2 else width2
        #maxLenght = lenght1 if lenght1 > lenght2 else lenght2

        # Dodanie i wypełnienie różnicę pikselami o wartości 1 w obrazie 2, który ma mniejszą wysokość.
        if image1.imageLength > image2.imageLength:
            print("Dlugosc obrazu 1 jest wieksza.")

            for i in range(image2.imageLength, image1.imageLength):
                image2.imageData.append([[1]])
                for j in range(image2.imageWidth-1):
                    image2.imageData[i].append([1])

            image2.imageLength = image1.imageLength

        else:
            # Dodanie i wypełnienie różnicę pikselami o wartości 1 w obrazie 1, który ma mniejszą wysokość.
            if image1.imageLength < image2.imageLength:
                print("Dlugosc obrazu 2 jest wieksza.")

                for i in range(image1.imageLength, image2.imageLength):
                    image1.imageData.append([[1]])
                    for j in range(image1.imageWidth-1):
                        image1.imageData[i].append([1])

                image1.imageLength = image2.imageLength

            else:
                print("Dlugosc obrazu 1 i 2 jest równa.")

        # Dodanie i wypełnienie różnicę pikselami o wartości 1 w obrazie 2, który ma mniejszą szerokość.
        if image1.imageWidth > image2.imageWidth:
            print("Szerokosc obrazu 1 jest wieksza.")

            for i in range(image2.imageLength):
                for j in range(image2.imageWidth, image1.imageWidth):
                    image2.imageData[i].append([1])

            image2.imageWidth = image1.imageWidth

        else:
            # Dodanie i wypełnienie różnicę pikselami o wartości 1 w obrazie 1, który ma mniejszą szerokość.
            if image1.imageWidth < image2.imageWidth:
                print("Szerokosc obrazu 2 jest wieksza.")

                for i in range(image1.imageLength):
                    for j in range(image1.imageWidth, image2.imageWidth):
                        image1.imageData[i].append([1])

                image1.imageWidth = image2.imageWidth

            else:
                print("Szerokosc obrazu 1 i 2 jest równa.")

        # Umieszczenie obrazu na środku macierzy w powiększonym obrazie
        # tempImage1 = np.ones((maxLenght, maxWidth), dtype=np.uint8)
        # tempImage2 = np.ones((maxLenght, maxWidth), dtype=np.uint8)
        #
        # startWidthCenter1 = int(round((maxWidth - width1) / 2))
        # startLenghtCenter1 = int(round((maxLenght - lenght1) / 2))
        #
        # startWidthCenter2 = int(round((maxWidth - width2) / 2))
        # startLenghtCenter2 = int(round((maxLenght - lenght2) / 2))
        #
        # for i in range(lenght1):
        #     for j in range(width1):
        #         tempImage1[i + startLenghtCenter1, j + startWidthCenter1] = image1.imageData[i][j][0]
        #
        # for i in range(lenght2):
        #     for j in range(width2):
        #         tempImage2[i + startLenghtCenter2, j + startWidthCenter2] = image2.imageData[i][j][0]
        #
        # for i in range(maxLenght):
        #     for j in range(maxWidth):
        #         image1.imageData[i][j][0] = int(tempImage1[i, j])
        #         image2.imageData[i][j][0] = int(tempImage2[i, j])

    else:
        raise Exception("Ta funkcja służy do ujednolicenia geometrycznie obrazów SZARYCH, a ktorys obraz jest RGB.")


# PUNKT 3 OK
def unification_RGB_Geometric(image1, image2):

    # Wybranie największej szerokości i wysokości z dwóch obrazów
    # width1 = image1.imageWidth
    # width2 = image2.imageWidth
    # lenght1 = image1.imageLength
    # lenght2 = image2.imageLength
    # maxWidth = width1 if width1 > width2 else width2
    # maxLenght = lenght1 if lenght1 > lenght2 else lenght2

    if image1.imageColor == 2 and image2.imageColor == 2:

        # Dodanie i wypełnienie różnicę pikselami o wartości 1 w obrazie 2, który ma mniejszą wysokość.
        if image1.imageLength > image2.imageLength:
            print("Dlugosc obrazu 1 jest wieksza.")

            for i in range(image2.imageLength, image1.imageLength):
                image2.imageData.append([[1, 1, 1]])
                for j in range(image2.imageWidth-1):
                    image2.imageData[i].append([1, 1, 1])

            image2.imageLength = image1.imageLength

        else:
            # Dodanie i wypełnienie różnicę pikselami o wartości 1 w obrazie 1, który ma mniejszą wysokość.
            if image1.imageLength < image2.imageLength:
                print("Dlugosc obrazu 2 jest wieksza.")

                for i in range(image1.imageLength, image2.imageLength):
                    image1.imageData.append([[1, 1, 1]])
                    for j in range(image1.imageWidth-1):
                        image1.imageData[i].append([1, 1, 1])

                image1.imageLength = image2.imageLength

            else:
                print("Dlugosc obrazu 1 i 2 jest równa.")

        # Dodanie i wypełnienie różnicę pikselami o wartości 1 w obrazie 2, który ma mniejszą szerokosc.
        if image1.imageWidth > image2.imageWidth:
            print("Szerokosc obrazu 1 jest wieksza.")

            for i in range(image2.imageLength):
                for j in range(image2.imageWidth, image1.imageWidth):
                    image2.imageData[i].append([1, 1, 1])

            image2.imageWidth = image1.imageWidth

        else:
            # Dodanie i wypełnienie różnicę pikselami o wartości 1 w obrazie 1, który ma mniejszą szerokosc.
            if image1.imageWidth < image2.imageWidth:
                print("Szerokosc obrazu 2 jest wieksza.")

                for i in range(image1.imageLength):
                    for j in range(image1.imageWidth, image2.imageWidth):
                        image1.imageData[i].append([1, 1, 1])

                image1.imageWidth = image2.imageWidth

            else:
                print("Szerokosc obrazu 1 i 2 jest równa.")

        # Umieszczenie obrazu na środku macierzy w powiększonym obrazie
        # tempImage1 = np.ones((maxLenght, maxWidth, 3), dtype=np.uint8)
        # tempImage2 = np.ones((maxLenght, maxWidth, 3), dtype=np.uint8)
        #
        # startWidthCenter1 = int(round((maxWidth - width1) / 2))
        # startLenghtCenter1 = int(round((maxLenght - lenght1) / 2))
        #
        # startWidthCenter2 = int(round((maxWidth - width2) / 2))
        # startLenghtCenter2 = int(round((maxLenght - lenght2) / 2))
        #
        # for i in range(lenght1):
        #     for j in range(width1):
        #         tempImage1[i + startLenghtCenter1, j + startWidthCenter1] = image1.imageData[i][j]
        #
        # for i in range(lenght2):
        #     for j in range(width2):
        #         tempImage2[i + startLenghtCenter2, j + startWidthCenter2] = image2.imageData[i][j]
        #
        # for i in range(maxLenght):
        #     for j in range(maxWidth):
        #         for k in range(3):
        #             image1.imageData[i][j][k] = int(tempImage1[i, j, k])
        #             image2.imageData[i][j][k] = int(tempImage2[i, j, k])

    else:
        raise Exception("Ta funkcja służy do ujednolicenia geometrycznie obrazów RGB, a ktorys obraz jest SZARY.")


# PUNKT 4 OK
def unification_RGB_Resolution(image1, image2):

    if image1.imageColor == 2 and image2.imageColor == 2:

        # width1 = image1.originalImageWidth
        # width2 = image2.originalImageWidth
        # lenght1 = image1.originalImageLength
        # lenght2 = image2.originalImageLength

        # # Skalowanie obydwóch obrazów
        # if lenght1 > lenght2:
        #     scaleLenght1 = 1
        #     scaleLenght2 = lenght2/lenght1
        # else:
        #     scaleLenght1 = lenght1/lenght2
        #     scaleLenght2 = 1
        #
        # if width1 > width2:
        #     scaleWidth1 = 1
        #     scaleWidth2 = width2 / width1
        # else:
        #     scaleWidth1 = width1 / width2
        #     scaleWidth2 = 1

        # Doprowadzenie obydwóch obrazów do takiej samej głębi kolorów
        if image1.imageBitsColor[0] != image2.imageBitsColor[0]:

            if image1.imageBitsColor[0] == 4:
                for i in range(image1.imageLength):
                    for j in range(image1.imageWidth):
                        for k in range(3):
                            image1.imageData[i][j][k] = image1.imageData[i][j][k] * 16
                for l in range(3):
                    image1.imageBitsColor[l] = 8

                for i in range(image1.originalImageLength):
                    for j in range(image1.originalImageWidth):
                        for k in range(3):
                            image1.originalImageData[i][j][k] = image1.originalImageData[i][j][k] * 16

            else:
                if image2.imageBitsColor[0] == 4:
                    for i in range(image2.imageLength):
                        for j in range(image2.imageWidth):
                            for k in range(3):
                                image2.imageData[i][j][k] = image2.imageData[i][j][k] * 16
                    for l in range(3):
                        image2.imageBitsColor[l] = 8

                    for i in range(image2.originalImageLength):
                        for j in range(image2.originalImageWidth):
                            for k in range(3):
                                image2.originalImageData[i][j][k] = image2.originalImageData[i][j][k] * 16

                else:
                    raise Exception("programu 3")

        else:
            print("Rozdzielczosc obrazow 1 i 2 RGB jest taka sama.")

         # Interpolowanie obrazu 1
        # if scaleWidth1 != 1 or scaleLenght1 != 1:
        #
        #     for j in range(image1.imageLength):
        #         for i in range(image1.imageWidth):
        #             x = i * scaleWidth1
        #             y = j * scaleLenght1
        #
        #             b = x - int(x)
        #             a = y - int(y)
        #
        #             if int(y) + 1 >= image1.originalImageLength:
        #                 tempy = image1.originalImageLength - 1
        #             else:
        #                 tempy = int(y) + 1
        #
        #             if int(x) + 1 >= image1.originalImageWidth:
        #                 tempx = image1.originalImageWidth - 1
        #             else:
        #                 tempx = int(x) + 1
        #
        #             Fa0 = (1 - a) * image1.originalImageData[int(y)][int(x)][0] + a * image1.originalImageData[tempy][int(x)][0]
        #             Fa1 = (1 - a) * image1.originalImageData[int(y)][tempx][0] + a * image1.originalImageData[tempy][tempx][0]
        #             Fab = (1 - b) * Fa0 + b * Fa1
        #
        #             image1.imageData[j][i][0] = int(round(Fab))
        #
        #             Fa0 = (1 - a) * image1.originalImageData[int(y)][int(x)][1] + a * image1.originalImageData[tempy][int(x)][1]
        #             Fa1 = (1 - a) * image1.originalImageData[int(y)][tempx][1] + a * image1.originalImageData[tempy][tempx][1]
        #             Fab = (1 - b) * Fa0 + b * Fa1
        #
        #             image1.imageData[j][i][1] = int(round(Fab))
        #
        #             Fa0 = (1 - a) * image1.originalImageData[int(y)][int(x)][2] + a * image1.originalImageData[tempy][int(x)][2]
        #             Fa1 = (1 - a) * image1.originalImageData[int(y)][tempx][2] + a * image1.originalImageData[tempy][tempx][2]
        #             Fab = (1 - b) * Fa0 + b * Fa1
        #
        #             image1.imageData[j][i][2] = int(round(Fab))
        #
        # # Interpolowanie obrazu 2
        # if scaleWidth2 != 1 or scaleLenght2 != 1:
        #
        #     for j in range(image2.imageLength):
        #         for i in range(image2.imageWidth):
        #             x = i * scaleWidth2
        #             y = j * scaleLenght2
        #
        #             b = x - int(x)
        #             a = y - int(y)
        #
        #             if int(y) + 1 >= image2.originalImageLength:
        #                 tempy = image2.originalImageLength - 1
        #             else:
        #                 tempy = int(y) + 1
        #
        #             if int(x) + 1 >= image2.originalImageWidth:
        #                 tempx = image2.originalImageWidth - 1
        #             else:
        #                 tempx = int(x) + 1
        #
        #             Fa0 = (1 - a) * image2.originalImageData[int(y)][int(x)][0] + a * image2.originalImageData[tempy][int(x)][0]
        #             Fa1 = (1 - a) * image2.originalImageData[int(y)][tempx][0] + a * image2.originalImageData[tempy][tempx][0]
        #             Fab = (1 - b) * Fa0 + b * Fa1
        #
        #             image2.imageData[j][i][0] = int(round(Fab))
        #
        #             Fa0 = (1 - a) * image2.originalImageData[int(y)][int(x)][1] + a * image2.originalImageData[tempy][int(x)][1]
        #             Fa1 = (1 - a) * image2.originalImageData[int(y)][tempx][1] + a * image2.originalImageData[tempy][tempx][1]
        #             Fab = (1 - b) * Fa0 + b * Fa1
        #
        #             image2.imageData[j][i][1] = int(round(Fab))
        #
        #             Fa0 = (1 - a) * image2.originalImageData[int(y)][int(x)][2] + a * image2.originalImageData[tempy][int(x)][2]
        #             Fa1 = (1 - a) * image2.originalImageData[int(y)][tempx][2] + a * image2.originalImageData[tempy][tempx][2]
        #             Fab = (1 - b) * Fa0 + b * Fa1
        #
        #             image2.imageData[j][i][2] = int(round(Fab))

    else:
        raise Exception("Ta funkcja służy do ujednolicenia rozdzielczosciowo obrazów RGB, a ktorys obraz jest SZARY.")


# PUNKT 2 OK
def unification_Grayscale_Resolution(image1, image2):
    # width1 = image1.originalImageWidth
    # width2 = image2.originalImageWidth
    # lenght1 = image1.originalImageLength
    # lenght2 = image2.originalImageLength
    #
    # # Skalowanie obydwóch obrazów
    # if lenght1 > lenght2:
    #     scaleLenght1 = 1
    #     scaleLenght2 = lenght2/lenght1
    # else:
    #     scaleLenght1 = lenght1/lenght2
    #     scaleLenght2 = 1
    #
    # if width1 > width2:
    #     scaleWidth1 = 1
    #     scaleWidth2 = width2 / width1
    # else:
    #     scaleWidth1 = width1 / width2
    #     scaleWidth2 = 1

    if (image1.imageColor == 0 or image1.imageColor == 1) and (image2.imageColor == 0 or image2.imageColor == 1):

        # Doprowadzenie obydwóch obrazów do takiej samej głębi kolorów
        if image1.imageBitsColor[0] != image2.imageBitsColor[0]:

            if image1.imageBitsColor[0] == 4:
                print("Zmiana rozdzielczosci obrazu 1 z 4 na 8 bitow.")
                for i in range(image1.imageLength):
                    for j in range(image1.imageWidth):
                        image1.imageData[i][j][0] = image1.imageData[i][j][0] * 16
                image1.imageBitsColor[0] = 8

                for i in range(image1.originalImageLength):
                    for j in range(image1.originalImageWidth):
                        image1.originalImageData[i][j][0] = image1.originalImageData[i][j][0] * 16

            else:
                print("Zmiana rozdzielczosci obrazu 2 z 4 na 8 bitow.")
                if image2.imageBitsColor[0] == 4:
                    for i in range(image2.imageLength):
                        for j in range(image2.imageWidth):
                            image2.imageData[i][j][0] = image2.imageData[i][j][0] * 16
                    image2.imageBitsColor[0] = 8

                    for i in range(image2.originalImageLength):
                        for j in range(image2.originalImageWidth):
                            image2.originalImageData[i][j][0] = image2.originalImageData[i][j][0] * 16

                else:
                    raise Exception("programu 3")

        else:
            print("Rozdzielczosc obrazow 1 i 2 SZARYCH jest taka sama.")

        # Doprowadzenie obydwóch obrazów do takiej samej interpretacji fotometrycznej
        if image1.imageColor != image2.imageColor:

            if image1.imageColor == 0:
                if image1.imageBitsColor[0] == 8:
                    for i in range(image1.imageLength):
                        for j in range(image1.imageWidth):
                            image1.imageData[i][j][0] = 255 - image1.imageData[i][j][0]

                    for i in range(image1.originalImageLength):
                        for j in range(image1.originalImageWidth):
                            image1.originalImageData[i][j][0] = 255 - image1.originalImageData[i][j][0]

                else:
                    if image1.imageBitsColor[0] == 4:
                        for i in range(image1.imageLength):
                            for j in range(image1.imageWidth):
                                image1.imageData[i][j][0] = 15 - image1.imageData[i][j][0]

                        for i in range(image1.originalImageLength):
                            for j in range(image1.originalImageWidth):
                                image1.originalImageData[i][j][0] = 15 - image1.originalImageData[i][j][0]

                    else:
                        raise Exception("programu 4")
                image1.imageColor = 1

            else:
                if image2.imageColor == 0:
                    if image2.imageBitsColor[0] == 8:
                        for i in range(image2.imageLength):
                            for j in range(image2.imageWidth):
                                image2.imageData[i][j][0] = 255 - image2.imageData[i][j][0]

                        for i in range(image2.originalImageLength):
                            for j in range(image2.originalImageWidth):
                                image2.originalImageData[i][j][0] = 255 - image2.originalImageData[i][j][0]

                    else:
                        if image2.imageBitsColor[0] == 4:
                            for i in range(image2.imageLength):
                                for j in range(image2.imageWidth):
                                    image2.imageData[i][j][0] = 15 - image2.imageData[i][j][0]

                            for i in range(image2.originalImageLength):
                                for j in range(image2.originalImageWidth):
                                    image2.originalImageData[i][j][0] = 15 - image2.originalImageData[i][j][0]

                        else:
                            raise Exception("programu 5")
                    image2.imageColor = 1
                else:
                    raise Exception("programu 6")
        else:
            print("Kolor obrazy maja taki sam.")

        # # Interpolowanie obrazu 1
        # if scaleWidth1 != 1 or scaleLenght1 != 1:
        #
        #     for j in range(image1.imageLength):
        #         for i in range(image1.imageWidth):
        #             x = i * scaleWidth1
        #             y = j * scaleLenght1
        #
        #             b = x - int(x)
        #             a = y - int(y)
        #
        #             if int(y) + 1 >= image1.originalImageLength:
        #                 tempy = image1.originalImageLength - 1
        #             else:
        #                 tempy = int(y) + 1
        #
        #             if int(x) + 1 >= image1.originalImageWidth:
        #                 tempx = image1.originalImageWidth - 1
        #             else:
        #                 tempx = int(x) + 1
        #
        #             Fa0 = (1 - a) * image1.originalImageData[int(y)][int(x)][0] + a * image1.originalImageData[tempy][int(x)][0]
        #             Fa1 = (1 - a) * image1.originalImageData[int(y)][tempx][0] + a * image1.originalImageData[tempy][tempx][0]
        #             Fab = (1 - b) * Fa0 + b * Fa1
        #
        #             image1.imageData[j][i][0] = int(round(Fab))
        #
        # # Interpolowanie obrazu 2
        # if scaleWidth2 != 1 or scaleLenght2 != 1:
        #
        #     for j in range(image2.imageLength):
        #         for i in range(image2.imageWidth):
        #             x = i * scaleWidth2
        #             y = j * scaleLenght2
        #
        #             b = x - int(x)
        #             a = y - int(y)
        #
        #             if int(y) + 1 >= image2.originalImageLength:
        #                 tempy = image2.originalImageLength - 1
        #             else:
        #                 tempy = int(y) + 1
        #
        #             if int(x) + 1 >= image2.originalImageWidth:
        #                 tempx = image2.originalImageWidth - 1
        #             else:
        #                 tempx = int(x) + 1
        #
        #             Fa0 = (1 - a) * image2.originalImageData[int(y)][int(x)][0] + a * image2.originalImageData[tempy][int(x)][0]
        #             Fa1 = (1 - a) * image2.originalImageData[int(y)][tempx][0] + a * image2.originalImageData[tempy][tempx][0]
        #             Fab = (1 - b) * Fa0 + b * Fa1
        #
        #             image2.imageData[j][i][0] = int(round(Fab))

    else:
        raise Exception("Ta funkcja służy do ujednolicenia rozdzielczosciowo obrazów SZARYCH, a ktorys obraz jest RGB.")


def unification_Grayscale_one_image(image1, length2, width2):

    width1 = image1.imageWidth
    length1 = image1.imageLength

    if length1 < length2 or width1 < width2:

        if length1 < length2:
            scaleLenght1 = length1/length2
        else:
            scaleLenght1 = 1

        if width1 < width2:
            scaleWidth1 = width1 / width2
        else:
            scaleWidth1 = 1

        if image1.imageLength < length2:
            print("Dlugosc obrazu 1 jest zwiekszana.")

            for i in range(image1.imageLength, length2):
                image1.imageData.append([[1]])
                for j in range(image1.imageWidth-1):
                    image1.imageData[i].append([1])

            image1.imageLength = length2

        if image1.imageWidth < width2:
            print("Szerokosc obrazu 1 jest zwiekszana.")

            for i in range(image1.imageLength):
               for j in range(image1.imageWidth, width2):
                    image1.imageData[i].append([1])

            image1.imageWidth = width2

        for j in range(image1.imageLength):
            for i in range(image1.imageWidth):
                x = i * scaleWidth1
                y = j * scaleLenght1

                b = x - int(x)
                a = y - int(y)

                if int(y) + 1 >= image1.originalImageLength:
                    tempy = image1.originalImageLength - 1
                else:
                    tempy = int(y) + 1

                if int(x) + 1 >= image1.originalImageWidth:
                    tempx = image1.originalImageWidth - 1
                else:
                    tempx = int(x) + 1

                Fa0 = (1 - a) * image1.originalImageData[int(y)][int(x)][0] + a * image1.originalImageData[tempy][int(x)][0]
                Fa1 = (1 - a) * image1.originalImageData[int(y)][tempx][0] + a * image1.originalImageData[tempy][tempx][0]
                Fab = (1 - b) * Fa0 + b * Fa1

                image1.imageData[j][i][0] = int(round(Fab))

    else:
        raise Exception("Ta funkcja służy do ujednolicenia obrazu SZAREGO, nie mozna zmniejszyc obrazu, poniewaz"
                        " prowadzi do utraty danych z obrazu.")


def unification_RGB_one_image(image1, length2, width2):

    width1 = image1.imageWidth
    length1 = image1.imageLength

    if length1 < length2 or width1 < width2:

        if length1 < length2:
            scaleLenght1 = length1/length2
        else:
            scaleLenght1 = 1

        if width1 < width2:
            scaleWidth1 = width1 / width2
        else:
            scaleWidth1 = 1

        if image1.imageLength < length2:
            print("Dlugosc obrazu 1 jest zwiekszana.")

            for i in range(image1.imageLength, length2):
                image1.imageData.append([[1, 1, 1]])
                for j in range(image1.imageWidth-1):
                    image1.imageData[i].append([1, 1, 1])

            image1.imageLength = length2

        if image1.imageWidth < width2:
            print("Szerokosc obrazu 1 jest zwiekszana.")

            for i in range(image1.imageLength):
                for j in range(image1.imageWidth, width2):
                    image1.imageData[i].append([1, 1, 1])

            image1.imageWidth = width2

        for j in range(image1.imageLength):
            for i in range(image1.imageWidth):
                x = i * scaleWidth1
                y = j * scaleLenght1

                b = x - int(x)
                a = y - int(y)

                if int(y) + 1 >= image1.originalImageLength:
                    tempy = image1.originalImageLength - 1
                else:
                    tempy = int(y) + 1

                if int(x) + 1 >= image1.originalImageWidth:
                    tempx = image1.originalImageWidth - 1
                else:
                    tempx = int(x) + 1

                Fa0 = (1 - a) * image1.originalImageData[int(y)][int(x)][0] + a * image1.originalImageData[tempy][int(x)][0]
                Fa1 = (1 - a) * image1.originalImageData[int(y)][tempx][0] + a * image1.originalImageData[tempy][tempx][0]
                Fab = (1 - b) * Fa0 + b * Fa1

                image1.imageData[j][i][0] = int(round(Fab))

                Fa0 = (1 - a) * image1.originalImageData[int(y)][int(x)][1] + a * image1.originalImageData[tempy][int(x)][1]
                Fa1 = (1 - a) * image1.originalImageData[int(y)][tempx][1] + a * image1.originalImageData[tempy][tempx][1]
                Fab = (1 - b) * Fa0 + b * Fa1

                image1.imageData[j][i][1] = int(round(Fab))

                Fa0 = (1 - a) * image1.originalImageData[int(y)][int(x)][2] + a * image1.originalImageData[tempy][int(x)][2]
                Fa1 = (1 - a) * image1.originalImageData[int(y)][tempx][2] + a * image1.originalImageData[tempy][tempx][2]
                Fab = (1 - b) * Fa0 + b * Fa1

                image1.imageData[j][i][2] = int(round(Fab))

    else:
        raise Exception("Ta funkcja służy do ujednolicenia obrazu SZAREGO, nie mozna zmniejszyc obrazu, poniewaz prowadzi do utraty danych z obrazu.")