def chain_of_thought(question):
    """
    Chain-of-Thought:
    Performs a multi-step reasoning process before producing
    the final answer. No external tool is used.
    """

    if question == "event_plan":
        reasoning_steps = [
            "Step 1: Identify the total number of participants: 120.",
            "Step 2: Divide participants by 4 members per team: 120 / 4 = 30 teams.",
            "Step 3: Calculate material cost: 30 × Rs.150 = Rs.4,500.",
            "Step 4: Compare Rs.4,500 with the Rs.5,000 budget limit.",
            "Step 5: Rs.4,500 is within the Rs.5,000 budget.",
            "Step 6: Select a suitable venue based on the available capacity."
        ]

        print("CHAIN-OF-THOUGHT")
        print("=" * 50)

        for step in reasoning_steps:
            print(step)

        print("\nFINAL ANSWER")
        print("-" * 50)
        print("30 teams are required.")
        print("The total material budget is Rs.4,500.")
        print("The plan is within the Rs.5,000 budget.")
        print("A venue with at least 120 capacity is required.")

        return


if __name__ == "__main__":
    chain_of_thought("event_plan")