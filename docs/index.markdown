---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default

# START COMMAND : bundle exec jekyll serve -l
# START COMMAND Pour loris: bundle exec jekyll serve --livereload
---
<!-- titre image  -->

<div class="container-fluid mb-5">
  <div class="row justify-content-center">
   <img src="/assets/img/Titre.png">
  </div>
</div>

<!-- 
<div class="container-fluid">
  <div class="row justify-content-center bokeh-plot">
   <iframe src="/assets/htmlplot/heatmap.html"></iframe>
  </div>
</div> -->

<!-- team member  -->

<div class="container-fluid">
  <div class="row justify-content-center text-center border border-dark-subtle rounded" style="background-color:rgb(193, 178, 185)">
    <div class="col">
      <span class="display-1 copper">The circus squad</span>
    </div>
  </div>
</div>

<div style="position: relative; text-align: center; color: white; width: 995px">
  <img src="/assets/img/bandrole.png" alt="Bandrole" style="width: 900px; height: auto; border-radius: 0px;">
  <div style="position: absolute; bottom: 15%; left: 50%; transform: translateX(-50%); padding: 10px; border-radius: 5px; display: flex; justify-content: center; align-items: center; flex-wrap: nowrap;">
    <div style="display: flex; flex-direction: row;">
      {% include team_members.html %}
    </div>
  </div>
</div>


<div class="container-fluid">
  <div class="row justify-content-center text-center">
    <div class="col-9 text-center border border-dark-subtle rounded" style="background-color:#ffe6f2">
      <span class="display-4 copper">Take it with a grain of sugar</span>
    </div>
  </div>
  <div class="row justify-content-center mt-2 mb-2">
    <div class="col-auto">
      <div class="image-container">
          <img src="assets/img/Barbe1.png" alt="Cotton Candy" class="first-image">
          <img src="assets/img/Barbe2.png" alt="Cotton Candy Hover" class="second-image">
        </div>
    </div>
    <div class="col-4">
          <p class="mt-2">
            The <strong>CMU Movie Summary Corpus</strong>, our trusty stick 🍭, holds the essential ingredients for our cinematic cotton candy: plot summaries, genres, countries, and languages of movies. To make it even tastier, we sprinkled it with sweet data from the <strong>OMDB API</strong> 🍬, adding flavors like <strong>ratings</strong> (IMDb, Rotten Tomatoes, Metascore), <strong>posters</strong>, <strong>age classifications (Rated)</strong>, and <strong>awards</strong>. Some of these layers even needed a little "reshaping" to avoid getting too sticky!
          </p>
          <p>
            Meanwhile, with the help of the <strong>CoreNLP pipeline</strong>, we spun the plot summaries like a real cotton candy machine, pulling linguistic threads to enrich our analysis. That said, some layers, like actor metadata (gender, age...) and other CMU treats, were left aside—like leftover sugar at the bottom of the vat 🍯.
          </p>
    </div>
  </div>
</div>


## Part 2 : Presentation

<div class="container-fluid">
  <div class="row">
    <div class="col-5">
      <p style="text-align: justify;">In our database, the "Genres" column was like a chaotic junk drawer full of random labels such as "World Cinema," "Short Film," or "Indie." 🗂️ These were about as useful as a punchline without a joke – confusing and totally unhelpful for analyzing comedy! 🤔</p>
      <p style="text-align: justify;">So, as true comedy enthusiasts 🎭😂, we rolled up our sleeves (and flexed our funny bones) to bring some order to the madness. Instead of trying to decode this mess, we decided to create our own subcategories to dive deeper into the delightful world of different types of comedy. 🕵️‍♂️🎬</p>
      <p style="text-align: justify;">To make it happen, we developed a magical dictionary 🪄📖 (sadly, it doesn’t talk… yet) that groups specific keywords linked to various comedy subgenres. With this genius tool, we can now automatically sort films into categories like "Comedy_Romance," "Comedy_Action," "Comedy_Animation," and many more. 🎉✨</p>
      <p style="text-align: justify;">For example, any film that dares to drop words like "romantic" or "romance" gets whisked straight into "Comedy_Romance." 💘😂 Meanwhile, those whispering terms like "animated" or "anime" are promptly filed under "Comedy_Animation." 🎨🤪 In short, we’ve turned a big ol’ mess into a well-organized laugh factory. And guess what? We’re having a blast doing it! 🎉🤣</p>
    </div>
    <div class="col-7">
      <div class="row justify-content-center">
        <!-- 1. Load the html template -->
        {% include movies_genres.html %}
        <!-- 2. Load the associated javascript -->
        <script src="{{ '/assets/js/movies_genres.js' | relative_url }}"></script>
      </div>
    </div>
  </div>
</div>


## Part 3 : Test's Caroussel

<div class="container-fluid">
  <div class="row">
    <div class="col-7">
      <div class="row justify-content-center">
        <img src="/assets/img/Haut carousel.png" alt="Haut carousel" style="width: 420px; height: auto;">
      </div>
      <div class="row justify-content-center">
        <div class="col-7">
          {% include carousel.html %}
        </div>
      </div>
      <div class="row justify-content-center">
        <img src="/assets/img/Bas carousel.png" alt="Haut carousel" style="width: 420px; height: auto;">
      </div>
    </div>
    <div class="col-5">
      <p style="text-align: justify;">Here we are at the test carousel, an interactive tool that brings together essential statistical methods for exploring and analyzing our dataset. These tests are indispensable for turning raw data into meaningful and actionable insights.</p>
      <p style="text-align: justify;">They help us validate hypotheses, identify significant relationships between variables, and compare groups or distributions. By using these tools, we can determine whether the patterns observed in the data are due to chance or reflect real differences. They are, therefore, key to making informed decisions and interpreting results with rigor.</p>
  </div>
</div>
</div>






## The rating of the comedies : critics vs users

<div class="container-fluid">
  <div class="row justify-content-end">
    <div class="col-7">
      <h3>Source of Ratings: Critics vs. Public</h3>
      <p>This table shows whether each rating source displays ratings from critics or the public.</p>
      <table style="width: 100%; border-collapse: collapse; text-align: left;">
        <thead>
          <tr style="background-color:rgb(180, 74, 58); color: white;">
            <th style="border: 1px solid #ddd; padding: 8px;">Role in the Circus</th>
            <th style="border: 1px solid #ddd; padding: 8px;">Rating Source</th>
            <th style="border: 1px solid #ddd; padding: 8px;">Type of Rating</th>
            <th style="border: 1px solid #ddd; padding: 8px;">Description</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">The Spectators</td>
            <td style="border: 1px solid #ddd; padding: 8px;">Imdb Rating</td>
            <td style="border: 1px solid #ddd; padding: 8px;">Public</td>
            <td style="border: 1px solid #ddd; padding: 8px;">Rating provided by IMDb users.</td>
          </tr>
          <tr style="background-color: #f2f2f2;">
            <td style="border: 1px solid #ddd; padding: 8px;">The Critics Panel</td>
            <td style="border: 1px solid #ddd; padding: 8px;">Rotten Tomatoes Rating</td>
            <td style="border: 1px solid #ddd; padding: 8px;">Critics</td>
            <td style="border: 1px solid #ddd; padding: 8px;">Represents the Tomatometer score, an aggregated rating from professional critics.</td>
          </tr>
          <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">The Master of Ceremony</td>
            <td style="border: 1px solid #ddd; padding: 8px;">Metacritic_Rating</td>
            <td style="border: 1px solid #ddd; padding: 8px;">Critics</td>
            <td style="border: 1px solid #ddd; padding: 8px;">Aggregated rating from professional critics, provided by Metacritic.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>


### Source of Ratings: Critics vs. Public

This table shows whether each rating source displays ratings from critics or the public.

| Rating Source                  | Type of Rating     | Description                                                                                       |
|--------------------------------|--------------------|---------------------------------------------------------------------------------------------------|
| **imdbRating**                 | Public             | Rating provided by IMDb users.                                                                    |
| **Rotten_Tomatoes_Rating**     | Critics            | Represents the **Tomatometer** score, an aggregated rating from professional critics.             |
| **Metacritic_Rating**          | Critics            | Aggregated rating from professional critics, provided by Metacritic.                              |

### Summary
- **Critics’ Ratings**: Rotten_Tomatoes_Rating (Tomatometer) and Metacritic_Rating.
- **Public Ratings**: imdbRating.


### Kolmogorov-Smirnov Test for Normality on Movie Ratings

### How the KS Test Works

1. **Define Hypotheses**:
   - **Null Hypothesis (H0)**: The data follows the specified distribution (e.g., normal distribution).
   - **Alternative Hypothesis (H1)**: The data does not follow the specified distribution.

2. **Calculate the KS Statistic**:
   - The KS statistic measures the maximum difference between the cumulative distribution of the sample data and the cumulative distribution of the normal distribution.
   - A larger KS statistic indicates a greater deviation between the sample data and the specified distribution.

3. **P-Value**:
   - The p-value tells us if the observed difference (measured by the KS statistic) is statistically significant.
   - A low p-value (typically < 0.05) means we can reject the null hypothesis and conclude that the data does not follow a normal distribution.
   - A high p-value (typically ≥ 0.05) means we fail to reject the null hypothesis, suggesting the data may follow a normal distribution.
  
<div class="container-fluid">
  <div class="row justify-content-center bokeh-plot">
   <iframe src="/assets/htmlplot/interactive_plotly_imdbRating.html"></iframe>
  </div>
</div>

<div class="container-fluid">
  <div class="row justify-content-center bokeh-plot">
   <iframe src="/assets/htmlplot/interactive_plotly_Metacritic_Rating.html"></iframe>
  </div>
</div>

<div class="container-fluid">
  <div class="row justify-content-center bokeh-plot">
   <iframe src="/assets/htmlplot/interactive_plotly_Rotten_Tomatoes_Rating.html"></iframe>
  </div>
</div>


### Results for Each Rating Source

| Rating Source                  | KS Statistic | P-Value | Interpretation                                                                                      |
|--------------------------------|--------------|---------|-----------------------------------------------------------------------------------------------------|
| **imdbRating**                 | 0.0648       | 0.0010  | The p-value of 0.001 suggests a significant deviation from normality, indicating this rating is not normally distributed. |
| **Rotten_Tomatoes_Rating**     | 0.0834       | 0.0010  | The highest KS statistic among all ratings, with a p-value of 0.001, suggesting a pronounced deviation from normality. |
| **Metacritic_Rating**          | 0.0350       | 0.0010  | Significant deviation from normality as indicated by the low p-value.                               |

### Summary

All ratings show p-values of 0.001, indicating that none of these datasets follow a normal distribution at a 0.05 significance level. The KS statistics for each rating source reinforce this conclusion, with **Rotten_Tomatoes_Rating** showing the highest deviation from normality. These results imply that assumptions of normality may not hold for analyses on these rating distributions.


## Analysis of Ratings: Do Critics Rate European Films More Severely Than Users? And the Same for American Films?

This analysis compares IMDb ratings (from users) with Rotten Tomatoes and Metacritic ratings (from critics) to determine if critics rate European and American films more severely than users.

### Methodology
- **Separate by Continent of Production**: The analysis is conducted separately for European and American films.
- **Combined Critic Ratings**: For each continent, Rotten Tomatoes and Metacritic ratings are combined into a single "Critics" group for analysis.
- **Statistical Tests**:
  - **Independent T-Test**: Used if both IMDb (user) and combined critics' ratings are normally distributed for each continent.
  - **Mann-Whitney U Test**: Used if the data is not normally distributed for each continent.
  
### Hypotheses

- **Null Hypothesis (H0)**: There is no difference between the ratings given by critics and users for films from each continent.
- **Alternative Hypothesis (H1)**: Critics rate films more severely than users for each continent, meaning critic ratings are lower than user ratings.

### Statistical Tests in Detail

#### Independent T-Test

The **Independent T-Test** compares the means of two independent groups (in this case, user ratings vs. critic ratings) to determine if there is a statistically significant difference between them.

- **Formula**:
  $
  t = \frac{\bar{X}_1 - \bar{X}_2}{\sqrt{\frac{s_1^2}{n_1} + \frac{s_2^2}{n_2}}}
  $
  Where:
  - $\bar{X}_1$ and $\bar{X}_2$ are the sample means for the two groups (users and critics).
  - $s_1^2$ and $s_2^2$ are the variances of the two groups.
  - $n_1$ and $n_2$ are the sample sizes of the two groups.

- **Assumptions**:
  - The data for each group should be normally distributed.
  - Variances of the two groups should be equal (if not, an adjusted version of the T-Test, known as Welch's T-Test, is used).

- **Interpretation of Results**:
  - If the p-value < 0.05, we reject the null hypothesis, suggesting a significant difference in mean ratings between critics and users.
  - If the p-value ≥ 0.05, we fail to reject the null hypothesis, indicating no significant difference in mean ratings.

#### Mann-Whitney U Test

If the data is not normally distributed, the **Mann-Whitney U Test** is a non-parametric alternative that compares the distributions of the two independent groups.

- **Formula**:
  $
  U = n_1 n_2 + \frac{n_1 (n_1 + 1)}{2} - R_1
  $
  Where:
  - $U$ is the test statistic.
  - $n_1$ and $n_2$ are the sample sizes of the two groups.
  - $R_1$ is the sum of ranks for the first group (users).

- **Interpretation of Results**:
  - If the p-value < 0.05, we reject the null hypothesis, indicating a significant difference in the distributions of ratings between critics and users.
  - If the p-value ≥ 0.05, we fail to reject the null hypothesis, suggesting no significant difference in distributions.

### Interpretation of Results
- **If p-value < 0.05**: Reject the null hypothesis, suggesting that critics rate films from that continent more severely than users.
- **If p-value ≥ 0.05**: Fail to reject the null hypothesis, indicating no significant difference between user and critic ratings for films from that continent.

### Summary

- **Independent T-Test** is used if ratings for each group (user and critic) are normally distributed.
- **Mann-Whitney U Test** is used as an alternative if data is not normally distributed.


### Summary of Mann-Whitney U Test Results: Do Critics Rate Films More Severely Than Users?

This table summarizes the results of the Mann-Whitney U Test comparing user and critic ratings for European and American films.

| Continent        | Test Statistic  | P-Value                   | Interpretation                                                                                           |
|------------------|-----------------|---------------------------|----------------------------------------------------------------------------------------------------------|
| **European Films** | Mann-Whitney U | 9.99e-1       | No significant difference between critics' and users' ratings; critics and users rate European films similarly. |
| **American Films** | Mann-Whitney U | 6.65e-192                 | Significant difference; critics rate American films more severely than users.                             |


# Are European comedies juged better than american comedies



### Mann-Whitney U Test Analysis of Ratings by Continent of Production

This analysis compares the distributions of ratings for comedies produced in Europe and America using the Mann-Whitney U test. This non-parametric test is chosen because it does not assume normality, making it suitable for datasets with deviations from normal distribution or large sample sizes.

<div class="container-fluid">
  <div class="row justify-content-center bokeh-plot">
   <iframe src="/assets/htmlplot/average_ratings_by_continent_collapsed.html"></iframe>
  </div>
</div>

#### Results

| Rating Source                  | U-Statistic      | P-Value               | Interpretation                                                                                      |
|--------------------------------|------------------|-----------------------|-----------------------------------------------------------------------------------------------------|
| **imdbRating**                 | 10,555,812.5     | 3.81e-21              | Statistically significant difference in IMDb ratings between European and American-produced comedies, indicating differing rating distributions. |
| **Rotten_Tomatoes_Rating**     | 1,634,734.0      | 1.68e-39              | The most significant difference observed, showing pronounced variation in Rotten Tomatoes ratings between the two continents. |
| **Metacritic_Rating**          | 624,487.5        | 6.17e-24              | Clear statistical difference in Metacritic ratings, further supporting the hypothesis of differing rating patterns. |

#### Summary

All three rating sources show statistically significant differences between comedies produced in Europe and America, as evidenced by the very low p-values (all below 0.05). These findings suggest that the continent of production has a notable influence on how movies are rated across different platforms.

The Rotten Tomatoes ratings exhibit the most pronounced differences, followed by Metacritic and IMDb. These variations could reflect cultural differences in audience perceptions, critical standards, or other region-specific factors influencing movie ratings.

## More specific analysis

Après des analyses plus générales sur les comédies, nous avons décidé de se concentrer plus en détails sur certains sous genres de comédies pour voir en profondeur ce qui fait qu'une comédie est plus aimé qu'une autre. Pour voir cela, nous nous sommes concentrés sur l'analyse de mots et de topics pour voir si il y a une différence de sujets traités en Europe en Amérique.

Ici, on a une heatmap de ces genres qu'on a sélectionné : le top 3 sous genres le plus aimé en Europe, en Amérique et en Both. Nous avons également sélectionner ceux qui ont la plus petite différence de note entre eux et la plus grande.

<div class="container-fluid">
  <div class="row justify-content-center bokeh-plot">
    <iframe src="/assets/htmlplot/Heatmap_imdbRating.html"></iframe>
  </div>
</div>


<div class="container-fluid">
<!-- Burger -->
  <div class="row justify-content-center text-center border border-dark-subtle rounded" style="background-color:rgb(223, 162, 78)">
    <div class="col">
      <span class="display-1 copper">American Burgers vs. European Gourmet</span>
    </div>
  </div>
  <!-- <div class="row mb-4 justify-content-center">
    <div class="col-8">
      <img src="{{ '/assets/img/stand_burger.png' | relative_url }}" alt="Stand Burger" style="height: 500px;">
    </div>
  </div> -->

  <!-- Box office -->
  <div class="row justify-content-center">
    <div class="col-7">
      <iframe src="{{ '/assets/htmlplot/box_office_revenue_distribution.html' | relative_url }}" style="height: 497px;" class="border border-secondary mt-1 p-2 rounded w-100"></iframe>
    </div>
    <div class="col-5 justify-content-center align-items-center mt-1">
      <div class="d-flex justify-content-center align-items-center">
        <img src="/assets/img/Americain burger1.jpeg" alt="Americain burger1.jpeg" class="img-fluid rounded shadow" id="burger1" style="width: 45%;">
        <h2 style="margin: 0 10px;">OR</h2>
        <img src="/assets/img/Europeen burger.avif" alt="Europeen burger.avif" class="img-fluid rounded shadow" id="burger2" style="width: 45%;">
      </div>
      <p class="border border-secondary fs-6 mt-1 p-2 rounded">
        Comparing American to European humor is like contrasting a burger that looks perfect in an ad with a subtly crafted gourmet dish. American jokes hit you with all the flash of a well-marketed blockbuster, designed to grab your attention immediately. Meanwhile, European humor is more like a delicately seasoned meal that reveals its depth over time. Perhaps one day, we’ll blend these styles to cook up the ultimate comedic dish! But let's not forget, the burger is just as delicious.
      </p>
    </div>
  </div>
  <div class="row justify-content-center">
    <div id="text-container" class="col-4 m-1 border border-warning rounded" style="border 2px solid orange; background-color: rgba(255, 165, 0, 0.5); transition: all 0.5s ease;">
      <p class="p-2">Looking at the average nominations for comedy films by continent, we find that Europe leads with the finesse of a gourmet dish, accumulating nominations like a chef garners Michelin stars. On the other hand, America, with its fast-food style cinema, snags fewer nods. Perhaps the European secret lies in their subtle, critical recipe, effective in charming juries. Meanwhile, America serves its comedies like burgers: quick and tasty, but less likely to win stars. Maybe a dash of refinement in American comedies could spice up this culinary competition between continents! Well, too lazy to dive into the math, but yes, it’s a Mann-Whitney U test that confirms Europeans get nominated more often. All that for this!</p>
    </div>
    <div class="col-3">
      <iframe id="graph-frame" class="w-100 rounded" src="/assets/htmlplot/nomination_mean_by_continent.html" style="border: 2px solid black; height: 450px; transition: all 0.5s ease;"></iframe>
    </div>
    <div class="col-auto align-self-center">
      <p style="text-align: center; font-family: 'Copperplate', sans-serif; font-size: 1rem;" class="highlight">Button</p>
      <div class="arrow text-center">⬇️</div>
      <div style="text-align: center;">
        <button id="burger-button" class="highlight">🍔</button>
      </div>
    </div>
  </div>
</div>
<!-- 2. Import burger javascript code -->
<script src="{{ '/assets/js/burgers.js' | relative_url }}"></script>

<div class="container-fluid">
  <div class="row justify-content-center text-center" >
    <div class="col-8 border border-dark-subtle rounded" style="background-color:rgb(218, 112, 174);">
      <span class="display-1 copper">Opening act</span>
    </div>
  </div>
</div>

## Semantic analysis

Now let’s try to analyze the semantic aspect of our comedies. Let’s first examine the most frequently occurring nouns in movie plots from each continent. The wordclouds below offer a visual representation of these prominent terms, giving us an idea of what are the most used words in plots for each continent.

<div class="container-fluid mt-2 mb-2">
  <div class="row justify-content-center">
    <div class="col-6 rounded shadow-sm">
      <img src="{{ '/assets/img/wordclouds/America__None__NN__1.jpg' | relative_url }}" alt="General word cloud" class="img-fluid">
    </div>
    <div class="col-6 rounded shadow-sm">
      <img src="{{ '/assets/img/wordclouds/Europe__None__NN__1.jpg' | relative_url }}" alt="General word cloud" class="img-fluid">
    </div>
  </div>
</div>


Shared Themes Across Continents
Both wordclouds reveal a universal focus on family, love, and life. This shows that these themes are timeless and they resonate with audiences worldwide. Despite regional differences, the foundation of cinema in both Europe and America seems to be built on human relationships.

These wordclouds set the stage for a deeper analysis now. Even though these 2 themes are the same across continents, do they represent the same type of humor?
Using singular value decomposition (SVD), a dimension reduction technique, we can break down the underlying topics in movie plots to uncover what truly defines the narratives in each continent and how they diverge or align thematically.
Looking at the following figure, we can see the two main topics we found for each continent:



<div class="container-fluid mt-2 mb-2">
  <div class="row justify-content-center">
    <div class="col-10 rounded shadow-sm">
      <img src="{{ '/assets/img/wordclouds/topic_modeling.jpeg' | relative_url }}" alt="General word cloud" class="img-fluid">
    </div>
  </div>
</div>

### Topic 1: Relationships & Family

This theme seems to be a shared priority across both American and European films, reflecting the universality of human experiences. As we saw with the wordclouds, terms like *life, **love, **family, **friend, and **man* dominate, pointing to narratives that emphasize human connections, personal struggles, and the importance of familial bonds. 

This topic shows that both continents value storytelling that resonates emotionally, whether through romantic comedies, family dramas, or coming-of-age tales.

So *Topic 1 transcends cultural boundaries* and highlights how both regions use movies to address universal emotions and relationships. 

Now let’s try to go deeper. *Do these shared themes truly represent the same topics in the same way across both continents?*

### Topic 2: Cartoon (America) vs. War & Conflict (Europe)

The second most represented topics diverges sharply between the two regions:

#### American Films:
Focus heavily on animated slapstick comedies, with characters like *Tom and Jerry*, capturing humor through physical and exaggerated action.  
Keywords such as *tom, **jerry, **dog, **cat, and **chase* emphasize light-hearted and family-friendly cartoons that appeals to a global audience.  
This might reflect America’s preference for escapism and universally accessible humor.  
*Example film: *Tom and Jerry: The Movie (1992)

#### European Films:
Emphasize historical narratives and intellectual satire, often set in the context of war and conflict.  
Keywords like *war, **soldier, **nazi, and **village* highlight humor derived from historical and cultural reflections, showing Europe’s tendency to intertwine comedy with societal critique.  
The darker and more cerebral tone of this humor reflects Europe’s unique storytelling style, grounded in its history.  
*Example film: *Train of Life (1998)

### Comparison

American films often portray themes through light-hearted comedies, uplifting stories, or hero-centric narratives. In contrast, European films tend to explore the same themes with nuanced, introspective perspectives, often incorporating social or historical commentary.

### Conclusion

While America leans toward escapism and visual comedy, Europe’s humor often explores the deeper, more serious aspects of life, blending satire with history. This divergence in comedic styles can, in part, be attributed to Europe’s deep historical scars, particularly the profound impact of World War II. The aftermath of the war left a lasting imprint on European storytelling, where humor often serves as a coping mechanism to reflect on and critique the societal and political consequences of conflict.

These differences underline the broader cultural role of cinema: for Europe, a mirror to history and social critique; for America, a stage for universal entertainment and relief.


### Now, presenting a star of the comedy data scene… give it up for the one, the only… WORDCLOUD! 🎭

We did our analysis, but you can make it too! This interactive tool is here to help us dive into the humor-filled rivalry between American and European comedies by analyzing the words that make each side laugh. Packed with a ton of features, Wordcloud is your go-to act for cracking the linguistic code of comedy. Let’s break down its impressive setlist:

1. **Regional Filters**  
   *“Are you into the loud, slapstick humor of Hollywood or the subtle, dry wit of Europe? No worries—this tool lets you toggle between regions faster than a comedian switching accents mid-joke!”*

2. **Subsets**  
   *“Whether you want a deep dive into the 5 specific subsets we created or to look at the whole genre, you’re in control. Pick your niche, and let the tool do the rest!”*

3. **Part-of-Speech Magic**  
   *“From dynamic verbs to clever nouns and everything in between, Wordcloud unveils the grammatical building blocks of comedy. Curious about which verbs dominate American punchlines or which nouns give European humor its sophistication? It’s all just a click away!”*

4. **N-grams**  
   *“Love the power of words working together? Whether it’s single-word jokes or multi-word punchlines, the n-grams feature highlights the patterns that make comedy memorable. One-liners or elaborate setups—this tool has it covered!”*

---

Wordcloud isn’t just a tool; it’s your backstage pass to the comedy world’s linguistic secrets. Ready to uncover what makes American and European humor tick? Let Wordcloud take the stage and show you the words that bring the laughs!

---

#### 🤫 Pssst… There’s a Secret Button! 🕵️‍♀️

Hidden in plain sight, there’s a **secret button** on the Wordcloud interface. What does it do? Click it to discover! 😉

(après il faudrait faire un peu mieux le bouton et faire un easter egg marrant mais je vous avoue je galère mdr)

<script src="{{ '/assets/js/wordclouds.js' | relative_url }}"></script>
{% include wordclouds.html %}



