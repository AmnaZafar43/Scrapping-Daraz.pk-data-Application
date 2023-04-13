from PyQt5 import QtWidgets
from PyQt5.uic import loadUi 
import pandas as pd
import sys
pf = pd.read_csv("data.csv")
print(pf.dtypes)
publishDate = pf["Publish Date"].values.tolist()
deleiverDate = pf["deliver Date"].values.tolist()
returnDate = pf["return "].values.tolist()
bookName = pf["Book Name"].values.tolist()
authorName = pf["Author Name"].values.tolist()
rating = pf["Raitng"].values.tolist()
price = pf["Price"].values.tolist()

class MainPage(QtWidgets.QDialog):
    def __init__(self):
        super(MainPage,self).__init__()
        loadUi('MainPage.ui',self)
        self.scrapbtn.clicked.connect(self.scrap)
        self.algbtn.clicked.connect(self.algo)
        self.exitbtn.clicked.connect(self.exit)
    def scrap(self):
        srp = scraping()
        widget.addWidget(srp)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def algo(self):
        al = algoritms()
        widget.addWidget(al)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def exit(self):
        widget.close()
        

class algoritms(QtWidgets.QDialog):
    def __init__(self):
        super(algoritms,self).__init__()
        loadUi('aloritems.ui',self)
        self.btnBack.clicked.connect(self.backalgorithm)     
        self.tableWidget.setRowCount(len(publishDate))
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setItem(0,0,QtWidgets.QTableWidgetItem("Book Name"))
        self.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem("Author Name"))
        self.tableWidget.setItem(0,2,QtWidgets.QTableWidgetItem("Publish Date"))
        self.tableWidget.setItem(0,3,QtWidgets.QTableWidgetItem("Rating"))
        self.tableWidget.setItem(0,4,QtWidgets.QTableWidgetItem("Price"))
        self.tableWidget.setItem(0,5,QtWidgets.QTableWidgetItem("Return"))
        self.tableWidget.setItem(0,6,QtWidgets.QTableWidgetItem("deliver Date"))
        row = 1
        for i in range(len(publishDate)):
            self.tableWidget.setItem(row,0,QtWidgets.QTableWidgetItem(str(bookName[i])))
            self.tableWidget.setItem(row,1,QtWidgets.QTableWidgetItem(str(authorName[i])))
            self.tableWidget.setItem(row,2,QtWidgets.QTableWidgetItem(str(publishDate[i])))
            self.tableWidget.setItem(row,3,QtWidgets.QTableWidgetItem(str(rating[i])))
            self.tableWidget.setItem(row,4,QtWidgets.QTableWidgetItem(str(price[i])))
            self.tableWidget.setItem(row,5,QtWidgets.QTableWidgetItem(str(returnDate[i])))
            self.tableWidget.setItem(row,6,QtWidgets.QTableWidgetItem(str(deleiverDate[i])))
            row+=1

    def backalgorithm(self):
        main = MainPage()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)


class scraping(QtWidgets.QDialog):
    def __init__(self):
        super(scraping,self).__init__()
        loadUi('scrapingUI.ui',self)
        self.backbtn.clicked.connect(self.back)
        
    def back(self):
        main = MainPage()
        widget.addWidget(main)
        widget.setCurrentIndex(widget.currentIndex()+1)

app=QtWidgets.QApplication(sys.argv)
scraper=scraping()
algoritm=algoritms()
mainPage=MainPage()
widget=QtWidgets.QStackedWidget()
# widget.addWidget(mainPage)
widget.addWidget(mainPage)
# widget.addWidget(scraper)
widget.setFixedWidth(1500)
widget.setFixedHeight(1000)

widget.show()
widget
try:
    sys.exit(app.exec_())
except:
    print('Page dosen\'t exist')


