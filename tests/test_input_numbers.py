


def validate_phone_number(phone_number):
    if phone_number.startswith("380") and len(phone_number) == 12 and phone_number[1:].isdigit():
        print("OK")
        return True
    else:
        print("NO")
        return False

