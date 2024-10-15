def generate_pyramid(n):
    """
    Function to return a pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid.
    """
    # Your code here
    pyramid=[]
    for i in range(1,n+1):
        pyramid.append(" "*(n-i)+"*"*((2*i)-1)+" "*(n-i))
            
    return pyramid


pyr=generate_pyramid(9)
for j in range(len(pyr)):   
    print(pyr[j],"\n")