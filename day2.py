from ast import While
from codecs import BOM_BE


format_output ="\033[47m\033[30m"
format_reset = "\033[0m"

#lists and loops

# creating a list

languages = ["Javascript","CSS", "HTML", "Python", "SQL"]

print(languages) # prints each item in languages

print(languages[2]) # prints item at index 2 (3rd item)

languages[2]="JAVA" # replaces HTML with "JAVA"
print(languages)














#########===============Task Questions===============#######################


Drinks = ["Coffee", "Tea", "Cola", "Fruit Juice", "Herbal Tea", "Whisky", "IPA"]

for drink in Drinks: # For Loop (List): Write a for loop that prints each item in a list
    print(drink)

Quote = "Now is the time for each man to do his duty"
print (Quote)

#for char in Quote: # For Loop (String): Write a for loop that prints each character in a string
    #print (char)
    
#foobar = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15] # For Loop with Range: Write a for loop that prints numbers 1 to 10 using the range function
#for i in (range(11)):
    #print (i)
    
# Basic While Loop: Write a while loop that prints numbers from 1 to 10.#
#numb = 1
    
#while numb < 10: 
    #print(numb)
    #numb = numb + 1
    
# While Loop with Break: Implement a 'break' statement in a while loop that prints numbers from 1 to 10 and stops when it reaches 5. #
#numb = 0
#while numb < 10:
    #print(numb)
    #if numb > 4:
        #break
    #numb = numb + 1
    
# implement a while loop that prints numbers from 1 to 10, but skips printing the number 5 using continue
#numb = 0
#while numb < 10:
    #numb = numb + 1 
    #if numb == 5:
         #continue
    #print(numb)
    
#def greet(yo):
    #name = input("What's your name: ")
    #return yo + name
#print (greet("hi! "))

def get_user_name():
    # Function to get the user's name from input
    name = input("Please enter your name: ")
    return name
def generate_a_greeting(name):
    # Function to generate a dynamic greeting message
    return (f"Hello, {name}! Welcome to the machine.")
def main():
    # Main function to run the program
    user_name = get_user_name()
    greeting = generate_a_greeting(user_name)
    print(greeting)
    
main()