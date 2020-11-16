# Import from our package the class you're going to use
from tir import Webapp
from datetime import datetime
import time
dataSystem = datetime.today().strftime('%d/%m/%y')

user = input("Digite o nome do usuário: ") #usuario informar 
pwd = input("Digite a nova senha:  ") # informar senha 

oHelper = Webapp()
oHelper.Setup("SIGAMDI", dataSystem, '01','11001','02')
oHelper.SetLateralMenu(' Miscelanea > Usuários ')
oHelper.SetButton("Não")
oHelper.SearchBrowse(term=user, key=2, index=True)
oHelper.SetButton("Alterar")
oHelper.SetValue("USR_PSW", pwd)
oHelper.SetValue("USR_PSWCMP", pwd)
oHelper.SetValue("USR_MSBLQL", "2 - Não") # Para bloquear para desbloquear > "2 - Não"
oHelper.SetValue("USR_MSBLQD","/  /"),
oHelper.SetValue("USR_CHGPSW", True, name_attr=True) #Para trocar a senha após logar
oHelper.SetButton("Confirmar")
oHelper.SetButton("Fechar")