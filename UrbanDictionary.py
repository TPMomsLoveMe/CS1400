#Tyler Potter Final Project: Urban Dictionary 12/13/2024
import random #this allowed me to pick a random word from my dictionary
import os #This helped with my clear function at the end of my code
print("Welcome to Tyler Potter's 12/13/24 Urban Dictionary!") #Intro statement

word_dictionary = {} # Global dictionary to store words and definitions

def load_dictionary(filename): #Loading my dictionary from a file
    global word_dictionary
    try:
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()  
                if ':' in line:  # Making sure that there is a : between each key and value
                    word, definition = line.split(':', 1)  # Split on the first colon
                    word_dictionary[word.strip()] = definition.strip()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def save_dictionary(filename): #Great because this saves the dictionary back to the file
    global word_dictionary
    try:
        with open(filename, 'w') as file:
            for word, definition in word_dictionary.items():
                file.write(f"{word}:{definition}\n")
    except Exception as e:
        print(f"An error occurred while saving: {e}")

def Valid_Input(question, valid_options): #prompting the user until a valid input is reached
    while True:
        user_input = input(question).strip().lower()
        if user_input in valid_options:
            return user_input
        print(f"Invalid input. Please choose from: {', '.join(valid_options)}.")

def Confirming_Action(question):
    return Valid_Input(question, {"y", "yes", "n", "no"}) in {"y", "yes"}

def Perform_Lookup(): #Looking up the word in the dictionary
    global word_dictionary
    while True:
        word = input("Enter the word you want to look up (or type 'back' to return to the main menu): ").strip().lower()
        if word.lower() == "back": # I gave the user the option to return to the main menu
            return
        if word in word_dictionary: # How I checked if the word was in my dictionary
            print(f"\nDefinition of '{word}': {word_dictionary[word]}\n")
        else: # Uh oh! That word wasn't found
            print(f"'{word}' is not defined in the Urban Dictionary yet.\n")
            if Confirming_Action(f"Do you want to add a definition for '{word}'? (Yes/No): "):
                Add_Definition(word)

def Random_Word(): #Displaying the random word.
    global word_dictionary
    if not word_dictionary: #checks to see if the dictionary is inherently empty
        print("The Urban Dictionary is currently empty.")
    else:
        word, definition = random.choice(list(word_dictionary.items()))
        print(f"Random Word:\n{word}: {definition}")

def Add_Definition(word=None): #Add or update a definition for a word.
    global word_dictionary
    if not word:
        word = input("Enter the word you want to add: ").strip().lower()
    if word in word_dictionary:
        print(f"The word '{word}' already exists: {word_dictionary[word]}")
        if not Confirming_Action("Do you want to overwrite it? (Yes/No): "):
            return
    definition = input(f"Enter the definition for '{word}': ").strip()
    if definition:
        word_dictionary[word] = definition
        print(f"'{word}' has been successfully added/updated.")
    else:
        print("Definition cannot be empty. Please try again.")

def Sort_Dictionary_Alphabetically(): #Sorting the dictionary alphabetically
    global word_dictionary
    word_dictionary = dict(sorted(word_dictionary.items()))

def Main_Menu(): #Main Menu Loop for code
    while True:
        print("\nMain Menu:\n1. Perform Lookup\n2. Random Word\n3. Add a Definition\n4. Leave Program")

        choice = Valid_Input("Enter your choice (1-4): ", {"1", "2", "3", "4"})

        if choice == "1":
            Perform_Lookup()
        elif choice == "2":
            Random_Word()
        elif choice == "3":
            Add_Definition()
        elif choice == "4":
            if Confirming_Action("Are you sure you want to leave the program? (Yes/No): "):
                print("Goodbye!")
                break

def Clear_Screen(): #Clearing the terminal screen
    input(f"Press enter to clear Terminal outputs.")
    os.system('clear')

if __name__ == "__main__":

    dictionary_file = "dictionary.txt"

    load_dictionary(dictionary_file)

    Main_Menu()

    Sort_Dictionary_Alphabetically() #This was totally not needed, but made my happy to see all of the terms in alphabetical order.

    save_dictionary(dictionary_file)
    print("Urban Dictionary Updated.")

    Clear_Screen()