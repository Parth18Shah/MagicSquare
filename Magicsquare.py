#Source Code to find/show the Magic Square for a certain order of matrix
'''A magic square of order n is an arrangement of n^2 numbers, usually distinct integers, 
in a square, such that the n numbers in all rows, all columns, 
and both diagonals sum to the same constant. 
A magic square contains the integers from 1 to n^2. '''

#Function for odd order magic squares 
def sq(n): 
  
    # 2-D array with all  
    # slots set to 0 
    ms = [[0 for x in range(n)] 
                      for y in range(n)] 
  
    # initialize position of 1 
    i = n / 2
    j = n - 1
      
    # Fill the magic square 
    # by placing values 
    num = 1
    while num <= (n * n): 
        if i == -1 and j == n:  
            j = n - 2
            i = 0
        else: 
              
            # next number goes out of right side of square  
            if j == n: 
                j = 0
                  
            # next number goes out of upper side 
            if i < 0: 
                i = n - 1
                  
        if ms[int(i)][int(j)]: # If the matrix already contains a number at the calculated position. 
            j = j - 2
            i = i + 1
            continue
        else: 
            ms[int(i)][int(j)] = num 
            num = num + 1
                  
        j = j + 1
        i = i - 1  
   
  
    # Printing magic square 
    print ("Magic Square for n =", n) 
    print ("Sum of each row or column", n * (n * n + 1) / 2, "\n") 
      
    for i in range(0, n):  # To display output in matrix form 
        for j in range(0, n): 
            print('%2d ' % (ms[i][j]), end = '')    
            if j == n - 1:  
                print() 
   
# Works only when n is odd 
n = int(input("Enter a number: "))
print(n) 
while n%2==0:
    n= int(input("We can take only odd numbers: "))
sq(n) # Calling the function sq. 