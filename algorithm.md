# Algorithm: Headline Analysis Program

Main Function: main
Purpose: Controls the program's flow, displays the menu, and processes user input.
Parameters: None
Return: None
Algorithm:
1. Initialize an empty list `headlines` to store loaded headlines.
2. Display the menu options:
   - 1: Load a headline file.
   - 2: Count headlines with a specific word.
   - 3: Write headlines with a specific word to a file.
   - 4: Calculate average characters per headline.
   - 5: Display the shortest and longest headlines.
   - 6: Quit the program.
3. Prompt the user to enter their choice.
4. Based on the user’s choice:
   - Option 1: 
     - Prompt for a file name and call `read_file`. 
     - Store the result in `headlines`. 
     - Print debug messages for the filename, file loading status, and the number of headlines loaded.
   - Option 2: 
     - If `headlines` is empty, display an error. 
     - Otherwise, prompt for a word and call `count_word_in_headlines`. 
     - Print debug messages for the search word and the number of matching headlines.
   - Option 3: 
     - If `headlines` is empty, display an error. 
     - Otherwise, prompt for a word and output file name, then call `write_headlines_to_file`. 
     - Print debug messages for the filtered word and the output file name.
   - Option 4: 
     - If `headlines` is empty, display an error. 
     - Otherwise, call `calculate_average_characters` and display the result. 
     - Print debug messages for the number of headlines and the average calculated.
   - Option 5: 
     - If `headlines` is empty, display an error. 
     - Otherwise, call `find_longest_and_shortest_headlines`. 
     - Print debug messages for the shortest and longest headlines.
   - Option 6: Exit the program with a goodbye message.
5. Handle invalid inputs by displaying an error message.
6. Repeat steps 2–5 until the user chooses to quit.

Function: read_file
Purpose: Read and return a list of headlines from the specified file.
Parameters: filename (str): The name of the file to read.
Return: List[str]: A list of headlines.
Algorithm:
1. Print a debug message indicating the file being opened.
2. Attempt to open the file in read mode.
3. For each line in the file:
   - Strip leading and trailing whitespace.
   - Append the line to a list.
4. Print a debug message showing the number of lines read.
5. If the file does not exist or another error occurs:
   - Print an error message.
   - Print a debug message if an unexpected error occurs.
   - Return an empty list.
6. Return the list of headlines.

Function: count_word_in_headlines
Purpose: Count the number of headlines that contain a given word.
Parameters:
   - headlines (List[str]): A list of headlines.
   - word (str): The word to search for.
Return: int: The count of headlines containing the word.
Algorithm:
1. Print a debug message showing the word being searched for and the number of headlines.
2. Initialize a counter to 0.
3. Loop through each headline in `headlines`.
4. Convert the headline and `word` to lowercase.
5. Check if `word` is in the headline.
6. If yes, increment the counter.
7. Return the counter.

Function: write_headlines_to_file
Purpose: Write headlines containing a specific word to a new file.
Parameters:
   - headlines (List[str]): A list of headlines.
   - word (str): The word to filter by.
   - output_file (str): The name of the file to write to.
Return: None
Algorithm:
1. Print a debug message showing the word being filtered and the output file name.
2. Filter the headlines containing the specified word (case-insensitive).
3. Open the output file in write mode.
4. Write each filtered headline to the file, separated by new lines.
5. Print a message confirming that the filtered headlines have been written.

Function: calculate_average_characters
Purpose: Calculate the average number of characters across all headlines.
Parameters: headlines (List[str]): A list of headlines.
Return:
   - float: The average number of characters.
Algorithm:
1. Print a debug message showing the number of headlines being processed.
2. Calculate the total number of characters in all headlines using `len`.
3. Divide the total characters by the number of headlines.
4. If there are no headlines, return 0.
5. Return the result.

Function: find_longest_and_shortest_headlines
Purpose: Find and return the shortest and longest headlines based on character count.
Parameters: headlines (List[str]): A list of headlines.
Return: Dict: A dictionary containing the shortest and longest headlines.
Algorithm:
1. Print a debug message showing the number of headlines being processed.
2. If `headlines` is empty, return a dictionary with `shortest` and `longest` as `None`.
3. Use `min` with `key=len` to find the shortest headline.
4. Use `max` with `key=len` to find the longest headline.
5. Print a debug message for the shortest and longest headlines found.
6. Return a dictionary with keys:
   - "shortest" containing the shortest headline.
   - "longest" containing the longest headline.
