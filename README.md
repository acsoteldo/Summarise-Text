# Summarise Text

### hw
Write a Python function summarise paras(f) to analyse the text found in a textfile
named ‘f’ and to print a summary (described below) of each paragraph found in the file.
Assume that the file exists and is in the same directory as your program.
Assume that each paragraph is followed by a single empty line i.e. a line that contains
no characters apart from the newline. The words in a paragraph are separated by
whitespace (spaces or newlines). Hyphenated words are treated as a single word and
similarly for other internal punctuation.
The summary of a paragraph consists of the first three words of the paragraph and the
last word and the total number of words in that paragraph. For example, the paragraph
Little Bo-Peep has lost her sheep,
And can’t tell where to find them;
Leave them alone, And they’ll come home,
Bringing their tails behind them.
should produce the following summary:
’Little Bo-Peep has . . . them.’ has 25 words.
For paragraphs with fewer than four words, the summary comprises all the words of the
paragraph and the word count
