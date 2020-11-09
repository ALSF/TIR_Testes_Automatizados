# Import from our package the class you're going to use
from tir import Webapp
from datetime import datetime
dataSystem = datetime.today().strftime('%d/%m/%y')

oHelper = Webapp()
oHelper.Setup("SIGAMDI", dataSystem, '01','11001','02')
oHelper.SetLateralMenu(' Atualizações (9) > Solicitar/cotar (10) > Solicit.de Compras')
oHelper.SetButton("Confirmar")
oHelper.SetButton("Incluir")
oHelper.SetValue("Produto","000000000000006",grid=True)
oHelper.SetValue("Quantidade","1,00000000", grid=True)
oHelper.SetValue("Centro Custo","010010010001", grid=True)
oHelper.LoadGrid()
oHelper.ClickLabel("Número")
oHelper.SetKey("CTRL+C")
oHelper.SetButton("Salvar")



