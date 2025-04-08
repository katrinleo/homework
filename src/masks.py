from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """функция маскировки номера банковской карты"""
    card_number_str = str(card_number)
    return (
        card_number_str[0:-16]
        + card_number_str[-16:-12]
        + " "
        + card_number_str[-12:-10]
        + "**"
        + " **** "
        + card_number_str[-4:]
    )


def get_mask_account(mask_account: Union[int, str]) -> str:
    """функция маскировки номера банковского счета"""
    mask_account_str = str(mask_account)
    return mask_account_str[0:5] + " **" + mask_account_str[-4:]
