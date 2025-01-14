import json


def load_html_data(file_path):
    with open(file_path, "r") as handle:
        return handle.read()


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)


def write_to_file(data):
    with open("animals.html", "w") as handle:
        return handle.write(data)


def serialize_animal(animal_obj):
    animal_data_string = ""
    name = animal_obj.get("name")
    characteristics = animal_obj.get("characteristics", {})
    diet = characteristics.get("diet")
    location = animal_obj.get("locations", [])[0]
    common_name = characteristics.get("common_name")
    lifespan = characteristics.get("lifespan")
    skin_type = characteristics.get("skin_type")

    animal_type = characteristics.get("type")
    animal_data_string += "<li class='cards__item'>\n"
    animal_data_string += "<div class ='card__title' > "f"{name}</div >\n"
    animal_data_string += "<p class='card__text'>\n"
    animal_data_string += "<ul class = 'card_list'>\n"

    if diet is not None:
        animal_data_string += "<li><strong>Diet:</strong> "f"{diet}</li>\n"
    if location is not None:
        animal_data_string += "<li><strong>Location:</strong> "f"{location}</li>\n"
    if animal_type is not None:
        animal_data_string += "<li><strong>Type:</strong> "f"{animal_type}</li>\n"
    if common_name is not None:
        animal_data_string += "<li><strong>Common Name:</strong> "f"{common_name}</li>\n"
    if lifespan is not None:
        animal_data_string += "<li><strong>Lifespan:</strong> "f"{lifespan}</li>\n"

    animal_data_string += '</ul>\n'
    animal_data_string += '</p>\n'
    animal_data_string += '</li>\n'
    return animal_data_string

def generate_html_data(animals_data):
    return  "".join(serialize_animal(animal) for animal in animals_data)

def main() :
    animal_data_html = load_html_data("animals_template.html")
    animals_data = load_data("animals_data.json")
    animal_data_string = generate_html_data(animals_data)
    new_data = animal_data_html.replace("__REPLACE_ANIMALS_INFO__", animal_data_string)
    print(new_data)
    write_to_file(new_data)



if __name__ == "__main__":
    main()


