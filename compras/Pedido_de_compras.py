# Import from our package the class you're going to use
from tir import Webapp
from datetime import datetime
data_system = datetime.today().strftime('%d/%m/%y')

test_helper = Webapp()
test_helper.Setup('SIGACOM', data_system,'01','11001','02')
test_helper.Program('MATA121')
test_helper.SetButton('ncluir')
test_helper.SearchBrowse('11001')
test_helper.SetButton('OK')
test_helper.SetValue("Fornecedor","017037")
test_helper.SetValue("Cond. Pagto","001")
test_helper.SetValue("Contato","Fabinho")
test_helper.SetValue("Moeda","1")
test_helper.SetValue("Produto","000000000035644", grid=True)
test_helper.SetValue("Quantidade","1,00000000", grid=True)
test_helper.SetValue("Prc Unitario","40,00000000", grid=True)
test_helper.SetKey("DOWN", grid=True)
test_helper.SetValue("Produto","000000000035644", grid=True)
test_helper.LoadGrid()
test_helper.SetButton("Salvar")
test_helper.SetButton("Não")

test_helper.SetButton("Fechar")
test_helper.SetButton('Entrar')
test_helper.AssertTrue()
test_helper.TearDown()



