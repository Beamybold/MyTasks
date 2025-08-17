#6 print to check the substring in a string
text = "I am learning python to become an AI developer"
print("python" in text)

#7 Reversing astring using join and reverse function
word = "capital"
reversed = "".join(reversed(word))
print(reversed)

#8  removing extra spaces in a string
state = " Adamawa       "
print(state.strip()) 

#9 printing out vowels from a sentence
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = 0
for char in sentence:
        if char in vowels:
                count += 1
print(f"There are {count} vowels in the sentence {sentence}.")

#10 convert a string to interger and * 2
num = "1234"
intNum = int(num)
operation = intNum * 2
print(f"{intNum} multiply by 2 is {operation}")


