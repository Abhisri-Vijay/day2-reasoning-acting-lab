def get_event_information():
    """
    Simulated external information tool.
    In a real agent, this could be replaced by a web search,
    database lookup, or external API.
    """

    return {
        "venue_capacity": 150,
        "available_venues": ["Seminar Hall", "Auditorium"],
        "seminar_hall_capacity": 150,
        "auditorium_capacity": 500,
        "event_material_cost_per_team": 150
    }


if __name__ == "__main__":
    information = get_event_information()

    print("External Tool Result")
    print("--------------------")
    for key, value in information.items():
        print(f"{key}: {value}")