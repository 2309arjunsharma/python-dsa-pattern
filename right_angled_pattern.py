def generate_triangle(n):
    """
    Function to return a right-angled triangle of '*' of side n as a list of strings.
    
    Parameters:
    n (int): The height and base of the triangle.
    
    Returns:
    list: A list of strings where each string represents a row of the triangle.
    """
    # Your code here
    right_angled=[]
    for i in range(1,n+1):
        right_angled.append("*"*(i))
        
    return right_angled
    
print(generate_triangle(5))