#String input
name=input("Enter your name: ")
print(name)
#Integer input
num=int(input("Enter a number: "))
print(num)
#Float input
price=float(input("Enter the price: "))
print(price)
#List of integers input
my_list=[1,2,3,4,5]  # Don't use 'list' as variable name - it's a keyword!
print(my_list)
print(type(my_list))

#Print()
print("Hello, World!")

name ="jhanu" 
age = 25
print(name ,age)
print('2000','06','05',sep='-')
print('Hello',end=' ')
print('World!')
print(f"Name: {name}, Age: {age}")
print("Name: %s, Age: %d" % (name, age))