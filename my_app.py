from PyQt6 import QtWidgets, uic
import sys
#dsfdsfdsf
def format_month_string(months):
    if months == 1:
        return "1 месяц"
    elif 2 <= months <= 4:
        return f"{months} месяца"
    else:
        return f"{months} месяцев"

def format_year_string(years):
    if years == 1:
        return "1 год"
    elif 2 <= years <= 4:
        return f"{years} года и"
    elif  years%10 == 1 and years!=11:
        return f"{years} год и"
    else:
        return f"{years} лет и"

class MyWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setFixedSize(550, 300)
        self.setWindowTitle('Пример обработки данных от пользователя')
        self.setGeometry(100, 100, 300, 200)

        uic.loadUi("money.ui", self)

        # Подключаем обработчики к сигналам textChanged для каждого QLineEdit
        self.lineEdit.textChanged.connect(self.on_lin1)
        self.lineEdit_2.textChanged.connect(self.on_lin2)
        self.lineEdit_3.textChanged.connect(self.on_lin3)
        self.lineEdit_4.textChanged.connect(self.on_lin4)

        # Подключаем обработчик к нажатию кнопки
        self.pushButton.clicked.connect(self.calculate_time_to_save)

        # Переменные для хранения введенных чисел
        self.number1 = 0
        self.number2 = 0
        self.number3 = 0
        self.number4 = 0

    def on_lin1(self, text):
        # Этот метод вызывается при изменении текста в lineEdit_1
        try:
            self.number1 = int(text)
        except ValueError:
            self.number1 = 0

    def on_lin2(self, text):
        # Этот метод вызывается при изменении текста в lineEdit_2
        try:
            self.number2 = int(text)
        except ValueError:
            self.number2 = 0

    def on_lin3(self, text):
        # Этот метод вызывается при изменении текста в lineEdit_3
        try:
            self.number3 = int(text)
        except ValueError:
            self.number3 = 0

    def on_lin4(self, text):
        # Этот метод вызывается при изменении текста в lineEdit_4
        try:
            self.number4 = int(text)
        except ValueError:
            self.number4 = 0

    def calculate_time_to_save(self):
        current_money = self.number1
        monthly_income = self.number2
        savings_percentage = self.number3
        target_purchase = self.number4

        if current_money >= target_purchase:
            self.lineEdit_5.setText("У вас уже достаточно денег для покупки!")
            return

        total_savings = current_money
        months = 0

        while total_savings < target_purchase:
            total_savings += monthly_income * (savings_percentage / 100)
            months += 1

            # Увеличиваем сумму, если после окончания года не хватает денег
            if months % 12 == 0 and total_savings < target_purchase:
                total_savings += monthly_income * (savings_percentage / 100)

        years = months // 12
        remaining_months = months % 12

        result_string = "Для суммы {} :".format(target_purchase)
        if years > 0:
            result_string += " " + format_year_string(years)
        if remaining_months > 0:
            result_string += " " + format_month_string(remaining_months)

        self.lineEdit_5.setText(result_string)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
