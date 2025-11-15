# scores.py
# Main branch: Only sum and average

def process_scores(scores):
    total = sum(scores)
    average = total / len(scores)
    return total, average


if _name_ == "_main_":
    user_input = input("Enter scores separated by commas: ")
    scores = [float(x.strip()) for x in user_input.split(",")]

    total, average = process_scores(scores)

    print("---- MAIN BRANCH OUTPUT ----")
    print("Scores:", scores)
    print("Sum:", total)
    print("Average:", average)