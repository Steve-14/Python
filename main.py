



print ("hell0")

print (2 + 2)

print("Current day of the month")


#format_output

# an f string is like a template literal in Javascript

day = "modnday"
print (f"Today is {day}")

name = "Steve"

print (name)

name = "Steve Mason"
age = 60
city = "Stoke"

print (f"My name is {name}. Im {age} and I live in {city}")

#user_name = input( "What is your name ?" )
#user_age = input( "Your Age ? ")
#user_city = input( "Where do you live ? ")

#print (f"Yor name is {user_name.upper()} ,aged {user_age} and you live in {user_city.upper()}.")

#num_one = input("Pease enter a number between 1 and 100")
#num_two = input("Please enter a second number between 1 and 50")

#result =int(num_one) + int(num_two)

#print (result)

#colour = "amber"

#if colour == "green":
    #print ("Traffic light says GO")
    
#if colour == "green":
        #print ("Traffic light says GO")
#else: print( "stop")


#if colour == "green":
    #print ("Traffic light says GO")
#elif colour == "amber":
    #print( "go for it") 
#else:
    #print("BRAKE NOW")

 #match case 
 # 
weather = "sunny"

match weather:
        case "rain":
            print( "waterproof coat needed")
        case "windy":
            print ("hat and  scarf required")
        case  "sunny":
            print ("sunspecs today")
            
animal = ["monkey", "elephant", "tiger", "cobra", "zebra", "giraffe", "hedgehog"] 
continent = ["asia", "europe", "africa"]

#myzoo = [[animal[-1]], [continent[1]]]
#if myzoo[animal[5,6]] and myzoo[continent[1]]:
    #print (myzoo)
    



#test_score = int(input("Please enter your test score. The number should be between 1 and 100"))
#grade = "Z"
#match  int(test_score):
    #case 90,91,92,93,100
        #grade = "A"
        #print (f"you have acheived {grade} grade")
        

test_score = int(input("Please enter your test score. The number should be between 1 and 100 score: "))
grade = "Z"
match test_score:
        case score if 1 <= test_score < 60:
            grade = "F"
            print (f" You have acheived {grade} grade.") 
        case score if 60 <= score < 69:
            grade = "D"
            print (f" You have acheived {grade} grade.")
        case score if 69 <= score < 79:
            grade = "C"
            print (f" You have acheived {grade} grade.")
        case score if 79 <= score < 89:
            grade = "B"
            print (f" You have acheived {grade} grade. Well Done!!")
        case score if 89 <= score < 101:
            grade = "A"
            print (f" You have acheived {grade} grade. Outstanding!!")
            
            
            
    

