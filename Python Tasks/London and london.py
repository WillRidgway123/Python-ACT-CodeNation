print("What is the capital of England?") 

answer = input("type answer here >>").lower()

if answer == "London":
    print(f"Correct! The answer is {answer}")
elif answer == "london":
    print(f"Correct! The answer is {answer}")
else:
    print(f"Incorrect,the answer is london, not {answer}")