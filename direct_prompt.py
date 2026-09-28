def direct_prompt(question):
    """
    Direct prompting:
    The model gives a final answer immediately.
    No tool is used and no reasoning process is shown.
    """

    if question == "event_plan":
        return """
DIRECT PROMPTING
==================================================
Event Planning Result

Participants: 120
Team size: 4 participants
Number of teams: 30
Material cost per team: Rs.150
Total material budget: Rs.4,500
Budget limit: Rs.5,000
Budget status: Within the budget

Venue recommendation: Seminar Hall
Reason: It can accommodate 150 participants, which is sufficient for the 120 participants.
"""

    return "I can answer the given event-planning question directly."


if __name__ == "__main__":
    question = "event_plan"
    answer = direct_prompt(question)
    print(answer)