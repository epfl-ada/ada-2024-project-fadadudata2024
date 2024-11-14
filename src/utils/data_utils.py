from collections import Counter

import pandas as pd
import numpy as np
from nltk import word_tokenize, ngrams
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import gzip
import xml.etree.ElementTree as ET


def get_word_count(tokenized_plots):
    """Returns a Counter of words in tokenized plots.

    :param tokenized_plots: pd.series, tokenized plots
    :return Counter: occurences of the words"""
    return Counter(tokenized_plots.dropna().explode())


lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))


def tok(sentence):
    """Tokenize and lemmatize a sentence, removing stop words.
    
    :param sentence: str the sentence to tokenize
    :return: List of tokens : The lemmatized sentence, without stop words."""
    tokenized = word_tokenize(sentence)
    return [lemmatizer.lemmatize(word.lower()) for word in tokenized if word.isalpha() and word.lower() not in stop_words]


def tok_by_region(df, region):
    """Tokenize a dataframe for a specific region

    :param df: dataframe
    :param region: str region
    :return tokenized_plots: tokenized plots of the region
    """
    return df[df['Continents'].str.contains(region)].apply(
        lambda row: tok(row['Plot_Summary_Base']) if pd.notna(row['Plot_Summary_Base'])
        else tok(row['Plot']) if pd.notna(row['Plot']) else np.nan,
        axis=1
    )

# === Filter Functions ===
def filter_words_by_pos(tokens_metadata, pos_tags):
    """Filter words by specified POS tags.
    
    :param tokens_metadata: List[Dict] containing the metadata of each word for a sentence.
    :param pos_tags: List[str] containing the POS we want to keep
    :return: Filtered list of tokens"""
    return [entry['word'] for entry in tokens_metadata if entry['POS'] in pos_tags]

def filter_words_by_pos_ngram(tokens_metadata, pos_tags, ngram):
    """Filter words by specified POS tags.
    
    :param tokens_metadata: List[Dict] containing the metadata of each word for a summary.
    :param pos_tags: List[str] containing the POS we want to keep
    :param ngram: length of the ngram
    :return: Filtered list of string, each string containing ngram tokens, where the first token has a POS tag that's inside pos_tags."""
    results = []
    for ngram_instance in ngrams(tokens_metadata, ngram):
        if ngram_instance[0]['POS'] in pos_tags:
            results.append(' '.join(entry['word'] for entry in ngram_instance))
    return results


def get_sentence_word_metadata(folder_path, id, print_output=False):
    """Retrieve Stanford CoreNLP metadata for a given ID from .xml.gz files.
    
    :param folder_path: Path to the folder containing the processed summaries
    :param id: Wikipedia Id of the movie used to resolve the correcti xml.gz file
    :param print_output: boolean
    :return List[Dict] containing the metadata of each word for a summary."""
    gz_file_path = folder_path.resolve() / f"{id}.xml.gz"
    if not gz_file_path.is_file():
        return []
    try:
        with gzip.open(gz_file_path, 'rb') as gz_file:
            xml_data = gz_file.read()
            root = ET.fromstring(xml_data.decode())
        
        summary_word_metadata = []
        for sentence in root[0][0]:
            if print_output:
                print(f"\n\n=================== Sentence n°{sentence.attrib['id']} ===================")
            for child in sentence:
                if child.tag != "tokens":
                    continue
                for token in child:
                    attribs = {c.tag: c.text for c in token}
                    if print_output:
                        print(f"{attribs['word']} ({attribs['lemma']}) => {attribs['POS']}")
                    summary_word_metadata.append(attribs)
        return summary_word_metadata
    except Exception as e:
        print(f"Error processing {gz_file_path}: {e}")
        return []
