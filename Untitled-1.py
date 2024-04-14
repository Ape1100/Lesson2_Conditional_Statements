number = input("Enter a number: ")
number = float(number)

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else : 
    print("The number is negative.")

    #removed "'number' after else statement as unnecesssary"
#Write a Python program that prompts the user to enter three numbers. The program should then identify and 
#print out the largest number among the three.

def identify_numbers(num1, num2, num3):
    if num1 == num2 == num3:
        print("All numbers are equal.")
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print("Two numbers are equal and the largest.")
    else:
        print("The largest number is:", identify_greatest(num1, num2, num3))
    print("The smallest number is:", identify_smallest(num1, num2, num3))

if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    identify_numbers(num1, num2, num3)