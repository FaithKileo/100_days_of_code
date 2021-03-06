from qn_model import Question
from data import question_data 
from quiz_brain import QuizBrain

question_bank = []
for data in question_data:
    
    q_text = data["text"]
    q_answer = data["answer"]
    new_question = Question(q_text, q_answer)
    question_bank.append(new_question)
    
quiz = QuizBrain(question_bank)    

while quiz.still_has_questions():
    quiz.next_question() 
    
print("You have completed your quiz.")
print(f"Your toal score is: {quiz.score}/{len(question_bank)}")