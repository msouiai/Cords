import pandas as pd

def process_cords_content(cords_content):
    print("Processing Cord Content")

def read_cords_file(cord_file_name):
    #print("Reading the following Cords File")
    #print(cord_file_name)
    # Opening file but its not read yet
    file = open(cords_file_name,'r')
    # Reading the file
    # Marcos Magic ***********
    for line in file:
        if cord_we_are_looking_for in line:
            print(f'Esse e o seu campo harmonico = ', line)
    file.close()
    """
    x = pd.read_excel('/Users/marcosvmsa/Cords/Acordes_e_Harmonia.xlsx', engine='openpyxl')
    if cord_we_are_looking_for == x.iloc[29, 2]:
        print(x.iloc[29, 2:9])
        print(x.index)
    else:
        print(f'Esse acord {cord_we_are_looking_for} nao e valido ')
    #tb = pd.read_excel('Acordes_e_Harmonia.xlsx')
    """

def read_cords(cord_file_name):
    #print("Reading Cords")
    # We are reading the file hereC7+

    cords_content = read_cords_file(cord_file_name)
    # Alright we have the content
    process_cords_content(cords_content)

#def look_for_the_line_where_the_cord_is(cord_we_are_looking_for):
        # print(cord_we_are_looking_for)
        #print("procurar o acord na lista ")


cords_file_name = "simple_acordes_e_harmonia.txt"
cord_we_are_looking_for = str(input('Digite o Acorde = '))
#look_for_the_line_where_the_cord_is(cord_we_are_looking_for)
read_cords(cords_file_name)


