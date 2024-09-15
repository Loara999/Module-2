ListOfNumbers = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
Counter = 0
while Counter < len(ListOfNumbers):
    if ListOfNumbers[Counter] > 0:
        print(ListOfNumbers[Counter])
    elif ListOfNumbers[Counter] < 0:
        break
    Counter = Counter + 1
