import random


def solve_reasoning_question(temperature):
    """
    Simulated self-consistency experiment.

    At temperature 0, the answer is deterministic.
    At non-zero temperature, different candidate answers
    can be sampled to demonstrate majority voting.
    """

    correct_answer = "30 teams"

    if temperature == 0:
        return correct_answer

    # Simulated candidate outputs
    candidates = [
        "30 teams",
        "30 teams",
        "30 teams",
        "29 teams",
        "31 teams"
    ]

    return random.choice(candidates)


def majority_vote(answers):
    counts = {}

    for answer in answers:
        counts[answer] = counts.get(answer, 0) + 1

    return max(counts, key=counts.get)


if __name__ == "__main__":

    print("SELF-CONSISTENCY EXPERIMENT")
    print("=" * 50)

    # Non-zero temperature
    temperature = 0.7
    runs = 5

    answers = []

    print(f"\nTemperature: {temperature}")
    print(f"Number of runs: {runs}")

    for i in range(runs):
        answer = solve_reasoning_question(temperature)
        answers.append(answer)
        print(f"Run {i + 1}: {answer}")

    final_answer = majority_vote(answers)

    print("\nMAJORITY ANSWER")
    print("-" * 50)
    print(final_answer)

    # Temperature 0
    print("\nTEMPERATURE 0")
    print("-" * 50)

    zero_temperature_answer = solve_reasoning_question(0)

    print(f"Run 1: {zero_temperature_answer}")
    print(f"Run 2: {zero_temperature_answer}")
    print(f"Run 3: {zero_temperature_answer}")
    print(f"Run 4: {zero_temperature_answer}")
    print(f"Run 5: {zero_temperature_answer}")