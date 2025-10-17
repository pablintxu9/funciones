def fact(num):
    print("el valor inicial es :", num)
    if num>1:
        num= num * fact(num-1)
    print("valor final->", num )
    return num
fact(5)
        


