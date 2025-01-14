import json


def load_html_data(file_path):
    """
    This fn reads the "animal_template.html" file .
    :param file_path:
    :return: file content
    """
    with open(file_path, "r") as handle:
        return handle.read()


def load_data(file_path):
    """
    This fn reads the "animal_data.json" file .
    :param file_path:
    :return: file content
    """
    with open(file_path, "r") as handle:
        return json.load(handle)


def write_to_file(data):
    """
    This fn writes into "animals.html" file .
    :param data:
    """
    with open("animals.html", "w") as handle:
        handle.write(data)


def serialize_animal(animal_obj):
    """
    This fn iterates through the animal_obj and extract the required data and formulates,
    serialized data ready to be written into "animals.html" file .
    :param animal_obj:
    :return: file content
    """
    animal_data_string = ""
    name = animal_obj.get("name")
    characteristics = animal_obj.get("characteristics", {})
    diet = characteristics.get("diet")
    location = animal_obj.get("locations", [])[0]
    common_name = characteristics.get("common_name")
    lifespan = characteristics.get("lifespan")
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
    """
    This fn act as a wrapper fn for the function  serialize_animal.
    :param animals_data:
    """
    return  "".join(serialize_animal(animal) for animal in animals_data)


def main() :
    """
    This is the main function through wich the sub functions get invoked .
    """

    animal_data_html = load_html_data("animals_template.html")
    animals_data = load_data("animals_data.json")
    animal_data_string = generate_html_data(animals_data)
    new_data = animal_data_html.replace("__REPLACE_ANIMALS_INFO__", animal_data_string)
    write_to_file(new_data)


if __name__ == "__main__":
    main()