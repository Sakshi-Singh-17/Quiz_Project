dict1={
    1:{
       "text":"Which data structure follows the LIFO principle?",
       "option":'''  A) Queue
  B) Stack
  C) Array
  D) Linked List''',
       "ans":"B" },

    2:{
        "text" : "What is the time complexity of Binary Search in the worst case?",
        "option" : '''  A) O(n)
  B) O(n log n)
  C) O(log n)
  D) O(1)''',
        "ans" : "B"  },

    3:{
        "text" : "Which SQL command is used to remove a table completely from a database?",
        "option" : '''  A) DELETE
  B) REMOVE
  C) DROP
  D) TRUNCATE''',
        "ans" : "C"  },

    4:{
        "text" : "Which scheduling algorithm may cause starvation?",
        "option" : '''  A) FCFS
  B) Round Robin
  C) Priority Scheduling
  D) FIFO''',
        "ans" : "C" },

    5:{
        "text" : "What is the default port number of HTTP?",
        "option" : '''  A) 21
  B) 80
  C) 443
  D) 25''',
        "ans" : "B" }     
    }


score=0

for i in range(1,6,1):
    print(dict1[i]["text"])
    print(dict1[i]["option"])
    choice=input("Choose the correct option A|B|C|D:  ").upper()
    if dict1[i]["ans"]==choice:
        score += 1
        print(f"Correct answer, your score is {score} out of {i}/5\n")
        print()
       

    else:
        print("Incorrect answer")
        print(f"Correct answer is {dict1[i]['ans']}")
        print(f"Your score is {score} out of {i}/5\n")
       

percent=(score/5)*100
print(f"\nYou have given {score} correct answers ")
print(f"Your total score is {score} and {percent}% ")



