def generate_inverted_pyramid(n):
    """
    Function to return an inverted pyramid pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows in the inverted pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the inverted pyramid.
    """
    # Your code here
    inverted_pyramid=[]
    for i in range(n,0,-1):
        inverted_pyramid.append(" "*(n-i)+"*"*((2*i)-1)+" "*(n-i))
            
    return inverted_pyramid

pyr=generate_inverted_pyramid(5)
for j in range(len(pyr)):   
    print(pyr[j],"\n")
