def generate_hollow_right_angled_triangle(n):
    """
    Function to return a hollow right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    hollow=[]
    if n>1:
        for i in range(1,3):
            hollow.append("*"*i)
        for i in range(2,n-1):
            hollow.append("*"+" "*(i-1)+"*")
        for i in range(n-1,n):
            hollow.append("*"*(i+1))
    else:
        if n==1:
            hollow.append("*")
        
    return hollow
    
print(generate_hollow_right_angled_triangle(5))
