# Humor Across Continents: Europe vs. America 😂🌎

## Abstract
This project tackles global humor like a foodie facing an all-you-can-eat dessert buffet: on one side, American comedy—generous with gags and explosions; on the other, European laughter—sometimes as refined as a delicate pastry, sometimes as bold as a strong espresso. By exploring the CMU Movie Summary Corpus and OMDB data, we’ll dive into storylines, the variety of actors, box-office success, and rich critiques. Our mission? To understand what makes audiences laugh out loud from one continent to another. By telling this story, we hope to highlight the rich diversity of humor around the world and show how laughter can be universal, yet shaped by specific cultural factors. 🤹‍♀🍰

## Datastory
Our project's data story is available at the following link: [Data Story](https://epfl-ada.github.io/ada-2024-project-fadadudata2024/)

## Required Python Packages

This project requires the Python packages in `pip_requirements.txt` to run properly.

## Repository Architecture

- **data**: Contains multiple CSV files created and utilized using datasets provided by the CMU Movie Summary Corpus and OMDB.

- **docs**: Includes all codes and files used to develop the data story.

- **src**:  
  - **data**: Example dataset retrieved from the OMDB API.  
  - **resource**: Masks for word clouds and images utilized in the notebook.  
  - **script**: Example implementation of the Stanford NLP pipeline.  
  - **utils**: Python module containing utility functions.  

- **`preprocessing.ipynb`**: A notebook detailing the data preprocessing steps used to compile and prepare the data.

- **`full_analysis.ipynb`**: A comprehensive notebook documenting all analyses performed, including results that were not incorporated into the final data story.

- **`results.ipynb`**: A refined notebook containing results specifically used in the data story. This is a reduced version of `full_analysis.ipynb`.



## Research Questions

### 1. Commercial and Critical Success
- Does a movie's success vary based on its age rating (e.g., 13+, 16+) and the number of awards it wins?
- Is there a correlation between commercial success (box office) and critical or audience recognition (ratings), and does this vary by continent or audience type?
- Are European comedies rated more favorably than American ones, and do they receive similar evaluations from critics and audiences across different subgenres?

### 2. Narrative and Thematic Analysis
- What recurring themes and narrative patterns define comedies from America and Europe?
- How do cultural differences shape the humor and storytelling styles of these films?
- In what ways do American and European comedies align in their themes, and where do they diverge?

### 3. Gender and Ethnic Representation
- How does ethnic diversity correlate with movie ratings?
- Can we develop a "diversity score" to quantify the level of diversity in a film's cast?

## Supplementary Dataset

1. **The Open Movie Database (OMDB)**:  
   OMDB provided valuable supplementary information, such as box office revenue, runtime, audience ratings, awards, and additional plot summaries. We used this dataset to fill missing values in our original dataset and enrich it with new variables. Merging the datasets was straightforward by aligning on movie titles, with careful handling of movies that share the same name.

2. **Stanford CoreNLP Pipeline**:  
   For missing plot summaries, we ran the Stanford CoreNLP pipeline locally on the remaining movies in our dataset. If a processed output was unavailable, we used the OMDB plot summary as input for the pipeline. This step augmented our dataset significantly, increasing the number of fully processed comedy-related movies from approximately 7,300 to 12,000.

## Methods
### 1. Data Collection and Preparation
   - **Data Wrangling**: Cleaning and organizing data from the CMU Movie Summary Corpus and OMDB to create a structured, unified dataset.
   - **Data Integration**: Merging datasets based on common identifiers to facilitate thematic analysis, character representation analysis, and success metrics.

### 2. Analysis Process
 - Patterns were identified across themes and ethnicity representation, ratings, and commercial success. To highlight these different data structures, various statistical tests were conducted, including:
   - **T-test**: Comparing the means of two groups to detect significant differences; often accompanied by confidence intervals (CIs) to estimate the mean difference.
   - **Kolmogorov-Smirnov (KS)**: Checking if a distribution follows a normal distribution.
   - **Mann-Whitney U**: Comparing ranks between two groups for non-normal distributions.
   - **Spearman**: Measuring the monotonic correlation between two variables, without assuming linearity.

   This variety of comparison tools ensures robust conclusions by accounting for potential initial hypothesis violations. It also provides objective means to assess the presence or absence of significant differences between two groups.
    

 -  For thematic analysis, NLP tools like Stanford CoreNLP to extract recurring narrative themes. For this part, we are going to make a frequency analysis on the plots summaries by leveraging the CoreNLP pipeline results.
    - **Tokenization & stopwords removal** : a common method when manipulating text data is to extract tokens and remove words that are not useful for our analysis.
    - **N-gram generation** : n-grams are a way of parsing sentences by group of n words. For example, we can look at the 2-grams of the form “<verb> <any other word>” to extract recurrent topics in the scenarios.
    - **Frequency analysis** : using the wordclouds visualization, we will extract the dominant topics and features of comedy movies across continents
    - **Topic modelling** : using TF-IDF factorization and Singular Value Decomposition (SVD) to identify key themes in European and American plot summaries.

 - For the ethnic representation analysis, the following choices were made about :
    - **Diversity Score**: The diversity score is calculated by using entropy and the proportion of each represented ethnicity in the cast of actors. 

### 3. Present the results

Finally, our findings are presented as an interactive data story on the following webpage: [Data Story](https://epfl-ada.github.io/ada-2024-project-fadadudata2024/)


## Timeline and Organization within the team

The following figure presents the provisionned timeline :

![Timeline](src/ressource/timeline.jpeg)


## References

 - [Applied Data Analysis course webpage](https://epfl-ada.github.io/teaching/fall2024/cs401/), EPFL.
 - Manning, Christopher D., Mihai Surdeanu, John Bauer, Jenny Finkel, Steven J. Bethard, and David McClosky. 2014. The Stanford CoreNLP Natural Language Processing Toolkit In Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics: System Demonstrations, pp. 55-60. [Accessible here](https://stanfordnlp.github.io/CoreNLP/)
 - [Freebase Data Dumps](https://developers.google.com/freebase/data). Google. Accessed on 15/11/2024.

## Acknowledgements

ChatGPT has been used to rephrase and translate to english some parts of this document as well as some comments in the code (thank you ChatGPT).