num = int(input("Enter a number: "))

t = num
numlen = 0

# Count number of digits
while t > 0:
    numlen = numlen + 1
    t = t // 10

if numlen >= 4:
    mid_index = numlen // 2
    chk = 0

    while num > 0:
        rem = num % 10

        if chk == mid_index:
            midone = rem
        elif chk == mid_index - 1:
            midtwo = rem

        num = num // 10
        chk = chk + 1

    prod = midone * midtwo
    print("Product of mid digits:", prod)

else:
    print("It's not more than four digits")
