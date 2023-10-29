#create a memory card application
#connect libraries
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QRadioButton, QHBoxLayout, QGroupBox, QButtonGroup
from random import shuffle,randint

class Question(): 
    def __init__ (self,textq,rquestion,wquestion1,wquestion2,wquestion3):
        self.textq = textq
        self.rquestion = rquestion
        self.wquestion1 = wquestion1
        self.wquestion2 = wquestion2
        self.wquestion3 = wquestion3
#create app and window 
app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle("Memory Card")
#create the widgets of the main window
questions = QLabel("Which nationality does not exist?")
RadioGroupBox = QGroupBox("Answer options")
answer1 = QRadioButton('Enets')
answer2 = QRadioButton('Chulyms')
answer3 = QRadioButton('Smurfs')
answer4 = QRadioButton('Aleuts')
RadioGroups = QButtonGroup()
RadioGroups.addButton(answer1)
RadioGroups.addButton(answer2)
RadioGroups.addButton(answer3)
RadioGroups.addButton(answer4)
answer_button = QPushButton("Answer")
answer_GroupBox = QGroupBox("Test result")
tf = QLabel("True/False")
correct_ans = QLabel("Correct answer")
layoutV3 = QVBoxLayout()
layoutV3.addWidget(tf, alignment = Qt.AlignLeft)
layoutV3.addWidget(correct_ans, alignment = Qt.AlignHCenter)
answer_GroupBox.setLayout(layoutV3)
#locate the widgets according to the layouts
layoutH1 = QHBoxLayout()
layoutV1 = QVBoxLayout()
layoutV2 = QVBoxLayout()

layoutV1.addWidget(answer1, alignment = Qt.AlignVCenter)
layoutV2.addWidget(answer2, alignment = Qt.AlignVCenter)
layoutV1.addWidget(answer3, alignment = Qt.AlignVCenter)
layoutV2.addWidget(answer4, alignment = Qt.AlignVCenter)
layoutH1.addLayout(layoutV1)
layoutH1.addLayout(layoutV2)

RadioGroupBox.setLayout(layoutH1)

v_line = QVBoxLayout()
v_line.addWidget(questions)
v_line.addWidget(RadioGroupBox)
v_line.addWidget(answer_GroupBox)
v_line.addWidget(answer_button, stretch = 3)
answer_GroupBox.hide()
my_win.setLayout(v_line)

#handling switch clicks
def show_result():
    RadioGroupBox.hide()
    answer_GroupBox.show()
    answer_button.setText("Next question")
def show_question():
    answer_GroupBox.hide()
    RadioGroupBox.show()
    answer_button.setText("Answer")
    RadioGroups.setExclusive(False)    
    answer1.setChecked(False)
    answer2.setChecked(False)
    answer3.setChecked(False)
    answer4.setChecked(False)
    RadioGroups.setExclusive(True) 
def start_test():
    if answer_button.text() == "Answer":
        check_answer()
    else:
        next_question()
answers = [answer1, answer2, answer3, answer4]
def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.rquestion)
    answers[1].setText(q.wquestion1)
    answers[2].setText(q.wquestion2)
    answers[3].setText(q.wquestion3)
    questions.setText(q.textq)
    correct_ans.setText(q.rquestion)
    show_question()
def check_answer():
    if answers[0].isChecked():
        tf.setText("Correct!!!")
        my_win.score += 1
    else:
        tf.setText("Not correct. The correct answer is ")
    show_result()
    print("Statistics")
    print("-Total question: ", my_win.total)
    print("-Correct aswers: ", my_win.score)
    print("Rating  %.2f"%( my_win.score / my_win.total * 100))
def next_question():
    current_question = randint(0, len(question_list) - 1 )
    q = question_list[current_question]
    ask(q)
    my_win.total += 1
#show the app window
question_list = []
q1 = Question("Who is the winner of the FIFA WorldCup 2018?", "France", "Argentina", "Brazil", "Portugal")
question_list.append(q1)
q2 = Question("What is the smallest country in the world", "Vatican City", "Monaco", "Nauru", "Tuvalu")
question_list.append(q2)
q3 = Question("What is the most played sport in the world", "Football", "Swimming", "Basketball", "Badminton")
question_list.append(q3)
q4 = Question("What is the most liked color in the world?", "Blue", "Yellow", "Red", "Purple")
question_list.append(q4)
q5 = Question("What is the rarest eye color", "Green", "Blue", "Brown", "Black")
question_list.append(q5)
q6 = Question("What is the most common blood type?", "Group O", "Group AB", "Group A", "Group B")
question_list.append(q6)
q7 = Question("what is the population of Thailand in 2021?", "71.6 m", "97.47 m", "67.39 m", "33.57 m")
question_list.append(q7)
q8 = Question("What is the year that World War II ended", "1945", "1925", "1935", "1975")
question_list.append(q8)
q9 = Question("WHat is the capital city of Switzerland?", "Bern", "Stockholm", "Canberra", "Reykjavik")
question_list.append(q9)
q10 = Question("How many layers those the earth atmosphere have?", "5 Layers", "4 Layers", "6 Layers", "7 Layers")
question_list.append(q10)
my_win.score = 0
my_win.total = 0
next_question()
answer_button.clicked.connect(start_test)

my_win.show()
app.exec_()