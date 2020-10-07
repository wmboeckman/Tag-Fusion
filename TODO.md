# TODO:

## The Current Plan

The first part of the application will process a given dataset of text, given an already agreed upon standard or custom model.

The best way I thought about generating usable keywords out of a body of text without having to keep updating the code for each new edge-case i find was to use [**Natural Language Processing(NLP)**](https://www.kdnuggets.com/2020/05/text-mining-python-steps-examples.html):
- **Tokenize** the given body of text (ex: `"Hello world!"` -> `['Hello','world','!']`)
- Find **frequency distribution** from tokens (ex: `"One fish, two fish."` -> `['one': 1,'fish': 2,',': 1,'two': 1,'.': 1]`)
- **Stemming**, or finding the root word (ex: `"wait","waited","waiting"` -> `"wait"`) Use Porter Stemming if possible, although Lancaster Stemming is more aggressive if needed.
- **Lemmatization**, or the process of converting a word to its 'base' form (ex: `"gone","going","went"` -> `"go"`) Its kinda like Stemming, but doesnt require a 'root' word. Implemented in python by using Wordnet Lemmatizer, Spacy Lemmatizer, TextBlob, Stanford CoreNLP.
- **Stop Words**, or the most common words in a language (ex: `"I was at the giant rock."` -> `["I","was","at","the"]`) These are removed to save processing power and to prevent them from becoming an SEO tag.
- **Part of speech tagging (POS)** (ex: `"vote to choose a particular man or a group (party) to represent them in parliament"` -> `[ [('vote', 'NN')], [('to', 'TO')], [('choose', 'NN')], [('a', 'DT')], [('particular', 'JJ')], [('man', 'NN')], [('or', 'CC')], [('a', 'DT')], [('group', 'NN')], [('(', '(')], [('party', 'NN')], [(')', ')')], [('to', 'TO')], [('represent', 'NN')], [('them', 'PRP')], [('in', 'IN')], [('parliament', 'NN')] ]`) assigns parts of the given text, such as nouns, verbs, pronouns, adverbs, conjunction, and adjectives, based on its definition and its context. Some of the most widely used taggers are NLTK, Spacy, TextBlob, Standford CoreNLP.
- **Named entity recognition**, the process of detecting named entities such as an individual's name (ex: `.`)
- **Chunking**, or grouping pieces of relevant information together (ex: `.`)

Utilizing these techniques, we can build a powerful SEO teg generator, and possibly even more, using this tool!

## The Plan, _but explained._

So, utilizing the above NLP functions, how can we generate usable SEO tags?

One basic strategy would be to run these functions in order:

- Remove stop words. Used to rid the text of 'useless' data.
- Named entity recognition, save in list for later.
- Tokenize rest of text.
- Find top `n` frequency distribution from tokens. Save for later.
- Part of speech tagging (only keep `NN`).

Return the names, token frequency distribution, and part of speech tagging data!