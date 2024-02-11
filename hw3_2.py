import random
def get_numbers_tickets(min, max, quanity):
    try:
        rand_list = []
        
        if min >= 1 and max <=1000 and min < max and max - min > quanity:
            while len(rand_list) < quanity:
                rand_elements_un = random.randint(min, max)
                if rand_elements_un not in rand_list:
                    rand_list.append(rand_elements_un)
            rand_list.sort()
            print(rand_list)
        else:
            print("Shit, more than 1 and less than 1000 and min > max")
    except ValueError:
        print("Did you read? Repeat ")
min_input = int(input("\nEnter min: "))
max_input = int(input("Enter max: "))
quanity_input = int(input("Enter quanity: "))
get_numbers_tickets(min_input, max_input, quanity_input)