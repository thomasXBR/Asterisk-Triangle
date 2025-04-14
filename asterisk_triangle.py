while True:
    height = int(input("Insert the height of the triangle: "))
    space = ' '
    space_count_pos = height # Counter used if n is positive
    space_count_neg = 0 # Counter used if n is negative

    if height > 0:
        while space_count_pos > 0:
            for c in range(1, height*2, 2):
                print(space*(space_count_pos), '*'*c)
                space_count_pos-=1
    elif height < 0:
        while space_count_neg != height*(-1):
            for c in range((height*(-1))*2-1, 0, -2):
                print(space*(space_count_neg), '*'*c)
                space_count_neg+=1

    else:
        print("End")
        break