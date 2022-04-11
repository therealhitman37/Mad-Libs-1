#string concatenation(aka how to put strings together)
#suppose we want to create a sting that says "subschribe to _____"

youtuber = input("Name of the youtuber: ") #some sring available

# a few ways to do this
print("subscribe to " + youtuber)
print("subscribe to {}" . format(youtuber))
print(f"subscribe to {youtuber}")