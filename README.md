An attempt to find out frequency of Top 800 GRE words in Classic books.

#Log:
1. **16/Feb/2014**:
    - High frequency words and corpus, were not lemmatized
    - Output is saved in `output.json`

2. **18/Feb/2014**:
    - High frequency words and corpus both were lemmatized 
    - Lemmatization was done using `WordNetLemmatizer`:

            from nltk.stem import WordNetLemmatizer
            wnl = WordNetLemmatizer()
            wnl.lemmatize(word)
    - Output is saved in `output-wnl.json`
