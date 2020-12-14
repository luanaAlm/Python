"""
Instalando e utilizando módulos externos
Para instalar usa-se o pip - instalador de pacotes python
"""
import pydf
pdf = pydf.generate_pdf('<h1> Teste </h1>')

with open('test_doc1.pdf', 'wb') as f:
    f.write(pdf)
