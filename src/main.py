from src.masks import get_mask_account, get_mask_card_number

card_number_str = input("Введите номер карты: ")
print(get_mask_card_number(card_number_str))

mask_account_str = input("Введите номер счета: ")
print(get_mask_account(mask_account_str))
