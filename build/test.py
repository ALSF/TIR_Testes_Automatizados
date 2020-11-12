# Import from our package the class you're going to use
from tir import Webapp
from datetime import datetime
dataSystem = datetime.today().strftime('%d/%m/%y')

oHelper = Webapp()
oHelper.Setup("SIGAMDI", dataSystem, '01','11001','02')
oHelper.Program("ATFA110")

oHelper.AddParameter("MV_ULTDEPR", "", "20160229")
oHelper.AddParameter("MV_ATFCTAP", "", "1")
oHelper.SetParameters()