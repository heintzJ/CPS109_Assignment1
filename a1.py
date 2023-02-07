'''
I need a quick, easy, way to do vector operations.
I can do this by implementing functions that correspond
to each operation (addition, subtraction, magnitude...)
'''
# create a file for output
f = open("output.txt", "a")

# list of possible vector operations
operations = ["+", "-", "mag", "unit"]

# empty list to store first vector input
vector_1 = []
# empty list to store second vector input
vector_2 = []

# initialize the addition function
def addition(v1,v2):
    # add each digit in the vector_1 to the corresponding digit in vector 2
    #   zip goes through each of the digits and pairs them 
    vector = [v1 + v2 for v1, v2 in zip(v1, v2)]
    # Could also use:
    #   list(map(sum, zip(v1, v2)))
    # print the sum of the two vectors
    answer = (f"{vector_1} + {vector_2} = {vector}")
    # write the answer to the output file
    f.write(f"{str(answer)}\n------\n")
    # close the file, so it cannot be edited anymore
    f.close()

# initialize the subtraction function
def subtraction(v1,v2):
    # subtract each digit in the vector_1 to the corresponding digit in vector 2
    #   zip goes through each of the digits and pairs them 
    vector = [v1 - v2 for v1, v2 in zip(v1, v2)]
    # print the sum of the two vectors
    answer = (f"{vector_1} - {vector_2} = {vector}")
    # write the answer to the output file
    f.write(f"{str(answer)}\n------\n")
    # close the file
    f.close()

# initialize the magnitude function
def magnitude():
    # take the square root of each digit in the vector
    mag = (sum(i**2 for i in vector_1))**(1/2)
    # print the magnitude to the output file
    f.write(f"Magnitude of {vector_1} = {str(mag)}\n------\n")
    # close the file
    f.close()

# initialize the unit vector function
def unit_vector():
    # create an empty list for the unit vector
    unit = []
    # find the magnitude
    mag = (sum(i**2 for i in vector_1))**(1/2)
    # divide each digit in vector_1 by the magnitude of the vector
    for i in vector_1:
        unit.append(i/mag)
    # print the unit vector to the output file
    f.write(f"Unit vector of {vector_1} = {str(unit)}\n------\n")
    # close the file
    f.close

# boolean
running = True

while running == True:
    # Any loop will start with one vector
    # First input is the x-value of the vector
    vector_1_x = float(input("Vector 1 x: "))
    # Append the x-value to the empty vector_1 list
    vector_1.append(vector_1_x)
    # Ask for the y-value, then append it to vector_1
    vector_1_y = float(input("Vector 1 y: "))
    vector_1.append(vector_1_y)
    # Ask for the x-value, then append it to vector_1
    vector_1_z = float(input("Vector 1 z: "))
    vector_1.append(vector_1_z)

    # Ask for a vector operation to do
    operation = input("Operation: ")
    # check if the input is valid
    if operation in operations:
        # if the input is addition...
        if operation == "+":
            # Take input for the x-value of vector_2  
            vector_2_x = float(input("Vector 2 x: "))
            # Append the x-value to the vector_2 list
            vector_2.append(vector_2_x)
            # Ask for the y-value, then append it to vector_2
            vector_2_y = float(input("Vector 2 y: "))
            vector_2.append(vector_2_y)
            # Ask for the y-value, then append it to vector_2
            vector_2_z = float(input("Vector 2 z: "))
            vector_2.append(vector_2_z)

            addition(vector_1, vector_2)
            running = False

        # if the input is subtraction...
        elif operation == "-":
            # Take input for the x-value of vector_2  
            vector_2_x = float(input("Vector 2 x: "))
            # Append the x-value to the vector_2 list
            vector_2.append(vector_2_x)
            # Ask for the y-value, then append it to vector_2
            vector_2_y = float(input("Vector 2 y: "))
            vector_2.append(vector_2_y)
            # Ask for the y-value, then append it to vector_2
            vector_2_z = float(input("Vector 2 z: "))
            vector_2.append(vector_2_z)

            subtraction(vector_1,vector_2)
            running = False

        # if the input is magnitude...  
        elif operation == "mag":
            magnitude()
            running = False

        # if the input is unit vector...
        elif operation == "unit":
            unit_vector()
            running = False

# 59 lines of code
# 48 lines of comments (excluding these two and the problem introduction)