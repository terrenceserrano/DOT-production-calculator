#create a program that will accept 2 arrays and multiply its indexes and add the indexes as an output

#using define function for OOP

def arrays():
    #array input that is separated by commas
    input_array = input("Enter your array here with comma: ")
    #using the 
    #list() for the collection of the variables of indexes
    #map() executes a specified function for each item in an iterable
    #split() divides the text around a specified character or string
    array = list(map(float, input_array.split(",")))
    return array #this is for the output of the function

#to call the define function
array1 = arrays()
array2 = arrays()

#this is for the calculation of the arrays
#sum() function add all the product inside the function
#for loop for reiteration of the indexes
#zip() function for pairing of the tuples and create a list
#use [] to create an empty list
sum = sum([a*b for a,b in zip(array1, array2)])

#converting the sum into string
print("The sum of the multipled array is: " + str(sum))

#the code above is the same as
#sum = 0 #this is the start of the count
#for i in range(len(array1)) #this is for the reiteration
#sum += array[i] * array[i] #this is for the computation
#print("sum is: " + str(sum)) #to convert the sum to string




