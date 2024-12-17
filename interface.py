# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from user import User
import pickle

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        self.users = {}
        try:
            with open("data.pkl", "rb") as file:
                loaded_data = pickle.load(file)
            self.users = loaded_data
        except:
            print("file does not exist")
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(428, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tab_vidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_vidget.setUsesScrollButtons(True)
        self.tab_vidget.setDocumentMode(False)
        self.tab_vidget.setTabsClosable(False)
        self.tab_vidget.setMovable(False)
        self.tab_vidget.setTabBarAutoHide(False)
        self.tab_vidget.setObjectName("tab_vidget")
        self.enter_tab = QtWidgets.QWidget()
        self.enter_tab.setObjectName("enter_tab")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.enter_tab)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.enter_log_pas = QtWidgets.QLabel(self.enter_tab)
        self.enter_log_pas.setObjectName("enter_log_pas")
        self.verticalLayout_3.addWidget(self.enter_log_pas)
        self.login_label = QtWidgets.QLabel(self.enter_tab)
        self.login_label.setObjectName("login_label")
        self.verticalLayout_3.addWidget(self.login_label)
        self.login_edit = QtWidgets.QLineEdit(self.enter_tab)
        self.login_edit.setMinimumSize(QtCore.QSize(0, 25))
        self.login_edit.setObjectName("login_edit")
        self.verticalLayout_3.addWidget(self.login_edit)
        self.password_label = QtWidgets.QLabel(self.enter_tab)
        self.password_label.setObjectName("password_label")
        self.verticalLayout_3.addWidget(self.password_label)
        self.password_edit = QtWidgets.QLineEdit(self.enter_tab)
        self.password_edit.setMinimumSize(QtCore.QSize(0, 25))
        self.password_edit.setObjectName("password_edit")
        self.verticalLayout_3.addWidget(self.password_edit)
        self.verticalLayout_9.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.reg_success = QtWidgets.QLabel(self.enter_tab)
        self.reg_success.setObjectName("reg_success")
        self.verticalLayout_2.addWidget(self.reg_success)
        self.enter_btn = QtWidgets.QPushButton(self.enter_tab)
        self.enter_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.enter_btn.setObjectName("enter_btn")
        self.verticalLayout_2.addWidget(self.enter_btn)
        self.reg_btn = QtWidgets.QPushButton(self.enter_tab)
        self.reg_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.reg_btn.setObjectName("reg_btn")
        self.verticalLayout_2.addWidget(self.reg_btn)
        self.anonim_btn = QtWidgets.QPushButton(self.enter_tab)
        self.anonim_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.anonim_btn.setObjectName("anonim_btn")
        self.verticalLayout_2.addWidget(self.anonim_btn)
        self.verticalLayout_9.addLayout(self.verticalLayout_2)
        self.tab_vidget.addTab(self.enter_tab, "")
        self.reg_tab = QtWidgets.QWidget()
        self.reg_tab.setObjectName("reg_tab")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.reg_tab)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.reg_login_label = QtWidgets.QLabel(self.reg_tab)
        self.reg_login_label.setObjectName("reg_login_label")
        self.verticalLayout_4.addWidget(self.reg_login_label)
        self.reg_line_login = QtWidgets.QLineEdit(self.reg_tab)
        self.reg_line_login.setMinimumSize(QtCore.QSize(0, 0))
        self.reg_line_login.setObjectName("reg_line_login")
        self.verticalLayout_4.addWidget(self.reg_line_login)
        self.reg_password_label = QtWidgets.QLabel(self.reg_tab)
        self.reg_password_label.setObjectName("reg_password_label")
        self.verticalLayout_4.addWidget(self.reg_password_label)
        self.reg_line_passw = QtWidgets.QLineEdit(self.reg_tab)
        self.reg_line_passw.setObjectName("reg_line_passw")
        self.verticalLayout_4.addWidget(self.reg_line_passw)
        self.reg_password2_label = QtWidgets.QLabel(self.reg_tab)
        self.reg_password2_label.setObjectName("reg_password2_label")
        self.verticalLayout_4.addWidget(self.reg_password2_label)
        self.reg_line_passw2 = QtWidgets.QLineEdit(self.reg_tab)
        self.reg_line_passw2.setObjectName("reg_line_passw2")
        self.verticalLayout_4.addWidget(self.reg_line_passw2)
        self.verticalLayout_10.addLayout(self.verticalLayout_4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.save_btn = QtWidgets.QPushButton(self.reg_tab)
        self.save_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.save_btn.setObjectName("save_btn")
        self.verticalLayout_5.addWidget(self.save_btn)
        self.back_btn = QtWidgets.QPushButton(self.reg_tab)
        self.back_btn.setMinimumSize(QtCore.QSize(0, 40))
        self.back_btn.setObjectName("back_btn")
        self.verticalLayout_5.addWidget(self.back_btn)
        self.verticalLayout_10.addLayout(self.verticalLayout_5)
        self.tab_vidget.addTab(self.reg_tab, "")
        self.main_tab = QtWidgets.QWidget()
        self.main_tab.setObjectName("main_tab")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.main_tab)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.scroll_habits = QtWidgets.QScrollArea(self.main_tab)
        self.scroll_habits.setWidgetResizable(True)
        self.scroll_habits.setObjectName("scroll_habits")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 362, 454))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scroll_habits.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_6.addWidget(self.scroll_habits)
        self.add_habit_btn = QtWidgets.QPushButton(self.main_tab)
        self.add_habit_btn.setObjectName("add_habit_btn")
        self.verticalLayout_6.addWidget(self.add_habit_btn)
        self.back_main_btn = QtWidgets.QPushButton(self.main_tab)
        self.back_main_btn.setObjectName("back_main_btn")
        self.verticalLayout_6.addWidget(self.back_main_btn)
        self.verticalLayout_11.addLayout(self.verticalLayout_6)
        self.tab_vidget.addTab(self.main_tab, "")
        self.habit_tab = QtWidgets.QWidget()
        self.habit_tab.setObjectName("habit_tab")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.habit_tab)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.name_habit_label = QtWidgets.QLabel(self.habit_tab)
        self.name_habit_label.setObjectName("name_habit_label")
        self.verticalLayout_7.addWidget(self.name_habit_label)
        self.time_label = QtWidgets.QLabel(self.habit_tab)
        self.time_label.setObjectName("time_label")
        self.verticalLayout_7.addWidget(self.time_label)
        self.scroll_comments_label = QtWidgets.QScrollArea(self.habit_tab)
        self.scroll_comments_label.setWidgetResizable(True)
        self.scroll_comments_label.setObjectName("scroll_comments_label")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 380, 387))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.scroll_comments_label.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_7.addWidget(self.scroll_comments_label)
        self.add_comment_btn = QtWidgets.QPushButton(self.habit_tab)
        self.add_comment_btn.setObjectName("add_comment_btn")
        self.verticalLayout_7.addWidget(self.add_comment_btn)
        self.delete_habit_btn = QtWidgets.QPushButton(self.habit_tab)
        self.delete_habit_btn.setObjectName("delete_habit_btn")
        self.verticalLayout_7.addWidget(self.delete_habit_btn)
        self.back3_main_btn = QtWidgets.QPushButton(self.habit_tab)
        self.back3_main_btn.setObjectName("back3_main_btn")
        self.verticalLayout_7.addWidget(self.back3_main_btn)

        self.verticalLayout_12.addLayout(self.verticalLayout_7)
        self.tab_vidget.addTab(self.habit_tab, "")
        self.verticalLayout.addWidget(self.tab_vidget)
        self.verticalLayout_8.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tab_vidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.reg_btn.clicked.connect(lambda: self.to_reg_tab())
        self.anonim_btn.clicked.connect(lambda: self.to_main_tab())
        self.back_btn.clicked.connect(lambda: self.to_enter_tab())
        self.enter_btn.clicked.connect(lambda: self.enter_check())
        self.save_btn.clicked.connect(lambda: self.save_user())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.enter_log_pas.setText(_translate("MainWindow", "Authorization"))
        self.login_label.setText(_translate("MainWindow", "Enter login:"))
        self.password_label.setText(_translate("MainWindow", "Enter password:"))
        self.reg_success.setText(_translate("MainWindow", ""))
        self.enter_btn.setText(_translate("MainWindow", "Enter"))
        self.reg_btn.setText(_translate("MainWindow", "Registration"))
        self.anonim_btn.setText(_translate("MainWindow", "Anonim enter"))
        self.tab_vidget.setTabText(self.tab_vidget.indexOf(self.enter_tab), _translate("MainWindow", "enter_tab"))
        self.reg_login_label.setText(_translate("MainWindow", "Enter login"))
        self.reg_password_label.setText(_translate("MainWindow", "Enter password"))
        self.reg_password2_label.setText(_translate("MainWindow", "Repeat password"))
        self.save_btn.setText(_translate("MainWindow", "Save"))
        self.back_btn.setText(_translate("MainWindow", "Back to enter"))
        self.tab_vidget.setTabText(self.tab_vidget.indexOf(self.reg_tab), _translate("MainWindow", "reg_tab"))
        self.add_habit_btn.setText(_translate("MainWindow", "PushButton"))
        self.back_main_btn.setText(_translate("MainWindow", "PushButton"))
        self.tab_vidget.setTabText(self.tab_vidget.indexOf(self.main_tab), _translate("MainWindow", "main_tab"))
        self.name_habit_label.setText(_translate("MainWindow", "TextLabel"))
        self.time_label.setText(_translate("MainWindow", "TextLabel"))
        self.add_comment_btn.setText(_translate("MainWindow", "уорцимпоыи"))
        self.delete_habit_btn.setText(_translate("MainWindow", "PushButton"))
        self.back3_main_btn.setText(_translate("MainWindow", "PushButton"))
        self.tab_vidget.setTabText(self.tab_vidget.indexOf(self.habit_tab), _translate("MainWindow", "habit_tab"))

    def to_reg_tab(self):
        self.tab_vidget.setCurrentIndex(1)

    def to_main_tab(self):
        self.tab_vidget.setCurrentIndex(2)

    def to_enter_tab(self):
        self.tab_vidget.setCurrentIndex(0)

    def enter_check(self):
        _translate = QtCore.QCoreApplication.translate
        login = self.login_edit.text()
        password = self.password_edit.text()
        if login in self.users and self.users[login].check_password(password):
            self.to_main_tab()
        else:
            self.reg_success.setText(_translate("MainWindow", "Wrong login or password"))

    def save_user(self):
        _translate = QtCore.QCoreApplication.translate
        login = self.reg_line_login.text()
        first_password = self.reg_line_passw.text()
        second_password = self.reg_line_passw2.text()
        if login not in self.users and first_password == second_password:
            self.users[login] = User(login, first_password)
            self.save_to_file()
            self.reg_success.setText(_translate("MainWindow", "Registration is successful"))
            self.to_enter_tab()
        elif login in self.users:
            self.reg_login_label.setText(_translate("MainWindow", "The username is already occupied"))
        else:
            self.reg_password2_label.setText(_translate("MainWindow", "Passwords don't match"))

    def save_to_file(self):
        with open("data.pkl", "wb") as file:
            pickle.dump(self.users, file)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
