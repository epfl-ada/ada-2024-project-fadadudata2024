---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default

# START COMMAND : bundle exec jekyll serve -l
# START COMMAND Pour loris: bundle exec jekyll serve --livereload
---
<!-- titre image  -->

<div class="big-image-wrapper">
  <img src="{{ '/assets/img/circus_lion.png' | relative_url }}" alt="Alternative text" class="big-image shadow shadow-lg">
</div>
<div class="big-image-spacer"></div>



<div class="container-fluid">
  <div class="row justify-content-center">
    <div class="col-8 text-justify">
      <h2>Abstract</h2>
    </div>
  </div>
  <div class="row mb-5 justify-content-center">
    <div class="col-8 text-justify">
    This project takes a dive into the comedic rivalry between American and European films, uncovering the cultural quirks that make each side laugh. Using data from the CMU Movie Summary Corpus and OMDB, we analyze recurring themes, linguistic styles, and narrative structures to decode the essence of humor on both sides of the Atlantic. Do Americans favor slapstick and sarcasm, while Europeans lean toward dry wit and intellectual wordplay? Are certain jokes universal, or do some fall flat across cultural divides? We also explore representation dynamics—examining how gender and ethnicity shape the humor landscape—and investigate box office trends to see if Hollywood's blockbuster comedies outshine Europe's subtler charm. Through text analysis, visualizations, and linguistic modeling, this project aims to answer whether humor truly transcends borders or remains firmly rooted in cultural context. Laugh, learn, and decide which side of the Atlantic rules the comedy game!
    </div>
  </div>

  <div class="row justify-content-center text-center border border-dark-subtle rounded" style="background-color:rgb(193, 178, 185)">
    <div class="col-md-12">
      <span class="display-1 copper">The circus squad</span>
    </div>
  </div>
  <div class="row justify-content-center">  
    <div style="position: relative; text-align: center; color: white; width: 1100px">
      <img src="/assets/img/circus_banner.png" alt="Bandrole" style="width: 1100px; height: auto; border-radius: 0px;">
      <div style="position: absolute; bottom: 17%; display: flex; justify-content: center; align-items: center; flex-wrap: nowrap; left: 103px;">
        <div style="display: flex; flex-direction: row;">
          {% include team_members.html %}
        </div>
      </div>
    </div>
  </div>
</div>


<div class="container-fluid">
  <div class="row justify-content-center text-center">
    <div class="col-12 text-center border border-dark-subtle rounded" style="background-color:#ffe6f2">
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
    <div class="col-6 text-justify">
          <p class="mt-2">
            The <strong>CMU Movie Summary Corpus</strong>, our trusty stick 🍭, holds the essential ingredients for our cinematic cotton candy: plot summaries, genres, countries, and languages of movies. To make it even tastier, we sprinkled it with sweet data from the <strong>OMDB API</strong> 🍬, adding flavors like <strong>ratings</strong> (IMDb, Rotten Tomatoes, Metascore), <strong>posters</strong>, <strong>age classifications (Rated)</strong>, and <strong>awards</strong>. Some of these layers even needed a little "reshaping" to avoid getting too sticky!
          </p>
          <p>
            Meanwhile, with the help of the <strong>CoreNLP pipeline</strong>, we spun the plot summaries like a real cotton candy machine, pulling linguistic threads to enrich our analysis. That said, some layers, like actor metadata (gender, age...) and other CMU treats, were left aside—like leftover sugar at the bottom of the vat 🍯.
          </p>
    </div>
  </div>
</div>

<div class="container-fluid mt-5 mb-2">
  <div class="row justify-content-center text-center" >
    <div class="col-8 border border-dark-subtle rounded" style="background-color:rgb(218, 112, 174);">
      <span class="display-1 copper">Opening act</span>
    </div>
  </div>
</div>

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


<div class="container-fluid">
  <div class="row justify-content-center text-center border border-dark-subtle rounded" style="background-color:rgb(193, 178, 185)">
    <div class="col-md-12">
      <span class="display-1 copper">A carousel of Tests</span>
    </div>
  </div>
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
    <div class="col-5 align-content-center">
      <p style="text-align: justify;">Welcome to the test carousel, an interactive space designed to guide you through the core statistical tools used to analyze and understand datasets. This carousel is not just a collection of definitions but a roadmap for tackling complex data questions systematically and effectively.</p>
      <p style="text-align: justify;">The carousel introduces statistical concepts tailored for different aspects of analysis. The KS Test helps determine whether a dataset follows a specific distribution, such as the normal distribution. The Independent T-Test compares the means of two independent groups to assess whether the differences are statistically significant or due to random variation. For data that doesn’t meet the assumption of normality, the Mann-Whitney U Test offers a non-parametric alternative by comparing distributions between two independent groups. Lastly, Confidence Intervals go beyond hypothesis testing, providing an estimated range where the true population parameter is likely to fall, helping quantify the reliability and precision of your estimates.</p>
      <p style="text-align: justify;">Each section of the carousel follows a consistent structure, making it easier to understand and apply the concepts. It provides an explanation, defines the hypotheses, lists the assumptions, guides interpretation of the results, and includes the mathematical formula for deeper exploration.</p>
    </div>
  </div>
</div>


## The rating of the comedies : critics vs users

<div class="container-fluid">
  <div class="row">
    <div class="col-6">
    <p style="text-align: justify;">To better analyze comedies and understand humor from different perspectives, we categorized ratings into three main groups of viewers: general spectators, professional critics, and evaluation experts. Each group offers a unique perspective, allowing us to explore differences in humor appreciation based on their roles and experiences.</p>
    <p style="text-align: justify;">- <strong>The Spectators</strong>: Represented by public ratings on IMDb, these reviews reflect a broad and popular perception of humor, offering direct insights from the general audience.</p>
    <p style="text-align: justify;">- <strong>The Critics' Panel</strong>: Ratings from Rotten Tomatoes (Tomatometer) aggregate opinions from professional critics. These bring a more technical and structured analysis of humorous content.</p>
    <p style="text-align: justify;">- <strong>The Evaluation Experts</strong>: Aggregated scores from Metacritic provide another professional perspective, combining various critical viewpoints to form a balanced and synthesized evaluation.</p>
    </div>
    <div class="col-6">
      <table style="width: 100%; border-collapse: collapse; text-align: left;">
        <thead>
          <tr style="background-color: rgb(180, 74, 58); color: white;">
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
            <td style="border: 1px solid #ddd; padding: 8px">Represents the Tomatometer score, an aggregated rating from professional critics.</td>
          </tr>
          <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">The Master of Ceremony</td>
            <td style="border: 1px solid #ddd; padding: 8px;">Metacritic Rating</td>
            <td style="border: 1px solid #ddd; padding: 8px;">Critics</td>
            <td style="border: 1px solid #ddd; padding: 8px;">Aggregated rating from professional critics, provided by Metacritic.</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</div>

<div class="container-fluid">
  <div class="row justify-content-center">
    <div class="col-6">
      <div class="ratings-plot-ctn">
        <img src="/assets/img/imdb_plot.png" alt="IMDB Ratings" class="plots-ratings">
        <img src="/assets/img/Carte.jpeg" alt="Carte 1" class="card-plots">
      </div>
    </div>
    <div class="col-6">
      <div class="ratings-plot-ctn">
        <img src="/assets/img/rottentom_plot.png" alt="Rotten Tomatoes Ratings" class="plots-ratings">
        <img src="/assets/img/Carte.jpeg" alt="Carte 2" class="card-plots">
      </div>
    </div>
    <div class="col-6">
      <div class="ratings-plot-ctn">
        <img src="/assets/img/metacritic_plot.png" alt="Metacritic Ratings" class="plots-ratings">
        <img src="/assets/img/Carte.jpeg" alt="Carte 3" class="card-plots">
      </div>
    </div>
  </div>
</div>


### Results for Each Rating Source

<div class="container-fluid">
  <div class="row">
    <div class="col-6">
      <table style="width: 100%; border-collapse: collapse; text-align: left;">
        <thead>
          <tr style="background-color: rgb(180, 74, 58); color: white;">
            <th style="border: 1px solid #ddd; padding: 8px;">Rating Source</th>
            <th style="border: 1px solid #ddd; padding: 8px;">KS Statistic</th>
            <th style="border: 1px solid #ddd; padding: 8px;">P-Value</th>
            <th style="border: 1px solid #ddd; padding: 8px;">Interpretation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">Imdb Rating</td>
            <td style="border: 1px solid #ddd; padding: 8px;">0.0648</td>
            <td style="border: 1px solid #ddd; padding: 8px;">0.0010</td>
            <td style="border: 1px solid #ddd; padding: 8px;">The p-value of 0.001 suggests a significant deviation from normality, indicating this rating is not normally distributed.</td>
          </tr>
          <tr style="background-color: #f2f2f2;">
            <td style="border: 1px solid #ddd; padding: 8px;">Rotten Tomatoes Rating</td>
            <td style="border: 1px solid #ddd; padding: 8px;">0.0834</td>
            <td style="border: 1px solid #ddd; padding: 8px;">0.0010</td>
            <td style="border: 1px solid #ddd; padding: 8px;">The highest KS statistic among all ratings, with a p-value of 0.001, suggesting a pronounced deviation from normality.</td>
          </tr>
          <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">Metacritic Rating</td>
            <td style="border: 1px solid #ddd; padding: 8px;">0.0350</td>
            <td style="border: 1px solid #ddd; padding: 8px;">0.0010</td>
            <td style="border: 1px solid #ddd; padding: 8px;">Significant deviation from normality as indicated by the low p-value.</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="col-6">
      <p style="text-align: justify;">To better analyze comedies and understand humor from different perspectives, we categorized ratings into three main groups of viewers: general spectators, professional critics, and evaluation experts. Each group offers a unique perspective, allowing us to explore differences in humor appreciation based on their roles and experiences.</p>
      <p style="text-align: justify;">All ratings show p-values of 0.001, indicating that none of these datasets follow a normal distribution at a 0.05 significance level. The KS statistics for each rating source reinforce this conclusion, with Rotten Tomatoes Rating showing the highest deviation from normality. These results imply that assumptions of normality may not hold for analyses on these rating distributions.</p>
    </div>
  </div>
</div>


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


### Summary of Mann-Whitney U Test Results: Do Critics Rate Films More Severely Than Users?

This table summarizes the results of the Mann-Whitney U Test comparing user and critic ratings for European and American films.

| Continent        | Test Statistic  | P-Value                   | Interpretation                                                                                           |
|------------------|-----------------|---------------------------|----------------------------------------------------------------------------------------------------------|
| **European Films** | Mann-Whitney U | 9.99e-1       | No significant difference between critics' and users' ratings; critics and users rate European films similarly. |
| **American Films** | Mann-Whitney U | 6.65e-192                 | Significant difference; critics rate American films more severely than users.                             |


## Are European comedies judged better than American comedies

<div class="container-fluid">
  <div class="row">
    <div class="col-4">
      <h3>Mann-Whitney U Test Analysis of Ratings by Continent of Production</h3>
      <p style="text-align: justify;">This analysis compares the distributions of ratings for comedies produced in Europe and America using the Mann-Whitney U test. This non-parametric test is chosen because it does not assume normality, making it suitable for datasets with deviations from normal distribution or large sample sizes.</p>
    </div>
    <div class="col-8">
      <div class="container-fluid">
        <div class="row justify-content-center bokeh-plot">
          <iframe src="/assets/htmlplot/average_ratings_by_continent_collapsed.html"></iframe>
        </div>
      </div>
    </div>
  </div>

  <div class="row">
    <div class="col-6">
      <h4>Results</h4>
      <table style="width: 100%; border-collapse: collapse; text-align: left;">
        <thead>
          <tr style="background-color: rgb(180, 74, 58); color: white;">
            <th style="border: 1px solid #ddd; padding: 8px;">Rating Source</th>
            <th style="border: 1px solid #ddd; padding: 8px;">U-Statistic</th>
            <th style="border: 1px solid #ddd; padding: 8px;">P-Value</th>
            <th style="border: 1px solid #ddd; padding: 8px;">Interpretation</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">**imdbRating**</td>
            <td style="border: 1px solid #ddd; padding: 8px;">10,555,812.5</td>
            <td style="border: 1px solid #ddd; padding: 8px;">3.81e-21</td>
            <td style="border: 1px solid #ddd; padding: 8px;">Statistically significant difference in IMDb ratings between European and American-produced comedies, indicating differing rating distributions.</td>
          </tr>
          <tr style="background-color: #f2f2f2;">
            <td style="border: 1px solid #ddd; padding: 8px;">**Rotten_Tomatoes_Rating**</td>
            <td style="border: 1px solid #ddd; padding: 8px;">1,634,734.0</td>
            <td style="border: 1px solid #ddd; padding: 8px;">1.68e-39</td>
            <td style="border: 1px solid #ddd; padding: 8px;">The most significant difference observed, showing pronounced variation in Rotten Tomatoes ratings between the two continents.</td>
          </tr>
          <tr>
            <td style="border: 1px solid #ddd; padding: 8px;">**Metacritic_Rating**</td>
            <td style="border: 1px solid #ddd; padding: 8px;">624,487.5</td>
            <td style="border: 1px solid #ddd; padding: 8px;">6.17e-24</td>
            <td style="border: 1px solid #ddd; padding: 8px;">Clear statistical difference in Metacritic ratings, further supporting the hypothesis of differing rating patterns.</td>
          </tr>
        </tbody>
      </table>
    </div>
    <div class="col-6">
      <h4>Summary</h4>
      <p style="text-align: justify;">All three rating sources show statistically significant differences between comedies produced in Europe and America, as evidenced by the very low p-values (all below 0.05). These findings suggest that the continent of production has a notable influence on how movies are rated across different platforms.</p>
      <p style="text-align: justify;">The Rotten Tomatoes ratings exhibit the most pronounced differences, followed by Metacritic and IMDb. These variations could reflect cultural differences in audience perceptions, critical standards, or other region-specific factors influencing movie ratings.</p>
    </div>
  </div>
</div>
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
      <span class="display-3 copper">American Burgers vs. European Gourmet</span>
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
    <div id="text-container" class="col-5 border border-warning rounded" style="border 2px solid orange; background-color: rgba(255, 165, 0, 0.5); transition: all 0.5s ease;">
      <p class="p-2">Looking at the average nominations for comedy films by continent, we find that Europe leads with the finesse of a gourmet dish, accumulating nominations like a chef garners Michelin stars. On the other hand, America, with its fast-food style cinema, snags fewer nods. Perhaps the European secret lies in their subtle, critical recipe, effective in charming juries. Meanwhile, America serves its comedies like burgers: quick and tasty, but less likely to win stars. Maybe a dash of refinement in American comedies could spice up this culinary competition between continents! Well, too lazy to dive into the math, but yes, it’s a Mann-Whitney U test that confirms Europeans get nominated more often. All that for this!</p>
    </div>
    <div class="col-6">
      <img id="graph-frame" class="w-100 rounded" src="/assets/img/nomination_plot.png" style="border: 2px solid black; height: 450px; transition: all 0.5s ease;">
    </div>
    <div class="col-1 align-self-center">
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

<div class="container-fluid mt-5 mb-2">
  <div class="row justify-content-center text-center border border-dark-subtle rounded" style="background-color:rgb(98, 176, 170)">
    <div class="row justify-content-center">
      <div class="col">
        <span class="display-4 copper">Ticket Booth - Adults and Kids for the Circus</span>
      </div>
    </div>
  </div>

  <div class="row mt-1 mb-2 justify-content-center">
    <div class="col-5 align-self-end">
      <img src="/assets/img/Guichet.jpeg" alt="Guichet" class="img-fluid rounded shadow">
    </div>
    <div class="col-7">
      <div class="image-container-tikets">
        <iframe src="/assets/htmlplot/mean_imdb_rating.html" class="plot-frame"></iframe>
      </div>
    </div>
  </div>
</div>

Step right up, ladies and gentlemen, to the great comedy showdown of the continents! 🎪 On my left, the United States, a land of comedies filled with visual humor, absurd situations, and accessible jokes that appeal to wide audiences. 🐶🐱 On my right, Europe, home to more adult comedies, Rated 16+, where humor often comes with satire, historical reflections, or deep social critiques. 🎭✨
But here’s the twist: we might have expected American films to dominate the Rated 13+ category... yet that’s not the case! Both continents seem to share a focus on broad, accessible humor aimed at families or younger audiences. The real difference emerges in the Rated 16+ category.
In this space, Europe clearly stands out. European comedies dive into darker, more subtle, or intellectual themes, often requiring more life experience or reflection to fully appreciate.
But let’s not forget, this is just a trend! 🧂 IMDb ratings can be subjective, influenced by different types of viewers, and should be taken with a grain of salt. Still, one thing is evident: European comedies tend to be more appreciated overall.
So, which ticket will you choose? The universal, accessible humor of the United States or Europe’s more refined and thought-provoking style? Either way, laughs are guaranteed... but the data suggests Europe often wins the audience’s favor. ❤️
And just below, you’ll find a plot breaking down the different sub-genres of comedy to confirm these observations, with data to back it up! 📊🎥"
<div class="container-fluid mt-3 mb-2">
  <div class="row g-0 justify-content-center" style="background-color: #f0f0f0; padding: 10px; border-radius: 5px;">
    <div class="col-6">
      <iframe src="/assets/htmlplot/interactive_heatmap_europe.html" style="width: 550px; height: 500px;"></iframe>
    </div>
    <div class="col-6">
      <iframe src="/assets/htmlplot/interactive_heatmap_america.html" style="width: 550px; height: 500px;"></iframe>
    </div>
  </div>
</div>
