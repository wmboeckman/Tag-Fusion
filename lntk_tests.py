import nltk.corpus  # sample text for performing tokenization
# Importing FreqDist library from nltk and passing token into FreqDist
from nltk.probability import FreqDist
# Importing PorterStemmer from nltk library
from nltk.stem import PorterStemmer
# Importing LancasterStemmer from nltk
from nltk.stem import LancasterStemmer
# Importing Lemmatizer library from nltk
from nltk.stem import WordNetLemmatizer
# importing stopwords from nltk library
from nltk import word_tokenize


def test():
    print('Running some nltk tests...')

    text = "In Brazil they drive on the right-hand side of the road. " \
           "Brazil has a large coastline on the eastern side of South America."
    print(f'Tokenization Input: {text}')
    token = word_tokenize(text)
    print(f'Tokenization Result: {token}')
    # finding the frequency distinct in the tokens
    print(f'Top 10 Frequency Distribution: {FreqDist(token).most_common(10)}')

    print('Starting Stemming tests...')
    print('Stemmer Type: Porter =>', end='  ')
    pst = PorterStemmer()
    stm = ["waited", "waiting", "waits"]
    for word in stm:
        print(word + ":" + pst.stem(word), end='  ')
    print('...Complete!')
    print('Stemmer Type: Lancaster =>', end='  ')
    lst = LancasterStemmer()
    stm = ["giving", "given", "given", "gave"]
    for word in stm:
        print(word + ":" + lst.stem(word), end="  ")
    print('...Complete!')

    print('Starting Lemmatizer Tests...')
    lemmatizer = WordNetLemmatizer()
    print(f"rocks:{lemmatizer.lemmatize('rocks')}", end='  ')
    print(f"corpora:{lemmatizer.lemmatize('corpora')}", end='  ')
    print('...Complete!')

    print('Stop Words...')
    from nltk.corpus import stopwords
    a = set(stopwords.words('english'))
    original = "Cristiano Ronaldo was born on February 5, 1985, in Funchal, Madeira, Portugal."
    tokens = word_tokenize(original.lower())
    sw = " ".join([x for x in tokens if x not in a])
    print(f'Original Text: {original}')
    print(f'Removed Stop Words: {sw}')

    text = "vote to choose a particular man or a group(party) to represent them in parliament"
    # Tokenize the text
    tex = word_tokenize(text)
    for token in tex:
        print(nltk.pos_tag([token]))


if __name__ == '__main__':
    test()
