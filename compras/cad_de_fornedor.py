# Import from our package the class you're going to use
from tir import Webapp
from datetime import datetime
import time
dataSystem = datetime.today().strftime('%d/%m/%y')


oHelper = Webapp()
oHelper.Setup("SIGAMDI", dataSystem, '01','11001','02')
oHelper.SetLateralMenu(' Atualizações  > Cadastros > Fornecedores ')
oHelper.SetButton("Confirmar")
oHelper.SetButton("Incluir")
oHelper.SetValue("Estado","SP")
oHelper.SetValue("CNPJ/CPF","52.417.762/0001-91")
oHelper.SetValue("Razão Social","Sistematizei")
oHelper.SetValue("Endereço","Rua protheuzeiro fontes")
oHelper.SetValue("N Fantasia","Protheuzando & cia")
oHelper.SetValue("Numero","11011")
oHelper.SetValue("CEP","15130009")
oHelper.SetValue("Bairro","centro")
oHelper.SetValue("Cod. Municip","30300")
oHelper.ClickFolder("Fiscais")
oHelper.SetValue("A2_TPESSOA", "CI - Comercio/Industria")
oHelper.SetButton("Confirmar")