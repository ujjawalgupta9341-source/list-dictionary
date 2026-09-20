#in this i will do code on the basis of list and dictionary
#WAP to asked to enter names of their 3 favourite movies and store them in a list .
movie1 = input("Enter the name of your 1 favourite movie: ")
movie2 = input("Enter the name of your 2 favourite movie: ")
movie3 = input("Enter the name of your 3favourite movie: ")

movies = [movie1, movie2, movie3]
print(movies)


#WAP to check if a list contains a palindrome of element.
list=[1,2,3,4,5,6,5,4,3,2,1]

if list==list[::-1]:
    print("this is palandromic sequence -",list)
else:
    print("this is not a Palindromic sequeunce")

#just used the input command .
list=input("enter the list of palindromic sequence").split()

if list==list[::-1]:
    print("this is palandromic sequence -",list)
else:
    print("this is not a Palindromic sequeunce")


####dictionary
#store following word meaning in a python dictionary
#table:"a peice of furniutre ", list of facts and figures 
#cat:'a small animal'

dict={
    "table":['a peice of furniture','use as study' 'table dining table'],

     "cat":'a small animal'

}
print(dict)
print(type(["table"]))


#1 you are given a list of subjects. assume one class is required for 1 subjects.
#how many classroom are needed by all students
#subjtec=pyhton, java, c++, python,javascript, java, python, java, c++, c '''

subjects=['python' ,'java' ,'c++' ,'python' ,'javascript' ,'java' ,'python' ,'java' ,'c++' ,'c']
a=len(set(subjects))
print("total no. of subject=",a,"\nso total subject =",a) 


#2 WAP to enter marks of 3 subjects from the user and store them is dictionary. 
#start whith ann empty dict &1 by 1. use subject name as key & marks as value
dict={}
subject=input("enter 1 subject name -")
marks=float(input("enter your marks--"))
dict[subject]=marks 

subject=input("enter 2 subject name-")
marks=float(input("enter the marks--"))
dict[subject]=marks

subject=input("enter the 3 subject name-")
marks=float(input("enter the marks--"))
dict[subject]=marks

print(dict)

#4. figure out a way to store 9 & 9.0 as seprate value in the set.
set={ (9,int), (9.0,float)

}
print(set)
print(len(set))