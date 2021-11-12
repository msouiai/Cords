def process_cords_content(cords_content):
    print("Processing Cord Content")

def read_cords_file(cord_file_name):
    print("Reading the following Cords File")
    print(cord_file_name)
    # Opening file but its not read yet
    file = open(cords_file_name,'r')
    # Reading the file
    # Marcos Magic ***********


def read_cords(cord_file_name):
    print("Reading Cords")
    # We are reading the file here
    cords_content = read_cords_file(cord_file_name)
    # Alright we have the content
    process_cords_content(cords_content)

def look_for_the_line_where_the_cord_is(cord_we_are_looking_for):
    print("procurar o acord na lista ")
    print(cord_we_are_looking_for)

    
cords_file_name = "simple_acordes_e_harmonia.txt"
cord_we_are_looking_for = "C7+"
look_for_the_line_where_the_cord_is(cord_we_are_looking_for)
#read_cords(cords_file_name)


