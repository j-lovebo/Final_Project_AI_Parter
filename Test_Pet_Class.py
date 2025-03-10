from Pet_Class import Pet

# Test 1: Creating a pet with typical attributes
pet1 = Pet("Buddy", "Dog", "Brown", "Friendly")
print("Test 1 - Standard Pet:")
print(f"Name: {pet1.name}, Type: {pet1.pet_type}, Color: {pet1.color}, Personality: {pet1.personality}")

# Test 2: Creating a pet with a different set of attributes
pet2 = Pet("Milo", "Cat", "Gray", "Curious")
print("\nTest 2 - Different Pet:")
print(f"Name: {pet2.name}, Type: {pet2.pet_type}, Color: {pet2.color}, Personality: {pet2.personality}")

#should give 2 pets with different attributes
