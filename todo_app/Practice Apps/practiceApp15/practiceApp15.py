import json

with open ('todo_app/practiceApp15/questions.json', 'r') as file:
    content = file.read()

data = json.loads(content)


for question in data:
    print(question['question_text'])
    for index, alternative in enumerate(question['alternative']):
        print(f"{index + 1} - {alternative}")
    user_choice = int(input("Enter your choice (#): "))
    question['user_choice'] = user_choice

score = 0

for index, question in enumerate(data):
    if question['user_choice'] == question['correct answer']:
        score = score + 1
        result = "Correct"
    else:
        result = "Incorrect"
    message = f"{index + 1} - Your answer: {question['user_choice']}, Correct answer: {question['correct answer']}...{result}``"
    print(message)

print(score, "/ ", len(data))