PRICE_CHILD = 4.50  
PRICE_SENIOR = 8.25 
PRICE_ADULT = 12.75 

total_cost = 0.0

print("вводите возраст каждого посетителя по одному.")
print("для завершения, нажмите enter (пустая строка). ")


while True:
    age_str = input("возраст посетителя: ")

    if age_str == "":
        print("ввод завершен.")
        break  

    try:
        age = int(age_str)
        if age < 0:
            print("возраст не может быть отрицательным. попробуйте снова.")
            continue  
        if age <= 2:
            current_price = 0.0
            print(f" (возраст {age}: билет бесплатный)")
        elif 3 <= age <= 12:
            current_price = PRICE_CHILD
            print(f" (возраст {age}: детский билет, {current_price:.2f} руб.)")
        elif age > 65:
            current_price = PRICE_SENIOR
            print(f" (возраст {age}: пенсионный билет, {current_price:.2f} руб.)")
        else:
            current_price = PRICE_ADULT
            print(f" (возраст {age}: взрослый билет, {current_price:.2f} руб.)")

        total_cost += current_price

    except ValueError:
        print(f"введено некорректное значение ('{age_str}'). требуется целое число.")


print(f"общая цена билетов для группы: {total_cost:.2f} руб.")