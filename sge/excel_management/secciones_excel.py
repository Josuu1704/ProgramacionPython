import openpyxl


woorbook = openpyxl.load_workbook("segundo.xlsx")
notas = woorbook["Notas"]
print(notas)
ejercicios = notas["B1":"E1"]
print(ejercicios)

for fila in ejercicios:
    for celda in fila:
        print(celda.coordinate, celda.value)
    print("Final de la Fila")

columna = notas.columns[1]
for celda in columna:
    print(celda.coordinate, celda.value)

print(notas.rows[1])