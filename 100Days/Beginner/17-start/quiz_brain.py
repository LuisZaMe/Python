class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list =  q_list
        self.gods = 0

    def still_ass_question(self):
        return self.question_number < len(self.question_list)

    def nex_question(self):
        
        current_question =self.question_list[self.question_number]
        self.question_number += 1
        response = input(f'Q {self.question_number}. {current_question.text} (True/False)')

        print(f'La respuesta es: {current_question.answer}')
        if response == current_question.answer:
            print(f'Correcto')
            self.gods += 1
        else:
            print(f'Fallaste bro')

    print(f'Respuestas buenas {self.gods}')