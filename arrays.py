# scores.py
# Local branch: Added max and min functionality

def process_scores(scores):
    total = sum(scores)
    average = total / len(scores)
    maximum = max(scores)
    minimum = min(scores)

    return total, average, maximum, minimum


if _name_ == "_main_":
    user_input = input("Enter scores separated by commas: ")
    scores = [float(x.strip()) for x in user_input.split(",")]

    total, average, maximum, minimum = process_scores(scores)

    print("---- LOCAL BRANCH OUTPUT ----")
    print("Scores:", scores)
    print("Sum:", total)
    print("Average:", average)
    print("Maximum:", maximum)
    print("Minimum:", minimum)