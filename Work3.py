#This is a program recieves a number from the user and determines if it is even or odd, then calculates its square and cube.

def main (): #this is the main function
    num = int(input("  Enter a number: \n")) #ensuring the value becomes and integer
    def EvenorOdd(num): #even or odd function, checks if the number is divisible by 2
        if num % 2 == 0:
            print("  The number is even")
        else:
            print("  The number is odd")
    EvenorOdd(num) #calling the function
    def SquareCube(num): #square and cube function
        print("  The square of the number is", num * num)
        print("  The cube of the number is", num * num * num)
    SquareCube(num)#calling the function
main()