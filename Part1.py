def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"I have a {animal_type} and its name is {pet_name}.")

# Call the function three times with different animals and names
describe_pet(animal_type="hamster", pet_name="Harry")
describe_pet(pet_name="Lucy", animal_type="Rabbit")
describe_pet("Bird", "Bella")