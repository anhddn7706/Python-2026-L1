favorite_color = input("What is your favorite color?")
color = ["red", "blue", "green", "yellow", "black", "white"]
print(f"your favorite color is {favorite_color}")
if favorite_color in color:
    print(f"Your color is at index {color.index(favorite_color)} in my list")
else:
    print("Sorry, I could not find your color")
