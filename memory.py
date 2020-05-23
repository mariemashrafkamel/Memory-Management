from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox

from PyQt5.QtCore import *
from PyQt5.uic import loadUiType
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

MainUI, _ = loadUiType('memory.ui')


class Main(QMainWindow, MainUI):
    i = 0
    j = 0
    k = 0
    r = 0


    def __init__(self):
        super().__init__()
        self.title = "Processes Scheduler"
        self.setIcon()
        self.setupUi(self)
        self.Handle_Buttons()
        self.tabWidget.tabBar().setVisible(False)


    def setIcon(self):
        appIcon=QIcon("process.png")
        self.setWindowIcon(appIcon)

    def Handle_Buttons(self):
        self.pushButton.clicked.connect(self.first_fit_open)  # open first fit tab
        self.pushButton_2.clicked.connect(self.best_fit_open)  # open best fit tab

        self.pushButton_7.clicked.connect(self.Show_Data)  # for first fit
        self.pushButton_10.clicked.connect(self.Show_Data2)  # for best fit

        self.pushButton_8.clicked.connect(self.show_data_proc)  # for first fit
        self.pushButton_9.clicked.connect(self.show_data_proc2)  # for best fit
        self.pushButton_11.clicked.connect(self.hole_table1)  # draw for first fit holes
        self.pushButton_12.clicked.connect(self.hole_table2)  # draw for best fit holes

        self.pushButton_13.clicked.connect(self.hole_table1)  # draw proc first fit
        self.pushButton_19.clicked.connect(self.hole_table2)  # draw proc best fit

        self.pushButton_14.clicked.connect(self.delet_row)  # delete hole

        self.pushButton_16.clicked.connect(self.delet_rowproc)  # delete process
        self.pushButton_15.clicked.connect(self.home)
        self.pushButton_21.clicked.connect(self.home)

        self.pushButton_24.clicked.connect(self.delet_row2)  # delete hole

        self.pushButton_22.clicked.connect(self.delet_rowproc2)  # delete process

    def first_fit_open(self):
        self.tabWidget.setCurrentIndex(1)
        scene = QtWidgets.QGraphicsScene()  # scene class of graphics
        self.graphicsView_3.setScene(scene)
        self.lineEdit_10.clear()
        self.lineEdit_11.clear()
        self.lineEdit_8.clear()
        self.lineEdit_13.clear()
        self.lineEdit_12.clear()
        self.lineEdit_14.clear()
        # self.graphicsView_3.setScene().clear()

        # self.tableWidget_5.clear()

    def best_fit_open(self):
        self.tabWidget.setCurrentIndex(2)
        scene = QtWidgets.QGraphicsScene()  # scene class of graphics
        self.graphicsView_4.setScene(scene)
        self.lineEdit_9.clear()
        self.lineEdit_18.clear()
        self.lineEdit_17.clear()
        self.lineEdit_15.clear()
        self.lineEdit_16.clear()
        self.lineEdit_19.clear()
        # self.graphicsView_3.setScene().clear()


    def home(self):
        self.tabWidget.setCurrentIndex(0)
        if (Main.i > 0):
            for i in range(Main.i):
                self.tableWidget_5.setRowCount(0)

            for j in range(Main.j):
                self.tableWidget_6.clear()
                self.tableWidget_9.clear()
                self.tableWidget_6.removeRow(j)
                self.tableWidget_9.removeRow(j)
            Main.i = 0
            Main.J = 0
        if (Main.k > 0):

            for i in range(Main.k):
                self.tableWidget_8.setRowCount(0)

            for j in range(Main.r):
                self.tableWidget_7.clear()
                self.tableWidget_10.clear()
                self.tableWidget_7.removeRow(j)
                self.tableWidget_10.removeRow(j)
            Main.k = 0
            Main.r = 0

        while self.tableWidget_5.rowCount() > 0:
            self.tableWidget_5.removeRow(0)
        while self.tableWidget_6.rowCount() > 0:
            self.tableWidget_6.removeRow(0)
        while self.tableWidget_9.rowCount() > 0:
            self.tableWidget_9.removeRow(0)
        Main.i = 0
        Main.j=0



        while self.tableWidget_8.rowCount() > 0:
            self.tableWidget_8.removeRow(0)
        while self.tableWidget_7.rowCount() > 0:
            self.tableWidget_7.removeRow(0)
        while self.tableWidget_10.rowCount() > 0:
            self.tableWidget_10.removeRow(0)
        Main.k = 0
        Main.r=0


    def Show_Data(self):  # for first fit holes
        index = Main.i
        self.tableWidget_5.setRowCount(index)
        self.tableWidget_5.insertRow(index)
        self.tableWidget_5.setItem(index, index, QTableWidgetItem(str('')))

        if ((self.lineEdit_8.text() == '') or (self.lineEdit_11.text() == '')):
            self.tableWidget_5.removeRow(index)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Insert data !')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            address = float(self.lineEdit_8.text())
            size = float(self.lineEdit_11.text())

            self.tableWidget_5.setItem(index, 0, QTableWidgetItem(str(address)))
            self.tableWidget_5.setItem(index, 1, QTableWidgetItem(str(size)))
            Main.i += 1




    def show_data_proc(self):  # for first fit

        index2 = Main.j
        self.tableWidget_6.setRowCount(index2)
        self.tableWidget_6.insertRow(index2)
        self.tableWidget_6.setItem(index2, index2, QTableWidgetItem(str('')))

        if ((self.lineEdit_13.text() == '') or (self.lineEdit_12.text() == '') or (self.lineEdit_14.text() == '')):
            self.tableWidget_6.removeRow(index2)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Insert data !')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:

            p_name = str(self.lineEdit_14.text())
            no_seg = int(self.lineEdit_12.text())
            seg_inf = str(self.lineEdit_13.text())
            self.tableWidget_6.setItem(index2, 0, QTableWidgetItem(p_name))
            self.tableWidget_6.setItem(index2, 1, QTableWidgetItem(str(no_seg)))
            self.tableWidget_6.setItem(index2, 2, QTableWidgetItem(seg_inf))
            Main.j += 1



    def hole_table1(self):
        mem = self.lineEdit_10.text()

        if (mem == ''):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Memory Size Is Empty')
            msg.setWindowTitle("Error")
            msg.exec_()

        else:

            mem_size = float(mem)
            #print(mem_size)

            hole_ad = []
            hole_s = []
            for m in range(Main.i):
                hole_ad.append(float(self.tableWidget_5.item(m, 0).text()))
                hole_s.append(float(self.tableWidget_5.item(m, 1).text()))

            h_ad, h_s = zip(*sorted(zip(hole_ad, hole_s)))
            hole_ad2 = list(h_ad)
            hole_s2 = list(h_s)
            hole_limit = []

            # print(hole_ad2)

            #####holes loop##############

            prev_it = 1  # previous index of iterator
            it_flag = 1
            while it_flag == 1:
                it_flag = False
                for i in range(prev_it, Main.i):
                    if i < Main.i:
                        if hole_ad2[i] < hole_ad2[i - 1] + hole_s2[i - 1]:
                            hole_s2.remove(hole_s2[i])
                            hole_ad2.remove(hole_ad2[i])
                            self.tableWidget_5.removeRow(i)
                            Main.i -= 1
                            self.hole_table1()
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Critical)
                            msg.setText("Error")
                            msg.setInformativeText('invalid hole (overlaps with previous hole)')
                            msg.setWindowTitle("Error")
                            msg.exec_()
                            return
                        elif hole_ad2[i] + hole_s2[i] > mem_size:
                            self.tableWidget_5.removeRow(i)
                            Main.i -= 1
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Critical)
                            msg.setText("Error")
                            msg.setInformativeText('invalid hole (exceeds memory limit)')
                            msg.setWindowTitle("Error")
                            msg.exec_()
                        elif hole_ad2[i] == hole_ad2[i - 1] + hole_s2[i - 1]:
                            hole_s2[i - 1] += hole_s2[i]
                            self.tableWidget_5.setItem(i - 1, 1, QTableWidgetItem(str(hole_s2[i - 1])))
                            self.tableWidget_5.removeRow(i)
                            hole_s2.remove(hole_s2[i])
                            hole_ad2.remove(hole_ad2[i])
                            Main.i -= 1
                            prev_it = i
                            it_flag = True
                            break

            # print(hole_ad2)

            for n in range(Main.i):
                hole_limit.append(hole_ad2[n] + hole_s2[n])

            process_name = []
            no_seg = []
            seg_inf = []

            ###take process from table to processes list################

            for m in range(Main.j):
                process_name.append(str(self.tableWidget_6.item(m, 0).text()))
                no_seg.append(int(self.tableWidget_6.item(m, 1).text()))
                seg_inf.append(str(self.tableWidget_6.item(m, 2).text()))


            #####split seg_info to take segments name and size#####################

            new_list = []
            elements_counter = 0
            for element in seg_inf:
                oneProcess_segments = element.split(',')
                if len(oneProcess_segments) != no_seg[elements_counter]:
                    self.tableWidget_6.removeRow(elements_counter)
                    Main.j -= 1
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Error")
                    msg.setInformativeText('invalid data')
                    msg.setWindowTitle("Error")
                    msg.exec_()
                    break
                else:
                    new_list.append([])
                    new_list.append([])
                    for i in range(len(oneProcess_segments)):
                        one_segment = oneProcess_segments[i].split(':')
                        if len(one_segment) != 2:
                            self.tableWidget_6.removeRow(elements_counter)
                            Main.j -= 1
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Critical)
                            msg.setText("Error")
                            msg.setInformativeText('invalid input')
                            msg.setWindowTitle("Error")
                            msg.exec_()
                            break
                        else:  # now we have 2 parts   ["name", "data"]
                            one_segment[1] = one_segment[1].replace(' ', '')
                            if(one_segment[1].isalpha() == False):
                                new_list[(2 * elements_counter)].append(one_segment[0])
                                new_list[(2 * elements_counter) + 1].append(float(one_segment[1]))



                            else:
                                self.tableWidget_6.removeRow(elements_counter)
                                Main.j -= 1
                                msg = QMessageBox()
                                msg.setIcon(QMessageBox.Critical)
                                msg.setText("Error")
                                msg.setInformativeText('invalid input')
                                msg.setWindowTitle("Error")
                                msg.exec_()
                                break

                    elements_counter += 1

            scene = QtWidgets.QGraphicsScene()  # scene class of graphics
            self.graphicsView_3.setScene(scene)

            pen = QtGui.QPen(QtCore.Qt.black, 3)  # pen object in class QtGui
            pen2 = QtGui.QPen(QtCore.Qt.black, 3)
            pen3 = QtGui.QPen(QtCore.Qt.black, 3)
            brush = QtGui.QBrush(QtCore.Qt.gray)  # brush for coloring
            brush2 = QtGui.QBrush(QtCore.Qt.darkBlue)
            brush3 = QtGui.QBrush(QtCore.Qt.white)
            self.text = self.tr("Categories")

            ################draw empty memoryyyyy ##############
            r = QtCore.QRectF(QtCore.QPointF(0, 0), QtCore.QSizeF(160, mem_size))
            scene.addRect(r, pen, brush)

            mytext1 = QGraphicsSimpleTextItem("Memory")
            scene.addItem(mytext1)  # add item 3shan arsm string el hwa a3rd asma2 el processes
            mytext1.setPos(70, 0)  # width hwa arr[i]
            mytext1.setScale(1)

            mytext2 = QGraphicsSimpleTextItem(str(0))
            scene.addItem(mytext2)  # add item 3shan arsm string el hwa a3rd asma2 el processes
            mytext2.setPos(-15, 0)  # width hwa arr[i]
            mytext2.setScale(1)

            mytext3 = QGraphicsSimpleTextItem(str(mem_size))
            scene.addItem(mytext3)  # add item 3shan arsm string el hwa a3rd asma2 el processes
            mytext3.setPos(-25, mem_size)  # width hwa arr[i]
            mytext3.setScale(1)

            ########draw holeees########
            for n in range(Main.i):
                p = QtCore.QRectF(QtCore.QPointF(0, hole_ad2[n]), QtCore.QSizeF(160, hole_s2[n]))
                scene.addRect(p, pen2, brush2)

                mytext5 = QGraphicsSimpleTextItem(str(hole_ad2[n]))
                scene.addItem(mytext5)  # add item 3shan arsm string el hwa a3rd asma2 el processes
                mytext5.setPos(-30, hole_ad2[n])  # width hwa arr[i]
                mytext5.setScale(1)

                mytext6 = QGraphicsSimpleTextItem(str(hole_limit[n]))
                scene.addItem(mytext6)  # add item 3shan arsm string el hwa a3rd asma2 el processes
                mytext6.setPos(-30, hole_limit[n])  # width hwa arr[i]
                mytext6.setScale(1)

            allocate_start = []
            allocate_limit = []
            allocate_p = []
            allocate_seg = []

            it = 1
            it2 = 0
            zero = 0
            for i in range(Main.j):  # process
                h_ad2, h_s2 = zip(*sorted(zip(hole_ad2, hole_s2)))
                hole_ad2 = list(h_ad2)
                hole_s2 = list(h_s2)
                for m in range(no_seg[i]):  # segments
                    h_ad2, h_s2 = zip(*sorted(zip(hole_ad2, hole_s2)))
                    hole_ad2 = list(h_ad2)
                    hole_s2 = list(h_s2)
                    success = 0
                    for j in range(Main.i):  # holes
                        if ((new_list[it][m]) < hole_s2[j]):
                            allocate_start.append(hole_ad2[j])
                            allocate_limit.append(hole_ad2[j] + new_list[it][m])
                            allocate_p.append(process_name[i])
                            allocate_seg.append(new_list[it2][m])
                            hole_s2[j] -= new_list[it][m]
                            hole_ad2[j] += new_list[it][m]
                            success = 1
                            break
                        elif ((new_list[it][m]) == hole_s2[j]):
                            allocate_start.append(hole_ad2[j])
                            allocate_limit.append(hole_ad2[j] + new_list[it][m])
                            allocate_p.append(process_name[i])
                            allocate_seg.append(new_list[it2][m])
                            # hole_ad2.remove(hole_ad2[j])
                            # hole_s2.remove(hole_s2[j])
                            hole_s2[j] = 0
                            success = 1
                            break
                            # self.tableWidget_5.removeRow(j)
                    if (success == 0):  # >

                        process_name.remove(process_name[i])
                        no_seg.remove(no_seg[i])
                        seg_inf.remove(seg_inf[i])
                        Main.j -= 1
                        self.hole_table1()
                        self.tableWidget_6.removeRow(i)
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Error")
                        msg.setInformativeText('this process does not fit!')
                        msg.setWindowTitle("Error")
                        msg.exec_()
                        # break
                        return
                it += 2
                it2 += 2

            allocate_width = []
            seg_width = []
            size_value = []
            size = "Size="

            for i in range(len(allocate_start)):
                allocate_width.append(allocate_limit[i] - allocate_start[i])
                seg_width.append((allocate_start[i] + allocate_limit[i]) / 2)
                size_value.append(size + str(allocate_width[i]))
                # allocate_seg

            for m in range(Main.j):
                temp = ""
                temp2 = ""
                temp3 = ""
                self.tableWidget_9.setRowCount(m)
                self.tableWidget_9.insertRow(m)
                self.tableWidget_9.setItem(m, m, QTableWidgetItem(str('')))

                self.tableWidget_9.setItem(m, 0, QTableWidgetItem(process_name[m]))
                self.tableWidget_9.setItem(m, 1, QTableWidgetItem(str(no_seg[m])))
                for i in range(no_seg[m]):
                    temp += allocate_seg[i] + '\n'
                    temp2 += str(allocate_start[i]) + '\n'
                    temp3 += str(allocate_width[i]) + '\n'
                self.tableWidget_9.setItem(m, 2, QTableWidgetItem(temp))
                self.tableWidget_9.setItem(m, 3, QTableWidgetItem(temp2))
                self.tableWidget_9.setItem(m, 4, QTableWidgetItem(temp3))
                self.tableWidget_9.resizeRowsToContents()

            for n in range(len(allocate_start)):  # processes
                k = QtCore.QRectF(QtCore.QPointF(0, allocate_start[n]), QtCore.QSizeF(160, allocate_width[n]))
                scene.addRect(k, pen3, brush3)

                mytext7 = QGraphicsSimpleTextItem(str(allocate_p[n]))
                scene.addItem(mytext7)  # add item 3shan arsm string el hwa a3rd asma2 el processes
                mytext7.setPos(70, allocate_start[n])  # width hwa arr[i]
                mytext7.setScale(1)

                mytext0 = QGraphicsSimpleTextItem(str(allocate_seg[n]))
                scene.addItem(mytext0)  # add item 3shan arsm string el hwa a3rd asma2 el processes
                mytext0.setPos(10, seg_width[n])  # width hwa arr[i]
                mytext0.setScale(1)

                mytext00 = QGraphicsSimpleTextItem(str(size_value[n]))
                scene.addItem(mytext00)  # add item 3shan arsm string el hwa a3rd asma2 el processes
                mytext00.setPos(70, seg_width[n])  # width hwa arr[i]
                mytext00.setScale(1)

                mytext9 = QGraphicsSimpleTextItem(str(allocate_limit[n]))
                scene.addItem(mytext9)  # add item 3shan arsm string el hwa a3rd asma2 el processes
                mytext9.setPos(-30, allocate_limit[n])  # width hwa arr[i]
                mytext9.setScale(1)







    def Show_Data2(self):  # for best fit holee
        index = Main.k
        self.tableWidget_8.setRowCount(index)
        self.tableWidget_8.insertRow(index)
        self.tableWidget_8.setItem(index, index, QTableWidgetItem(str('')))

        if ((self.lineEdit_9.text() == '') or (self.lineEdit_18.text() == '') ):
            self.tableWidget_8.removeRow(index)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Insert data !')
            msg.setWindowTitle("Error")
            msg.exec_()

        else:
            address = float(self.lineEdit_9.text())
            size = float(self.lineEdit_18.text())
            self.tableWidget_8.setItem(index, 0, QTableWidgetItem(str(address)))
            self.tableWidget_8.setItem(index, 1, QTableWidgetItem(str(size)))
            Main.k += 1

    def not_fit(self):
        #self.hole_table1()
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText("Error")
        msg.setInformativeText('add holes')
        msg.setWindowTitle("Error")
        msg.exec_()


    def show_data_proc2(self):  # for best fit
        index2 = Main.r
        self.tableWidget_7.setRowCount(index2)
        self.tableWidget_7.insertRow(index2)
        self.tableWidget_7.setItem(index2, index2, QTableWidgetItem(str('')))

        if ((self.lineEdit_15.text() == '') or (self.lineEdit_16.text() == '') or (self.lineEdit_19.text() == '')):
            self.tableWidget_7.removeRow(index2)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Insert data !')
            msg.setWindowTitle("Error")
            msg.exec_()
        else:
            p_name = str(self.lineEdit_19.text())
            no_seg = int(self.lineEdit_16.text())
            seg_inf = str(self.lineEdit_15.text())
            self.tableWidget_7.setItem(index2, 0, QTableWidgetItem(p_name))
            self.tableWidget_7.setItem(index2, 1, QTableWidgetItem(str(no_seg)))
            self.tableWidget_7.setItem(index2, 2, QTableWidgetItem(seg_inf))
            Main.r += 1


    def hole_table2(self):
        mem = self.lineEdit_17.text()

        if (mem == ''):
            # QMessageBox.about(self, "Error", "Please Enter Memory Size")
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText('Memory Size Is Empty')
            msg.setWindowTitle("Error")
            msg.exec_()


        else:
            mem_size = float(mem)
            hole_ad = []
            hole_s = []

            for m in range(Main.k):
                hole_ad.append(float(self.tableWidget_8.item(m, 0).text()))
                hole_s.append(float(self.tableWidget_8.item(m, 1).text()))

            h_ad, h_s = zip(*sorted(zip(hole_ad, hole_s)))
            hole_ad2 = list(h_ad)
            hole_s2 = list(h_s)
            hole_limit = []

            prev_it = 1  # previous index of iterator
            it_flag = 1
            while it_flag == 1:
                it_flag = False
                for i in range(prev_it, Main.k):
                    if i < Main.k:
                        if hole_ad2[i] < hole_ad2[i - 1] + hole_s2[i - 1]:

                            hole_s2.remove(hole_s2[i])
                            hole_ad2.remove(hole_ad2[i])
                            self.tableWidget_8.removeRow(i)
                            Main.k -= 1
                            self.hole_table2()
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Critical)
                            msg.setText("Error")
                            msg.setInformativeText('invalid hole (overlaps with previous hole)')
                            msg.setWindowTitle("Error")
                            msg.exec_()
                            return



                        elif hole_ad2[i] + hole_s2[i] > mem_size:
                            self.tableWidget_8.removeRow(i)
                            Main.k -= 1
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Critical)
                            msg.setText("Error")
                            msg.setInformativeText('invalid hole (exceeds memory limit)')
                            msg.setWindowTitle("Error")
                            msg.exec_()


                        elif hole_ad2[i] == hole_ad2[i - 1] + hole_s2[i - 1]:
                            hole_s2[i - 1] += hole_s2[i]
                            self.tableWidget_8.setItem(i - 1, 1, QTableWidgetItem(str(hole_s2[i - 1])))
                            self.tableWidget_8.removeRow(i)
                            hole_s2.remove(hole_s2[i])
                            hole_ad2.remove(hole_ad2[i])
                            Main.k -= 1
                            prev_it = i
                            it_flag = True
                            break

            for n in range(Main.k):
                hole_limit.append(hole_ad2[n] + hole_s2[n])

            scene = QtWidgets.QGraphicsScene()  # scene class of graphics
            self.graphicsView_4.setScene(scene)
            pen = QtGui.QPen(QtCore.Qt.black, 3)  # pen object in class QtGui
            pen2 = QtGui.QPen(QtCore.Qt.black, 3)
            pen3 = QtGui.QPen(QtCore.Qt.black, 3)
            brush = QtGui.QBrush(QtCore.Qt.gray)  # brush for coloring
            brush2 = QtGui.QBrush(QtCore.Qt.darkBlue)
            brush3 = QtGui.QBrush(QtCore.Qt.white)
            self.text = self.tr("Categories")

            ################draw empty memoryyyyy ##############
            r = QtCore.QRectF(QtCore.QPointF(0, 0), QtCore.QSizeF(160, mem_size))
            scene.addRect(r, pen, brush)

            mytext1 = QGraphicsSimpleTextItem("Memory")
            scene.addItem(mytext1)  # add item 3shan arsm string el hwa a3rd asma2 el processes
            mytext1.setPos(70, 0)  # width hwa arr[i]
            mytext1.setScale(1)

            mytext2 = QGraphicsSimpleTextItem(str(0))
            scene.addItem(mytext2)  # add item 3shan arsm string el hwa a3rd asma2 el processes
            mytext2.setPos(-15, 0)  # width hwa arr[i]
            mytext2.setScale(1)

            mytext3 = QGraphicsSimpleTextItem(str(mem_size))
            scene.addItem(mytext3)  # add item 3shan arsm string el hwa a3rd asma2 el processes
            mytext3.setPos(-25, mem_size)  # width hwa arr[i]
            mytext3.setScale(1)

            ########draw holeees########
            for n in range(Main.k):
                p = QtCore.QRectF(QtCore.QPointF(0, hole_ad2[n]), QtCore.QSizeF(160, hole_s2[n]))
                scene.addRect(p, pen2, brush2)

                mytext5 = QGraphicsSimpleTextItem(str(hole_ad2[n]))
                scene.addItem(mytext5)  # add item 3shan arsm string el hwa a3rd asma2 el processes
                mytext5.setPos(-30, hole_ad2[n])  # width hwa arr[i]
                mytext5.setScale(1)

                mytext6 = QGraphicsSimpleTextItem(str(hole_limit[n]))
                scene.addItem(mytext6)  # add item 3shan arsm string el hwa a3rd asma2 el processes
                mytext6.setPos(-30, hole_limit[n])  # width hwa arr[i]
                mytext6.setScale(1)

            process_name = []
            no_seg = []
            seg_inf = []
            staaaack = []

            ####take elemetns from table to process list#####
            for m in range(Main.r):
                process_name.append(str(self.tableWidget_7.item(m, 0).text()))
                no_seg.append(int(self.tableWidget_7.item(m, 1).text()))
                seg_inf.append(str(self.tableWidget_7.item(m, 2).text()))

            ###split no_seg list to take segments size and name)

            new_list = []
            elements_counter = 0
            for element in seg_inf:
                oneProcess_segments = element.split(',')
                if len(oneProcess_segments) != no_seg[elements_counter]:
                    self.tableWidget_7.removeRow(elements_counter)
                    Main.r -= 1
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Critical)
                    msg.setText("Error")
                    msg.setInformativeText('invalid data')
                    msg.setWindowTitle("Error")
                    msg.exec_()
                    break
                else:
                    new_list.append([])
                    new_list.append([])
                    for i in range(len(oneProcess_segments)):
                        one_segment = oneProcess_segments[i].split(':')
                        if len(one_segment) != 2:
                            self.tableWidget_7.removeRow(elements_counter)
                            Main.r -= 1
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Critical)
                            msg.setText("Error")
                            msg.setInformativeText('invalid input')
                            msg.setWindowTitle("Error")
                            msg.exec_()
                            break
                        else:  # now we have 2 parts   ["name", "data"]
                            one_segment[1] = one_segment[1].replace(' ', '')
                            if (one_segment[1].isalpha() == False):
                                new_list[(2 * elements_counter)].append(one_segment[0])
                                new_list[(2 * elements_counter) + 1].append(float(one_segment[1]))
                            else:
                                self.tableWidget_7.removeRow(elements_counter)
                                Main.r -= 1
                                msg = QMessageBox()
                                msg.setIcon(QMessageBox.Critical)
                                msg.setText("Error")
                                msg.setInformativeText('invalid input')
                                msg.setWindowTitle("Error")
                                msg.exec_()
                                break
                    elements_counter += 1

            allocate_start = []
            allocate_limit = []
            allocate_p = []
            allocate_seg = []


            # hole_limit = []
            ##allocate segments into holes################

            it = 1
            it2 = 0
            zero = 0
            for i in range(Main.r):  #process
                h_s2, h_ad2 = zip(*sorted(zip(hole_s2, hole_ad2)))
                hole_ad2 = list(h_ad2)
                hole_s2 = list(h_s2)

                for m in range(no_seg[i]):  # segments
                    h_s2, h_ad2 = zip(*sorted(zip(hole_s2, hole_ad2)))
                    hole_ad2 = list(h_ad2)
                    hole_s2 = list(h_s2)
                    success = 0
                    for j in range(Main.k):  # holes
                        if ((new_list[it][m]) < hole_s2[j]):
                            allocate_start.append(hole_ad2[j])
                            allocate_limit.append(hole_ad2[j] + new_list[it][m])
                            allocate_p.append(process_name[i])
                            allocate_seg.append(new_list[it2][m])
                            hole_s2[j] -= new_list[it][m]
                            hole_ad2[j] += new_list[it][m]
                            success = 1
                            break
                        elif ((new_list[it][m]) == hole_s2[j]):
                            allocate_start.append(hole_ad2[j])
                            allocate_limit.append(hole_ad2[j] + new_list[it][m])
                            allocate_p.append(process_name[i])
                            allocate_seg.append(new_list[it2][m])
                            #hole_ad2.remove(hole_ad2[j])
                            #hole_s2.remove(hole_s2[j])
                            hole_s2[j]=0
                            success = 1
                            break
                            # self.tableWidget_5.removeRow(j)
                    if (success == 0):  # >

                        process_name.remove(process_name[i])
                        no_seg.remove(no_seg[i])
                        seg_inf.remove(seg_inf[i])
                        Main.r -= 1
                        self.hole_table2()
                        self.tableWidget_7.removeRow(i)
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Critical)
                        msg.setText("Error")
                        msg.setInformativeText('this process does not fit!')
                        msg.setWindowTitle("Error")
                        msg.exec_()
                        # break
                        return

                it += 2
                it2 += 2

            allocate_width = []
            seg_width = []
            size_value = []
            size = "Size="

            for i in range(len(allocate_start)):
                allocate_width.append(allocate_limit[i] - allocate_start[i])
                seg_width.append((allocate_start[i] + allocate_limit[i]) / 2)
                size_value.append(size + str(allocate_width[i]))
                # allocate_seg

            ##output tableeeeeee ##################

            for m in range(Main.r):
                temp = ""
                temp2 = ""
                temp3 = ""
                self.tableWidget_10.setRowCount(m)
                self.tableWidget_10.insertRow(m)
                self.tableWidget_10.setItem(m, m, QTableWidgetItem(str('')))
                self.tableWidget_10.setItem(m, 0, QTableWidgetItem(process_name[m]))
                self.tableWidget_10.setItem(m, 1, QTableWidgetItem(str(no_seg[m])))

                for i in range(no_seg[m]):
                    temp += allocate_seg[i] + '\n'
                    temp2 += str(allocate_start[i]) + '\n'
                    temp3 += str(allocate_width[i]) + '\n'
                self.tableWidget_10.setItem(m, 2, QTableWidgetItem(temp))
                self.tableWidget_10.setItem(m, 3, QTableWidgetItem(temp2))
                self.tableWidget_10.setItem(m, 4, QTableWidgetItem(temp3))
                self.tableWidget_10.resizeRowsToContents()


            #############draaaaw processes ###############

            # for n in range(len(allocate_start)):  # processes
            for n in range(len(allocate_start)):  # processes
                k = QtCore.QRectF(QtCore.QPointF(0, allocate_start[n]), QtCore.QSizeF(160, allocate_width[n]))
                scene.addRect(k, pen3, brush3)

                mytext7 = QGraphicsSimpleTextItem(str(allocate_p[n]))
                scene.addItem(mytext7)  # add item 3shan arsm string el hwa a3rd asma2 el processes
                mytext7.setPos(70, allocate_start[n])  # width hwa arr[i]
                mytext7.setScale(1)

                mytext0 = QGraphicsSimpleTextItem(str(allocate_seg[n]))
                scene.addItem(mytext0)  # add item 3shan arsm string el hwa a3rd asma2 el processes
                mytext0.setPos(10, seg_width[n])  # width hwa arr[i]
                mytext0.setScale(1)

                mytext00 = QGraphicsSimpleTextItem(str(size_value[n]))
                scene.addItem(mytext00)  # add item 3shan arsm string el hwa a3rd asma2 el processes
                mytext00.setPos(70, seg_width[n])  # width hwa arr[i]
                mytext00.setScale(1)

                mytext9 = QGraphicsSimpleTextItem(str(allocate_limit[n]))
                scene.addItem(mytext9)  # add item 3shan arsm string el hwa a3rd asma2 el processes
                mytext9.setPos(-30, allocate_limit[n])  # width hwa arr[i]
                mytext9.setScale(1)





    def first_fit_table(self):
        pass

    def best_fit_table(self):
        pass

    def delet_row(self):
        r = self.tableWidget_5.currentRow()
        if (r > -1):
            #self.pushButton_17.setVisible(True)
            # hole_ad.remove(float(self.tableWidget_5.item(r, 0).text()))
            # hole_s.remove(float(self.tableWidget_5.item(r, 1).text()))
            self.tableWidget_5.removeRow(r)
            Main.i -= 1
            self.hole_table1()
            return

    def delet_rowproc(self):
        r2 = self.tableWidget_6.currentRow()
        if (r2 > -1):
            #self.pushButton_18.setVisible(True)
            # hole_ad.remove(float(self.tableWidget_5.item(r, 0).text()))
            # hole_s.remove(float(self.tableWidget_5.item(r, 1).text()))
            self.tableWidget_6.removeRow(r2)
            self.tableWidget_9.removeRow(r2)
            Main.j -= 1
            self.hole_table1()
            return

    def delet_row2(self):
        r3 = self.tableWidget_8.currentRow()
        if (r3 > -1):
            #self.pushButton_23.setVisible(True)
            # hole_ad.remove(float(self.tableWidget_5.item(r, 0).text()))
            # hole_s.remove(float(self.tableWidget_5.item(r, 1).text()))
            self.tableWidget_8.removeRow(r3)
            Main.k -= 1
            self.hole_table2()
            return

    def delet_rowproc2(self):
        r4 = self.tableWidget_7.currentRow()
        if (r4 > -1):
            #self.pushButton_20.setVisible(True)
            # hole_ad.remove(float(self.tableWidget_5.item(r, 0).text()))
            # hole_s.remove(float(self.tableWidget_5.item(r, 1).text()))
            self.tableWidget_7.removeRow(r4)
            self.tableWidget_10.removeRow(r4)
            Main.r -= 1
            self.hole_table2()
            return


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()