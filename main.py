from functions import execute_query

def get_heroes_and_villains_relationships():
    # Copy the provided SQL query here
    # Ensure you import the execute_query function and other necessary modules if any
    pass  # Placeholder to avoid indentation issues, replace with the actual query

if __name__ == "__main__":
    relationships_data = get_heroes_and_villains_relationships()

    # Process the retrieved data as needed
    for row in relationships_data:
        hero_name = row[0]
        villain_name = row[1]
        relationship_type = row[2]
        ability = row[3]

        # Do whatever you need with the data, e.g., print it
        print(f"Hero: {hero_name}, Villain: {villain_name}, Relationship: {relationship_type}, Ability: {ability}")
