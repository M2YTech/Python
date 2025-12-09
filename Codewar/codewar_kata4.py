def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        for i in pin:
            if not i.isdigit():
                return False
        return True
    return False
    # return true or false

print(validate_pin("123\n"))