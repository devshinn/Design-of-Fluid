#!/usr/bin/env python
# coding: utf-8
__author__ = "ShinHyeok_Kim <hostomer@khu.ac.kr>"
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from solution1 import*
from time import sleep
file = open('table_data.bin','rb'); table = pickle.load(file);file.close()

# Q, L, dz,dp liquid_type, pipe_standard, merterial, loss
form_class = uic.loadUiType("열에시.ui")[0]
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
        self. sol_arg_list = [0,0,0,0,0,0,0,0,0,0]; self.loss = [0,0,0,0,0,0,0,0]
        # self.syncComboBox()

        self.bt_calculation.clicked.connect(self.Bt_Calculation)
        
        #select Type
        self.select_type_1.clicked.connect(lambda: self.Select_Type(self.select_type_1)); self.select_type_2.clicked.connect(lambda: self.Select_Type(self.select_type_2));self.select_type_3.clicked.connect(lambda: self.Select_Type(self.select_type_3))

        #minors losses
        self.ml_check_1.stateChanged.connect(self.Minor_losses);self.ml_check_3.stateChanged.connect(self.Minor_losses);  self.ml_check_5.stateChanged.connect(self.Minor_losses);self.ml_check_7.stateChanged.connect(self.Minor_losses);
        self.ml_check_2.stateChanged.connect(self.Minor_losses);self.ml_check_4.stateChanged.connect(self.Minor_losses);  self.ml_check_6.stateChanged.connect(self.Minor_losses);self.ml_check_8.stateChanged.connect(self.Minor_losses);
        # minors losses 갯수
        self.ml_num_1.valueChanged.connect(self.Minor_losses);self.ml_num_3.valueChanged.connect(self.Minor_losses);self.ml_num_5.valueChanged.connect(self.Minor_losses);self.ml_num_7.valueChanged.connect(self.Minor_losses)
        self.ml_num_2.valueChanged.connect(self.Minor_losses);self.ml_num_4.valueChanged.connect(self.Minor_losses);self.ml_num_6.valueChanged.connect(self.Minor_losses);self.ml_num_8.valueChanged.connect(self.Minor_losses)


        self.pipe_length_value.valueChanged.connect(self.Minor_losses);self.height_drop_value.valueChanged.connect(self.Minor_losses);
        self.flow_rate_value.valueChanged.connect(self.Minor_losses);self.pressure_drop_value.valueChanged.connect(self.Minor_losses)

#new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new new
        
        self.calcul_list.itemDoubleClicked.connect(self.DoubleClice_remove_list_item)
        # self.calcul_list.currentItemChanged.connect(self.chkCurrentItemChanged)
        
        #라인에딧에 추가
        self.lt_add_btn.clicked.connect(self.lt_addListWidget)
        self.ps_add_btn.clicked.connect(self.ps_addListWidget)
        self.pm_add_btn.clicked.connect(self.pm_addListWidget)
        self.bt_clear.clicked.connect(self.clear_Btn) # clear button


    def DoubleClice_remove_list_item(self) : #더블클릭 삭제

        self.removeItemRow = self.calcul_list.currentRow()
        self.calcul_list.takeItem(self.removeItemRow)


        # 콤보 박스에서 리스트위젯으로
    def lt_addListWidget(self) :
        self.addItemText = self.lt_combo.currentText()
        self.calcul_list.addItem(self.addItemText)
        self.sol_arg_list[1]=self.lt_combo.currentText()

    def pm_addListWidget(self):
        self.addItemText = self.pm_combo.currentText()
        self.calcul_list.addItem(self.addItemText)
        self.sol_arg_list[3]=self.pm_combo.currentText()


    def ps_addListWidget(self):
        self.addItemText = self.ps_combo.currentText()
        self.calcul_list.addItem(self.addItemText)
        self.sol_arg_list[2]=self.ps_combo.currentText()


    def clear_Btn(self) : # clear function
        self.calcul_list.clear()
        self.calcul_list.addItem('선택목록')
        #self.selec_type_line.clear(); self.selec_type_line.setText('Type : ')
        self.pipe_length_value.clear()
        self. sol_arg_list = [0,0,0,0,0,0,0,0,0,0]; self.loss = [0,0,0,0,0,0,0,0]
        

    def Select_Type(self, st):
        if st.isChecked(): 
            self.sol_arg_list[0]=st.text()
            self.selec_type_line.setText('Type: '+ self.sol_arg_list[0])
 


    def Minor_losses(self):
        self.sol_arg_list[4]=self.flow_rate_value.value() # Q
        self.sol_arg_list[5]=self.pipe_length_value.value() # L
        self.sol_arg_list[6]=self.height_drop_value.value() # dz
        self.sol_arg_list[7]=self.pressure_drop_value.value()#dp 
        
        if self.ml_check_1.isChecked(): self.loss[0]=[self.ml_check_1.text(),self.ml_num_1.value()]
        if self.ml_check_2.isChecked(): self.loss[1]=[self.ml_check_2.text(),self.ml_num_2.value()]
        if self.ml_check_3.isChecked(): self.loss[2]=[self.ml_check_3.text(),self.ml_num_3.value()]
        if self.ml_check_4.isChecked(): self.loss[3]=[self.ml_check_4.text(),self.ml_num_4.value()]
        if self.ml_check_5.isChecked(): self.loss[4]=[self.ml_check_5.text(),self.ml_num_5.value()]
        if self.ml_check_6.isChecked(): self.loss[5]=[self.ml_check_6.text(),self.ml_num_6.value()]
        if self.ml_check_7.isChecked(): self.loss[6]=[self.ml_check_7.text(),self.ml_num_7.value()]
        if self.ml_check_8.isChecked(): self.loss[7]=[self.ml_check_8.text(),self.ml_num_8.value()]
    
    def Bt_Calculation(self):
        print(self.sol_arg_list)
        
        try:
            self.flow_rate_value.clear()
            if self.sol_arg_list[0] == 'Pressure Drop':
                result = Pressure_drop(self.sol_arg_list[4], self.sol_arg_list[5], self.sol_arg_list[6], self.sol_arg_list[1], self.sol_arg_list[2], self.sol_arg_list[3], self.loss) # Q, L, dz,liquid_type, pipe_standard, merterial, self.loss
                self.solution = str(round(result*10**-6,3))+' KPa'
            elif self.self.sol_arg_list[0] == 'Flow Rate':
                result = Flow_rate(self.self.sol_arg_list[7], self.sol_arg_list[5], self.sol_arg_list[6], self.sol_arg_list[1],self.sol_arg_list[2], self.sol_arg_list[3], self.loss) #dp, L, dz, liquid_type, pipe_standard, merterial, self.loss
                self.solution = str(result)+' m³/s'
            elif self.self.sol_arg_list[0] == 'Diameter':
                result = Pipe_diameter(self.self.sol_arg_list[7],self.sol_arg_list[4], self.sol_arg_list[5], self.sol_arg_list[6], self.sol_arg_list[1], self.sol_arg_list[3], self.loss)
                self.solution = str(round(result,5))+' m'
            self.result_line.setText(self.solution) #str(result)
        except (AttributeError,KeyError):
            self.err_message.setText('필수 요소 를 확인해 주세요!!')
            
            sleep(3)
            self.err_message.setText('')
            pass
            
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()