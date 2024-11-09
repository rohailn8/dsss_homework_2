import random


def generateRandomNumber(minimumNumber: int, maximumNumber: int) -> int:
    """
    Random integer is generated in between the numbers min and max
    """
    if not isinstance(minimumNumber, int) or not isinstance(maximumNumber, int):
        raise ValueError("Both minimumNumber and maximumNumber should be an integer")
    if minimumNumber > maximumNumber:
        raise ValueError("minimumNumber should be less than maximumNumber")
    
    return random.randint(minimumNumber, maximumNumber)


def generateRandomOperator():
    """
    Random operator is generated from the given choices
    """
    return random.choice(['+', '-', '*'])


def calculatorFunction(firstNumber: int, secondNumber: int, operator) -> int:
    """
    Function to calculate the resultant based on the firstNumber, secondNumber and the operator
    """
    equation = f"{firstNumber} {operator} {secondNumber}"
    if operator == '+': 
        answer = firstNumber + secondNumber
    elif operator == '-': 
        answer = firstNumber - secondNumber
    else: 
        answer = firstNumber * secondNumber
    return equation, answer

def math_quiz():
    totalPoints = 0
    # totalQuestions = 3.14159265359. This should have been an integer
    totalQuestions = 3

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(totalQuestions):
        firstNumber = generateRandomNumber(1, 10); 
        # secondNumber = generateRandomNumber(1, 5.5); both numbers should be an integer
        secondNumber = generateRandomNumber(1, 5); 
        operator = generateRandomOperator()

        equation, answer = calculatorFunction(firstNumber, secondNumber, operator)
        print(f"\nQuestion: {equation}")
        userAnswer = input("Your answer: ")
        try:
            userAnswer = int(userAnswer)
        except ValueError:
            raise ValueError("User answer should be in the correct integer format")

        if userAnswer == answer:
            print("Correct! You earned a point.")
            totalPoints += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {totalPoints}/{totalQuestions}")

if __name__ == "__main__":
    math_quiz()
