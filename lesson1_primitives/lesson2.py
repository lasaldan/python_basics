Name = input("What is your name? : ")
Age = input("What is your age? : ")
Height = input("What is your height? (ex. 5'8\") : ")
Favcereal = input("What is your favorite cereal? : ")
Heading = " My Profile"

width = 1

Name = " Name : " + Name + " "
Age = " Age : " + Age + " "
Height = " Height : " + Height + " "
Favcereal = " Favorite Cereal : " + Favcereal + " "

width = max( len(Name), len(Age), len(Height), len(Favcereal) )
# if(len(Name) > width):
#     width = len(Name)
#
# if(len(Age) > width):
#     width = len(Age)
#
# if(len(Height) > width):
#     width = len(Height)
#
# if(len(Favcereal) > width):
#     width = len(Favcereal)


while(len(Name ) < width):
    Name = Name + " "

while(len(Age ) < width):
    Age = Age + " "

while(len(Height ) < width):
    Height = Height + " "

while(len(Favcereal ) < width):
    Favcereal = Favcereal + " "

while(len(Heading ) < width):
    Heading = Heading + " "

# Adds a horizontal line
def horizontal_line():
    i = 0
    line = ""
    while(i < width + 2):
        line += "-"
        i = i + 1
    print(line)

# prints a row with pipes
def print_row_with_pipes(inner):
    line = "|"
    line += inner
    line += "|"
    print(line)



horizontal_line()
print_row_with_pipes(Heading)
horizontal_line()
print_row_with_pipes(Name)
# horizontal_line()
print_row_with_pipes(Age)
# horizontal_line()
print_row_with_pipes(Height)
# horizontal_line()
print_row_with_pipes(Favcereal)
horizontal_line()




# print("----------------------------------")
# print("|           My Profile           |")
# print("----------------------------------")
# print("| Name: " + Name +"|")
# print("----------------------------------")
# print("| Age: " + Age +"|")
# print("----------------------------------")
# print("| Height: " + Height +"|")
# print("----------------------------------")
# print("| Favorite Cereal: " + Favcereal +"|")
# print("----------------------------------")
