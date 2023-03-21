#Question 1: Write a function to print "hello_USERNAME!" USERNAME is the input of hte fuchtion.

def hello_name(user_name):
 print("hello " + user_name)
user_name = input('What is your user name?  ')
hello_name(user_name.upper() +"!")

#Question 2: Write a pythod function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds():
   for odds in range(1,101):
     if odds % 2 != 0:
        print(odds)
first_odds()

#Question 3: Please write a Phyton function, max_num_in_list to return the max number of the given list,

def max_num_in_list(a_list):
    maximum = a_list[0]
    for i in range(len(a_list)):
        if a_list[i] > maximum:
            maximum = a_list[i]
    return maximum
a_list = [3, 20, 680, 1980, 25]
print(max_num_in_list(a_list))

#Question 4: Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. 
#The return should be a boolean Type (true/flase.)

def is_leap_year(a_year):
    #divisible by 4 True
    if a_year % 4 == 0:
        return True
     #divisible by  100 False   
    elif a_year % 100 == 0:
        return False
    #divisible by 400 True
    elif a_year % 400 == 0:
        return True    
    #the rest False
    else:
        return False

a_year = int(input("Enter a year "))            
print(is_leap_year(a_year))

#Question 5: Write a function to check to see if alll numbers in list are consecutive numbers. 
#Example, [2, 3, 4, 5, 6, 7] are consecutive numbers but [1, 2, 4, 5] are not.

def is_consecutive(a_list):
      return sorted(a_list) == list(range(min(a_list), max(a_list)+1))
a_list = [2,3,4,5,6,7]
print(is_consecutive(a_list))
a_list = [1,2,4,5]
print(is_consecutive(a_list))

print("Thank you!")