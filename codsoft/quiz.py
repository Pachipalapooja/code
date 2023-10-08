import random

# Quiz questions and answers
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer": "Paris",
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Jupiter", "Saturn"],
        "correct_answer": "Mars",
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Giraffe", "Blue Whale", "Hippopotamus"],
        "correct_answer": "Blue Whale",
    },
]

def display_welcome_message():
    print("Welcome to the Quiz Game!")
    print("You will be asked multiple-choice questions. Let's test your knowledge!\n")

def ask_question(question_data):
    print(question_data["question"])
    for i, option in enumerate(question_data["options"], start=1):
        print(f"{i}. {option}")
    
    user_answer = input("Your answer (Enter the number corresponding to your choice): ")
    return int(user_answer)

def evaluate_answer(question_data, user_answer):
    correct_answer = question_data["correct_answer"]
    if user_answer == correct_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Sorry, that's incorrect. The correct answer is {correct_answer}.\n")
        return False

def play_quiz(quiz_data):
    score = 0
    total_questions = len(quiz_data)

    for question_data in random.sample(quiz_data, total_questions):
        user_choice = ask_question(question_data)
        is_correct = evaluate_answer(question_data, user_choice)
        
        if is_correct:
            score += 1

    return score

def display_final_results(score, total_questions):
    print(f"You've completed the quiz!")
    print(f"Your score: {score}/{total_questions}")
    if score == total_questions:
        print("Congratulations! You got all the questions correct.")
    else:
        print("Good effort!")

def play_again():
    return input("Do you want to play again? (yes/no): ").lower().strip() == "yes"

if __name__ == "__main__":
    while True:
        display_welcome_message()
        user_score = play_quiz(quiz_data)
        display_final_results(user_score, len(quiz_data))
        play_again_response = play_again()
        
        if not play_again_response:
            print("Thank you for playing! Goodbye!")
            break
