# Programmer: Ethan D'Souza
# Course:  CS151, Dr. Zelalem Jembre Yalew
# Due Date: 11/21/2024
# Programming Assignment: 04
# Problem Statement: Analyze headlines from the Australian Broadcasting Company.
# Purpose: Analyze headlines from a file.
# Data In: Filename, word to search, user choices.
# Data Out: Analysis results, new file with filtered headlines.

def read_file(filename):
    # Read file and return list of headlines.
    try:
        print(f"DEBUG: Attempting to open file: {filename}")  # Debugging
        with open(filename, 'r') as file:
            headlines = [line.strip() for line in file]
            print(f"DEBUG: Successfully read {len(headlines)} lines from the file.")  # Debugging
            return headlines
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"DEBUG: Unexpected error while reading file '{filename}': {e}")
        return []


def count_word_in_headlines(headlines, word):
    # Count headlines containing a specific word.
    print(f"DEBUG: Counting occurrences of the word '{word}' in {len(headlines)} headlines.")  # Debugging
    return sum(1 for headline in headlines if word.lower() in headline.lower())


def write_headlines_to_file(headlines, word, output_file):
    # Write headlines containing a specific word to a new file.
    print(f"DEBUG: Writing filtered headlines containing '{word}' to file '{output_file}'.")  # Debugging
    with open(output_file, 'w') as file:
        matches = [headline for headline in headlines if word.lower() in headline.lower()]
        file.write("\n".join(matches))
    print(f"Headlines containing '{word}' have been written to '{output_file}'.")


def calculate_average_characters(headlines):
    # Calculate the average number of characters per headline.
    print(f"DEBUG: Calculating average characters for {len(headlines)} headlines.")  # Debugging
    total_chars = sum(len(headline) for headline in headlines)
    return total_chars / len(headlines) if headlines else 0


def find_longest_and_shortest_headlines(headlines):
    # Find the shortest and longest headlines.
    print(f"DEBUG: Finding shortest and longest headlines in {len(headlines)} headlines.")  # Debugging
    if not headlines:
        return {"shortest": None, "longest": None}
    shortest = min(headlines, key=len)
    longest = max(headlines, key=len)
    print(f"DEBUG: Shortest headline: '{shortest}', Longest headline: '{longest}'")  # Debugging
    return {"shortest": shortest, "longest": longest}


def main():
    # Main program for user interaction.
    headlines = []
    user_choice = ""
    while user_choice != "6":  # Continue until the user chooses to quit
        print("\n--- Headline Analysis Program ---")
        print("1. Load a headline file")
        print("2. Count headlines with a specific word")
        print("3. Write headlines with a specific word to a file")
        print("4. Calculate average characters per headline")
        print("5. Display longest and shortest headlines")
        print("6. Quit")

        user_choice = input("Enter your choice: ").strip()
        if user_choice == "1":
            filename = input("Enter the filename to load: ").strip()
            print(f"DEBUG: User entered filename '{filename}'")  # Debugging
            headlines = read_file(filename)
            if headlines:
                print(f"{len(headlines)} headlines loaded successfully.")
            else:
                print("DEBUG: No headlines were loaded.")  # Debugging
        elif user_choice == "2":
            if not headlines:
                print("No file loaded. Please load a file first.")
            else:
                word = input("Enter the word to search for: ").strip()
                print(f"DEBUG: User entered search word '{word}'")  # Debugging
                print(f"Headlines with '{word}': {count_word_in_headlines(headlines, word)}")
        elif user_choice == "3":
            if not headlines:
                print("No file loaded. Please load a file first.")
            else:
                word = input("Enter the word to search for: ").strip()
                output_file = input("Enter the output filename: ").strip()
                print(f"DEBUG: User entered output file '{output_file}'")  # Debugging
                write_headlines_to_file(headlines, word, output_file)
        elif user_choice == "4":
            if not headlines:
                print("No file loaded. Please load a file first.")
            else:
                avg_chars = calculate_average_characters(headlines)
                print(f"Average characters per headline: {avg_chars:.2f}")
        elif user_choice == "5":
            if not headlines:
                print("No file loaded. Please load a file first.")
            else:
                result = find_longest_and_shortest_headlines(headlines)
                print(f"Shortest headline: {result['shortest']}")
                print(f"Longest headline: {result['longest']}")
        elif user_choice == "6":
            print("Exiting the program. Goodbye!")
        else:
            print("Invalid choice. Please try again.")


main()


