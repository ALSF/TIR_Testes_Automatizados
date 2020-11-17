# Import from our package the class you're going to use
from tir import Webapp
from datetime import datetime
import time
dataSystem = datetime.today().strftime('%d/%m/%y')


estado = input("digite o codigo do estado: ") #usuario informar 
cnpjCpf  = input("digite o cnpj ou cpf: ") #usuario informar 
razaoSocial  = input("digite a razao social: ") #usuario informar 
endereco  = input(" Digite o endereço: ") #usuario informar 
Nfantasia  = input(" Digite o Nome Fantasia: ") #usuario informar 
numero  = input("digite o numero: ") #usuario informar 
cep  = input("Digite o digite o cep: ") #usuario informar 
bairro  = input("digite o bairro: ") #usuario informar 
codMunicip  = input("digite o codigo de municipio: ") #usuario informar 


oHelper = Webapp()
oHelper.Setup("SIGAMDI", dataSystem, '01','11001','02')
oHelper.SetLateralMenu(' Atualizações  > Cadastros > Fornecedores ')
oHelper.SetButton("Confirmar")
oHelper.SetButton("Incluir")
oHelper.SetValue("Estado", estado)
oHelper.SetValue("CNPJ/CPF", cnpjCpf)
oHelper.SetValue("Razão Social", razaoSocial)
oHelper.SetValue("Endereço", razaoSocial)
oHelper.SetValue("N Fantasia", Nfantasia)
oHelper.SetValue("Numero", numero)
oHelper.SetValue("CEP", cep)
oHelper.SetValue("Bairro", bairro)
oHelper.SetValue("Cod. Municip", codMunicip)
oHelper.ClickFolder("Fiscais")
oHelper.SetValue("A2_TPESSOA", "CI - Comercio/Industria")
oHelper.SetButton("Confirmar")