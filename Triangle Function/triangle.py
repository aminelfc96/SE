def can_form_triangle(a, b, c):
    if not all(isinstance(side, (int, float)) for side in [a, b, c]):
        raise TypeError("All sides must be numeric values")
    
    if not all(side > 0 for side in [a, b, c]):
        raise ValueError("All sides must be positive")
    
    # Triangle inequality theorem: sum of any two sides must be greater than the third
    return (a + b > c) and (a + c > b) and (b + c > a)