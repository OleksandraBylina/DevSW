s = input("")
suma = 0
for c in s:
    try:
        suma += int(c)
    except ValueError:
        pass
print(suma)
