                                # Mario (more) 

"""
Create a program that prints the following shape with a user-inputted height: 

~/workspace/ $ mario.py
height: 5
    #  #
   ##  ##
  ###  ###
 ####  ####
#####  #####

Specification: 
    1. First prompt the user for the height of the pyramid 
    2. Generate the desired half-pyramids (with the help of print and one or more loops)
    3. Take care to align the bottom-left corner of your half-pyramid with the left-hand edge of your terminal window.
"""

# Code goes below here 
# get a height between 0 and 23 (inclusive)

while True: 
    height = int(input("height: "))
    if height >= 0 and height <= 23:
        break
    
for line in range(height): 
    # print spaces
    for spaces in range(height - line - 1):
        print(" ", end = "")
    
    # print left-pyramid  
    for hashes in range(line + 2):
        print("#", end = "")

    # print gap 
    print("  ", end = "")

    # print right-pyramid 
    for hashes in range(line + 2):
        print("#", end = "")

    # Print newline 
    print() 