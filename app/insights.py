from collections import Counter
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download("punkt")
nltk.download('punkt_tab')
nltk.download("stopwords")

def generate_vocabulary_insights(text):
    words = [word.lower() for word in word_tokenize(text) if word.isalpha()]
    
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    unique_words = set(filtered_words)
    lexical_richness = len(unique_words) / len(filtered_words) if filtered_words else 0
    
    words_count = Counter(filtered_words)
    total_word_count = Counter(words)
    rare_words = [word for word, count in words_count.items() if count == 1]
    
    common_words = [word for word, count in total_word_count.items() if count > 1]
    
    word_diversity = (len(unique_words) / len(filtered_words) * 100) if filtered_words else 0
    
    return {
        "lexical_richness": lexical_richness,
        "rare_words": rare_words,
        "word_diversity": word_diversity,
        "top_words": words_count.most_common(10),
        "common_words_count": len(common_words),
        "unique_words_count": len(unique_words)
    }
