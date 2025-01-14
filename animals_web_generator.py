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

def generate_html_data(animals_data):
    animal_data_string = ""
    for animal_data in animals_data:
        name = animal_data.get("name")
        characteristics = animal_data.get("characteristics", {})
        diet = characteristics.get("diet")
        location = animal_data.get("locations", [])[0]
        animal_type = characteristics.get("type")
        animal_data_string += "<li class='cards__item'>\n"
        animal_data_string += "<div class ='card__title' > "f"{name}</div >\n"
        animal_data_string += "<p class='card__text'>\n"
        if diet is not None:
            animal_data_string += "<strong>Diet:</strong> "f"{diet}<br/>\n"
        if location is not None:
            animal_data_string += "<strong>Location:</strong> "f"{location}<br/>\n"
        if animal_type is not None:
            animal_data_string += "<strong>Type:</strong> "f"{animal_type}<br/>\n"
        animal_data_string += '</p>\n'
        animal_data_string += '</li>'
    return animal_data_string







def main() :
    animal_data_html = load_html_data("animals_template.html")
    animals_data = load_data("animals_data.json")
    animal_data_string = generate_html_data(animals_data)
    new_data = animal_data_html.replace("__REPLACE_ANIMALS_INFO__", animal_data_string)
    print(new_data)
    write_to_file(new_data)



if __name__ == "__main__":
    main()


