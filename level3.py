# Step 1   - printing for display
print("G U E S S I N G    G A M E")
print("--------------------------")
print("Please think of a number (between 1 and 5) ")

# Step 2  - interactivity, getting input from user
input("Press enter when you are ready!...")

# Step 3 - conditionals
guess = 1 
print ("Is it", guess, "?")
resp = input("Is it correct? (Higher/H, Lower/L or yes) ")
if resp in ['yes', 'Yes', 'Y', 'y']:
	print("Number in 1 tries!")

count = 1
