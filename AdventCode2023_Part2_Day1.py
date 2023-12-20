import re

matchStr = ""
flag = 0

def partTwo():

    global flag
    sumList = []
    a = 0
    b = 0
    total = 0

    with open("Day1_Puzzle.txt", "r") as file:
        file_list = file.readlines()

        # Big loop to traverse thru each document lines.
        for line in file_list:

            # Iterates (left -> right) through each element within string.
            # Finds the first number.
            for text in line:
                a = stringMatch(text, 0)
                if flag == 1:
                    flag = 0
                    break

            # Iterates (left <- right) through each element within string.
            # Finds the last number.
            for text in reversed(line):
                b = stringMatch(text, 1)
                if flag == 1:
                    flag = 0
                    break

            sumList.append(((a*10) + b))
        
        # Sum all our entries up together to get the total final answer.
        for numEntry in sumList:
            total += numEntry

        print(total)

# (left -> right): dir = 0
# (left <- right): dir = 1
def stringMatch(text, dir):

    global matchStr, flag
    numKey = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    numKeyDict = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}

    if text.isnumeric():
        flag = 1
        return int(text)

    matchStr += text

    for i in range(len(numKey)):

        if dir == 0:
            if re.search(numKey[i], matchStr):

                matchStr = ''
                flag = 1
                return (numKeyDict[numKey[i]])
            
        if dir == 1:

            # TODO Why does this work?
            # Reverses the match string to get back the original (since it is originally read backward).
            reverseMatchStr = matchStr[::-1]
            if re.search(numKey[i], reverseMatchStr):

                matchStr = ''
                reverseMatchStr = ''
                flag = 1
                return (numKeyDict[numKey[i]])
            
partTwo()

# TODO Why does this work?
# while None in numberList:
#     numberList.remove(None)