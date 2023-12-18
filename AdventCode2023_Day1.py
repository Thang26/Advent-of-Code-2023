def main():

    indvCharList = []
    sumList = []
    a = 0
    b = 0
    total = 0

    with open("Day1_Puzzle.txt", "r") as file:
        file_list = file.readlines()

        # Big loop to traverse thru each document lines.
        for line in file_list:

            # Loop to go thru each char (left -> right) & find first num.
            for firstNum in line:
                
                if firstNum.isnumeric():
                    a = int(firstNum)
                    break

            # Loop to go thru each char (right -> left) & find last num.
            for lastNum in reversed(line):

                if lastNum.isnumeric():
                    b = int(lastNum)
                    break

            sumList.append(((a*10) + b))

            # At the end of everything, clear list for next iteration of document line.
            indvCharList.clear()

        # Sum all our entries up together to get the total final answer.
        for numEntry in sumList:
            total += numEntry

        print(total)

main()
