# dir, hasattr e getattr em python
#o dir funciona para ver tudo que está dentro da string, seja ela classes, funçoes e etc
#o hasattr checa se existe algum método, por exemplo, upper, lower, etc.
#o getattr funciona para puxar esse método

string = 'Luiz'
metodo = 'upper' #o metodo precisa estar como string

if hasattr(string, metodo):
    print('Existe Upper')
    print(getattr(string, metodo)()) #precisamos colocar os "()" para fazer com que execute a função.
else:
    print('Não existe o método', metodo)