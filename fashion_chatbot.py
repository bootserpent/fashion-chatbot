import spacy
import os
import actions
import filters

nlp = spacy.load("en_core_web_md")
minimum_similarity = 0.75
def main():
    # Greeting, list of suggested actions
    print("""Hello! Would you like to search for...\n
                \t...different applications/uses?\n
                \t...something random?\n
                \t...advice or inspiration?\n
                \t...brands or designers?\n
                \t...something specific?\n""")

    action = input("Your message: ")

        # List of the industries/intended uses of apparel to explore
            # Task size M - 1 hour 
    actions.find_applications(action)

        # Show me advice or inspiration
            # Task size M - 1 hour
    actions.advice_or_insipration(action)

        # Piece or name (top, bottom, shoe, etc.)
            # Task size L - 2 hours 
    actions.specific_search(action)

        # Show me something random
            # Task size M - 1 hour
    actions.discover(action)

        # Brand/Designer
            # Task size M - 1 hour
    filters.find_brand(action)

        # Color
    
    return

main()
