import csv      
import pickle   
import re       


ATOMIC_WEIGHTS = {
    'H': 1.008,
    'C': 12.011,
    'N': 14.007,
    'O': 15.999,
    'Na': 22.990,
    'Cl': 35.453,
    'Fe': 55.845,
}


class ChemicalCompound:
    def __init__(self, formula: str):
        self.formula = formula
        self.molar_mass = 0.0  

    def __repr__(self):
        
        return f"compound(formula='{self.formula}', mass={self.molar_mass:.3f} г/моль)"




def calculate_molar_mass(formula: str, weights_dict: dict) -> float:
    total_mass = 0.0
 
    try:
        matches = re.findall(r'([A-Z][a-z]*)(\d*)', formula)  
        if not matches:
            raise ValueError(f"не удалось распознать формулу: {formula}")
        for (element, count_str) in matches:
            if element not in weights_dict:
                raise ValueError(f"неизвестный элемент в словаре: {element}")
            count = int(count_str) if count_str else 1          
            total_mass += weights_dict[element] * count
            
    except ValueError as e:
        print(f"ошибка при расчете '{formula}': {e}")
        return 0.0
        
    return total_mass


if __name__ == "__main__":
    
    INPUT_FILE = 'data/formulas.csv'
    OUTPUT_FILE = 'compounds.pkl'  
    
    compounds_list = []  
    
    print(f"чтение CSV файла '{INPUT_FILE}'...")
    
    try:
        with open(INPUT_FILE, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                formula = row['formula']
                compound = ChemicalCompound(formula)
                compound.molar_mass = calculate_molar_mass(compound.formula, ATOMIC_WEIGHTS)
                compounds_list.append(compound)
                print(f"рассчитано: {compound}")

        print(f"\nзапись в бинарный файл '{OUTPUT_FILE}'...")
        
        
        
        with open(OUTPUT_FILE, mode='wb') as f:
            pickle.dump(compounds_list, f)
            
        print("данные успешно сохранены.")

        
        print(f"\nпроверка: чтение из '{OUTPUT_FILE}'...")
        
        with open(OUTPUT_FILE, mode='rb') as f:
            loaded_data = pickle.load(f)
            print("данные успешно загружены:")
            for item in loaded_data:
                print(item)

    except FileNotFoundError:
        print(f"не найден входной файл '{INPUT_FILE}'.")
    except Exception as e:
        print(f"произошла непредвиденная ошибка: {e}")