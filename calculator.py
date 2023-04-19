def add(numb1, numb2):
    if type(numb1) != int or type(numb2) != int:
        raise ValueError("Expected two integers")
    summ = numb1 + numb2
    return summ

