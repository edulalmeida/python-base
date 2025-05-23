#/usr/bin/env/ python3





"""
Hello World Multi Linguas

Dependeno da lingua configurada no ambiente o programa exibe a correspondente.

Como usar:
Tenha a variavel LANG devidademente configurada, por ex:
    export LANG=pt_BR

Execução:
    python3 hello.py
    ou 
    ./hello.py

"""
__version__ = "0.0.1"
__author__ = "Edu Almeida"
__license__ = "Unlicense"

# Dunder = __(Underline Underline)

import os

current_language = os.getenv("LANG", "en_US")[:5]

msg = "Hello, World!"

if current_language == "pt_BR":
    msg = "Olá, Mundo!"
elif current_language == "it_IT":
    msg = "Ciao, Mondo!"
elif current_language == "es_SP":
    msg = "Hola, Mundo!"
elif current_language == "fr_FR":
    msg = "Boujour Monde"

print(msg)





