def printPicnic(itemDict, leftWidth, rightWidht):
    print('PICNIC ITEMS'.center(leftWidth+rightWidht, '-'))
    for k, v in itemDict.items():
        print(k.ljust(leftWidth, '.') + str(v).rjust(rightWidht))

picnicItems = {'sandwiches': 4, 'apple': 12, 'cups': 4, 'cookies':8000}
printPicnic(picnicItems, 12, 5)