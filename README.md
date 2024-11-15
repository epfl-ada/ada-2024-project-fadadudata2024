# The Cold War of Laughter: Western Humor vs. Eastern Wit 😂🌍🧊

## Abstract
This project takes a dive into the comedic rivalry between American and European films, uncovering the cultural quirks that make each side laugh. Using data from the CMU Movie Summary Corpus and OMDB, we analyze recurring themes, linguistic styles, and narrative structures to decode the essence of humor on both sides of the Atlantic. Do Americans favor slapstick and sarcasm, while Europeans lean toward dry wit and intellectual wordplay? Are certain jokes universal, or do some fall flat across cultural divides? We also explore representation dynamics—examining how gender and ethnicity shape the humor landscape—and investigate box office trends to see if Hollywood's blockbuster comedies outshine Europe's subtler charm. Through text analysis, visualizations, and linguistic modeling, this project aims to answer whether humor truly transcends borders or remains firmly rooted in cultural context. Laugh, learn, and decide which side of the Atlantic rules the comedy game!


## Research Questions

### 1. Narrative and Thematic Analysis
- What recurring themes and narrative patterns define comedies from America and Europe?
- How do cultural differences shape the humor and storytelling styles of these films?
- In what ways do American and European comedies align in their themes, and where do they diverge?

### 2. Gender and Ethnic Representation
- What are the gender and ethnic compositions in American and European comedies?
- How has the representation of these groups evolved over time, and what cultural insights can be drawn from these changes?
- How do leading roles vary by gender and ethnicity across American and European comedies, and how have these trends shifted over the years?

### 3. Commercial and Critical Success
- What factors—such as themes, casting, runtime, and distribution—drive the success of comedies in these regions?
- Is there a correlation between commercial success (box office) and critical or audience recognition (ratings), and does this vary by continent or audience type?
- Are European comedies rated more favorably than American ones, and do they receive similar evaluations from critics and audiences across different subgenres?


## Supplementary Dataset

1. **The Open Movie Database (OMDB)**:  
   OMDB provided valuable supplementary information, such as box office revenue, runtime, audience ratings, awards, and additional plot summaries. We used this dataset to fill missing values in our original dataset and enrich it with new variables. Merging the datasets was straightforward by aligning on movie titles, with careful handling of movies that share the same name.

2. **Stanford CoreNLP Pipeline**:  
   For missing plot summaries, we ran the Stanford CoreNLP pipeline locally on the remaining movies in our dataset. If a processed output was unavailable, we used the OMDB plot summary as input for the pipeline. This step augmented our dataset significantly, increasing the number of fully processed comedy-related movies from approximately 7,300 to 12,000.

## Methods

## Proposed timeline

## Organization within the team

## Questions for TA's

Given our preliminary exploration of Latent Dirichlet Allocation (LDA) for uncovering thematic structures, do you think it is worthwhile to invest more time refining the LDA process (e.g., optimizing preprocessing, tuning parameters, or increasing topic granularity)? Or would you recommend focusing on alternative methods to achieve deeper insights into narrative trends?

## References

