"""
1. Stwórz funkcję która przyjmuje jeden argument który ma być stringiem, funkcja powinna policzyć których znaków w stringu były najwięcej
i zwrócić znak oraz liczbę powtórzeń.
Np. dla stringa 'ala ma kota' wynikiem powinno być a, 4"""



def how_many_letter(string):
    max_number = 0
    any_letter = ""
    for letter in string:
        number = string.count(letter)
        if max_number < number:
            max_number = number
            any_letter = letter
    return f'{any_letter} = {max_number}'
print(how_many_letter("była sobie żabka"))