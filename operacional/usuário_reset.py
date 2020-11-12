# Import from our package the class you're going to use
from tir import Webapp
from datetime import datetime
import time
dataSystem = datetime.today().strftime('%d/%m/%y')

oHelper = Webapp()
oHelper.Setup("SIGAMDI", dataSystem, '01','11001','02')
oHelper.SetLateralMenu(' Miscelanea (15) > Usuários ')
oHelper.SetButton("Confirmar")
oHelper.SetButton("Não")
oHelper.SearchBrowse()
oHelper.ClickCheckBox("Usuário",2)