from math import floor


class ReadTiff:

    nameImage = None
    tiffOrder = ""
    compression = 1
    color = -1
    offsetIDF = -1
    countNumerDirectoryEntries = -1
    nextOffsetIDF = -1
    stripOffset = -1
    stripByteCounts = -1
    rowsPerStrip = 4294967295
    imageRowsPerStrip = 4294967295
    constRowsPerStrip = 4294967295
    imageLength = -1
    imageWidth = -1
    isTag278 = False
    isTag279 = False

    def __init__(self, nameFile):

        global plik
        try:
            self.nameImage = nameFile
            #czytanie pierwszych 8 byte pliku
            plik = open(nameFile, 'rb')
            byteOrder = plik.read(2)
            byteTiffIs = plik.read(2)
            byteOffsetIDF = plik.read(4)

            order = byteOrder.decode()
            if order == "II":
                self.tiffOrder = "little"
            else:
                if order == "MM":
                    self.tiffOrder = "big"
                else:
                    raise Exception("To nie plik tiff.")

            tiffIs = int.from_bytes(byteTiffIs, byteorder=self.tiffOrder)

            if tiffIs != 42:
                raise Exception("To nie plik tiff.")

            self.offsetIDF = int.from_bytes(byteOffsetIDF, byteorder=self.tiffOrder)
            self.nextOffsetIDF = self.offsetIDF

            print("Dane obrazu:")
            print("Name image: %s" %nameFile)
            print("--------------HEADER---------------")
            print(order)
            print(tiffIs)
            print(self.offsetIDF)

            countIDF = 0
            while self.nextOffsetIDF != 0:

                countIDF=countIDF+1
                print("----------------IDF %d-------------------" %countIDF)
                plik.seek(self.offsetIDF)

                byteNumerDE = plik.read(2)
                self.countNumerDirectoryEntries = int.from_bytes(byteNumerDE, byteorder=self.tiffOrder)

                print(self.countNumerDirectoryEntries)

                for x in range(0, self.countNumerDirectoryEntries):

                    byteTag = plik.read(2)
                    byteType = plik.read(2)
                    byteCount = plik.read(4)
                    byteValueORffset = plik.read(4)

                    print("--------------Directory Entry %d---------------" %x)
                    tag = int.from_bytes(byteTag, byteorder=self.tiffOrder)
                    print(tag)
                    type = int.from_bytes(byteType, byteorder=self.tiffOrder)
                    print(type)
                    count = int.from_bytes(byteCount, byteorder=self.tiffOrder)
                    print(count)
                    valueOROffset = int.from_bytes(byteValueORffset, byteorder=self.tiffOrder)
                    print(valueOROffset)

                    if tag == 256:
                        isValue, sizebyte = self.typeVariable(type, count)

                        if isValue == 0:
                            self.imageWidth = valueOROffset

                    else:
                        if tag == 257:
                            isValue, sizebyte = self.typeVariable(type, count)

                            if isValue == 0:
                                self.imageLength = valueOROffset

                        else:
                            if tag ==258:
                                self.imageBitsColor = []
                                isValue, sizebyte = self.typeVariable(type, count)

                                if isValue == 0:
                                    self.imageBitsColor.append(valueOROffset)
                                    print(self.imageBitsColor)
                                else:

                                    plikTell = plik.tell()
                                    plik.seek(valueOROffset)
                                    for x in range(0, count):
                                        byte = plik.read(sizebyte)
                                        data = int.from_bytes(byte, byteorder=self.tiffOrder)
                                        self.imageBitsColor.append(data)
                                    print(self.imageBitsColor)
                                    plik.seek(plikTell)



                            else:
                                if tag == 259:
                                    isValue, sizebyte = self.typeVariable(type, count)

                                    if isValue == 0:
                                        self.compression = valueOROffset

                                else:
                                    if tag == 262:
                                        isValue, sizebyte = self.typeVariable(type, count)

                                        if isValue == 0:
                                            self.color = valueOROffset

                                    else:
                                        if tag == 273:
                                            self.imageDataStripOffset = []
                                            isValue, sizebyte = self.typeVariable(type, count)

                                            self.stripOffset = valueOROffset
                                            plikTell = plik.tell()
                                            if isValue == 1:

                                                plik.seek(valueOROffset)
                                                for x in range(0, count):
                                                    byte = plik.read(sizebyte)
                                                    data = int.from_bytes(byte, byteorder=self.tiffOrder)
                                                    self.imageDataStripOffset.append(data)

                                                plik.seek(plikTell)
                                            else:
                                                self.imageDataStripOffset.append(valueOROffset)

                                            print(self.imageDataStripOffset)

                                        else:
                                            if tag == 278:
                                                self.isTag278 = True
                                                isValue, sizebyte = self.typeVariable(type, count)

                                                if isValue == 0:
                                                    self.constRowsPerStrip = valueOROffset
                                                    self.imageRowsPerStrip = valueOROffset
                                                    self.rowsPerStrip = floor((self.imageLength + valueOROffset - 1)/ valueOROffset)
                                                    print(self.rowsPerStrip)

                                            else:
                                                if tag == 279:
                                                    self.imageDataStripByteCounts = []
                                                    self.isTag279 = True
                                                    isValue, sizebyte = self.typeVariable(type, count)

                                                    self.stripByteCounts = valueOROffset
                                                    plikTell = plik.tell()
                                                    if isValue == 1:

                                                        plik.seek(valueOROffset)
                                                        for x in range(0, count):
                                                            byte = plik.read(sizebyte)
                                                            data = int.from_bytes(byte, byteorder=self.tiffOrder)
                                                            self.imageDataStripByteCounts.append(data)

                                                        plik.seek(plikTell)
                                                    else:
                                                        self.imageDataStripByteCounts.append(valueOROffset)

                                                    print(self.imageDataStripByteCounts)

                    print("------------------------------------------------")

                byteNextOffsetIDF = plik.read(4)
                self.nextOffsetIDF = int.from_bytes(byteNextOffsetIDF, byteorder=self.tiffOrder)
                print(self.nextOffsetIDF)
                self.offsetIDF = self.nextOffsetIDF

                if self.nextOffsetIDF != 0:
                    raise Exception("Blad")

                if self.isTag278 == False:
                    self.rowsPerStrip = floor((self.imageLength + self.rowsPerStrip - 1)/self.rowsPerStrip)

                if self.isTag279 == False:
                        imageByte = self.imageLength * self.imageWidth * len(self.imageBitsColor)
                        self.imageDataStripByteCounts = []
                        self.imageDataStripByteCounts.append(imageByte)

                print("---------------IMAGE--------------")

                if self.color != 0 and self.color != 1 and self.color != 2:
                    raise Exception("Program nie obsluguje tego coloru %d." %self.color)

                if self.compression != 1:
                    raise Exception("Program nie obsluguje tej kompresji %d." %self.compression)

                if self.color == 2:
                    if len(self.imageBitsColor) == 4:
                        raise Exception("Program nie obsluguje kanału alfa dla obrazow RGB.")
                else:
                    if len(self.imageBitsColor) == 2:
                        raise Exception("Program nie obsluguje kanału alfa dla obrazow SZARYCH.")

                if self.compression == 1:
                    self.noCompression(plik)

            plik.close()

        finally:
            plik.close()

    # funkcja, ktora sprawddza czy watrosc znajduje sie w tagu tiff-a czy w innym miejscu pliku
    def typeVariable(self, t, c):

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
        if bytes <= 4 and c <= 1:
            return 0, sizebytec
        else:
            return 1, sizebytec

    # czytanie z pliku tiff danych obrazu
    def noCompression(self, plik):

        if self.color == 0 or self.color == 1:
            self.imageData = []
            for i in range(self.imageLength):
                self.imageData.append([[-1]])
                for j in range(self.imageWidth-1):
                    self.imageData[i].append([-1])

            tempX = 0
            tempY = 0

            if self.imageBitsColor[0] == 8:

                for x in range(0, self.rowsPerStrip):
                    plik.seek(self.imageDataStripOffset[x])

                    for y in range(0, self.imageDataStripByteCounts[x]):
                        byte = plik.read(1)
                        data = int.from_bytes(byte, byteorder=self.tiffOrder)
                        self.imageData[tempY][tempX][0] = data
                        tempX += 1

                        if(tempX == self.imageWidth):
                            tempY += 1
                            tempX = 0

            else:
                if self.imageBitsColor[0] == 1:

                    for x in range(0, self.rowsPerStrip):
                        plik.seek(self.imageDataStripOffset[x])

                        for y in range(0, self.imageDataStripByteCounts[x]):
                            byte = plik.read(1)
                            data = int.from_bytes(byte, byteorder=self.tiffOrder)
                            bits = bin(data)
                            bits = bits[2:len(bits)]
                            bits = bits.zfill(8)

                            for z in range(len(bits)):
                                self.imageData[tempY][tempX][0] = int(bits[z])
                                tempX += 1

                                if(tempX == self.imageWidth):
                                    tempY += 1
                                    tempX = 0
                                    break

                else:
                    if self.imageBitsColor[0] == 4:

                        for x in range(0, self.rowsPerStrip):
                            plik.seek(self.imageDataStripOffset[x])

                            for y in range(0, self.imageDataStripByteCounts[x]):
                                byte = plik.read(1)
                                data = int.from_bytes(byte, byteorder=self.tiffOrder)
                                bits = bin(data)
                                bits = bits[2:len(bits)]
                                bits = bits.zfill(8)

                                for z in range(2):
                                    bits4 = ""

                                    if z == 0:
                                        bits4 = bits[0:4]
                                        tempb = int(bits4, 2)
                                        self.imageData[tempY][tempX][0] = int(tempb)
                                        tempX += 1
                                        if tempX == self.imageWidth:
                                            tempY += 1
                                            tempX = 0
                                            break

                                    else:
                                        if z == 1:
                                            bits4 = bits[4:8]
                                            tempb = int(bits4, 2)
                                            self.imageData[tempY][tempX][0] = int(tempb)
                                            tempX += 1
                                            if tempX == self.imageWidth:
                                                tempX += 1
                                                tempY = 0
                                                break

                    else:
                        raise Exception("program obsługuje tylko wczytywanie obrazów SZARYCH 1,4,8 bitowych.")

        else:
            if self.color == 2:
                self.imageData = []
                for i in range(self.imageLength):
                    self.imageData.append([[-1, -1, -1]])
                    for j in range(self.imageWidth-1):
                         self.imageData[i].append([-1, -1, -1])

                tempX = 0
                tempY = 0
                tempRGB = 0

                if self.imageBitsColor[0] == 8:

                    for x in range(0, self.rowsPerStrip):
                        plik.seek(self.imageDataStripOffset[x])

                        for y in range(0, self.imageDataStripByteCounts[x]):
                            byte = plik.read(1)
                            data = int.from_bytes(byte, byteorder=self.tiffOrder)
                            self.imageData[tempY][tempX][tempRGB] = data

                            tempRGB += 1
                            if tempRGB == 3:

                                tempRGB = 0
                                tempX += 1
                                if(tempX == self.imageWidth):

                                    tempY += 1
                                    tempX = 0

                else:
                    if self.imageBitsColor[0] == 4:
                        for x in range(0, self.rowsPerStrip):
                            plik.seek(self.imageDataStripOffset[x])

                            for y in range(0, self.imageDataStripByteCounts[x]):
                                byte = plik.read(1)
                                data = int.from_bytes(byte, byteorder=self.tiffOrder)
                                bits = bin(data)
                                bits = bits[2:len(bits)]
                                bits = bits.zfill(8)

                                for z in range(2):
                                    bits4 = ""

                                    if z == 0:
                                        bits4 = bits[0:4]
                                        tempb = int(bits4, 2)
                                        self.imageData[tempY][tempX][tempRGB] = int(tempb)
                                        tempRGB += 1
                                        if tempRGB == 3:
                                            tempRGB = 0
                                            tempX += 1

                                        if tempX == self.imageWidth:
                                            tempY += 1
                                            tempX = 0
                                            break

                                    else:
                                        if z == 1:
                                            bits4 = bits[4:8]
                                            tempb = int(bits4, 2)
                                            self.imageData[tempY][tempX][tempRGB] = int(tempb)
                                            tempRGB += 1
                                            if tempRGB == 3:
                                                tempRGB = 0
                                                tempX += 1

                                            if tempX == self.imageWidth:
                                                tempX += 1
                                                tempY = 0
                                                break

                        #raise Exception("brak implementacji dla wczytywanie obrazów RGB 12 bitowych.")

                    else:
                        raise Exception("program obsługuje tylko wczytywanie obrazów RGB 12, 24 bitowych.")

            else:
                raise Exception("programu 1")