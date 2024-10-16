def generate_sandglass(n):
    """
    Function to return a sandglass pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the sandglass.
    
    Returns:
    list: A list of strings where each string represents a row of the sandglass pattern.
    """
    # Your code here
    sandglass=[]
    for i in range(n):
        sandglass.append((" "*i+"*"*((2*(n-i))-1)+" "*i))
    for i in range(n-1):
        sandglass.append((" "*(n-i-2)+"*"*((2*(i+1))+1)+" "*(n-i-2)))
            
    return sandglass
    
sandy=generate_sandglass(3)
##for j in range(len(dim)):   
print(sandy)