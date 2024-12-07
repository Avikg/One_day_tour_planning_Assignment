# Test Saving Preferences
neo4j_agent.save_preference("user123", "city", "Berlin")
neo4j_agent.save_preference("user123", "budget", "100")

# Test Retrieving Preferences
preferences = neo4j_agent.get_preferences("user123")
print(preferences)  # Output: {'city': 'Berlin', 'budget': '100'}
