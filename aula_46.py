# o for também pode ter laços dentro dele como o else

for i in range(10):
    if i == 2:
        print('i é 2, pulando...')
        continue

    if i == 8:
        print('i é 8, seu else nao executará')
        break
    for j in range (1,3):
        print (i,j)
else:
    print('For completado com sucesso.')