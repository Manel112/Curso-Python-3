"""
Ambientes virtuais em Python (venv)
Um ambiente virtual carrega toda a sua instalação
do Python para uma pasta no caminho escolhido.
Ao ativar um ambiente virtual, a instalação do
ambiente virtual será usada.
venv é o módulo que vamos usar para
criar ambientes virtuais.
Você pode dar o nome que preferir para um
ambiente virtual, mas os mais comuns são:
venv env .venv .env

cria o venv - python -m venv "nome do ambiente virtual

Para ativar o ambiente virtual usamos
.\(pasta)\Scripts\activate
deactivate para desativar o ambiente

# pip uninstall nome_pacote
# Congelar (ver pacotes)
# pip freeze
#
# Criando e usando um requirements.txt
# pip freeze > requirements.txt
# Instalando tudo do requirements.txt
# pip install -r requirements.txt
"""