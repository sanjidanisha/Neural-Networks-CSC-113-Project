# Group Members:
# Sanjida Nisha
# Afsana Sultana
# Aliaa Abdelrahman
# Pierce Ruddock Taylor
# Moshe Oppenheim
# Marianna U. Fervenza

import random
import copy


def binaryToDecimal(n):
    return int(n, 2)


class L:
    def __init__(self):
        self.firstArray = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]]
        self.sum = 0

    def change(self, listOftuples):
        for i in range(len(listOftuples)):
            newTup = ''.join([str(listOftuples[i][0]), str(listOftuples[i][1]), str(listOftuples[i][2])])
            newArr = binaryToDecimal(newTup)
            self.firstArray[i][int(newArr)] += 1

    def test(self, listOftuples):
        for i in range(len(listOftuples)):
            newTup1 = ''.join([str(listOftuples[i][0]), str(listOftuples[i][1]), str(listOftuples[i][2])])
            newArr1 = binaryToDecimal(newTup1)
            self.sum += self.firstArray[i][int(newArr1)]
        temp = self.sum
        self.sum = 0
        return temp

    def __str__(self):
        return str(self.firstArray)


class H:
    def __init__(self):
        self.firstArray = [[0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                           [0, 0, 0, 0, 0, 0, 0, 0]]
        self.sum = 0

    def change(self, listOftuples):
        for i in range(len(listOftuples)):
            newTup = ''.join([str(listOftuples[i][0]), str(listOftuples[i][1]), str(listOftuples[i][2])])
            newArr = binaryToDecimal(newTup)
            self.firstArray[i][int(newArr)] += 1
        # print(self.firstArray)

    def test(self, listOftuples):
        for i in range(len(listOftuples)):
            newTup1 = ''.join([str(listOftuples[i][0]), str(listOftuples[i][1]), str(listOftuples[i][2])])
            newArr1 = binaryToDecimal(newTup1)
            self.sum += self.firstArray[i][int(newArr1)]
        temp = self.sum
        self.sum = 0
        return temp

    def __str__(self):
        return str(self.firstArray)


# Generate Lists for One Image Function

def createSubset(copiedSet, tupleSize):
    tupleSets = []
    for i in range(12 // tupleSize):
        value = random.choice(copiedSet)
        copiedSet.remove(value)
        val1 = random.choice(copiedSet)
        copiedSet.remove(val1)
        val2 = random.choice(copiedSet)
        copiedSet.remove(val2)
        tupleSets.append((value, val1, val2))
    return tupleSets


def generateLists():
    "represents all the indexes of the"
    "arrays(pixel positions of the images"
    indexSet = []
    for i in range(12):
        indexSet.append(i + 1)
    # list R, values that stored in indexes
    copiedSet = copy.deepcopy(indexSet)
    tupleSize = 3
    first = createSubset(copiedSet, tupleSize)
    # print("indexes:",indexSet)
    return first


def createImage(first):
    imageVal = []
    # random positions of 0 and 1 for array representation of image
    for i in range(12):
        imageVal.append(random.choice([0, 1]))
    imageVal2 = []
    for i in first:
        imageVal2.append((imageVal[i[0] - 1], imageVal[i[1] - 1], imageVal[i[2] - 1]))
    return imageVal2


def createImage1(first, imageVal):
    imageVal2 = []
    for i in first:
        imageVal2.append((imageVal[i[0] - 1], imageVal[i[1] - 1], imageVal[i[2] - 1]))
    return imageVal2


def actualTest():
    f = open("actual.txt", "r")
    images = []
    x = []
    for i in f:
        images.append(i.split())
    for j in images:
        for i in range(len(j[0])):
            x.append(int(j[0][i]))
        j[0] = x
        x = []

    return images


def trainNetwork(totalImages):
    first = generateLists()
    l = L()
    h = H()
    # Sampling the images for each class
    for i in range(totalImages):
        l.change(createImage(first))
    for i in range(totalImages):
        h.change(createImage(first))
    return first, l, h


def predictedTest(imageX, first, l, h):
    # Image X
    imagen = createImage1(first, imageX)
    print(l.test(imagen))
    print(h.test(imagen))
    if l.test(imagen) > h.test(imagen):
        return 'L'
    else:
        return 'H'


def main():
    first, l, h = trainNetwork(400)
    ratio = 0
    actual = actualTest()
    output = []
    for i in range(len(actual)):
        predict = predictedTest(actual[i][0], first, l, h)
        output.append(actual[i][0])
        output.append(" Actual: ," + actual[i][1] + " Predicted Class: ," + predict)
        if (actual[i][1] == predict):
            output.append(",True")
            ratio += 1
        else:
            output.append(", False ")
        print(output)
        output = []
    print("Accuracy: ", (ratio / len(actual)) * 100, "%")


main()