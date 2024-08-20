import spacy
import urllib

nlp = spacy.load("en_core_web_md")
minimum_similarity = 0.75

# Fit on body (measurements, size, relaxed, taper, flared, etc.)


# Brand/Designer
def find_brand(action):
    category_file = "none"
    designers_non_alphabet = 0

    # determine which category to search in
    if nlp(action).similarity(nlp("brands")) >= minimum_similarity or nlp(action).similarity(nlp("designers")) >= minimum_similarity:
        category = input("Would you like to find designers in menswear, womenswear, or everything else?: ")

        if nlp(category).similarity(nlp("menswear")) >= minimum_similarity or nlp(action).similarity(nlp("mens")) >= minimum_similarity:
            category_file = "menswear_designers.txt"
            designers_non_alphabet = 16

        elif nlp(category).similarity(nlp("womenswear")) >= minimum_similarity or nlp(action).similarity(nlp("womens")) >= minimum_similarity:
            category_file = "womenswear_designers.txt"
            designers_non_alphabet = 16

        elif nlp(category).similarity(nlp("everything else")) >= minimum_similarity or nlp(action).similarity(nlp("other")) >= minimum_similarity:
            category_file = "misc_items_designers.txt"
            designers_non_alphabet = 9

            
        # exit condition
        elif nlp(category).similarity(nlp("exit")) >= minimum_similarity or nlp(action).similarity(nlp("escape")) >= minimum_similarity:
            return

        #recursively call the function if input does not fall into buckets
        else:
            print("Sorry, I don't understand. Try \"mens\", \"womens\", \"other\", or \"exit\".")
            new_input = input("Would you like to find a designer in menswear, womenswear, or everything else?: ")
            find_brand(new_input)
            return

        #determine what portion of designers to show
        list_filter = input("Would you like to see \"all designers\", or only those starting with a \"specific letter\"?: ")
        if nlp(list_filter).similarity(nlp("all designers")) >= minimum_similarity:
            with open("designers/" + category_file) as file:
                for line in file:
                    print(line.strip("\n"))
            return
        
        #print all designers starting with specified letter
        elif nlp(list_filter).similarity(nlp("specific letter")) >= minimum_similarity:
            input_letter = input("Which letter? Type \"#\" for designers names with non-alphabetic characters: ")

           
            with open("designers/" + category_file) as file:
                 # show designers starting with non alphabetic characters
                if input_letter == "#":
                    line_index = 0
                    for line in file:
                        if line_index < designers_non_alphabet:
                            print(line.strip("\n"))
                            line_index += 1
                        else:
                            break
            
                # show designers starting with a user-provided character            
                else:
                    for line in file:
                        capital_input_letter = nlp(input_letter.capitalize())
                        first_letter = nlp(line[0])
                        capital_first_letter = nlp(line[0].capitalize())

                        if nlp(input_letter).similarity(first_letter) >= minimum_similarity:
                            print(line.strip("\n"))

                        elif nlp(capital_input_letter).similarity(capital_first_letter) >= minimum_similarity:
                            print(line.strip("\n")) 

                        else: 
                            print("No designers were found. Try searching a different letter.\n")
                            find_brand()
            return
        return
    return

# Color

