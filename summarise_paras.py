def summarise_paras(f):
  # Open the file for reading
  with open(f, 'r') as file:
    # Read the contents of the file
    contents = file.read()
  
  # Split the contents into paragraphs by splitting on the empty lines
  paras = contents.split("\n\n")
  
  # Iterate over the paragraphs
  for para in paras:
    # Split the paragraph into words
    words = para.split()
    
    # Get the first three words and the last word
    first_three_words = words[:3]
    last_word = words[-1]
    
    # If there are fewer than four words, use all the words in the paragraph
    if len(words) < 4:
      summary = " ".join(words)
    else:
      summary = " ".join(first_three_words) + " . . . " + last_word
      
    # Print the summary and the word count
    print(f"'{summary}' has {len(words)} words.")
    
summarise_paras("my_file.txt")
