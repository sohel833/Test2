userName = '''
1. User Input and Replace String Template “Hello <<UserName>>, How are you?”
a. I/P -> Take Username as Input. Ensure UserName has min 3 char
b. Logic -> Replace <<UserName>> with the proper name
c. O/P -> Print the String with username
'''
username = input("Enter Your Name: ")
Greetings = "Hello <<UserName>>, How are you?"
GreetingsOutput = Greetings.replace("<<UserName>>",username)
print(GreetingsOutput)
