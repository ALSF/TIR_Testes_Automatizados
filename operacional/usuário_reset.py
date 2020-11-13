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
oHelper.SearchBrowse(term="dtcassavara", key=2, index=True)
oHelper.SetButton("Alterar")
oHelper.SetValue("USR_PSW","lar004")
oHelper.SetValue("USR_PSWCMP","lar004")
oHelper.SetValue("USR_MSBLQL", "2 - Não")
oHelper.SetValue("USR_CHGPSW", True, name_attr=True)
oHelper.SetButton("Confirmar")
oHelper.SetButton("Fechar")