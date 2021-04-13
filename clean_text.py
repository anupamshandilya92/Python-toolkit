#Clean the review text data

tokenizer = RegexpTokenizer(r'\w+')
lemmatizer = WordNetLemmatizer()

def clean_text(text):
    """
        text: a string
        
        return: modified initial string
    """
    #tokenizer breaks string into a list of words
    text=str(text)
    text = tokenizer.tokenize(text)
    text = " ".join([c for c in text if c not in string.punctuation])
    
   #text = text.replace('º','')
   #text = text.replace('¾','')
   #text = text.replace('ƒ','')
   #text = text.replace('œ','')
   #text = text.replace('ð','')
    #ð,œ,ƒ,ª,¾,º
    text = text.lower() # lowercase text
    text = re.compile('"''#&?!:[/(){}\[\]\|@,;.]').sub(' ', text)
    text = re.compile('[ðœƒª¾º³µ¼ˆ]').sub('', text)
    # replace symbols by space in text. substitute the matched string with space.
#     text = re.sub(r'\d+','', text) # remove symbols and numbers
    text = " ".join(word for word in text.split() if word not in stopWords) # remove stopwors from text
    return text
