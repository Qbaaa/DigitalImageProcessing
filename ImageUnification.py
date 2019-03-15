def unificationImageGrayscaleGeometric(image1, image2):

    if (image1.imageColor == 0 or image1.imageColor == 1) and (image2.imageColor == 0 or image2.imageColor == 1):

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

            for i in range(image2.imaeLength):
                for j in range(image2.imageWidth, image1.imageWidth):
                    image2.imageData[i].append([1])

            image2.imageWidth = image1.imageWidth

        else:
            if image1.imageWidth < image2.imageWidth:
                print("Szerokosc obrazu 2 jest wieksza.")

                for i in range(image1.imageLength):
                    for j in range(image1.imageWidth, image2.imageWidth):
                        image2.imageData[i].append([1])

                image1.imageWidth = image2.imageWidth

            else:
                print("Szerokosc obrazu 1 i 2 jest równa.")


    else:
        raise Exception("Ta funkcja służy do ujednolicenia geometrycznie obrazów SZARYCH, a ktorys obraz jest RGB.")


def unificationImageRGBGeometric(image1, image2):

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

            for i in range(image2.imaeLength):
                for j in range(image2.imageWidth, image1.imageWidth):
                    image2.imageData[i].append([1, 1, 1])

            image2.imageWidth = image1.imageWidth

        else:
            if image1.imageWidth < image2.imageWidth:
                print("Szerokosc obrazu 2 jest wieksza.")

                for i in range(image1.imageLength):
                    for j in range(image1.imageWidth, image2.imageWidth):
                        image2.imageData[i].append([1, 1, 1])

                image1.imageWidth = image2.imageWidth

            else:
                print("Szerokosc obrazu 1 i 2 jest równa.")


    else:
        raise Exception("Ta funkcja służy do ujednolicenia geometrycznie obrazów RGB, a ktorys obraz jest SZARY.")


def unificationImageRGBResolution(image1, image2):

    if image1.imageColor == 2 and image2.imageColor == 2:

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

    else:
        raise Exception("Ta funkcja służy do ujednolicenia rozdzielczosciowo obrazów RGB, a ktorys obraz jest SZARY.")


def unificationImageGrayscaleResolution(image1, image2):

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

    else:
        raise Exception("Ta funkcja służy do ujednolicenia rozdzielczosciowo obrazów SZARYCH, a ktorys obraz jest RGB.")


class ImageUnification:
    pass
