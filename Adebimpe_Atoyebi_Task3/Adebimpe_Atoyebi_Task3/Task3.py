#11 using split to turn strings into list
fruits = "apple banana orange"
print(fruits.split())

#printing each word of a sentence in a new line
sentence = input("Enter a sentence: ")
words = sentence.split()
print(sentence)

#13 replacing spaces in a string with _
greeting = "hello, welcome to NCC"
print(greeting.replace(" ", "_"))

#14 counting 
fruit = "banana"
count = fruit.count("a")
print("There are", count, "a's in", fruit)

#15 To check if a string start with a word
hobby = "running and cooking"
print(hobby.startswith("https://"))