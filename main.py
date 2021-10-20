#####################################
##                                 ##
##        AUTHOR: ABHIJITH EA      ##
##                                 ##
####################################

import sys
import time

def findReverse(num):
    reverse = 0
    number = num
    while num!=0:
        lastDigit = num%10
        reverse = (reverse*10) + lastDigit
        num//=10

    print(f"reverse of {number} is {reverse}")
    time.sleep(1)
    print("------finished---------")

def sumOfDigits(num):
    sum = 0
    number = num
    while num!=0:
        lastDigit = num % 10
        sum = sum + lastDigit
        num //=10
    print(f"sum of the digits of the number{number} is {sum}")
    time.sleep(1)
    print("------finished---------")

def multTable(num):
    for i in range(1,11):
        print(f"{i}*{num} = {i*num}")
    time.sleep(1)
    print("------finished---------")

def checkPrime(num):
    flag = 0
    for i in range(2, num//2 + 1):
        if num%i == 0:
            flag = 1
            print(f'{num} is not prime')
            break
    if not flag:
        print(f"{num} is a prime number")
    time.sleep(1)
    print("------finished---------")

def checkAmstrong(num):
    number = num
    sum = 0
    while num!=0:
        lastDigit = num % 10
        sum = sum + (lastDigit**3)
        num //= 10

    if  number == sum:
        print(f"{number} is an amstrong")
    else:
        print(f"{number} is not an amstrong")
    time.sleep(1)
    print("------finished---------")

def perfectNumber(num):
    number = num
    sum = 1
    for i in range(2, num//2 + 1):
        if num%i == 0:
            sum+=i
    if  number == sum:
        print(f"{number} is a perfect number")
    else:
        print(f"{number} is not a perfect number")
    time.sleep(1)
    print("------finished---------")

def factorial(num, helper=False):
    sum = 1
    for i in range(1, num+1):
        sum = sum * i
    if not helper:
        print(f"fuctorial of {num} is {sum}")
        time.sleep(1)
        print("------finished---------")
    else:
        return sum

def  strongNumber(num):
    number = num
    sum = 0
    while num!=0:
        lastDigit = num % 10
        sum = sum + factorial(lastDigit, helper=True)
        num //= 10
    if  number == sum:
        print(f"{number} is a strong number")
    else:
        print(f"{number} is not a strong number")
    time.sleep(1)
    print("------finished---------")

def numberProblems():
    while True:
        print("---------------------------------")
        print("welcome to number problems thread")
        print("---------------------------------")
        print("1.reverse number")
        print("2.sum of digits")
        print("3.multiplication table")
        print("4.prime number")
        print("5.amstrong number")
        print("6.perfect number")
        print("7.factorial")
        print("8.strong number")
        print("9.Exit thread")
        option = int(input("Enter option:"))
        if option <=9 and option >= 1:
            if option == 1:
                number = int(input("Enter a number:"))
                findReverse(number)
            elif option ==2:
                number = int(input("Enter a number:"))
                sumOfDigits(number)
            elif option == 3:
                number = int(input("Enter a number:"))
                multTable(number)
            elif option == 4:
                number = int(input("Enter a number:"))
                checkPrime(number)
            elif option == 5:
                number = int(input("Enter a number:"))
                checkAmstrong(number)
            elif option == 6:
                number = int(input("Enter a number:"))
                perfectNumber(number)
            elif option == 7:
                number = int(input("Enter a number:"))
                factorial(number)
            elif option == 8:
                number = int(input("Enter a number:"))
                strongNumber(number)
            else:
                print("--------Exiting--------")
                time.sleep(1)
                break
        else:
            print("invalid option")
            time.sleep(1)
            print("------finished---------")

def listProblems():
    while True:
        print("---------------------------------")
        print("welcome to list problems thread")
        print("---------------------------------")
        print("----------------")
        print("Choose an option")
        print("----------------")
        print("1.second large")
        print("2.swap first and last element")
        print("3.Exit thread")
        option = int(input("Enter option:"))
        if option <=3 and option >= 1:
            if option == 1:
                inputList = readList()
                secondLarge(inputList)
            elif option == 2:
                inputList = readList()
                swapFirstAndLast(inputList)
            else:
                print("--------Exiting--------")
                time.sleep(1)
                break
        else:
            print("invalid option")
            time.sleep(1)
            print("------finished---------")

def readList(helper=True):
    size = int(input("list size:"))
    inputList = [int(input("enter element:")) for _ in range(size)]
    if helper:
        return inputList
    else:
        print(f"the list elements is {inputList}")

def secondLarge(processList):
    processList.sort()
    print(f'Second largets element is {processList[-2]}')
    time.sleep(1)
    print("------finished---------")

def swapFirstAndLast(processList):
    temp = processList[0]
    processList[0] = processList[-1]
    processList[-1] = temp
    print(f"after swap list is {processList}")
    time.sleep(1)
    print("------finished---------")

def stringProblems():
    while True:
        print("---------------------------------")
        print("welcome to string problems thread")
        print("---------------------------------")
        print("----------------")
        print("Choose an option")
        print("----------------")
        print("1.palliandrome")
        print("2.reverse string")
        print("3.count vowels")
        print("4.common letter")
        print("5.Exit thread")
        option = int(input("Enter option:"))
        if option <=5 and option >= 1:
            if option == 1:
                inputString = readString()
                checkPalliandrome(inputString)
            if option == 2:
                inputString = readString()
                reverseStr(inputString)
            if option == 3:
                inputString = readString()
                countVowels(inputString)
            if option == 4:
                fisrtStatement = readString()
                secondStatement = readString()
                commonLetter(fisrtStatement, secondStatement)
            else:
                print("--------Exiting--------")
                time.sleep(1)
                break
        else:
            print("invalid option")
            time.sleep(1)
            print("------finished---------")

def readString():
    inputString = input("Enter string:")
    return inputString

def checkPalliandrome(string):
    reversedStr = reverseStr(string, helper=True)
    if string == reversedStr:
        print(f"{string} is a palliandrome")
    else:
        print(f"{string} is not a palliandrome")

def reverseStr(string, helper=False):
    reverse = ''
    count = len(string) - 1
    while count!=-1:
        reverse = reverse + string[count]
        count -= 1
    if not helper:
        print(f"reverse of the string is {reverse}")
    else:
        return reverse
    time.sleep(1)
    print("------finished---------")

def countVowels(inputString):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count=0
    for i in inputString:
        if i.lower() in vowels:
            count+=1
    print(f'number of vowels in {inputString} is {count}')
    time.sleep(1)
    print("------finished---------")

def commonLetter(fisrt, second):
    commons = False
    for i in fisrt.replace(' ', ''):
        if i in second:
            print(f"{i} is common in both statements")
            commons = True
    if not commons:
        print('nothing is common')
    time.sleep(1)
    print("------finished---------")
    
if __name__ == '__main__':
    while True:
        print("Choose an option")
        print("----------------")
        print("1.Number problems")
        print("2.List problems")
        print("3.String problems")
        print("4.Exit")
        option = int(input("Enter option:"))

        if option <= 4 and option >=1:
            if option == 1:
                numberProblems()
            elif option == 2:
                listProblems()
            elif option == 3:
                stringProblems()
            else:
                sys.exit(0)
        else:
            print("invalid option")
            time.sleep(1)
            print("------finished---------")
