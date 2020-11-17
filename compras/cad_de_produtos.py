# Import from our package the class you're going to use
from tir import Webapp
from datetime import datetime
import time
dataSystem = datetime.today().strftime('%d/%m/%y')

oHelper = Webapp()
oHelper.Setup("SIGAMDI", dataSystem, '01','11001','02')
oHelper.SetLateralMenu("Atualizações > Cadastros > Produtos")
oHelper.SetButton("Confirmar")
oHelper.SetButton("Incluir")
oHelper.SetValue("Descricao","curso de protheuzeiro 2 - o retorno")
oHelper.SetValue("Tipo","SV")
oHelper.SetValue("Unidade","HR")
oHelper.SetValue("Grupo","0013")
oHelper.ClickFolder("Impostos")
oHelper.SetValue("Pos.IPI/NCM","0000.00.00")
oHelper.SetValue("Nome Cientif","pao de batata")
oHelper.SetValue("Origem","0")
oHelper.SetButton("Confirmar")