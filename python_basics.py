#Python lab 1
#Learn from the online interactive tutorial and finish below tasks
#You can edit in this file by filling blanks after each question.
#Submit the .py file for your own reference
#This practice is graded only on submission.
#It will help you to get started on Python for the homework

#####
#Example function
#####
def example(): #def is function definition
    print("I am the example code")
#Now, go to the end of this file and you will find the main function & how to run your code there
#Around line #94


#####
#1. function in python
####

def printHello(): #Remove the # at the begining of this line.
    #tab is IMPORTANT in python. tab in python replaces {} in C++
    #print string hello world. One line of code here. Make sure it is indented to show it belongs to this function
    print("Hello World!")

#####
#2. variable definition in python
#####

def someVars():
    #define a few integer and float numbers, add them together and print result out
    a = 1
    b = 2.2
    c = a+b
    print(c)
#call the function to run it in the main function at the end of the file

#####
#3. define a list in python
#####

def mylis():
    #define a list with 5 numbers, print it out
    myList = [1,2,3,4,5]
    print(myList)
    #define an empty list and append a few numbers into it, then print it out
    emptyList = []
    emptyList.append(1)
    emptyList.append(2)
    emptyList.append(3)
    emptyList.append(4)
    emptyList.append(5)
    print(emptyList)

#call your mylis func to execute in the main function at the end of the file

#####
#4. string output
#####

def printstr(input_str1, input_int1):
    #convert int into string and append the int with the string to form a long string
    #(technical googling practice -- google what func to use)
    #print the long str out
    input_int1 = str(input_int1)
    print(input_str1 + input_int1)
#In the main function, define an input string and an input int.
#Pass them in as parameters to the function. Call and run the function to see results.

####
#5. passing var to func and return
####

def funcvars(inputvar1, inputvar2):
    #add the input numbers together
    #returen the result
    result = inputvar1 + inputvar2
    print(result)

#Define the input variables in main, pass them into the function.
#In main, use a result variable to receive the result from funcvars and print the result out

####
#6. for loop
####

def go_over_list(mylis):
    #use for loop to go over the input list and print out items one by one
    for asdf in mylis:
        print(asdf)
def go_over_list1():
    #use for loop to directly print out numbers from 10 to 17
    for q in range(10,18):
        print(q)

def go_over_list2(mylis):
    #use for loop & go over your list
    #multiply 2 to every item in your list, print results out
    for q in mylis: # q = 1,2,3,4,5
        q = 2 * q      #q = (1,2,3,4,5) * 2
        print(q)
def go_over_list3(mylis):
    #create an empty list resLis
    #go over items in the input list, multiply 2 to every item
    #add result one by one to resLis
    #return resLis
    resLis = []
    for q in mylis:
        q = q * 2
        resLis.append(q)
        print(resLis)
    print("or...")
    print(resLis)

#Call all the functions in main. Provide necessary inputs to the functions.
#For those with return values, print the return values out in main.

####
#7. while loop
####

#do all the problems in 6 using while loop instead
def go_over_list_list(mylis):
    while mylis:
        print(mylis.pop(0)) #zachary you are a fucking genius

def go_over_list_list1():
    #use while loop to directly print out numbers from 10 to 17
    a = 10
    while a <= 17:
        print(a)
        a = a + 1
def go_over_list_list2(mylis):
    #use a while loop & go over your list
    #multiply 2 to every item in your list, print results out
    while mylis:
        print((mylis.pop(0)) *2)
def go_over_list_list3(mylis):
    #create an empty list resLis
    #go over items in the input list, multiply 2 to every item
    #add result one by one to resLis
    #return resLis
    resLis = []
    while mylis:
        resLis.append(mylis.pop(0) * 2)
        print(resLis)
    print("or...")
    print(resLis)

#####
#Here is the main function
#You can have only 1 main function in 1 script
#Left click on the green arrow next to the line number of the line of the main function definition
#Your code would run.
if __name__ == '__main__': #a quick way to type this line is: type "main" and then tab
    print("****Question 1****")
    example()
    print("****Question 2****")
    #you can start call and run your functions here
    printHello()
    print("****Question 3****")
    someVars()
    print("****Question 4****")
    mylis()
    print("****Question 5****")
    printstr("two",2)
    print("****Question 6****")
    funcvars(1,2)
    print("****Question 7****")
    go_over_list([1,2,3,4,5])
    print("****Question 8****")
    go_over_list1()
    print("****Question 9****")
    go_over_list2([1,2,3,4,5])
    print("****Question 10****")
    go_over_list3([1,2,3,4,5])
    print("****Question 11****")
    go_over_list_list([1,2,3,4,5])
    print("****Question 12****")
    go_over_list_list1()
    print("****Question 13****")
    go_over_list_list2([1,2,3,4,5])
    print("****Question 14****")
    go_over_list_list3([1,2,3,4,5])
    print("****Question 15****")

######
#Python is an easier PL to learn than C++ and looks like C++
#From this lab experience, reflect and summary what it feels like
#when you are learning a new PL that is similar to a PL that you already know?
#Your answer here:

#In this case, when you want to learn a new PL that looks like a PL that you already know,
#how can you learn the new PL quickly? Any steps?
#Your answer here:
