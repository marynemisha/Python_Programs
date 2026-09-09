def check_age(age):
    if age<18:
        raise ValueError("Not eligible...!")
    return "Eligible"

print(check_age(12))