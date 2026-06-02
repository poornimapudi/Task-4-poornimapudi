# General Knowledge Quiz Game

# Variable to keep track of the user's score
score = 0

# Welcome message
print("===================================")
print("   Welcome to the GK Quiz Game")
print("===================================\n")

# Question 1
print("Q1. What is the capital of Bihar?")
answer = input("Your Answer: ")

# Check whether the answer is correct
if answer.lower() == "patna":
    print("Correct Answer!\n")
    score += 1
else:
    print("Wrong Answer.\nCorrect Answer: Patna\n")

# Question 2
print("Q2. Which planet is known as the Red Planet?")
answer = input("Your Answer: ")

# Check the answer
if answer.lower() == "mars":
    print("Correct Answer!\n")
    score += 1
else:
    print("Wrong Answer.\nCorrect Answer: Mars\n")

# Question 3
print("Q3. How many continents are there in the world?")
answer = input("Your Answer: ")

# Check the answer
if answer == "7":
    print("Correct Answer!\n")
    score += 1
else:
    print("Wrong Answer.\nCorrect Answer: 7\n")

# Question 4
print("Q4. What is the hardest natural substance on Earth?")
answer = input("Your Answer: ")

# Check the answer
if answer.lower() == "diamond":
    print("Correct Answer!\n")
    score += 1
else:
    print("Wrong Answer.\nCorrect Answer: Diamond\n")

# Question 5
print("Q5. Which is the largest ocean in the world?")
answer = input("Your Answer: ")

# Check the answer
if answer.lower() == "pacific ocean" or answer.lower() == "pacific":
    print("Correct Answer!\n")
    score += 1
else:
    print("Wrong Answer.\nCorrect Answer: Pacific Ocean\n")

# Display final score
print("===================================")
print("          Quiz Completed")
print("===================================")

print(f"Your Score: {score}/5")

# Display performance based on score
if score == 5:
    print("Excellent! You got all answers correct.")
elif score >= 3:
    print("Good Job! Keep improving your knowledge.")
else:
    print("Keep Learning! You can do better next time.")