import random
import re
import sys
import timeit
import datetime

def ex_1():
    random_numbers =[]
    sum = 0

    for i in range(10):
        random_numbers.append(random.randint(0,100))
        sum += random_numbers[i]
    
    print(f'sum: {sum} for array list {random_numbers}')



def ex_2():
    width = input("Enter width:")
    length = input("Enter length: ")
    height = input("Enter height: ")

    width = float(width)
    length = float(length)
    height = float(height)
    
    print(f'Volume is: {width * length * height}')

def ex_3():
    str = input("Enter a list of numbers ex 1,2,3 : ")
    nums = str.split(',')
    print(int(nums[0]) == int(nums[-1]))

def ex_4():
    txt = "Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to ABC programming language, which was inspired by SETL capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his permanent vacation from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected a 5-member Steering Council to lead the project. As of 2021, the current members of this council are Barry Warsaw, Brett Cannon, Carol Willing, Thomas Wouters, and Pablo Galindo Salgado."
    words = txt.split(' ')
    pattern = re.compile("^Python$")
    cnt = 0
    for word in words:
        if pattern.match(word):
            cnt += 1
    print(cnt)

def ex_5():
    myList = [1,2,3]
    mySet = {3,4,5}
    mySet.update(myList)
    print(mySet)

def ex_6(): 
    myList = [11, 100, 101, 999, 1001]
    for i in range(int(len(myList)/2)):
        myList[i], myList[-1-i] = myList[-1-i], myList[i]
    print(myList)

def ex_7():
    random_number = random.randint(1,100)
    if random_number < 10:
        print(f'{random_number} you lose')
    elif 50 > random_number >= 10:
        print(f'{random_number} try again')
    else:
        print(f'{random_number} you win')

def ex_8():
    myList = [6,2,7,3,-33,77,7,1]
    mx = sys.maxsize
    for i in range(len(myList)):
        if myList[i]<mx:
            mx = myList[i]
    print(mx)
    
def ex_9():
    word1_is_upper ="HELLO"
    word2_is_not_upper="world"
    print(word1_is_upper.isupper())
    print(word2_is_not_upper.isupper())

def ex_10():
    mySet = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    txt = "HellO"
    vowels = 0
    for letter in txt:
        if letter in mySet:
            vowels += 1
    consonants = len(txt) - vowels
#     print(f'''Vowels: {vowels}
# Consonants: {consonants}''')
    return
    
def ex_102():
    string = "HellO"
    vowels = r'[aeiouAEIOU]'
    vowel_count = len(re.findall(vowels, string))
    cons_count = len(string) - vowel_count
#     print(f'''Vowels: {vowel_count}
# Consonants: {cons_count}''')
    return
def ex_11():
    file1 = open('output.txt', 'w')
    current_time = datetime.datetime.today()
    current_time = current_time.strftime('%m/%d/%Y')
    # Writing a string to file

    file1.write(f'Today\'s date is: {current_time}')
    # Closing file
    file1.close()
    return
def ex_12():
   my_num= input("Enter a num:  ")
   try: 
    my_num = int(my_num)
    print(int(my_num) * -1)
   except:
    print(f'ERROR: {my_num} is not an integer')

def ex_13():

    while(True):
        num1 = input("Enter first integer: ")
        if(num1 == 'exit'):
            break
        num2 = input("Enter a second integer: ")
        if(num2 == 'exit'):
            break
        else:
            print(f'Answer {int(num1) + int(num2)}')

    return
# def ex_14():
#     return
# def ex_15():
#     return
# def ex_16():
#     return
# def ex_17():
#     return
# def ex_18():
#     return
# def ex_19():
#     return
# def ex_20():
#     return        

#ex_1()
# ex_2()
# ex_3()
# ex_4()
# ex_5()
ex_6()
# ex_7()
# ex_8()
# ex_9()

# exec_time = timeit.timeit(ex_10, number=10**6)
# exec_time2 = timeit.timeit(ex_102, number=10**6)
# print(exec_time,exec_time2)
# ex_10()
# ex_102()
# ex_11()
# ex_12()
# ex_13()

