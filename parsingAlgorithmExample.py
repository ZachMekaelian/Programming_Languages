def square_num (mylist):

    resultlist = []

    q = [1,2,3,4,5,6]

    while mylist:
        resultlist.append(mylist.pop(0) * q.pop(0))
    print(resultlist)

#in this main function, create a list with 6 numbers, call the second function in this question, print out the returned result. 

if __name__ == '__main__':

   #your answer here, can be multiple lines

   square_num([1,2,3,4,5,6])