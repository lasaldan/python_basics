age = 25
name = input("What is your name? ")
hourlyWage = 16.50
single = True

def generateProfile():
    profile = "My name is " + name + ". My age is " + str(age)
    return profile

print( generateProfile() )

if(age > 24):
    print( "You are very old." )
    print( "And you're cool.")

elif(age > 20):
    print( "You are old.")

else:
    print( "You are young." )

counter = 0
while(counter < 5):
    print("  Python is cool.\n\n")
    counter = counter + 1
