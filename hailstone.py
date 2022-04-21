# Author: Kai Geller
# GitHub Username: KaiGeller
# Date: 4/20/2022
# To give the value of the fibonacci sequence
term = int(input("Hailstone:"))
i = 0
while term != 1:
    if term % 2 == 0:
        term = term/2

    elif term % 2 != 0:
        term = (term*3)+1
    i = i+1
print(i)