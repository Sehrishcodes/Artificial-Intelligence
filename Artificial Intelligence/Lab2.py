    #while loop
count=0
while (count<3):
    count =count+ 1
print("Hello World")

 


#for in loop
print("List Iteration")
list1 = [ "Greeks", "for","Greeks"]
for i in list1:
        print(i)


print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
        print(i)


        print("\nString Iteration")
        s= "Geeks"
        for i in s:
               print(i)


#Iteration by Index
list2= ["geeks","for","geeks"]
for index in range(len(list2)):

    print (list2[index])



    #control statements
    #print all letters except e and s
for letter in 'geeksforgeeks':
    if letter=='e'or letter== 's':
          continue
    print ('Current Letter:', letter)
    var = 10

#break statement
    for letter in 'geeksforgeeks':
     if letter=='e'or letter== 's':
          break
    print ('Current Letter:', letter)

#function
def my_function(): print("Hello from a function") 
my_function() 

#Example2 Calling  a function
def my_function(fname): 
     print(fname + " Refsnes") 
my_function("Emil") 
my_function("Tobias")
my_function("Linus") 

#default parameter 
def my_function(country = "Norway" ):print("I am from " + country) 
my_function("Sweden")  
my_function("India")  
my_function() 
my_function("Brazil") 


#passing a list parameter
def my_function(food): 
    for x in food: 
     print(x) 
fruits = ["apple", "banana", "cherry"] 
my_function(fruits) 

def my_function(child3, child2, child1): 
     print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus") 


#Create a class named Person, use the     init    () function to assign values for name and age: 
class Person:
     def init (self, name, age): self.name = name ,self.age = age 
p1 = Person("John", 36) 
print(p1.name) 
print(p1.age) 



class Person: 
    def init (self, name, age): self.name = name, self.age = age
    def myfunc(self): print("Hello my name is " + self.name)
p1 = Person("John", 36) 
p1.myfunc() 

