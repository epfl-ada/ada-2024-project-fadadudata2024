from collections import Counter

import pandas as pd
import numpy as np
from nltk import word_tokenize, ngrams
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import gzip
import xml.etree.ElementTree as ET
import re
import json

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

continent_classification = {
    'America': [
        'United States of America', 'Canada', 'Mexico', 'Argentina', 'Brazil', 'Chile', 'Cuba', 'Colombia', 
        'Uruguay', 'Venezuela', 'Jamaica', 'Panama', 'Costa Rica', 'Bahamas', 'Haiti', 'Puerto Rico', 'Bolivia', 'Peru'
    ],
    'Europe': [
        'United Kingdom', 'France', 'Italy', 'Germany', 'West Germany', 'Soviet Union', 'Poland', 'Czechoslovakia', 
        'Belgium', 'Norway', 'Hungary', 'German Democratic Republic', 'Yugoslavia', 'Ireland', 'Switzerland', 'Austria', 
        'Finland', 'Czech Republic', 'Russia', 'Turkey', 'England', 'Greece', 'Portugal', 'Croatia', 'Romania', 
        'Iceland', 'Luxembourg', 'Weimar Republic', 'Serbia', 'Scotland', 'Estonia', 'Bosnia and Herzegovina', 'Slovakia', 
        'Slovenia', 'Albania', 'Ukraine', 'Azerbaijan', 'Nazi Germany', 'Republic of Macedonia', 'Socialist Federal Republic of Yugoslavia', 
        'Serbia and Montenegro', 'Georgia', 'Lithuania', 'Armenia', 'Kingdom of Great Britain', 'Federal Republic of Yugoslavia', 
        'Georgian SSR', 'Slovak Republic', 'Malta', 'Northern Ireland', 'Montenegro', 'Kingdom of Italy', 'Monaco', 'Cyprus', 
        'Ukrainian SSR', 'Isle of Man', 'Soviet occupation zone', 'German Language', 'Ukranian SSR', 'Spain', 'Netherlands', 
        'Sweden', 'Denmark', 'Bulgaria', 'Wales'
    ],
    'Asia': [
        'India', 'Japan', 'Hong Kong', 'China', 'Israel', 'Iran', 'Thailand', 'Pakistan', 'Taiwan', 'Indonesia', 'Malaysia', 
        'Sri Lanka', 'Singapore', 'Cambodia', 'Bangladesh', 'Nepal', 'Lebanon', 'Vietnam', 'Korea', 'Burma', 'Iraq', 
        'United Arab Emirates', 'Afghanistan', 'Iraqi Kurdistan', 'Uzbek SSR', 'Uzbekistan', 'Mongolia', 'Kuwait', 
        'Bhutan', 'Aruba', 'Bahrain', 'Qatar', 'Jordan', 'Turkmenistan', 'Republic of China', 'Macau', 
        'Palestinian Territories', 'Mandatory Palestine', 'Palestinian territories', 'Malayalam Language', 'South Korea', 'Philippines'
    ],
    'Africa': [
        'South Africa', 'Egypt', 'Morocco', 'Algeria', 'Tunisia', 'Burkina Faso', 'Senegal', 'Nigeria', 
        'Democratic Republic of the Congo', 'Mali', 'Kenya', 'Cameroon', 'Ethiopia', 'Zimbabwe', 'Guinea', 'Libya', 
        'Guinea-Bissau', 'Congo', 'Zambia'
    ],
    'Oceania': [
        'Australia', 'New Zealand'
    ]
}

# Function to map countries to continents
def map_country_to_continent(country):
    for continent, countries in continent_classification.items():
        if country in countries:
            return continent
    return 'Other'
def map_country_list_to_continent(country_list):
    return [map_country_to_continent(country) for country in country_list]

def treat_continent(continent):
    new_continent =  []
    if "America" in continent and "Europe" in continent:
        new_continent.append("Both")
    else :
        if "America" in continent:
            new_continent.append("America")
        if "Europe" in continent:
            new_continent.append("Europe")
    if "Asia" in continent:
        new_continent.append("Asia")
    if "Africa" in continent:
        new_continent.append("Africa")
    if "Oceania" in continent:
        new_continent.append("Oceania")
    return new_continent


# Function to extract the number of awards from the Awards column
def extract_awards(awards_str):
    if pd.isna(awards_str):
        return 0, 0, 0
    oscar = 0
    nomination = 0
    win = 0
    oscar_match = re.search(r'Won (\d+) Oscar', awards_str)
    if oscar_match:
        oscar = int(oscar_match.group(1))
    nomination_match = re.search(r'(\d+) nomination', awards_str)
    if nomination_match:
        nomination = int(nomination_match.group(1))
    win_match = re.search(r'(\d+) win', awards_str)
    if win_match:
        win = int(win_match.group(1))
    return oscar, nomination, win


# Function to extract ratings from the Ratings column
def extract_ratings(ratings_str):
    if pd.isna(ratings_str) or ratings_str == '[]':
        return {}
    ratings_list = json.loads(ratings_str.replace("'", '"'))
    ratings_dict = {rating['Source']: rating['Value'] for rating in ratings_list}
    return ratings_dict

# Function to convert ratings to a scale of 10
def convert_to_scale_of_10(rating):
    if pd.isna(rating):
        return None
    if isinstance(rating, str):
        if '%' in rating:
            return float(rating.replace('%', '')) / 10
        if '/10' in rating:
            return float(rating.replace('/10', ''))
        if '/100' in rating:
            return float(rating.replace('/100', '')) / 10
    return float(rating)

def classifier_age(rating):
    if rating in ["G", "TV-G", "U", "Approved", "EM"]:
        return "All Audiences (TP)"

    elif rating in ["PG", "PG-13", "TV-PG", "TV-Y7", "TV-Y7-FV", "Atp"]:
        return "Recommended Parental Agreement (AP)"

    elif rating in ["13+", "TV-14", "M/PG", "M"]:
        return "13+"

    elif rating in ["R", "TV-MA", "16+", "NC-17"]:
        return "16+"

    elif rating in ["X", "AO", "18"]:
        return "18+"
    else:
        return "Not Rated"
    

# Dictionnaire pour les mots-clés principaux par type
genre_keywords = {
    'Comedy_Romance': ['romance', 'romantic'],
    'Comedy_Drama': ['drama', 'tragedy', 'tragicomedy', 'melodrama'],
    'Comedy_Action': ['action', 'action comedy', 'martial arts film', 'superhero'],
    'Comedy_Adventure': ['adventure', 'action/adventure', 'family-oriented adventure', 'road movie'],
    'Comedy_Horror': ['horror', 'slasher', 'sci-fi horror', 'natural horror', 'haunted house film', 'horror comedy'],
    'Comedy_Musical': ['musical', 'hip hop', 'dance', 'opera', 'jukebox musical'],
    'Comedy_Crime': ['crime', 'crime fiction', 'crime drama', 'heist', 'detective', 'gangster film'],
    'Comedy_Western': ['western', 'spaghetti western', 'comedy western', 'revisionist western'],
    'Comedy_Documentary': ['documentary', 'docudrama', 'mockumentary', 'rockumentary'],
    'Comedy_LGBT': ['lgbt', 'gay', 'gay interest', 'gay themed'],
    'Comedy_Fantasy': ['fantasy', 'fairy tale', 'fantasy adventure', 'supernatural'],
    'Comedy_Thriller': ['thriller', 'suspense', 'mystery', 'spy', 'political thriller', 'psychological thriller'],
    'Comedy_Animation': ['animation', 'computer animation', 'animated cartoon', 'anime', 'stop motion'],
    'Comedy_Parody': ['parody', 'comedy of errors', 'satire', 'media satire'],
    'Comedy_Satire': ['satire', 'political satire', 'absurdism'],
    'Comedy_Mockumentary': ['mockumentary', 'pseudo-documentary', 'satirical documentary'],
    'Comedy_Sports': ['sports', 'boxing', 'baseball', 'basketball', 'soccer'],
    'Comedy_Political': ['political', 'political drama', 'political cinema'],
    'Comedy_Adult': ['adult', 'erotic', 'sexploitation', 'pornography', 'softcore porn','sex comedy'],
    'Comedy_Blaxploitation': ['blaxploitation'],
    'Comedy_Science_Fiction': ['science', 'sci-fi', 'science fiction', 'time travel', 'superhero', 'dystopia'],
    'Comedy_Black': ['black comedy', 'dark humor', 'gallows humor'],
    'Comedy_Teen': ['teen', 'coming of age', 'teen drama', 'high school'],
    'Comedy_Family': ['family', 'children', 'family film', 'children’s/family','domestic comedy'],
    'Comedy_Slapstick': ['slapstick', 'physical comedy', 'gross-out', 'gross-out film'],
    'Comedy_Screwball': ['screwball', 'screwball comedy', 'comedy of manners'],
    'Comedy_Buddy': ['buddy film', 'buddy cop', 'buddy comedy'],
    'Comedy_Superhero': ['superhero', 'comic book', 'comic superheroes'],
    'Comedy_War': ['war film', 'anti-war', 'military comedy'],
    'Comedy_Road_movie': ['road movie', 'road comedy', 'road trip'],
    'Comedy_Holiday': ['holiday', 'christmas', 'christmas movie', 'holiday film'],

}

def determine_types(genres):
    """
    Détermine les types de genres en utilisant les mots-clés principaux et recherche de sous-chaînes.

    Parameters:
    - genres (list of str): La liste des genres pour un film.

    Returns:
    - list: Une liste des types associés au film, sans doublons.
    """
    types = set()  # Utiliser un set pour éviter les doublons
    
    # Convertir la chaîne en liste si nécessaire
    if isinstance(genres, str):
        try:
            genres = ast.literal_eval(genres)
        except (ValueError, SyntaxError):
            return ['Comedy_Other']  # Retourner 'Comedy' si la conversion échoue
    
    # Vérifier que genres est une liste
    if not isinstance(genres, list):
        return ['Comedy_Other']

    # Concaténer tous les genres en une seule chaîne en minuscule
    genres_text = " ".join(genres).lower()

    # Parcourir le dictionnaire des mots-clés principaux et ajouter les types si un mot-clé est présent
    for type_name, keywords in genre_keywords.items():
        if any(keyword.lower() in genres_text for keyword in keywords):
            types.add(type_name)  # Ajouter au set pour éviter les doublons

    # Ajouter 'Other' si aucun type spécifique n'est trouvé
    if not types:
        types.add('Comedy_Other')
    
    return list(types)

# Modifier la colonne 'Continents' pour n'avoir que les valeurs "Europe", "America" ou "Both"
def simplify_continent(continent_list):
    if 'Europe' in continent_list and 'America' in continent_list or 'Both' in continent_list:
        return 'Both'
    elif 'Europe' in continent_list:
        return 'Europe'
    elif 'America' in continent_list:
        return 'America'
    else:
        return 'Other'
