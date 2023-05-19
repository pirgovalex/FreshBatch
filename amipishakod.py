def is_happy_year(year):
    digits = set()
    for digit in str(year):
        if digit in digits:
            return False
        digits.add(digit)
    return True

year = int(input())
year += 1
while not is_happy_year(year):
    year += 1
print(year)
