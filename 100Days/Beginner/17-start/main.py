from model_questions import Questions
from data import questions_data
from quiz_brain import QuizBrain

question_bank = []
for question in questions_data:
    question_text = question["text"]
    question_answer = question["answer"]
    question_bank.append(Questions(question_text, question_answer))


for item in question_bank:
    print(item.text)  
    print(f'Respuesta {item.answer}')



quiz = QuizBrain(question_bank)


while quiz.still_ass_question():
    quiz.nex_question()
    