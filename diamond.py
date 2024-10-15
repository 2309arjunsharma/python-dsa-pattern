def generate_diamond(n):
    """
    Function to return a diamond pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The number of rows for the upper part of the diamond.
    
    Returns:
    list: A list of strings where each string represents a row of the diamond.
    """
    # Your code here
    diamond=[]
    for i in range(1,n):
        diamond.append((" "*((n)-i)+"*"*((2*i)-1)+" "*(n-i)))
    for i in range(n,0,-1):
        diamond.append((" "*(n-i)+"*"*((2*i)-1)+" "*(n-i)))
            
    return diamond


dim=generate_diamond(3)
##for j in range(len(dim)):   
print(dim)
