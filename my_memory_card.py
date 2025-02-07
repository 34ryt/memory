#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QButtonGroup, QMessageBox, QPushButton, QRadioButton, QVBoxLayout, QHBoxLayout, QLabel, QGroupBox
from random import randint, shuffle
# генерация приложения
app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.resize(400, 200)
# классы и списки
class Question():
    def __init__(self, question, right_answer, wr1, wr2, wr3):
        self.question_text = question
        self.right_answer = right_answer
        self.wr1 = wr1
        self.wr2 = wr2
        self.wr3 = wr3
questions_list = list()
main_win.cur_question = -1
questions_list.append(Question('Какой национальности не существует?', 'Смурфы', 'Энцы', 'Чулымцы', 'Алеуты'))
questions_list.append(Question('Какого цвета нету в флаге РФ?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Официальный язык в ОАЭ?', 'Арабский', 'Русский', 'Английский', 'Чероки'))
questions_list.append(Question('Когда была создана Москва?', '1147', '2010', '1345', '9999'))
questions_list.append(Question('Что изображено на флаге Казахстана?', 'Солнце и орёл', 'Триколор (белый-синий-красный)', 'Желтая звезда на красном полотне', 'Красное полотно с 5 звёздочками'))
questions_list.append(Question('Столица Эфиопии?', 'Аддис-Абеба', 'Иерусалим', 'Минск', 'Лондон'))
questions_list.append(Question('Герб России?', 'Двухглавый Орёл', 'Георгий Победоносец', 'Иркутская Куница', 'Русский Лев'))
questions_list.append(Question('Национальность Татарстана?', 'Татары', 'Башкиры', 'Американцы', 'Эфиопы'))
questions_list.append(Question('Кто НЕ живёт в России?', 'Таджики', 'Россияне', 'Тувинцы', 'Алеуты'))
questions_list.append(Question('Какое(-ая) животное/птица не водится в России?', 'Обезьяна', 'Медведь', 'Заяц', 'Синица'))
# создание вопроса
question = QLabel('Какой национальности не существует?')
RadioGroupBox = QGroupBox('Варианты ответа')
ans1 = QRadioButton('Энцы') 
ans2 = QRadioButton('Чулымцы') 
ans3 = QRadioButton('Смурфы') 
ans4 = QRadioButton('Алеуты') 
answer = QPushButton('Ответить')
answers = [ans1, ans2, ans3, ans4]
layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout()
layout_ans3 = QVBoxLayout()
layout_ans4 = QHBoxLayout()
layout_ans5 = QHBoxLayout()
main_layout = QVBoxLayout()
ButtonGroup = QButtonGroup()
ButtonGroup.addButton(ans1)
ButtonGroup.addButton(ans2)
ButtonGroup.addButton(ans3)
ButtonGroup.addButton(ans4)
# счётчики
main_win.right = 0
main_win.total = 0
# ответить/следующий вопрос
def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    answer.setText('Следующий вопрос')
def show_question():
    AnsGroupBox.hide()
    RadioGroupBox.show()
    answer.setText('Ответить')
    ButtonGroup.setExclusive(False)
    ans1.setChecked(False)
    ans2.setChecked(False)
    ans3.setChecked(False)
    ans4.setChecked(False)
    ButtonGroup.setExclusive(True)
def start_test():
    if answer.text() == 'Ответить':
        show_result()
    else:
        show_question()
def next_question():
    cur_question = randint(0, len(questions_list) - 1)
    q = questions_list[cur_question]
    main_win.total += 1
    ask(q)
def click_ok():
    if answer.text() == 'Ответить':
        check_answer()
    else:
        next_question()
# генератор викторины
def ask(q: Question):
    shuffle(answers)
    question.setText(q.question_text)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wr1)
    answers[2].setText(q.wr2)
    answers[3].setText(q.wr3)
    correct.setText(q.right_answer)
    show_question()
def check_answer():
    if answers[0].isChecked():
        main_win.right += 1
        show_correct('Правильно!')
    else:
        show_correct('Неправильно!')
def show_correct(res):
    result.setText(res)
    print('Статистика', '\n-Всего вопросов:', main_win.total, '\n-Правильных ответов:', main_win.right, '\nРейтинг:', main_win.right/main_win.total*100, '%')
    show_result()
answer.clicked.connect(click_ok)
# результаты
AnsGroupBox = QGroupBox('Результат теста')
result = QLabel('Правильно/Неправильно')
correct = QLabel('Правильный ответ')
layout_ans6 = QVBoxLayout()
layout_ans6.addWidget(result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_ans6.addWidget(correct, alignment = Qt.AlignHCenter)
AnsGroupBox.setLayout(layout_ans6)
# расположение лэйаутов (ответы)
layout_ans2.addWidget(ans1, alignment = Qt.AlignCenter)
layout_ans2.addWidget(ans2, alignment = Qt.AlignCenter)
layout_ans3.addWidget(ans3, alignment = Qt.AlignCenter)
layout_ans3.addWidget(ans4, alignment = Qt.AlignCenter)
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)
RadioGroupBox.setLayout(layout_ans1)
# расположение лэйаутов (основное)
layout_ans4.addWidget(question, alignment = Qt.AlignCenter)
layout_ans5.addStretch(1)
layout_ans5.addWidget(answer, stretch = 2)
layout_ans5.addStretch(1)
main_layout.addLayout(layout_ans4)
main_layout.addWidget(RadioGroupBox, alignment = Qt.AlignCenter)
main_layout.addWidget(AnsGroupBox, alignment = Qt.AlignCenter)
main_layout.addLayout(layout_ans5)
main_layout.setSpacing(5)
# исчезновение РадиоГрупБокса
RadioGroupBox.hide()
# показ приложения + вопросы
next_question()
main_win.setLayout(main_layout)
main_win.show()
app.exec_()