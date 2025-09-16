from itertools import permutations

def get_all_digit_subsets(n: int) -> set:
    s = str(n)
    all_m_values = set()
    for k in range(1, len(s) + 1):
        for p in permutations(s, k):
            m_str = "".join(p)          

            if len(m_str) > 1 and m_str[0] == '0':
                continue
                
            all_m_values.add(int(m_str))
            
    return all_m_values

def generate_sorted_list(n: int, mink: int, maxk: int) -> list:
    all_m = get_all_digit_subsets(n)
    
    final_results = set()
    
    for m in all_m:
        if mink <= m <= maxk:
            final_results.add(m * 2)  
            if m % 2 == 0:
                final_results.add(m // 2) 
    if not final_results:    
        return [] 
        
    return sorted(list(final_results))


n1, mink1, maxk1 = 10, 2, 5

print(f"n={n1}, mink={mink1}, maxk={maxk1} -> {generate_sorted_list(n1, mink1, maxk1)}")

n2, mink2, maxk2 = 9, 1, 4

print(f"\nn={n2}, mink={mink2}, maxk={maxk2} -> {generate_sorted_list(n2, mink2, maxk2)}")

n3, mink3, maxk3 = 47, 1, 1

print(f"\nn={n3}, mink={mink3}, maxk={maxk3} -> {generate_sorted_list(n3, mink3, maxk3)}")

n4, mink4, maxk4 = 100, 84, 99

print(f"\nn={n4}, mink={mink4}, maxk={maxk4} -> {generate_sorted_list(n4, mink4, maxk4)}")


print(f"n=210, mink=10, maxk=20 -> {generate_sorted_list(210, 10, 20)}")