from stat import FILE_ATTRIBUTE_SPARSE_FILE


format_output ="\033[47m\033[30m"
format_reset = "\033[0m"

print(f"{format_output}--START--{format_reset}")

#tuples
#tuples are immutable data collections
#Think of them as lists that dont change

fruits = ("apple", "orange", "banana")

print(fruits)
print(fruits[1])

print("items in tuple:", len(fruits))

#iterating thru a tuple
for fruit in fruits:
    print(fruit)
    
#SETS
## a set uses curly brackets ## 
days_of_week = {"monday", "tuesday", "wednesday", "thursday", "friday","saturday","sunday"}
print(days_of_week)

weekend = {"saturday", "sunday"}
print(days_of_week.intersection(weekend))

print(days_of_week & weekend)

# difference allows us to access values that are in the FIRST set but NOT the second
print(days_of_week.difference(weekend))

"""def view_playlist():
    for song in playlist:
        print(f"Song: {song}")
        print(f"Artist: {playlist}[{song}]["Artist"]")
        #print(f"Genre: {song}['Genre']")"""







