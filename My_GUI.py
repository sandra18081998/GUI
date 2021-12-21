import sys
from PyQt5.QtWidgets import *  # imports section
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import uic
from scipy import integrate
from math import exp, cos, pi, atan, log, sqrt

class DlgMain(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('/Users/aleksandrapavlovskaya/IdeaProjects/diplom/my_project.ui', self)
        self.setFixedSize(822, 664)
        self.tabWidget.setCurrentIndex(0)

        redBrush = QBrush(Qt.red)
        blueBrush = QBrush(Qt.blue)
        blackPen = QPen(Qt.black)
        blackPen.setWidth(2)


        scene = QGraphicsScene(self.tab)

        scene.addLine(QLineF(40, 140, 290, 140), blackPen)
        scene.addLine(QLineF(40, 140, 2, 240), blackPen)
        scene.addLine(QLineF(40, 140, 40, 10), blackPen)


        graphicsView = QGraphicsView(scene, self.tab)
        graphicsView.setGeometry(305, 221, 481, 381)
        graphicsView.setObjectName("graphicsView")

        #подключение функций для пересчета активности из Бк в Ки
        self.lineEdit_nuc_1_Bc.setPlaceholderText('3.7e10')
        self.lineEdit_nuc_1_Bc.editingFinished.connect(self.calc_Ku_1)
        self.lineEdit_nuc_2_Bc.setPlaceholderText('3.7e10')
        self.lineEdit_nuc_2_Bc.editingFinished.connect(self.calc_Ku_2)
        self.lineEdit_nuc_3_Bc.setPlaceholderText('3.7e10')
        self.lineEdit_nuc_3_Bc.editingFinished.connect(self.calc_Ku_3)
        self.lineEdit_nuc_4_Bc.setPlaceholderText('3.7e10')
        self.lineEdit_nuc_4_Bc.editingFinished.connect(self.calc_Ku_4)

        #подключение функций для пересчета активности из Ки в Бк
        self.lineEdit_nuc_1_Ku.editingFinished.connect(self.calc_Bk_1)
        self.lineEdit_nuc_2_Ku.editingFinished.connect(self.calc_Bk_2)
        self.lineEdit_nuc_3_Ku.editingFinished.connect(self.calc_Bk_3)
        self.lineEdit_nuc_4_Ku.editingFinished.connect(self.calc_Bk_4)


        self.rbt_point.toggled.connect(self.set_point_settings)
        self.rbt_line.toggled.connect(self.set_line_settings)
        self.rbt_disc.toggled.connect(self.set_disc_settings)
        self.rbt_cylinder.toggled.connect(self.set_cylinder_settings)

        #добавление элементов в 1-й комбобокс с материалом защитного экрана
        self.cmb_shield_material_1.addItem('Железо', 7.86)
        self.cmb_shield_material_1.addItem('Бетон', 2.3)
        self.cmb_shield_material_1.addItem('Вода', 1.0)
        self.cmb_shield_material_1.addItem('Алюминий', 2.7)
        self.cmb_shield_material_1.addItem('Свинец', 11.34)
        self.cmb_shield_material_1.currentIndexChanged.connect(self.set_density_shield_1)

        #добавление элементов в 2-й комбобокс с материалом защитного экрана
        self.cmb_shield_material_2.addItem('Железо', 7.86)
        self.cmb_shield_material_2.addItem('Бетон', 2.3)
        self.cmb_shield_material_2.addItem('Вода', 1.0)
        self.cmb_shield_material_2.addItem('Алюминий', 2.7)
        self.cmb_shield_material_2.addItem('Свинец', 11.34)
        self.cmb_shield_material_2.currentIndexChanged.connect(self.set_density_shield_2)

        #добавление элементов в 3-й комбобокс с материалом защитного экрана
        self.cmb_shield_material_3.addItem('Железо', 7.86)
        self.cmb_shield_material_3.addItem('Бетон', 2.3)
        self.cmb_shield_material_3.addItem('Вода', 1.0)
        self.cmb_shield_material_3.addItem('Алюминий', 2.7)
        self.cmb_shield_material_3.addItem('Свинец', 11.34)
        self.cmb_shield_material_3.currentIndexChanged.connect(self.set_density_shield_3)

        #элементы 1 комбобокса с гамма-постоянными
        self.cmb_nuc_1.addItem('', 0.0)
        self.cmb_nuc_1.addItem('Co-60', 83.8)
        self.cmb_nuc_1.addItem('Cs-137', 21.2)
        self.cmb_nuc_1.addItem('I-131', 14.1)
        self.cmb_nuc_1.addItem('Na-24', 77.3)
        self.cmb_nuc_1.currentIndexChanged.connect(self.set_gamma_1)


        #элементы 1 комбобокса с гамма-постоянными
        self.cmb_nuc_2.addItem('', 0.0)
        self.cmb_nuc_2.addItem('Co-60', 83.8)
        self.cmb_nuc_2.addItem('Cs-137', 21.2)
        self.cmb_nuc_2.addItem('I-131', 14.1)
        self.cmb_nuc_2.addItem('Na-24', 77.3)
        self.cmb_nuc_2.currentIndexChanged.connect(self.set_gamma_2)

        #элементы 1 комбобокса с гамма-постоянными
        self.cmb_nuc_3.addItem('', 0.0)
        self.cmb_nuc_3.addItem('Co-60', 83.8)
        self.cmb_nuc_3.addItem('Cs-137', 21.2)
        self.cmb_nuc_3.addItem('I-131', 14.1)
        self.cmb_nuc_3.addItem('Na-24', 77.3)
        self.cmb_nuc_3.currentIndexChanged.connect(self.set_gamma_3)

        #элементы 1 комбобокса с гамма-постоянными
        self.cmb_nuc_4.addItem('', 0.0)
        self.cmb_nuc_4.addItem('Co-60', 83.8)
        self.cmb_nuc_4.addItem('Cs-137', 21.2)
        self.cmb_nuc_4.addItem('I-131', 14.1)
        self.cmb_nuc_4.addItem('Na-24', 77.3)
        self.cmb_nuc_4.currentIndexChanged.connect(self.set_gamma_4)


        #расчет удельной активности
        self.btn_result.clicked.connect(self.calc_doza)



    def set_gamma_1(self, idx_1):
        self.spb_gamma_1.setValue(self.cmb_nuc_1.itemData(idx_1))

    def set_gamma_2(self, idx_1):
        self.spb_gamma_2.setValue(self.cmb_nuc_2.itemData(idx_1))

    def set_gamma_3(self, idx_1):
        self.spb_gamma_3.setValue(self.cmb_nuc_3.itemData(idx_1))

    def set_gamma_4(self, idx_1):
        self.spb_gamma_4.setValue(self.cmb_nuc_4.itemData(idx_1))

    def set_density_shield_1(self, idx):
        self.spb_dens_shield_1.setValue(self.cmb_shield_material_1.itemData(idx))

    def set_density_shield_2(self, idx):
        self.spb_dens_shield_2.setValue(self.cmb_shield_material_1.itemData(idx))

    def set_density_shield_3(self, idx):
        self.spb_dens_shield_3.setValue(self.cmb_shield_material_1.itemData(idx))



    def set_point_settings(self):
        self.lbl_specific_activity_Bc.setText('Бк')
        self.lbl_specific_activity_Ku.setText('Ки')

    def set_line_settings(self):
        self.lbl_specific_activity_Bc.setText('Бк/см')
        self.lbl_specific_activity_Ku.setText('Ки/см')

    def set_disc_settings(self):
        self.lbl_specific_activity_Bc.setText('Бк/см^2')
        self.lbl_specific_activity_Ku.setText('Ки/см^2')

    def set_cylinder_settings(self):
        self.lbl_specific_activity_Bc.setText('Бк/см^3')
        self.lbl_specific_activity_Ku.setText('Ки/см^3')


    def calc_Ku_1(self):
        Ku_activ_1 = float(self.lineEdit_nuc_1_Bc.text()) * 2.7027 * 10**(-11)
        Ku_activ_1_print = format(float(self.lineEdit_nuc_1_Bc.text()) * 2.7027 * 10**(-11), '.2e')
        circle_area = pi * (self.spinbox_radius.value())**2
        cylinder_volume = circle_area * self.spinbox_height.value()
        self.lineEdit_nuc_1_Ku.setText(str(Ku_activ_1_print))
        if self.rbt_point.isChecked():
            self.lineEd_spec_act_nuc_1_Ku.setText(str(Ku_activ_1_print))
            self.lineEd_spec_act_nuc_1_Bc.setText(self.lineEdit_nuc_1_Bc.text())
        elif self.rbt_line.isChecked():
            self.lineEd_spec_act_nuc_1_Ku.setText(format((Ku_activ_1 / self.spinbox_length.value()), '.2e'))
            self.lineEd_spec_act_nuc_1_Bc.setText(format((float(self.lineEdit_nuc_1_Bc.text()) / self.spinbox_length.value()), '.2e'))
        elif self.rbt_disc.isChecked():
            self.lineEd_spec_act_nuc_1_Bc.setText(format(float(self.lineEdit_nuc_1_Bc.text())/circle_area, '.2e'))
            self.lineEd_spec_act_nuc_1_Ku.setText(format(Ku_activ_1/circle_area, '.2e'))
        elif self.rbt_cylinder.isChecked():
            self.lineEd_spec_act_nuc_1_Ku.setText(format(Ku_activ_1/cylinder_volume, '.2e'))
            self.lineEd_spec_act_nuc_1_Bc.setText(format(float(self.lineEdit_nuc_1_Bc.text())/cylinder_volume, '.2e'))

    def calc_Ku_2(self):
        Ku_activ_2 = float(self.lineEdit_nuc_2_Bc.text()) * 2.7027 * 10**(-11)
        Ku_activ_2_print = format(float(self.lineEdit_nuc_2_Bc.text()) * 2.7027 * 10**(-11), '.2e')
        circle_area = pi * (self.spinbox_radius.value())**2
        cylinder_volume = circle_area * self.spinbox_height.value()
        self.lineEdit_nuc_2_Ku.setText(str(Ku_activ_2))
        if self.rbt_point.isChecked():
            self.lineEd_spec_act_nuc_2_Ku.setText(str(Ku_activ_2_print))
            self.lineEd_spec_act_nuc_2_Bc.setText(self.lineEdit_nuc_2_Bc.text())
        elif self.rbt_line.isChecked():
            self.lineEd_spec_act_nuc_2_Ku.setText(format((Ku_activ_2 / self.spinbox_length.value()), '.2e'))
            self.lineEd_spec_act_nuc_2_Bc.setText(format((float(self.lineEdit_nuc_2_Bc.text()) / self.spinbox_length.value()), '.2e'))
        elif self.rbt_disc.isChecked():
            self.lineEd_spec_act_nuc_2_Bc.setText(format(float(self.lineEdit_nuc_2_Bc.text())/circle_area, '.2e'))
            self.lineEd_spec_act_nuc_2_Ku.setText(format(Ku_activ_2/circle_area, '.2e'))
        elif self.rbt_cylinder.isChecked():
            self.lineEd_spec_act_nuc_2_Ku.setText(format(Ku_activ_2/cylinder_volume, '.2e'))
            self.lineEd_spec_act_nuc_2_Bc.setText(format(float(self.lineEdit_nuc_2_Bc.text())/cylinder_volume, '.2e'))


    def calc_Ku_3(self):
        Ku_activ_3 = float(self.lineEdit_nuc_3_Bc.text()) * 2.7027 * 10**(-11)
        Ku_activ_3_print = format(float(self.lineEdit_nuc_3_Bc.text()) * 2.7027 * 10**(-11), '.2e')
        circle_area = pi * (self.spinbox_radius.value())**2
        cylinder_volume = circle_area * self.spinbox_height.value()
        self.lineEdit_nuc_3_Ku.setText(str(Ku_activ_3))
        if self.rbt_point.isChecked():
            self.lineEd_spec_act_nuc_3_Ku.setText(str(Ku_activ_3_print))
            self.lineEd_spec_act_nuc_3_Bc.setText(self.lineEdit_nuc_3_Bc.text())
        if self.rbt_line.isChecked():
            self.lineEd_spec_act_nuc_3_Ku.setText(format((Ku_activ_3 / self.spinbox_length.value()), '.2e'))
            self.lineEd_spec_act_nuc_3_Bc.setText(format((float(self.lineEdit_nuc_3_Bc.text()) / self.spinbox_length.value()), '.2e'))
        elif self.rbt_disc.isChecked():
            self.lineEd_spec_act_nuc_3_Bc.setText(format(float(self.lineEdit_nuc_3_Bc.text())/circle_area, '.2e'))
            self.lineEd_spec_act_nuc_3_Ku.setText(format(Ku_activ_3/circle_area, '.2e'))
        elif self.rbt_cylinder.isChecked():
            self.lineEd_spec_act_nuc_3_Ku.setText(format(Ku_activ_3/cylinder_volume, '.2e'))
            self.lineEd_spec_act_nuc_3_Bc.setText(format(float(self.lineEdit_nuc_3_Bc.text())/cylinder_volume, '.2e'))


    def calc_Ku_4(self):
        Ku_activ_4 = float(self.lineEdit_nuc_4_Bc.text()) * 2.7027 * 10**(-11)
        circle_area = pi * (self.spinbox_radius.value())**2
        cylinder_volume = circle_area * self.spinbox_height.value()
        self.lineEdit_nuc_4_Ku.setText(str(Ku_activ_4))
        if self.rbt_point.isChecked():
            self.lineEd_spec_act_nuc_4_Ku.setText(format((Ku_activ_4), '.2e'))
            self.lineEd_spec_act_nuc_4_Bc.setText(self.lineEdit_nuc_4_Bc.text())
        elif self.rbt_line.isChecked():
            self.lineEd_spec_act_nuc_4_Ku.setText(format((Ku_activ_4 / self.spinbox_length.value()), '.2e'))
            self.lineEd_spec_act_nuc_4_Bc.setText(format((float(self.lineEdit_nuc_4_Bc.text()) / self.spinbox_length.value()), '.2e'))
        elif self.rbt_disc.isChecked():
            self.lineEd_spec_act_nuc_4_Bc.setText(format(float(self.lineEdit_nuc_4_Bc.text())/circle_area, '.2e'))
            self.lineEd_spec_act_nuc_4_Ku.setText(format(Ku_activ_4/circle_area, '.2e'))
        elif self.rbt_cylinder.isChecked():
            self.lineEd_spec_act_nuc_4_Ku.setText(format(Ku_activ_4/cylinder_volume, '.2e'))
            self.lineEd_spec_act_nuc_4_Bc.setText(format(float(self.lineEdit_nuc_4_Bc.text())/cylinder_volume, '.2e'))


    def calc_Bk_1(self):
        Bk_activ_1 = float(self.lineEdit_nuc_1_Ku.text()) * 3.7 * 10**10
        Bk_activ_1_print = format(float(self.lineEdit_nuc_1_Ku.text()) * 3.7 * 10**10, '.2e')
        circle_area = pi * (self.spinbox_radius.value())**2
        cylinder_volume = circle_area * self.spinbox_height.value()
        #пересчитываем введенную пользователем активность из Ки в Бк и выводим
        self.lineEdit_nuc_1_Bc.setText(str(Bk_activ_1_print))
        if self.rbt_point.isChecked():
            self.lineEd_spec_act_nuc_1_Bc.setText(format(Bk_activ_1, '.2e'))
            self.lineEd_spec_act_nuc_1_Ku.setText(self.lineEdit_nuc_1_Ku.text())
        elif self.rbt_line.isChecked():
            self.lineEd_spec_act_nuc_1_Bc.setText(str(Bk_activ_1 / self.spinbox_length.value()))
            self.lineEd_spec_act_nuc_1_Ku.setText(str(float(self.lineEdit_nuc_1_Ku.text()) / self.spinbox_length.value()))
        elif self.rbt_disc.isChecked():
            self.lineEd_spec_act_nuc_1_Ku.setText(format(float(self.lineEdit_nuc_1_Ku.text())/circle_area, '.2e'))
            self.lineEd_spec_act_nuc_1_Bc.setText(format(Bk_activ_1/circle_area, '.2e'))
        elif self.rbt_cylinder.isChecked():
            self.lineEd_spec_act_nuc_1_Bc.setText(format(Bk_activ_1/cylinder_volume, '.2e'))
            self.lineEd_spec_act_nuc_1_Ku.setText(format(float(self.lineEdit_nuc_1_Ku.text())/cylinder_volume, '.2e'))

    def calc_Bk_2(self):
        Bk_activ_2 = float(self.lineEdit_nuc_2_Ku.text()) * 3.7 * 10**10
        self.lineEdit_nuc_2_Bc.setText(str(Bk_activ_2))
        Bk_activ_2_print = format(float(self.lineEdit_nuc_2_Ku.text()) * 3.7 * 10**10, '.2e')
        circle_area = pi * (self.spinbox_radius.value())**2
        cylinder_volume = circle_area * self.spinbox_height.value()
        #пересчитываем введенную пользователем активность из Ки в Бк и выводим
        self.lineEdit_nuc_1_Bc.setText(str(Bk_activ_2_print))
        if self.rbt_point.isChecked():
            self.lineEd_spec_act_nuc_2_Bc.setText(format(Bk_activ_2, '.2e'))
            self.lineEd_spec_act_nuc_2_Ku.setText(self.lineEdit_nuc_2_Ku.text())
        elif self.rbt_line.isChecked():
            self.lineEd_spec_act_nuc_2_Bc.setText(str(Bk_activ_2 / self.spinbox_length.value()))
            self.lineEd_spec_act_nuc_2_Ku.setText(str(float(self.lineEdit_nuc_2_Ku.text()) / self.spinbox_length.value()))
        elif self.rbt_disc.isChecked():
            self.lineEd_spec_act_nuc_2_Ku.setText(format(float(self.lineEdit_nuc_2_Ku.text())/circle_area, '.2e'))
            self.lineEd_spec_act_nuc_2_Bc.setText(format(Bk_activ_2/circle_area, '.2e'))
        elif self.rbt_cylinder.isChecked():
            self.lineEd_spec_act_nuc_2_Bc.setText(format(Bk_activ_2/cylinder_volume, '.2e'))
            self.lineEd_spec_act_nuc_2_Ku.setText(format(float(self.lineEdit_nuc_2_Ku.text())/cylinder_volume, '.2e'))


    def calc_Bk_3(self):
        Bk_activ_3 = float(self.lineEdit_nuc_3_Ku.text()) * 3.7 * 10**10
        self.lineEdit_nuc_3_Bc.setText(str(Bk_activ_3))
        Bk_activ_3_print = format(float(self.lineEdit_nuc_1_Ku.text()) * 3.7 * 10**10, '.2e')
        circle_area = pi * (self.spinbox_radius.value())**2
        cylinder_volume = circle_area * self.spinbox_height.value()
        #пересчитываем введенную пользователем активность из Ки в Бк и выводим
        self.lineEdit_nuc_3_Bc.setText(str(Bk_activ_3_print))
        if self.rbt_point.isChecked():
            self.lineEd_spec_act_nuc_3_Bc.setText(format(Bk_activ_3, '.2e'))
            self.lineEd_spec_act_nuc_3_Ku.setText(self.lineEdit_nuc_3_Ku.text())
        elif self.rbt_line.isChecked():
            self.lineEd_spec_act_nuc_3_Bc.setText(format(Bk_activ_3 / self.spinbox_length.value()), '.2e')
            self.lineEd_spec_act_nuc_3_Ku.setText(format(float(self.lineEdit_nuc_3_Ku.text()) / self.spinbox_length.value()), '.2e')
        elif self.rbt_disc.isChecked():
            self.lineEd_spec_act_nuc_3_Ku.setText(format(float(self.lineEdit_nuc_3_Ku.text())/circle_area, '.2e'))
            self.lineEd_spec_act_nuc_3_Bc.setText(format(Bk_activ_3/circle_area, '.2e'))
        elif self.rbt_cylinder.isChecked():
            self.lineEd_spec_act_nuc_3_Bc.setText(format(Bk_activ_3/cylinder_volume, '.2e'))
            self.lineEd_spec_act_nuc_3_Ku.setText(format(float(self.lineEdit_nuc_3_Ku.text())/cylinder_volume, '.2e'))


    def calc_Bk_4(self):
        Bk_activ_4 = float(self.lineEdit_nuc_4_Ku.text()) * 3.7 * 10**10
        self.lineEdit_nuc_4_Bc.setText(str(Bk_activ_4))
        Bk_activ_4_print = format(float(self.lineEdit_nuc_4_Ku.text()) * 3.7 * 10**10, '.2e')
        circle_area = pi * (self.spinbox_radius.value())**2
        cylinder_volume = circle_area * self.spinbox_height.value()
        #пересчитываем введенную пользователем активность из Ки в Бк и выводим
        self.lineEdit_nuc_4_Bc.setText(str(Bk_activ_4_print))
        if self.rbt_point.isChecked():
            self.lineEd_spec_act_nuc_4_Bc.setText(format(Bk_activ_4, '.2e'))
            self.lineEd_spec_act_nuc_4_Ku.setText(self.lineEdit_nuc_4_Ku.text())
        elif self.rbt_line.isChecked():
            self.lineEd_spec_act_nuc_4_Bc.setText(format(Bk_activ_4 / self.spinbox_length.value()), '.2e')
            self.lineEd_spec_act_nuc_4_Ku.setText(format(float(self.lineEdit_nuc_4_Ku.text()) / self.spinbox_length.value()), '.2e')
        elif self.rbt_disc.isChecked():
            self.lineEd_spec_act_nuc_4_Ku.setText(format(float(self.lineEdit_nuc_4_Ku.text())/circle_area, '.2e'))
            self.lineEd_spec_act_nuc_4_Bc.setText(format(Bk_activ_4/circle_area, '.2e'))
        elif self.rbt_cylinder.isChecked():
            self.lineEd_spec_act_nuc_4_Bc.setText(format(Bk_activ_4/cylinder_volume, '.2e'))
            self.lineEd_spec_act_nuc_4_Ku.setText(format(float(self.lineEdit_nuc_4_Ku.text())/cylinder_volume, '.2e'))


    def calc_doza(self):
        #переписать значения активности
        #брать пересчитанные
        activity_1 = float(self.lineEd_spec_act_nuc_1_Bc.text())
        activity_2 = float(self.lineEd_spec_act_nuc_2_Bc.text())
        activity_3 = float(self.lineEd_spec_act_nuc_3_Bc.text())
        activity_4 = float(self.lineEd_spec_act_nuc_4_Bc.text())
        Gr_per_hour = 10**(-18) * 3600
        x = self.spinbox_x.value() / 100
        y = self.spinbox_y.value() / 100
        z = self.spinbox_z.value() / 100
        distance = (x**2 + y**2 + z**2)**0.5
        length = self.spinbox_length.value() / 100
        radius = self.spinbox_radius.value() / 100
        # height = spinbox_height.value()
        gamma_1 = self.spb_gamma_1.value()
        gamma_2 = self.spb_gamma_2.value()
        gamma_3 = self.spb_gamma_3.value()
        gamma_4 = self.spb_gamma_4.value()

        #защита
        Ferrum = {'Co-60': 0.422, 'Cs-137': 0.570, 'I-131': 0.717, 'Na-24': 0.291, '' : 0.0}
        Beton = {'Co-60': 0.131, 'Cs-137': 0.177, 'I-131': 0.223, 'Na-24': 0.0874, '' : 0.0}
        Water = {'Co-60': 0.0631, 'Cs-137': 0.0857, 'I-131': 0.106, 'Na-24': 0.0410, '' : 0.0}
        Aluminium = {'Co-60': 0.148, 'Cs-137': 0.201, 'I-131': 0.278, 'Na-24': 0.0994, '' : 0.0}
        Plumbum = {'Co-60': 0.658, 'Cs-137': 1.18, 'I-131': 2.44, 'Na-24': 0.476, '' : 0.0}

        material_1 = self.cmb_shield_material_1.currentText()
        material_2 = self.cmb_shield_material_2.currentText()
        material_3 = self.cmb_shield_material_3.currentText()
        material_lst = [material_1, material_2, material_3]

        nuclide_1 = self.cmb_nuc_1.currentText()
        nuclide_2 = self.cmb_nuc_2.currentText()
        nuclide_3 = self.cmb_nuc_3.currentText()
        nuclide_4 = self.cmb_nuc_4.currentText()
        nuc_lst = [nuclide_1, nuclide_2, nuclide_3, nuclide_4]

        thickness_1 = self.spb_thick_1.value()
        thickness_2 = self.spb_thick_2.value()
        thickness_3 = self.spb_thick_3.value()
        thick_lst = [thickness_1, thickness_2, thickness_3]


        koef_osl_lst = []

        for nuclide in nuc_lst:
            koef_for_nuc = []
            for material in material_lst:
                if material == 'Железо':
                    koef_osl = Ferrum[nuclide]
                elif material == 'Бетон':
                    koef_osl = Beton[nuclide]
                elif material == 'Вода':
                    koef_osl = Water[nuclide]
                elif material == 'Алюминий':
                    koef_osl = Aluminium[nuclide]
                elif material == 'Свинец':
                    koef_osl = Plumbum[nuclide]
                koef_for_nuc.append(koef_osl)
            koef_osl_lst.append(koef_for_nuc)

        list_of_d = []

        for i in range(4):
            for j in range(3):
                d = round(thick_lst[j] * koef_osl_lst[i][j], 2)
                list_of_d.append(d)

        d_1 = round(sum(list_of_d[:3]), 2)
        d_2 = round(sum(list_of_d[3:6]), 2)
        d_3 = round(sum(list_of_d[6:9]), 2)
        d_4 = round(sum(list_of_d[9:12]), 2)

        if self.rbt_point.isChecked(): #расчет для точечного источника
            D_1 = Gr_per_hour * activity_1 * gamma_1 * exp(-d_1) / distance**2
            D_2 = Gr_per_hour * activity_2 * gamma_2 * exp(-d_2) / distance**2
            D_3 = Gr_per_hour * activity_3 * gamma_3 * exp(-d_3) / distance**2
            D_4 = Gr_per_hour * activity_4 * gamma_4 * exp(-d_4) / distance**2
            self.res_nuc_1_without_buildup.setText(str(format(D_1, '.2e')))
            self.res_nuc_2_without_buildup.setText(str(format(D_2, '.2e')))
            self.res_nuc_3_without_buildup.setText(str(format(D_3, '.2e')))
            self.res_nuc_4_without_buildup.setText(str(format(D_4, '.2e')))
        elif self.rbt_line.isChecked(): #расчет для линейного источника
            tetta_1 = atan(abs(length-z)/x)
            tetta_2 = atan(z / x)
            F = lambda x, b: exp(-b/cos(x))
            v_1_d_1, err_1 = integrate.quad(F, 0, tetta_1, args=(d_1,))
            v_1_d_2, err_1 = integrate.quad(F, 0, tetta_1, args=(d_2,))
            v_1_d_3, err_1 = integrate.quad(F, 0, tetta_1, args=(d_3,))
            v_1_d_4, err_1 = integrate.quad(F, 0, tetta_1, args=(d_4,))
            v_2_d_1, err_2 = integrate.quad(F, 0, tetta_2, args=(d_1,))
            v_2_d_2, err_2 = integrate.quad(F, 0, tetta_2, args=(d_2,))
            v_2_d_3, err_2 = integrate.quad(F, 0, tetta_2, args=(d_3,))
            v_2_d_4, err_2 = integrate.quad(F, 0, tetta_2, args=(d_4,))
            if 0 <= z <= length:
                D_1 = activity_1 * 10**2 * (gamma_1 / x) * (v_1_d_1 + v_2_d_1) * Gr_per_hour
                D_2 = activity_2 * 10**2 * (gamma_2 / x) * (v_1_d_2 + v_2_d_2) * Gr_per_hour
                D_3 = activity_3 * 10**2 * (gamma_3 / x) * (v_1_d_3 + v_2_d_3) * Gr_per_hour
                D_4 = activity_4 * 10**2 * (gamma_4 / x) * (v_1_d_4 + v_2_d_4) * Gr_per_hour
                self.res_nuc_1_without_buildup.setText(str(format(D_1, '.2e')))
                self.res_nuc_2_without_buildup.setText(str(format(D_2, '.2e')))
                self.res_nuc_3_without_buildup.setText(str(format(D_3, '.2e')))
                self.res_nuc_4_without_buildup.setText(str(format(D_4, '.2e')))
            else:
                D_1 = activity_1 * 10**2 * (gamma_1 / x) * (v_2_d_1 - v_1_d_1) * Gr_per_hour
                D_2 = activity_2 * 10**2 * (gamma_2 / x) * (v_2_d_2 - v_1_d_2) * Gr_per_hour
                D_3 = activity_3 * 10**2 * (gamma_3 / x) * (v_2_d_3 - v_1_d_3) * Gr_per_hour
                D_4 = activity_4 * 10**2 * (gamma_4 / x) * (v_2_d_4 - v_1_d_4) * Gr_per_hour
                self.res_nuc_1_without_buildup.setText(str(format(D_1, '.2e')))
                self.res_nuc_2_without_buildup.setText(str(format(D_2, '.2e')))
                self.res_nuc_3_without_buildup.setText(str(format(D_3, '.2e')))
                self.res_nuc_4_without_buildup.setText(str(format(D_4, '.2e')))
        elif self.rbt_disc.isChecked(): #расчет дозы для дискового источника
            if z == 0:
                D_1 = pi * activity_1 * 10**4 * gamma_1 * log((x**2 + radius**2)/x**2) * Gr_per_hour
                D_2 = pi * activity_2 * 10**4 * gamma_2 * log((x**2 + radius**2)/x**2) * Gr_per_hour
                D_3 = pi * activity_3 * 10**4 * gamma_3 * log((x**2 + radius**2)/x**2) * Gr_per_hour
                D_4 = pi * activity_4 * 10**4 * gamma_4 * log((x**2 + radius**2)/x**2) * Gr_per_hour
                self.res_nuc_1_without_buildup.setText(str(format(D_1, '.2e')))
                self.res_nuc_2_without_buildup.setText(str(format(D_2, '.2e')))
                self.res_nuc_3_without_buildup.setText(str(format(D_3, '.2e')))
                self.res_nuc_4_without_buildup.setText(str(format(D_4, '.2e')))
            elif abs(z) == radius:
                D_1 = pi * activity_1 * 10**4 * gamma_1 * log((x + sqrt(4*radius**2 + x**2))/(2*x)) * Gr_per_hour
                D_2 = pi * activity_2 * 10**4 * gamma_2 * log((x + sqrt(4*radius**2 + x**2))/(2*x)) * Gr_per_hour
                D_3 = pi * activity_3 * 10**4 * gamma_3 * log((x + sqrt(4*radius**2 + x**2))/(2*x)) * Gr_per_hour
                D_4 = pi * activity_4 * 10**4 * gamma_4 * log((x + sqrt(4*radius**2 + x**2))/(2*x)) * Gr_per_hour
                self.res_nuc_1_without_buildup.setText(str(format(D_1, '.2e')))
                self.res_nuc_2_without_buildup.setText(str(format(D_2, '.2e')))
                self.res_nuc_3_without_buildup.setText(str(format(D_3, '.2e')))
                self.res_nuc_4_without_buildup.setText(str(format(D_4, '.2e')))
            elif x == 0:
                D_1 = pi * activity_1 * 10**4 * gamma_1 * log(z**2/(z**2 - radius**2)) * Gr_per_hour
                D_2 = pi * activity_2 * 10**4 * gamma_2 * log(z**2/(z**2 - radius**2)) * Gr_per_hour
                D_3 = pi * activity_3 * 10**4 * gamma_3 * log(z**2/(z**2 - radius**2)) * Gr_per_hour
                D_4 = pi * activity_4 * 10**4 * gamma_4 * log(z**2/(z**2 - radius**2)) * Gr_per_hour
                self.res_nuc_1_without_buildup.setText(str(format(D_1, '.2e')))
                self.res_nuc_2_without_buildup.setText(str(format(D_2, '.2e')))
                self.res_nuc_3_without_buildup.setText(str(format(D_3, '.2e')))
                self.res_nuc_4_without_buildup.setText(str(format(D_4, '.2e')))
            else:
                D_1 = pi * activity_1 * 10**4 * gamma_1 * log((x**2 + radius**2 - z**2 + sqrt(radius**4 + 2*radius**2*(x**2-z**2)
                                                                           + (x**2 + z**2)**2))/(2*x**2)) * Gr_per_hour
                D_2 = pi * activity_2 * 10**4 * gamma_2 * log((x**2 + radius**2 - z**2 + sqrt(radius**4 + 2*radius**2*(x**2-z**2)
                                                                           + (x**2 + z**2)**2))/(2*x**2)) * Gr_per_hour
                D_3 = pi * activity_3 * 10**4 * gamma_3 * log((x**2 + radius**2 - z**2 + sqrt(radius**4 + 2*radius**2*(x**2-z**2)
                                                                           + (x**2 + z**2)**2))/(2*x**2)) * Gr_per_hour
                D_4 = pi * activity_4 * 10**4 * gamma_4 * log((x**2 + radius**2 - z**2 + sqrt(radius**4 + 2*radius**2*(x**2-z**2)
                                                                           + (x**2 + z**2)**2))/(2*x**2)) * Gr_per_hour
                self.res_nuc_1_without_buildup.setText(str(format(D_1, '.2e')))
                self.res_nuc_2_without_buildup.setText(str(format(D_2, '.2e')))
                self.res_nuc_3_without_buildup.setText(str(format(D_3, '.2e')))
                self.res_nuc_4_without_buildup.setText(str(format(D_4, '.2e')))

            print(self.totals.setText(format(float(self.res_nuc_1_without_buildup)+float(self.res_nuc_2_without_buildup) + \
                    float(self.res_nuc_3_without_buildup) + float(self.res_nuc_4_without_buildup)), '.2e'))

        res_1 = float(self.res_nuc_1_without_buildup.text())
        res_2 = float(self.res_nuc_2_without_buildup.text())
        res_3 = float(self.res_nuc_3_without_buildup.text())
        res_4 = float(self.res_nuc_4_without_buildup.text())
        total = format(res_1 + res_2 + res_3 + res_4,'.2e')
        self.totals.setText(total)





if __name__ == '__main__':
    app = QApplication(sys.argv)  # create application
    dlgMain = DlgMain()  # create main GUI window
    dlgMain.show()# show GUI
    sys.exit(app.exec_())  # execute the application
