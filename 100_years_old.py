#Austin Lindstrom
#Program - What year will you be 100 years old



print('What is your name?')
name = input()

print('How old are you?')
ages = int(input())

print('What year is it?')
years = int(input())



def year(age,year):
        
        newYear = (years-ages) + 100
        print(name + ", you will be 100 years old in the year " + str(newYear))
        return newYear
        
    
year(ages,years)