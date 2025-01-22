from data_fetcher import fetch_data


WEBSITE_FILE_NAME = "animals.html"
TEMPLATE_FILE_NAME = "animals_template.html"


def load_html_data(file_path):
    """
    This fn reads the "animal_template.html" file.
    :param file_path:
    :return: file content
    """
    with open(file_path, "r") as handle:
        return handle.read()


def write_to_file(data, file_name):
    """
    This fn writes into "animals.html" file .
    :param file_name:
    :param data:
    """
    with open(file_name, "w") as handle:
        handle.write(data)


def serialize_animal(animal_obj):
    """
    This fn iterates through the animal_obj and extract the
    required data and formulates,serialized data ready to be written into
    "animals.html" file .
    :param animal_obj:
    :return: file content
    """
    animal_data_string = ""
    name = animal_obj.get("name")
    characteristics = animal_obj.get("characteristics", {})
    diet = characteristics.get("diet")
    location = animal_obj.get("locations", [])
    common_name = characteristics.get("common_name")
    lifespan = characteristics.get("lifespan")
    animal_type = characteristics.get("type")

    animal_data_string += "<li class='cards__item'>\n"
    animal_data_string += "<div class ='card__title' > "f"{name}</div >\n"
    animal_data_string += "<p class='card__text'>\n"
    animal_data_string += "<ul class = 'card_list'>\n"

    if diet is not None:
        animal_data_string += "<li><strong>Diet:</strong> "f"{diet}</li>\n"
    if len(location)>0:
        animal_data_string += "<li><strong>Location:</strong> "f"{location[0]}</li>\n"
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


def website_generator(website_template, animal_data_string):
    """
    This fn adds animal data into the template file which is used to
    generate the final website file .
    :param website_template:
    :param animal_data_string:
    """
    website_content = website_template.replace("__REPLACE_ANIMALS_INFO__",
                                               animal_data_string)
    write_to_file(website_content, WEBSITE_FILE_NAME)
    print(f"Website was successfully generated to the file "
          f"{WEBSITE_FILE_NAME}.")


def main() :
    """
    This is the main function through which the sub functions get invoked .
    """
    website_template = load_html_data(TEMPLATE_FILE_NAME)
    animal_name = input("Please enter the animal name: ")
    animals_data = fetch_data(animal_name)
    if animals_data :
        animal_data_string = generate_html_data(animals_data)
    else :
        animal_data_string= f"<h2>The animal {animal_name} doesn't exist.</h2>"
    website_generator(website_template, animal_data_string)


if __name__ == "__main__":
    main()