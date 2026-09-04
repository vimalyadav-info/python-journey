#Build an RPG Character

def create_character(name, strength, intelligence, charisma):

    # Name must be a string
    if not isinstance(name, str):
        return "The character name should be a string"

    # Name cannot be empty
    if name == "":
        return "The character should have a name"

    # Name cannot be longer than 10 characters
    if len(name) > 10:
        return "The character name is too long"

    # Name cannot contain spaces
    if " " in name:
        return "The character name should not contain spaces"

    # All stats must be integers
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"

    # Stats cannot be less than 1
    if strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"

    # Stats cannot be greater than 4
    if strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"

    # Stats must total 7
    if strength + intelligence + charisma != 7:
        return "The character should start with 7 points"

    # Create stat bars
    strength_bar = "●" * strength + "○" * (10 - strength)
    intelligence_bar = "●" * intelligence + "○" * (10 - intelligence)
    charisma_bar = "●" * charisma + "○" * (10 - charisma)

    return (
        f"{name}\n"
        f"STR {strength_bar}\n"
        f"INT {intelligence_bar}\n"
        f"CHA {charisma_bar}"
    )


print(create_character("ren", 4, 2, 1))