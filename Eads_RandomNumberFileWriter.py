# Programming Exercise 6-7

import random
def main():
    #local variables
    filename = ''
    numberOfRandoms= 0
    randomNumber = 0

    #Get the file name as imput from the user
    filename = input('Enter the name of the file to '\
                    'which results should be written: ')

    # Get the number of items to write to the file.
    numberOfRandoms = int(input('Enter the number of '
                                'random numbers to be written to the file: '))
    
    # Open output file.
    outputFile = open(filename, 'w')

    # Write specified number of random numbers to the file.
    for counter in range (numberOfRandoms):
        #calling the randint function to generate a random number interger
        randomNumber = random.randint(1, 100)
        outputFile.write(str(randomNumber) + '\n')

    # Close the file.
    outputFile.close()
    print(numberOfRandoms, 'numbers were written to', filename)
#Call the main function.
main()

