questions = [
  
    ["What is the capital of India?", "New Delhi", "Kolkata", "Mumbai", "Chennai", 1],
    ["What is the largest planet in our Solar System?", "Earth", "Mars", "Jupiter", "Saturn", 3],
    ["What is the chemical symbol for water?", "HO", "H2O", "H2", "OH", 2],
    ["Who wrote 'To Kill a Mockingbird'?", "Harper Lee", "Mark Twain", "Jane Austen", "Ernest Hemingway", 1],
    ["Which element has the atomic number 1?", "Oxygen", "Helium", "Hydrogen", "Nitrogen", 3],
    ["Which country is known as the Land of the Rising Sun?", "China", "Thailand", "Japan", "South Korea", 3],
    ["What is the smallest prime number?", "1", "2", "3", "5", 2],
    ["In which year did the Titanic sink?", "1910", "1912", "1914", "1916", 2],
    ["What is the capital city of Australia?", "Sydney", "Melbourne", "Perth", "Canberra", 4],
    ["Which planet is known as the Red Planet?", "Mercury", "Venus", "Earth", "Mars", 4]
] 



levels = [1000, 2000, 3000, 10000, 20000, 40000, 
80000, 160000, 320000, 10000000]
money = 0


i = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"Question for Rs. {levels[i]}")
    print(f"a. {question[1]}      a. {question[2]}")
    print(f"c. {question[3]}      b. {question[4]}")
    reply = int(input("Enter your answer (1-4) or 0 to quit" ))
    if (reply == 0):
        money = levels[i-1]
        break
    if(reply == question[-1]):
        print(f"Correct answer, you have won Rs. {levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000       
    else:
        print("Wrong answer!")
        break 

print(f"your take home money is {money}")            

