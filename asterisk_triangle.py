while True:
    n = int(input("Insert the height of the triangle: "))
    space = ' '
    space_count_pos = n #Espaçamento caso n for positivo 
    space_count_neg = 0 #Espaçamento caso n for negativo

    if n > 0:
        while space_count_pos > 0:
            for c in range(1, n*2, 2):
                print(space*(space_count_pos), '*'*c)
                space_count_pos-=1
    elif n < 0:
        while space_count_neg != n*(-1):
            for c in range((n*(-1))*2-1, 0, -2):
                print(space*(space_count_neg), '*'*c)
                space_count_neg+=1

    else:
        print("End")
        break