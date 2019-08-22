# Create a program that prints the user input until they enter 'q' to quit.

askUser = ''

while askUser != 'q':
    askUser = input('enter something')
    print(askUser)


# Create a program that takes user input in a while loop. 
# If they enter 1, print 1. If they enter 2, print 2. If they enter 3 print 3. 
# If they enter ‘q’ or 0 (your choice), quit. Else, print “ERROR”.

askUser2 = ''

while askUser2 != 'q':
    askUser2 = input('enter 1 ,2 or 3 until you press q to quit')
    if askUser2 == '1':
        print('1')
    elif askUser2 == '2':
        print('2')
    elif askUser2 == '3':
        print('3')
    else:
        print('error')
 
# Create a program that takes the user input until they enter 'q'. 
# You should store all of their input and separate the input with a comma.
# Once they enter 'q', print all of the comma separated words they entered.

askUser3 = ''
storeIt = ''
while askUser3 != 'q':
    storeIt = storeIt + ", " +askUser3
    askUser3 = input('enter something')
print(storeIt)