"""
Documentando funções Docstrings
podemos ter acesso a documentação de uma função em python
utilizando o _doc_
"""
def diz_oi():
    """Uma função simples que retorna uma String 'oi' """
    return 'oi'

def exponencial(numero, potencial=2):
    """
    :param numero:
    :param potencial:
    :return:
    """
    return numero ** potencial
