---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default

# START COMMAND : bundle exec jekyll serve -l
# START COMMAND Pour loris: bundle exec jekyll serve --livereload
---
<!-- titre image  -->
![Titre](assets/img/Titre.png)

Add a bokeh plot :


<div class="container-fluid">
  <div class="row justify-content-center bokeh-plot">
   <iframe src="/assets/htmlplot/heatmap.html"></iframe>
  </div>
</div>

<!-- team member  -->

<div class="container-fluid">
  <div class="row justify-content-center text-center border border-dark-subtle rounded" style="background-color:rgb(193, 178, 185)">
    <div class="col">
      <span class="display-1">The circus squad</span>
    </div>
  </div>
</div>

<div style="position: relative; text-align: center; color: white;">
  <img src="/assets/img/bandrole.png" alt="Bandrole" style="width: 100%; height: auto; border-radius: 0px;">
  <div style="position: absolute; bottom: 15%; left: 50%; transform: translateX(-50%); padding: 10px; border-radius: 5px; display: flex; justify-content: center; align-items: center; flex-wrap: nowrap;">
    <div style="display: flex; flex-direction: row;">
      {% include team_members.html %}
    </div>
  </div>
</div>






<!-- barbe à papa -->
  <html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Interactive Image</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f9f9f9;
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        text-align: center;
      }
      h1 {
        font-family: 'Copperplate', 'Copper Black', serif;
        font-size: 3em;
        color: #333;
        margin-bottom: 40px;
        width: 100%;
      }
      .content {
        display: flex;
        align-items: center;
        gap: 40px;
        max-width: 1200px;
      }
      .image-container {
        position: relative;
        width: 300px;
        height: auto;
      }
      .image-container img {
        width: 100%;
        height: auto;
        transition: opacity 0.3s ease-in-out;
      }
      .image-container img.second-image {
        display: none;
        position: absolute;
        top: 0;
        left: 0;
        transform: translateY(-45%);
      }
      .image-container:hover img.first-image {
        display: none;
      }
      .image-container:hover img.second-image {
        display: block;
      }
      .text {
        max-width: 1000px;
        font-size: 1em;
        color: #444;
        font-family: Arial, sans-serif;
        text-align: left;
      }
    </style>
  </head>
  <body>
    <div>
      <div style="background-color: #ffe6f2; padding: 20px; border-radius: 10px; text-align: center;">
        <h1 style="text-align: center;">Take it with a grain of sugar</h1>
      </div>
      <div class="content">
        <div class="image-container">
          <img src="assets/img/Barbe1.png" alt="Cotton Candy" class="first-image">
          <img src="assets/img/Barbe2.png" alt="Cotton Candy Hover" class="second-image">
        </div>
        <div class="text">
          <p>
            The <strong>CMU Movie Summary Corpus</strong>, our trusty stick 🍭, holds the essential ingredients for our cinematic cotton candy: plot summaries, genres, countries, and languages of movies. To make it even tastier, we sprinkled it with sweet data from the <strong>OMDB API</strong> 🍬, adding flavors like <strong>ratings</strong> (IMDb, Rotten Tomatoes, Metascore), <strong>posters</strong>, <strong>age classifications (Rated)</strong>, and <strong>awards</strong>. Some of these layers even needed a little "reshaping" to avoid getting too sticky!
          </p>
          <p>
            Meanwhile, with the help of the <strong>CoreNLP pipeline</strong>, we spun the plot summaries like a real cotton candy machine, pulling linguistic threads to enrich our analysis. That said, some layers, like actor metadata (gender, age...) and other CMU treats, were left aside—like leftover sugar at the bottom of the vat 🍯.
          </p>
        </div>
      </div>
    </div>
  </body>






<!-- Burger -->
  <div style="background-color:rgb(223, 162, 78); padding: 20px; border-radius: 10px; text-align: center;">
  <h1 style="text-align: center;">American Burgers vs. European Gourmet</h1>
  </div>
  <div style="text-align: center;">
    <img src="/assets/img/stand_burger.png" alt="Stand Burger" style="width: 50%; height: auto;">
  </div>

<div class="container-fluid">
  <div class="row justify-content-center">
    <div class="col-7">
      <iframe src="{{ '/assets/htmlplot/box_office_revenue_distribution.html' | relative_url }}" style="height: 450px;" class="border border-secondary mt-1 p-2 rounded w-100"></iframe>
    </div>
    <div class="col-5 justify-content-center align-items-center mt-1">
      <div class="d-flex justify-content-center align-items-center">
        <img src="/assets/img/Americain burger1.jpeg" alt="Americain burger1.jpeg" class="img-fluid rounded shadow" id="burger1" style="width: 45%;">
        <h2 style="margin: 0 10px;">OR</h2>
        <img src="/assets/img/Europeen burger.avif" alt="Europeen burger.avif" class="img-fluid rounded shadow" id="burger2" style="width: 45%;">
      </div>
      <p style="font-family: 'COPPERPLATE', sans-serif; font-size: 12px;" class="border border-secondary mt-1 p-2 rounded">
        Comparing American to European humor is like contrasting a burger that looks perfect in an ad with a subtly crafted gourmet dish. American jokes hit you with all the flash of a well-marketed blockbuster, designed to grab your attention immediately. Meanwhile, European humor is more like a delicately seasoned meal that reveals its depth over time. Perhaps one day, we’ll blend these styles to cook up the ultimate comedic dish! But let's not forget, the burger is just as delicious.
      </p>
    </div>
  </div>
  <div class="row justify-content-center">
    <div id="text-container" class="col-4" style="background-color: rgba(255, 255, 255, 0.95); border: 2px solid orange; border-radius: 5px; transition: all 0.5s ease;">
      <p>Looking at the average nominations for comedy films by continent, we find that Europe leads with the finesse of a gourmet dish, accumulating nominations like a chef garners Michelin stars. On the other hand, America, with its fast-food style cinema, snags fewer nods. Perhaps the European secret lies in their subtle, critical recipe, effective in charming juries. Meanwhile, America serves its comedies like burgers: quick and tasty, but less likely to win stars. Maybe a dash of refinement in American comedies could spice up this culinary competition between continents! Well, too lazy to dive into the math, but yes, it’s a Mann-Whitney U test that confirms Europeans get nominated more often. All that for this!</p>
    </div>
    <div class="col-6">
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


<div style="background-color:rgb(218, 112, 174); padding: 20px; border-radius: 10px; text-align: center;">
<h1 style="text-align: center;">Opening act</h1>
</div>


<div style="text-align: center; font-family: 'Park Avenue', cursive;">
  In our database, the "Genres" column was like a chaotic junk drawer full of random labels such as "World Cinema," "Short Film," or "Indie." 🗂️ These were about as useful as a punchline without a joke – confusing and totally unhelpful for analyzing comedy! 🤔

  So, as true comedy enthusiasts 🎭😂, we rolled up our sleeves (and flexed our funny bones) to bring some order to the madness. Instead of trying to decode this mess, we decided to create our own subcategories to dive deeper into the delightful world of different types of comedy. 🕵️‍♂️🎬

  To make it happen, we developed a magical dictionary 🪄📖 (sadly, it doesn’t talk… yet) that groups specific keywords linked to various comedy subgenres. With this genius tool, we can now automatically sort films into categories like "Comedy_Romance," "Comedy_Action," "Comedy_Animation," and many more. 🎉✨

  For example, any film that dares to drop words like "romantic" or "romance" gets whisked straight into "Comedy_Romance." 💘😂 Meanwhile, those whispering terms like "animated" or "anime" are promptly filed under "Comedy_Animation." 🎨🤪 In short, we’ve turned a big ol’ mess into a well-organized laugh factory. And guess what? We’re having a blast doing it! 🎉🤣
</div>




<div style="text-align: center; position: relative; left: 15%; transform: scale(0.6);">
  <img src="/assets/img/Bouche_fermée.png" alt="Bouche fermée" style="position: absolute; top: -40%; left: -20%; width: 700%; height: 200%; z-index: 1; transition: opacity 0.3s ease-in-out;" onmouseover="this.style.display='none';">
  <img src="/assets/img/Bouche_ouverte.png" alt="Bouche ouverte" style="position: absolute; top: -40%; left: -20%; width: 700%; height: 170%; z-index: -1 ; opacity: 0; transition: opacity 0.3s ease-in-out;" onmouseover="this.style.opacity=1;">
  <!-- 1. Load the html template -->
  {% include movies_genres.html %}
  <!-- 2. Load the associated javascript -->
  <script src="{{ '/assets/js/movies_genres.js' | relative_url }}"></script>
</div>






























## Part 1 : Introduction

## Part 2 : Presentation




In our database, we noticed that the "Genres" column contained many descriptions that were not particularly relevant to our subject, such as "World Cinema," "Short Film," or "Indie." These categories did not provide meaningful information about the type of comedy, making the analysis more confusing. As enthusiasts of humorous films, we decided to restructure this classification to create our own subcategories, allowing for a deeper exploration of the different types of comedies available.

To achieve this, we developed a dictionary that groups specific keywords associated with various comedy subgenres. These keywords enable us to automatically reorganize and identify films into categories such as "Comedy_Romance," "Comedy_Action," "Comedy_Animation," and many others. For instance, films containing words like "romantic" or "romance" are categorized under "Comedy_Romance," while those with terms like "animated" or "anime" are classified under "Comedy_Animation."

<!-- 1. Load the html template -->
{% include movies_genres.html %}
<!-- 2. Load the associated javascript -->
<script src="{{ '/assets/js/movies_genres.js' | relative_url }}"></script>


## Wordclouds

### Now, presenting a star of the comedy data scene… give it up for the one, the only… WORDCLOUD! 🎭

<div class="container-fluid mt-2 mb-2">
  <div class="row justify-content-center">
    <div class="col-6 rounded shadow-sm">
      <img src="{{ '/assets/img/wordclouds/globale_wordcloud.png' | relative_url }}" alt="General word cloud" class="img-fluid">
    </div>
  </div>
</div>

This interactive tool is here to help us dive into the humor-filled rivalry between American and European comedies by analyzing the words that make each side laugh. Packed with a ton of features, Wordcloud is your go-to act for cracking the linguistic code of comedy. Let’s break down its impressive setlist:

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



  <div style="text-align: center;">
    <img src="/assets/img/Haut carousel.png" alt="Haut carousel" style="width: 50%; height: auto;">
  </div>
  <style>
    .rotating-image {
      animation: rotation 10s infinite linear;
    }

    @keyframes rotation {
      from {
        transform: rotate(0deg);
      }
      to {
        transform: rotate(360deg);
      }
    }
  </style>
  <div class="container-fluid" style="text-align: center;">
    <div class="row justify-content-center">
      <div class="col-12">
        {% include carousel2.html %}
      </div>
    </div>

  <div style="text-align: center;">
    <img src="/assets/img/Bas carousel.png" alt="Bas carousel" style="width: 50%; height: auto;">




# LOLO TEST


---

<!-- These are example components, inspire from them to add new content -->
{% include examples.md %}
