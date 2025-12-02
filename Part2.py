def describe_pet(animal_type, pet_name):
    
    print(f"I have a {animal_type} and its name is {pet_name}.")

# Using positional arguments
describe_pet("dog", "Buddy")

# Using keyword arguments (reverse the order)
describe_pet(pet_name="Milo", animal_type="cat")
