# Author: Khrystian Clark
# Date: 11/18/2020
# Description:

def count_seq():
    first = "12"
    print("2, 12" + ", ")
    while (1):
        show = ""
        count = 1
        prev = first[0]
        for i in range(1, len(first)):
            if i == (len(first) - 1):
                if first[i-1] == first[i]:
                    show += str(count) + prev
                else:
                    show += str(count) + first[i]
            if first[i] == first[i+1]:
                count += 1
            else:
                show += str(count) + prev
                count = 1
                prev = first[i+1]
        first = show
        print(first + ", ")

count_seq()
