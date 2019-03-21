from datetime import datetime
from math import floor, ceil


def writeTiff(name, image):

    global tag_273, type_273
    temp_RowsPerStrip = image.imageRowsPerStrip
    image.imageRowsPerStrip = floor((image.imageLength + image.imageRowsPerStrip - 1)/image.imageRowsPerStrip)

    if image.imageRowsPerStrip == 1:

        if image.imageColor == 0 or image.imageColor == 1:
            if image.imageBitsColor[0] == 8:
                image.imageDataStripByteCounts.append(image.imageLength * image.imageWidth)

            else:
                if image.imageBitsColor[0] == 1:
                    temp_strip_byte_count = ceil(image.imageWidth/8)
                    temp_strip_byte_count = temp_strip_byte_count * image.imageLength
                    image.imageDataStripByteCounts.append(temp_strip_byte_count)

                else:
                    raise Exception("Program nie zapisuje obrazow, ktore maja taki bit.")

        else:
            image.imageDataStripByteCounts.append(image.imageLength * image.imageWidth * 3)

    else:
        if image.imageColor == 0 or image.imageColor == 1:
            if image.imageBitsColor[0] == 8:
                temp_byte_counts = image.imageLength * image.imageWidth

            else:
                if image.imageBitsColor[0] == 1:
                    temp_strip_byte_count = ceil(image.imageWidth/8)
                    temp_strip_byte_count = temp_strip_byte_count * image.imageLength

                    temp_byte_counts = temp_strip_byte_count

                else:
                    raise Exception("Program nie zapisuje obrazow, ktore maja taki bit.")

        else:
            temp_byte_counts = image.imageLength * image.imageWidth * 3

        for i in range(image.imageRowsPerStrip):

            if image.imageRowsPerStrip - 1 == i:
                image.imageDataStripByteCounts.append(temp_byte_counts)
            else:
                image.imageDataStripByteCounts.append(ceil((image.imageWidth * image.imageBitsColor[0])/8) * len(image.imageBitsColor) * temp_RowsPerStrip)

            temp_byte_counts = temp_byte_counts - (ceil((image.imageWidth * image.imageBitsColor[0])/8) * len(image.imageBitsColor) * temp_RowsPerStrip)


    print(image.imageDataStripByteCounts)
    dateTime = datetime.now().strftime("%Y%m%d_%H%M%S_")
    nameWrite = "results/" + dateTime + name + ".tif"

    plikRead = open(image.nameImageTiff, 'rb')
    plikWrite = open(nameWrite, 'wb')

    byteOrder = plikRead.read(2)
    plikWrite.write(byteOrder)

    byteTiffIs = plikRead.read(2)
    plikWrite.write(byteTiffIs)

    byteOffsetIDF = plikRead.read(4)
    offsetIDF = int.from_bytes(byteOffsetIDF, byteorder=image.imageTiffOrder)

    tempOffsetIDF = 8
    byte = tempOffsetIDF.to_bytes(4, byteorder=image.imageTiffOrder)
    plikWrite.write(byte)

    plikRead.seek(offsetIDF)
    byteNumerDE = plikRead.read(2)
    countNumerDirectoryEntries = int.from_bytes(byteNumerDE, byteorder=image.imageTiffOrder)
    plikWrite.write(byteNumerDE)

    newOffset = tempOffsetIDF + 2 + countNumerDirectoryEntries * 12 + 4
    for x in range(0, countNumerDirectoryEntries):

        byteTag = plikRead.read(2)
        byteType = plikRead.read(2)
        byteCount = plikRead.read(4)
        byteValueORffset = plikRead.read(4)

        tag = int.from_bytes(byteTag, byteorder=image.imageTiffOrder)
        ttype = int.from_bytes(byteType, byteorder=image.imageTiffOrder)
        count = int.from_bytes(byteCount, byteorder=image.imageTiffOrder)
        valueOROffset = int.from_bytes(byteValueORffset, byteorder=image.imageTiffOrder)

        plikWrite.write(byteTag)
        plikWrite.write(byteType)

        count_is, temp_type = typeVariable(ttype, count)

        if count_is == 0:

            if tag == 256:

                temp = image.imageWidth
                byte = temp.to_bytes(4, byteorder=image.imageTiffOrder)
                plikWrite.write(byteCount)
                plikWrite.write(byte)
            else:
                if tag == 257:

                    temp = image.imageLength
                    byte = temp.to_bytes(4, byteorder=image.imageTiffOrder)
                    plikWrite.write(byteCount)
                    plikWrite.write(byte)
                else:
                    if tag == 258:

                        temp = image.imageBitsColor[0]
                        byte = temp.to_bytes(4, byteorder=image.imageTiffOrder)
                        plikWrite.write(byteCount)
                        plikWrite.write(byte)
                    else:
                        if tag == 262:

                            temp = image.imageColor
                            byte = temp.to_bytes(4, byteorder=image.imageTiffOrder)
                            plikWrite.write(byteCount)
                            plikWrite.write(byte)
                        else:
                            if tag == 273:
                                type_273 = temp_type

                                if image.imageRowsPerStrip == 1:

                                    plikWrite.write(byteCount)
                                    tag_273 = plikWrite.tell()
                                    plikWrite.write(byteValueORffset)
                                else:

                                    temp = image.imageRowsPerStrip
                                    byte = temp.to_bytes(4, byteorder=image.imageTiffOrder)
                                    plikWrite.write(byte)
                                    temp = newOffset
                                    tag_273 = newOffset
                                    byte = temp.to_bytes(4, byteorder=image.imageTiffOrder)
                                    plikWrite.write(byte)


                                    plikWriteTell = plikWrite.tell()
                                    plikWrite.seek(newOffset)
                                    for i in range(image.imageRowsPerStrip):
                                        temp = 100
                                        byte = temp.to_bytes(temp_type, byteorder=image.imageTiffOrder)
                                        plikWrite.write(byte)

                                    newOffset = plikWrite.tell()
                                    plikWrite.seek(plikWriteTell)


                            else:
                                if tag == 278:

                                    plikWrite.write(byteCount)
                                    plikWrite.write(byteValueORffset)

                                else:
                                    if tag == 279:

                                        if image.imageRowsPerStrip == 1:
                                            if image.imageColor == 0 or image.imageColor == 1:
                                                #temp = image.imageLength * image.imageWidth
                                                #byte = temp.to_bytes(4, byteorder=image.imageTiffOrder)
                                                temp = image.imageDataStripByteCounts[0]
                                                byte = temp.to_bytes(4, byteorder=image.imageTiffOrder)

                                                plikWrite.write(byteCount)
                                                plikWrite.write(byte)
                                            else:
                                                temp = image.imageLength * image.imageWidth * 3
                                                byte = temp.to_bytes(4, byteorder=image.imageTiffOrder)
                                                plikWrite.write(byteCount)
                                                plikWrite.write(byte)
                                        else:
                                            temp = image.imageRowsPerStrip
                                            byte = temp.to_bytes(4, byteorder=image.imageTiffOrder)
                                            plikWrite.write(byte)
                                            temp = newOffset
                                            byte = temp.to_bytes(4, byteorder=image.imageTiffOrder)
                                            plikWrite.write(byte)


                                            plikWriteTell = plikWrite.tell()
                                            plikWrite.seek(newOffset)
                                            for i in range(image.imageRowsPerStrip):
                                                temp = image.imageDataStripByteCounts[i]
                                                byte = temp.to_bytes(temp_type, byteorder=image.imageTiffOrder)
                                                plikWrite.write(byte)

                                            newOffset = plikWrite.tell()
                                            plikWrite.seek(plikWriteTell)

                                    else:
                                        plikWrite.write(byteCount)
                                        plikWrite.write(byteValueORffset)

        else:
            if ttype == 5 or ttype == 10:
                count = 2
                temp_type = 4

            if tag == 258:

                plikWrite.write(byteCount)
                temp = newOffset
                byte = temp.to_bytes(4, byteorder=image.imageTiffOrder)
                plikWrite.write(byte)
                plikWriteTell = plikWrite.tell()

                plikWrite.seek(newOffset)
                for i in range(count):
                    temp = image.imageBitsColor[i]
                    byte = temp.to_bytes(temp_type, byteorder=image.imageTiffOrder)
                    plikWrite.write(byte)

                newOffset = plikWrite.tell()
                plikWrite.seek(plikWriteTell)

            else:
                if tag == 273:
                    type_273 = temp_type

                    temp = image.imageRowsPerStrip
                    byte = temp.to_bytes(4, byteorder=image.imageTiffOrder)
                    plikWrite.write(byte)

                    temp = newOffset
                    tag_273 = newOffset
                    byte = temp.to_bytes(4, byteorder=image.imageTiffOrder)
                    plikWrite.write(byte)
                    plikWriteTell = plikWrite.tell()

                    plikWrite.seek(newOffset)
                    for i in range(image.imageRowsPerStrip):
                        temp = 100
                        byte = temp.to_bytes(temp_type, byteorder=image.imageTiffOrder)
                        plikWrite.write(byte)

                    newOffset = plikWrite.tell()
                    plikWrite.seek(plikWriteTell)

                else:
                    if tag == 279:

                        temp = image.imageRowsPerStrip
                        byte = temp.to_bytes(4, byteorder=image.imageTiffOrder)
                        plikWrite.write(byte)
                        temp = newOffset
                        byte = temp.to_bytes(4, byteorder=image.imageTiffOrder)
                        plikWrite.write(byte)


                        plikWriteTell = plikWrite.tell()
                        plikWrite.seek(newOffset)
                        for i in range(image.imageRowsPerStrip):
                            temp = image.imageDataStripByteCounts[i]
                            byte = temp.to_bytes(temp_type, byteorder=image.imageTiffOrder)
                            plikWrite.write(byte)

                        newOffset = plikWrite.tell()
                        plikWrite.seek(plikWriteTell)


                    else:
                        plikWrite.write(byteCount)
                        temp = newOffset
                        byte = temp.to_bytes(4, byteorder=image.imageTiffOrder)
                        plikWrite.write(byte)
                        plikWriteTell = plikWrite.tell()
                        plikReadTell = plikRead.tell()

                        plikWrite.seek(newOffset)
                        plikRead.seek(valueOROffset)
                        for i in range(count):
                            byte = plikRead.read(temp_type)
                            plikWrite.write(byte)

                        newOffset = plikWrite.tell()
                        plikWrite.seek(plikWriteTell)
                        plikRead.seek(plikReadTell)


    byteNextOffsetIDF = plikRead.read(4)
    plikWrite.write(byteNextOffsetIDF)

    if image.imageRowsPerStrip == 1:

        plikWrite.seek(tag_273)
        image.imageDataStripOffset.append(newOffset)
        byte = newOffset.to_bytes(4, byteorder=image.imageTiffOrder)
        plikWrite.write(byte)
        plikWrite.seek(newOffset)

    else:

        plikWrite.seek(tag_273)
        temp = newOffset
        for i in range(image.imageRowsPerStrip):
            image.imageDataStripOffset.append(temp)
            byte = temp.to_bytes(type_273, byteorder=image.imageTiffOrder)
            plikWrite.write(byte)
            temp = temp + image.imageDataStripByteCounts[i]

    if image.imageColor == 0 or image.imageColor == 1:

        tempX = 0
        tempY = 0

        if image.imageBitsColor[0] == 8:

            for i in range(len(image.imageDataStripOffset)):
                plikWrite.seek(image.imageDataStripOffset[i])

                for j in range(image.imageDataStripByteCounts[i]):
                    temp = image.imageData[tempY][tempX][0]
                    byte = temp.to_bytes(1, byteorder=image.imageTiffOrder)
                    plikWrite.write(byte)
                    tempX = tempX + 1

                    if tempX == image.imageWidth:
                        tempX = 0
                        tempY = tempY + 1
        else:
            if image.imageBitsColor[0] == 1:

                for i in range(len(image.imageDataStripOffset)):
                    plikWrite.seek(image.imageDataStripOffset[i])

                    for j in range(image.imageDataStripByteCounts[i]):
                        bits = ""

                        for k in range(8):
                            temp = str(image.imageData[tempY][tempX][0])
                            bits += temp
                            tempX += 1
                            if tempX == image.imageWidth:
                                tempX = 0
                                tempY += 1
                                break

                        tempb = int(bits, 2)
                        byte = tempb.to_bytes(1, byteorder=image.imageTiffOrder)
                        plikWrite.write(byte)

            else:
                raise Exception("Program nie zapisuje obrazow, ktore maja taki bit.")


    else:
        tempX = 0
        tempY = 0
        tempRGB = 0

        for i in range(len(image.imageDataStripOffset)):
            plikWrite.seek(image.imageDataStripOffset[i])

            for j in range(image.imageDataStripByteCounts[i]):

                temp = image.imageData[tempY][tempX][tempRGB]
                byte = temp.to_bytes(1, byteorder=image.imageTiffOrder)
                plikWrite.write(byte)
                tempRGB = tempRGB + 1

                if tempRGB == 3:
                    tempX = tempX + 1
                    tempRGB = 0

                if tempX == image.imageWidth:
                    tempX = 0
                    tempY = tempY + 1

    plikWrite.close()
    plikRead.close()


def typeVariable(t, c):

    bytes = -1
    sizebytec = -1

    if t == 1:
        sizebytec = 1
        bytes = 1*c
    else:
        if t == 2:
            sizebytec = 1
            bytes = 1*c
        else:
            if t == 3:
                sizebytec = 2
                bytes = 2*c
            else:
                if t == 4:
                    sizebytec = 4
                    bytes = 4*c
                else:
                    if t == 5:
                        sizebytec = 4
                        bytes = 2*4*c
                    else:
                        if t == 6:
                            sizebytec = 1
                            bytes = 1*c
                        else:
                            if t == 7:
                                sizebytec = 1
                                bytes = 1*c
                            else:
                                if t == 8:
                                    sizebytec = 2
                                    bytes = 2*c
                                else:
                                    if t == 9:
                                        sizebytec = 4
                                        bytes = 4*c
                                    else:
                                        if t == 10:
                                            sizebytec = 4
                                            bytes = 2*4*c
                                        else:
                                            if t == 11:
                                                sizebytec = 4
                                                bytes = 4*c
                                            else:
                                                if t == 12:
                                                    sizebytec = 8
                                                    bytes = 8*c
                                                else:
                                                    if t == 13:
                                                        sizebytec = 4
                                                        bytes = 4*c

    if bytes <= 4 and c <= 1:
        return 0, sizebytec
    else:
        return 1, sizebytec