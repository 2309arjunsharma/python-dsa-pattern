def generate_number_pyramid(n):
    """
    Function to return a pyramid pattern of numbers of height n as a list of strings.
    
    Parameters:
    n (int): The height of the pyramid.
    
    Returns:
    list: A list of strings where each string represents a row of the pyramid pattern.
    """
    # Your code here
    pyramid = []
    for i in range(1, n + 1):
        spaces = ' ' * (n - i)
        numbers = ' '.join(str(x) for x in range(1, i + 1))
        pyramid.append(spaces + numbers + spaces)
    return pyramid


print(generate_number_pyramid(4))
