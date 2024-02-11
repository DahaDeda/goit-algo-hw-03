import re
raw_number = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    for phone_number in raw_number:
        if phone_number.isalpha() == False:
            if phone_number.strip() == True:
                print(phone_number.strip())
                return phone_number
            phone_number = re.sub(r"[(, ), \-, /, \\, a-z, A-Z]", "", phone_number)
            # print(phone_number)
            if len(phone_number) == 10:
                phone_number = re.sub(r"(\d{10})", r"+38\1", phone_number)
                # print(phone_number)
            elif len(phone_number) == 12:
                phone_number = re.sub(r"(\d{12})", r"+\1", phone_number)
                # print(phone_number)
            print(phone_number)
        else:
            print("We need phone number, try again")
    
# phone_input= input("Enter your phone pls:\n")
normalize_phone(raw_number)  