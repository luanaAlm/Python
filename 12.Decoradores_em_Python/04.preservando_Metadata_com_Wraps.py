"""
Preservando Metadata com Wraps
Metadatas -> são dados intrísecos em arquivos.
Wraps -> São funções decoratorns que envolvem elementos com diversas finalidades
"""
from functools import wraps

def ver_log(funcao):
    @wraps(funcao)
    def logar(*args, **kwargs):
        """Função logar dentro de outra"""
        print(f'Voce esta chaamando funcao: {funcao.__name__}')
        print(f'Aqui e a documentacao: {funcao.__doc__}')
        return funcao(*args, **kwargs)
    return logar

@ver_log
def soma(a, b):
    """Soma dois numeros"""
    return a + b

print(soma(5, 55))
print(soma.__name__)
print(soma.__doc__)
print(help(soma))
