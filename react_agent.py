from tools import get_event_information


def react_agent():
    print("REACT AGENT")
    print("=" * 50)

    # Thought
    print("\nTHOUGHT")
    print("I need to calculate the number of teams and material budget.")
    print("I also need venue capacity information before selecting a venue.")

    # Action
    print("\nACTION")
    print("Calling get_event_information()...")

    tool_result = get_event_information()

    # Observation
    print("\nOBSERVATION")
    print(f"Available venues: {tool_result['available_venues']}")
    print(f"Seminar Hall capacity: {tool_result['seminar_hall_capacity']}")
    print(f"Auditorium capacity: {tool_result['auditorium_capacity']}")
    print(
        f"Material cost per team: "
        f"Rs.{tool_result['event_material_cost_per_team']}"
    )

    # Thought
    participants = 120
    team_size = 4

    teams = participants // team_size

    material_cost = (
        teams * tool_result["event_material_cost_per_team"]
    )

    print("\nTHOUGHT")
    print(f"{participants} participants / {team_size} per team = {teams} teams.")
    print(
        f"{teams} teams × "
        f"Rs.{tool_result['event_material_cost_per_team']} "
        f"= Rs.{material_cost}."
    )

    if tool_result["seminar_hall_capacity"] >= participants:
        selected_venue = "Seminar Hall"
    else:
        selected_venue = "Auditorium"

    # Final Answer
    print("\nFINAL ANSWER")
    print("-" * 50)
    print(f"Number of teams: {teams}")
    print(f"Total material budget: Rs.{material_cost}")
    print("Budget limit: Rs.5,000")
    print(
        "Budget status:",
        "Within the budget" if material_cost <= 5000 else "Over the budget"
    )
    print(f"Selected venue: {selected_venue}")


if __name__ == "__main__":
    react_agent()