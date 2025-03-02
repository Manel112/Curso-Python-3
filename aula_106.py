#Funções decoradoras e decoradores
#Decorar = Adicionar/ Remover / Restringir / Alterar
#Funções decoradoras são as funções que decoram outras funções
#Decoradores são usados para fazer o Python
#usar as funções decoradoras em outras funções
#Os decoradores do python são os Syntax Sugar (Açucar sintatico)

def criar_funcao(func):
    def interna(*args, **kwargs):
        print('Vou te decorar')
        for arg in args:
            e_string(arg)
        resultado =  func(*args, **kwargs)
        print(f'O seu resultado foi {resultado}')
        print('Ok, agora você foi decorado!')
        return resultado
    return interna

@criar_funcao #isso faz com que agora, a inverte_string seja a funcao interna()
def inverte_string(string):
    return string[::-1]

def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')

inverte_string_checando_param = criar_funcao(inverte_string)
invertida = inverte_string_checando_param('123')
print(invertida)
