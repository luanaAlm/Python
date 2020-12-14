"""
Módulos são outros arquivos python
São úteis para reutilização de códigos
Módulo Random -> Possui várias funçoes para geração de números  pseudo-aleatório
"""

"""
#forma 1 - importando todo o modulo
#ficará na memória
import random
#primeiro random -> pacote
# segundo random() -> função
print(random.random())
"""

#Forma 2 - Importando uma função especifica do random
from random import random

for i in range(10):
    print(random())
