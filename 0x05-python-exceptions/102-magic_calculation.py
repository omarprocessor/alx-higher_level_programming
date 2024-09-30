#!/usr/bin/python3

def magic_calculation(num1, num2):
    total = 0
    for index in range(1, 3):
        try:
            if index > num1:
                raise Exception("Too far")
            else:
                total += num1 ** num2 / index
        except Exception:
            total = num2 + num1
            break
    return total
