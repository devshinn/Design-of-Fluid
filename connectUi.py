# -*- coding: utf-8 -*-
__author__ = "ShinHyeok_Kim <hostomer@khu.ac.kr>"
import sys
import Ui
from PyQt5.QtWidgets import *
from DesignSolution import *





class WindowClass(QMainWindow, Ui.Ui_Dialog) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self. sol_arg_list = [0,0,0,0,0,0,0,0,0,0]; self.loss = [0,0,0,0,0,0,0,0,0,0]; self.summation = [0]


        self.bt_calculation.clicked.connect(self.Bt_Calculation)
        
        #select Type
        
        self.select_type_1.clicked.connect(lambda: self.Select_Type(self.select_type_1))
        self.select_type_2.clicked.connect(lambda: self.Select_Type(self.select_type_2))
        self.select_type_3.clicked.connect(lambda: self.Select_Type(self.select_type_3))

        #minors losses
        self.ml_check_1.stateChanged.connect(self.Minor_losses);self.ml_check_3.stateChanged.connect(self.Minor_losses);  self.ml_check_5.stateChanged.connect(self.Minor_losses);self.ml_check_7.stateChanged.connect(self.Minor_losses);
        self.ml_check_2.stateChanged.connect(self.Minor_losses);self.ml_check_4.stateChanged.connect(self.Minor_losses);  self.ml_check_6.stateChanged.connect(self.Minor_losses);self.ml_check_8.stateChanged.connect(self.Minor_losses);
        self.ml_check_9.stateChanged.connect(self.Minor_losses);self.ml_check_10.stateChanged.connect(self.Sum_K);
        # minors losses 갯수

        self.ml_num_1.valueChanged.connect(self.Minor_losses);self.ml_num_3.valueChanged.connect(self.Minor_losses);self.ml_num_5.valueChanged.connect(self.Minor_losses);self.ml_num_7.valueChanged.connect(self.Minor_losses)
        self.ml_num_2.valueChanged.connect(self.Minor_losses);self.ml_num_4.valueChanged.connect(self.Minor_losses);self.ml_num_6.valueChanged.connect(self.Minor_losses);self.ml_num_8.valueChanged.connect(self.Minor_losses)
        self.ml_num_9.valueChanged.connect(self.Minor_losses)

        self.pipe_length_value.valueChanged.connect(self.Minor_losses);self.height_drop_value.valueChanged.connect(self.Minor_losses);
        self.flow_rate_value.valueChanged.connect(self.Minor_losses);self.pressure_drop_value.valueChanged.connect(self.Minor_losses); self.sum_k.valueChanged.connect(self.Sum_K)
        
        self.calcul_list.itemDoubleClicked.connect(self.DoubleClice_remove_list_item)
        # self.calcul_list.currentItemChanged.connect(self.chkCurrentItemChanged)
        
        #라인에딧에 추가
        self.lt_add_btn.clicked.connect(self.lt_addListWidget)
        self.ps_add_btn.clicked.connect(self.ps_addListWidget)
        self.pm_add_btn.clicked.connect(self.pm_addListWidget)
        self.bt_clear.clicked.connect(self.clear_Btn) # clear button

    def clear_Btn(self) : # clear function
        self.calcul_list.clear()
        self.calcul_list.addItem('선택목록')
        #self.selec_type_line.clear(); self.selec_type_line.setText('Type : ')
        self.pipe_length_value.clear()
        self.sol_arg_list = [0,0,0,0,0,0,0,0,0,0]; self.loss = [0,0,0,0,0,0,0,0,0]
        self.sol_arg_list[0] = self.selec_type_line.text()
        self.ml_num_1.clear()
        self.sum_k.clear
        self.err_message.setText('')

#더블클릭 삭제
    def DoubleClice_remove_list_item(self) : 

        self.removeItemRow = self.calcul_list.currentRow()
        self.calcul_list.takeItem(self.removeItemRow)

        self.err_message.setText('')
 # 콤보 박스에서 리스트위젯으로
    def lt_addListWidget(self) :
        self.addItemText = self.lt_combo.currentText()
        self.calcul_list.addItem(self.addItemText)
        self.sol_arg_list[1]=self.lt_combo.currentText()
        self.err_message.setText('')
    def pm_addListWidget(self):
        self.addItemText = self.pm_combo.currentText()
        self.calcul_list.addItem(self.addItemText)
        self.sol_arg_list[3]=self.pm_combo.currentText()
        self.err_message.setText('')

    def ps_addListWidget(self):
        self.addItemText = self.ps_combo.currentText()
        self.calcul_list.addItem(self.addItemText)
        self.sol_arg_list[2]=self.ps_combo.currentText()

        self.err_message.setText('')

        

    def Select_Type(self, st):
        if st.isChecked(): 
            self.sol_arg_list[0]=st.text()
            self.selec_type_line.setText('Type: '+ self.sol_arg_list[0])
        self.err_message.setText('')

    def Sum_K(self):
        if self.ml_check_10.isChecked():
            self.summation[0]=self.sum_k.text()
            self.err_message.setText('')
    def Minor_losses(self):
        self.sol_arg_list[4]=self.flow_rate_value.text() # Q
        self.sol_arg_list[5]=self.pipe_length_value.text() # L
        self.sol_arg_list[6]=self.height_drop_value.text()# dz
        self.sol_arg_list[7]=self.pressure_drop_value.text()#dp 
        
        if self.ml_check_1.isChecked(): self.loss[0]=[self.ml_check_1.text(),self.ml_num_1.text()]
        if self.ml_check_2.isChecked(): self.loss[1]=[self.ml_check_2.text(),self.ml_num_2.text()]
        if self.ml_check_3.isChecked(): self.loss[2]=[self.ml_check_3.text(),self.ml_num_3.text()]
        if self.ml_check_4.isChecked(): self.loss[3]=[self.ml_check_4.text(),self.ml_num_4.text()]
        if self.ml_check_5.isChecked(): self.loss[4]=[self.ml_check_5.text(),self.ml_num_5.text()]
        if self.ml_check_6.isChecked(): self.loss[5]=[self.ml_check_6.text(),self.ml_num_6.text()]
        if self.ml_check_7.isChecked(): self.loss[6]=[self.ml_check_7.text(),self.ml_num_7.text()]
        if self.ml_check_8.isChecked(): self.loss[7]=[self.ml_check_8.text(),self.ml_num_8.text()]
        if self.ml_check_9.isChecked(): self.loss[8]=[self.ml_check_9.text(),self.ml_num_9.text()]
        self.err_message.setText('')
    
    def Bt_Calculation(self):
        if self.summation[0] != 0:
            self.loss = self.summation
        try:
            if self.sol_arg_list[0] == 'Pressure Drop':
                result = Pressure_drop(self.sol_arg_list[4], self.sol_arg_list[5], self.sol_arg_list[6], self.sol_arg_list[1], self.sol_arg_list[2], self.sol_arg_list[3], self.loss) # Q, L, dz,liquid_type, pipe_standard, merterial, self.loss
                self.solution = str(round(result[0],4))+' KPa'+ '    f:'+str(round(result[1],4))
            elif self.sol_arg_list[0] == 'Flow Rate':
                result = Flow_rate(self.sol_arg_list[7], self.sol_arg_list[5], self.sol_arg_list[6], self.sol_arg_list[1],self.sol_arg_list[2], self.sol_arg_list[3], self.loss) #dp, L, dz, liquid_type, pipe_standard, merterial, self.loss
                self.solution = str(round(result[0],4))+' m³/s'+'  f: '+str(round(result[1],4))
            elif self.sol_arg_list[0] == 'Diameter':
                result = Pipe_diameter(self.sol_arg_list[7],self.sol_arg_list[4], self.sol_arg_list[5], self.sol_arg_list[6], self.sol_arg_list[1], self.sol_arg_list[3], self.loss)
                self.solution = str(round(result,5))+' m'+'   f: '+str(round(result[1],4))
                
            self.result_line.setText(self.solution) #str(result)
        
        except (AttributeError,KeyError,ZeroDivisionError):
            self.err_message.setText('필수 요소 를 확인 or 재시작!!')
            pass
            
if __name__ == "__main__" :
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()

