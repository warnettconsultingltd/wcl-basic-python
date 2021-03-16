# Prompt the user to enter a name
name = input("Enter name! ")

# Output a Hello message containing the user name entered by separating th message portion from the name via a comma.
# This explicitly add a space between the two.
print("Hello", name)

# Output a Hello message containing the user name entered by concatenating the name.
# No space is added through this process, therefore we need to add one to the message.
print("Hello " + name)

# Create the message as a separate variable to output.
helloMessage = "Hello " + name
print(helloMessage)

