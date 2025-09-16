import sys

class RomanConverter:
    def __init__(self):
        
        self.roman_map = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    def to_integer(self, roman_str: str) -> int:
        total = 0
        prev_value = 0
        
        
        for char in reversed(roman_str.upper()):
            current_value = self.roman_map.get(char)
            
            if current_value is None:
                raise ValueError(f"недопустимый символ в римском числе: '{char}'")
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value           
            prev_value = current_value
            
        return total


class SubsetGenerator:
    def get_subsets(self, nums_list: list) -> list:
        results = [[]]
        distinct_nums = sorted(list(set(nums_list)))
        
        for num in distinct_nums:
            new_subsets = [subset + [num] for subset in results]
            results.extend(new_subsets)     
        return results


class TwoSumFinder:
    def find_pair(self, nums_list: list, target: int) -> list | None:
        seen_map = {}  
        
        for index, value in enumerate(nums_list):
            complement = target - value
            if complement in seen_map:
                return [seen_map[complement], index]
            seen_map[value] = index
            
        
        return None



class StringReverser:
    def reverse_words(self, s: str) -> str:  
        words = s.split()
        reversed_words = reversed(words)

        return " ".join(reversed_words)


if __name__ == "__main__":
    print("\nзадача 1: римские числа")
    converter = RomanConverter()
    test_roman = "MCMXCIV" 
    print(f"число '{test_roman}' в int: {converter.to_integer(test_roman)}")
    test_roman_2 = "LVIII" 
    print(f"число '{test_roman_2}' в int: {converter.to_integer(test_roman_2)}")

    
    print("\nзадача 2: уникальные подмножества  ")
    subset_gen = SubsetGenerator()
    test_nums_1 = [1, 2, 3]
    print(f"подмножества для {test_nums_1}: {subset_gen.get_subsets(test_nums_1)}")
    
    
    print("\nзадача 3: поиск суммы (two-sum)  ")
    finder = TwoSumFinder()
    test_nums_2 = [2, 7, 11, 15]
    target_1 = 9
    print(f"индексы для {test_nums_2} (сумма {target_1}): {finder.find_pair(test_nums_2, target_1)}")
    target_2 = 26
    print(f"индексы для {test_nums_2} (сумма {target_2}): {finder.find_pair(test_nums_2, target_2)}")
    
    
    print("\nзадача 4: переворот слов в строке  ")
    reverser = StringReverser()
    test_str_1 = "  hello world  "
    print(f"строка: '{test_str_1}'\nрезультат: '{reverser.reverse_words(test_str_1)}'")
    test_str_2 = "the sky is blue"
    print(f"\nстрока: '{test_str_2}'\nрезультат: '{reverser.reverse_words(test_str_2)}'")