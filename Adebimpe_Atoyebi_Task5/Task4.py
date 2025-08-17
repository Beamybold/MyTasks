print("Enter your deatails")
FirstName = input("Enter your first name: ")
Age = int(input("Enter your age: "))
FavouriteColor = input("Enter your fav colour: ")
HomeTown = input("Enter your hometown: ")
userDetails = (FirstName, Age, FavouriteColor, HomeTown)
# print(userDetails)
FirstName, Age, FavouriteColor, HomeTown = userDetails
print(f"User Details\tResponses\nFirst name\t{FirstName}\nAge\t\t{Age}\nFavourite color\t{FavouriteColor}\nHome town\t{HomeTown}")
