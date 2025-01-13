import json


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


def generate_html_data(animals_data):
    for animal_data in animals_data:
        name = animal_data.get("name")
        characteristics = animal_data.get("characteristics", {})
        diet = characteristics.get("diet")
        location = animal_data.get("locations", [])[0]
        animal_type = characteristics.get("type")
        if name is not None:
            print(f"Name: {name}")
        if diet is not None:
            print(f"Diet: {diet}")
        if location is not None:
            print(f"Location: {location}")
        if animal_type is not None:
            print(f"Type: {animal_type}")







def main() :
    animals_data = load_data("animals_data.json")
    generate_html_data(animals_data)


if __name__ == "__main__":
    main()

