---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
# START COMMAND : bundle exec jekyll serve --l
# START COMMAND Pour loris: bundle exec jekyll serve --livereload
---

# The Nuances of Humor Across America and Europe

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

![Wordcloud example on the whole dataset](assets/img/wordclouds/globale_wordcloud.png)

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


# LOLO TEST 
<style>
  .hover-title {
    color: black;
    font-family: 'Arial', sans-serif;
    font-weight: bold;
  }
  .hover-title:hover::after {
    content: "➜ NOP";
    color: black;
    font-family: 'Arial', sans-serif;
    font-weight: bold;
  }
</style>

## <span class="hover-title">Very strudent group</span>
{% include team_members.html %}



<div style="font-family: 'COPPERPLATE', sans-serif; text-align: center; font-size: 1rem;">
  American Burgers vs. European Gourmet
</div>

<div class="d-flex justify-content-center">
  <iframe src="{{ '/assets/htmlplot/box_office_revenue_distribution.html' | relative_url }}" style="border: 2px solid black; width: 60%; height: 450px;"></iframe>
  <div class="d-flex flex-column justify-content-center" style="width: 35%; padding-left: 20px;">
    <div class="d-flex justify-content-center align-items-center">
      <img src="/assets/img/Americain burger.jpeg" alt="Americain burger.jpeg" class="img-fluid" id="burger1" style="width: 45%;">
      <h2 style="margin: 0 10px;">VS</h2>
      <img src="/assets/img/Europeen burger.jpeg" alt="Europeen burger.jpeg" class="img-fluid" id="burger2" style="width: 45%;">
    </div>
    <p style="font-family: 'COPPERPLATE', sans-serif; font-size: 12px; margin-top: 10px; border: 3px solid black; padding: 5px;">
      Comparing American to European humor is like contrasting a burger that looks perfect in an ad with a subtly crafted gourmet dish. American jokes hit you with all the flash of a well-marketed blockbuster, designed to grab your attention immediately. Meanwhile, European humor is more like a delicately seasoned meal that reveals its depth over time. Perhaps one day, we’ll blend these styles to cook up the ultimate comedic dish! But let's not forget, the burger is just as delicious.
    </p>
  </div>
</div>

<script>
  document.getElementById('burger1').addEventListener('mouseover', function() {
    let tempSrc = this.src;
    this.src = document.getElementById('burger2').src;
    document.getElementById('burger2').src = tempSrc;
  });
  document.getElementById('burger2').addEventListener('mouseover', function() {
    let tempSrc = this.src;
    this.src = document.getElementById('burger1').src;
    document.getElementById('burger1').src = tempSrc;
  });
</script>


<style>
  .container {
    display: flex;
    justify-content: center;
    width: 100%;
    align-items: center;
  }
  .text {
    width: 35%;
    padding-left: 20px;
    padding: 10px;
    font-family: 'Copperplate', sans-serif;
    font-size: 7pt;
    margin-left: 20px;
  }
  .button-container {
    margin-top: 20px;
  }
  button#burger-button {
    font-size: 2rem;
    border: none;
    background: none;
    cursor: pointer;
  }
  .arrow {
    position: absolute;
    top: -40px;
    left: 50%;
    transform: translateX(-50%);
    font-size: 2rem;
    animation: blink 1s infinite;
  }
  @keyframes blink {
    0%, 100% { opacity: 1; }
    50% { opacity: 0; }
  }
  .highlight {
    background-color: lightgray;
    padding: 5px;
    border-radius: 5px;
  }
</style>

<div class="container">
  <div id="text-container" class="text" style="background-color: rgba(255, 165, 0, 0.5); border: 2px solid orange; transition: all 0.5s ease;">
    <p>Looking at the average nominations for comedy films by continent, we find that Europe leads with the finesse of a gourmet dish, accumulating nominations like a chef garners Michelin stars. On the other hand, America, with its fast-food style cinema, snags fewer nods. Perhaps the European secret lies in their subtle, critical recipe, effective in charming juries. Meanwhile, America serves its comedies like burgers: quick and tasty, but less likely to win stars. Maybe a dash of refinement in American comedies could spice up this culinary competition between continents! In the end, it seems Americans might be doing just like us with this job: they throw in 3D graphs to look pretty with the help of their super powerful computers, but ultimately? Well, too lazy to dive into the math, but yes, it’s a Mann-Whitney U test that confirms Europeans get nominated more often. All that for this!</p>
  </div>
  <iframe id="graph-frame" src="/assets/htmlplot/nomination_mean_by_continent.html" style="border: 2px solid black; width: 60%; height: 450px; transition: all 0.5s ease;"></iframe>
  <div class="button-container">
    <div class="arrow">⬇️</div>
    <p style="text-align: center; font-family: 'Copperplate', sans-serif; font-size: 1rem;" class="highlight">Button</p>
    <div style="text-align: center;">
      <button id="burger-button" class="highlight">🍔</button>
    </div>
  </div>
</div>

Another one some text


<script>
  let isOriginal = true;
  document.getElementById('burger-button').addEventListener('click', function() {
    const iframe = document.getElementById('graph-frame');
    const textContainer = document.getElementById('text-container');
    if (isOriginal) {
      iframe.src = "/assets/htmlplot/nomination_distribution_by_continent.html";
      textContainer.style.backgroundColor = 'rgba(128, 0, 128, 0.5)';
      textContainer.style.border = '2px solid purple';
      textContainer.innerHTML = 'When comparing nomination rates, European comedy films seem to have a slight edge (41.16% snag at least one nomination) over their American counterparts (37.74%). But remember, this stat is like judging a restaurant’s success solely on how many reservations it gets—informative, but not the whole story. We haven’t considered other factors like audience scores or box-office earnings, which could definitely flip the script. And to spice things up, here’s the distribution of nominations after removing all outliers. Of course, we subtly favored the French, as one must in any respectable culinary competition. After all, if you\'re not a bit biased, are you even playing the game?';
    } else {
      iframe.src = "/assets/htmlplot/nomination_mean_by_continent.html";
      textContainer.style.backgroundColor = 'rgba(255, 165, 0, 0.5)';
      textContainer.style.border = '2px solid orange';
      textContainer.innerHTML = 'Looking at the average nominations for comedy films by continent, we find that Europe leads with the finesse of a gourmet dish, accumulating nominations like a chef garners Michelin stars. On the other hand, America, with its fast-food style cinema, snags fewer nods. Perhaps the European secret lies in their subtle, critical recipe, effective in charming juries. Meanwhile, America serves its comedies like burgers: quick and tasty, but less likely to win stars. Maybe a dash of refinement in American comedies could spice up this culinary competition between continents! In the end, it seems Americans might be doing just like us with this job: they throw in 3D graphs to look pretty with the help of their super powerful computers, but ultimately? Well, too lazy to dive into the math, but yes, it’s a Mann-Whitney U test that confirms Europeans get nominated more often. All that for this!';
    }
    isOriginal = !isOriginal;
  });
</script>

<!-- These are example components, inspire from them to add new content -->
{% include examples.md %}
