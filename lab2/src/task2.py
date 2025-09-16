NOISE_LEVELS_DB = {
    130: "отбойный молоток",
    106: "газовая газонокосилка",
    70: "будильник",
    40: "тихая комната"
}

LEVELS_SORTED = sorted(NOISE_LEVELS_DB.keys())
MIN_LEVEL = LEVELS_SORTED[0]  
MAX_LEVEL = LEVELS_SORTED[-1] 


try:
    level_str = input("введите уровень шума в децибелах (дБ): ")
    user_level = float(level_str) 
 
    if user_level in NOISE_LEVELS_DB:
        source = NOISE_LEVELS_DB[user_level]
        print(f"уровень {user_level} дБ в точности соответствует источнику: {source}.")   
    elif user_level > MAX_LEVEL:
        print(f"уровень {user_level} дБ выше максимального значения в таблице ({MAX_LEVEL} дБ, {NOISE_LEVELS_DB[MAX_LEVEL]}).") 
    elif user_level < MIN_LEVEL:
        print(f"Уровень {user_level} дБ ниже минимального значения в таблице ({MIN_LEVEL} дБ, {NOISE_LEVELS_DB[MIN_LEVEL]}).") 
    else:    
        for i in range(len(LEVELS_SORTED) - 1):
            lower_bound = LEVELS_SORTED[i]      
            upper_bound = LEVELS_SORTED[i+1]    
            
            
            if lower_bound < user_level < upper_bound:
                source_low = NOISE_LEVELS_DB[lower_bound]
                source_up = NOISE_LEVELS_DB[upper_bound]
                print(f"уровень {user_level} дБ находится между {lower_bound} дБ ({source_low}) и {upper_bound} дБ ({source_up}).")
                break 

except ValueError:
    print(f"введено некорректное значение ('{level_str}'); требуется число.")