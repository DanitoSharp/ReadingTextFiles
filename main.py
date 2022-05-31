# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}

def read_file_content(filename):
    # [assignment] Add your code here

    # Opening the file and storing it in variable "File"
    file = open(filename, 'r')

    # Reading the file using the "readlines()" extension method
    read = file.readlines()

    # Created list
    lists =[]

    for lines in read:
        # striping off the escape character '\n' and storing
        # each line into the list created
        lists.append(lines.strip())

    # Declared to store the refined text.
    cont = ""

    # Using a for loop to pick and concatenate each line to 
    # declared variable "cont"
    for sentance in lists:
        if sentance == lists[:-1]:
            cont += sentance
        else:
            #Adding a space after each concatination
            cont += sentance + ' '

    return cont # Returning cont



def count_words():
    text = read_file_content("story.txt")
    # [assignment] Add your code here
    #return {"as": 10, "would": 20}

    # Created a dictionary
    Dic = {}

    # Using the split function to cut
    # each words and storing them in a list.
    words = text.split()

    # Using a for loop in combination with the dictionary
    # picking each word and storing them as a key and the
    # count as the value.
    for word in words:
        if(word in Dic):
            continue
        else:
            Dic[word] = words.count(word)
    
    #Returning the Dictionary
    return Dic

# Using the Dictionary's extension method (.items())
# to display all the elements stored.
print(count_words().items()) #Done
