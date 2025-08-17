votersName = set()
name = input("enter voters name: ")
name2 = input("enter voters name2: ")
name3 = input("enter voters name3: ")
name4 = input("Enter your name4:")
names = (name, name2, name3, name4)
votersName = set(names)
print(votersName)

if names in votersName: #to check if name is in votersname
    print(f"Warning:{name} You have been registered.")
# else:
#     votersName.add()
#     print(f"{name} You have successfully register.")
print("Registration complete!")
print(f"The total number of unique voters are {len(votersName)}")