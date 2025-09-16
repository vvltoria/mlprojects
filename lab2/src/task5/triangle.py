def is_triangle_possible(a: float, b: float, c: float) -> bool:
    if a <= 0 or b <= 0 or c <= 0:
        return False
    
    return (a + b > c) and (a + c > b) and (b + c > a)