import nltk==3.9
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import heapq

def text_summarizer(text):
    # Tokenize the text into sentences
    sentences = sent_tokenize(text)
    
    # Remove stopwords (common words that don't carry much meaning)
    stop_words = set(stopwords.words("english"))
    
    # Calculate the frequency of each word
    word_frequencies = {}
    for sentence in sentences:
        words = word_tokenize(sentence)
        for word in words:
            if word.lower() not in stop_words:
                if word not in word_frequencies:
                    word_frequencies[word] = 1
                else:
                    word_frequencies[word] += 1
    
    # Assign weights to each sentence based on word frequencies
    sentence_scores = {}
    for sentence in sentences:
        words = word_tokenize(sentence)
        for word in words:
            if word.lower() in word_frequencies:
                if sentence not in sentence_scores:
                    sentence_scores[sentence] = word_frequencies[word.lower()]
                else:
                    sentence_scores[sentence] += word_frequencies[word.lower()]
    
    # Select the top N sentences with highest weights
    summary_sentences = heapq.nlargest(3, sentence_scores, key=sentence_scores.get)
    
    # Join the summary sentences into a single string
    summary = ' '.join(summary_sentences)
    return summary

text = input("Enter Your Text")

summary = text_summarizer(text)
print(summary)
