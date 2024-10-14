def generate_hollow_square(n):
    """
    Function to return a hollow square pattern of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The size of the square.
    
    Returns:
    list: A list of strings where each string represents a row of the hollow square.
    """
    # Your code here
    hollow_square=[]
    hollow_square.append("*"*n)
    
    for i in range(1, n-1):
        hollow_square.append("*"+" "*(n-2)+"*")
        
    if n>1:
        hollow_square.append("*"*n)
    return hollow_square
    
print(generate_hollow_square(3))