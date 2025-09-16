REGULAR_PRICE = 3.52  
DISCOUNT_RATE = 0.55  

try:
    quantity_str = input("введите количество вчерашних буханок хлеба: ")
    quantity = int(quantity_str)

    if quantity < 0:
        print("количество не может быть отрицательным.")
    else:
        discounted_price = REGULAR_PRICE * (1 - DISCOUNT_RATE)
        total_cost = discounted_price * quantity
        FIELD_WIDTH = 10 

        print(f"обычная цена (1 шт.):     {REGULAR_PRICE:>{FIELD_WIDTH}.2f} руб.")
        print(f"цена со скидкой (1 шт.):  {discounted_price:>{FIELD_WIDTH}.2f} руб.")
        print(f"общая стоимость ({quantity} шт.):  {total_cost:>{FIELD_WIDTH}.2f} руб.")

except ValueError:
    print(f"введено некорректное значение ('{quantity_str}'); требуется целое число.")