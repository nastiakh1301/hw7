"""
    Написать функцию, которая будет проверять счастливый билетик или нет.
    Билет счастливый, если сумма одной половины цифр равняется сумме второй.
"""
import random

def main():
    ticket_num = str(random.randint(1, 100000000))
    is_lucky(ticket_num)

def is_lucky(ticket_num):
    print(ticket_num)
    first = 0
    second = 0
    ticket = len(str(ticket_num))
    if ticket % 2 == 0:
        for i in ticket_num[:int(ticket / 2)]:
            first += int(i)
        for i in ticket_num[int(ticket / 2):]:
            second += int(i)
        if first == second:
            print("Your ticket is lucky")   
            return ticket_num
        else:
            print("Your ticket is unlucky")
            return ticket_num
    else:
        print("Your ticket is unlucky")
        return ticket_num




if __name__ == "__main__":
    main()

    
assert is_lucky(1230) is True
assert is_lucky(239017) is False
assert is_lucky(134008) is True
assert is_lucky(15) is False
assert is_lucky(2020) is True
assert is_lucky(199999) is False
assert is_lucky(77) is True
assert is_lucky(479974) is True

print("All tests passed successfully!")