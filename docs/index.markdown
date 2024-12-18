---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
# START COMMAND : bundle exec jekyll serve -l
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


# LOLO TEST


## <span class="hover-title">Very strudent group</span>
{% include team_members.html %}

<!-- 1. Html code for burgers -->
<div style="font-family: 'COPPERPLATE', sans-serif; text-align: center; font-size: 1rem;">
  American Burgers vs. European Gourmet
</div>
<div class="container-fluid">
  <div class="row justify-content-center">
    <div class="col-7">
      <iframe src="{{ '/assets/htmlplot/box_office_revenue_distribution.html' | relative_url }}" style="height: 450px;" class="border border-secondary mt-1 p-2 rounded w-100"></iframe>
    </div>
    <div class="col-5 justify-content-center align-items-center mt-1">
      <div class="d-flex justify-content-center align-items-center">
        <img src="/assets/img/Americain burger.jpeg" alt="Americain burger.jpeg" class="img-fluid rounded shadow" id="burger1" style="width: 45%;">
        <h2 style="margin: 0 10px;">VS</h2>
        <img src="/assets/img/Europeen burger.jpeg" alt="Europeen burger.jpeg" class="img-fluid rounded shadow" id="burger2" style="width: 45%;">
      </div>
      <p style="font-family: 'COPPERPLATE', sans-serif; font-size: 12px;" class="border border-secondary mt-1 p-2 rounded">
        Comparing American to European humor is like contrasting a burger that looks perfect in an ad with a subtly crafted gourmet dish. American jokes hit you with all the flash of a well-marketed blockbuster, designed to grab your attention immediately. Meanwhile, European humor is more like a delicately seasoned meal that reveals its depth over time. Perhaps one day, we’ll blend these styles to cook up the ultimate comedic dish! But let's not forget, the burger is just as delicious.
      </p>
    </div>
  </div>
  <div class="row justify-content-center">
    <div id="text-container" class="col-4" style="background-color: rgba(255, 165, 0, 0.5); border: 2px solid orange; border-radius: 5px; transition: all 0.5s ease;">
      <p>Looking at the average nominations for comedy films by continent, we find that Europe leads with the finesse of a gourmet dish, accumulating nominations like a chef garners Michelin stars. On the other hand, America, with its fast-food style cinema, snags fewer nods. Perhaps the European secret lies in their subtle, critical recipe, effective in charming juries. Meanwhile, America serves its comedies like burgers: quick and tasty, but less likely to win stars. Maybe a dash of refinement in American comedies could spice up this culinary competition between continents! In the end, it seems Americans might be doing just like us with this job: they throw in 3D graphs to look pretty with the help of their super powerful computers, but ultimately? Well, too lazy to dive into the math, but yes, it’s a Mann-Whitney U test that confirms Europeans get nominated more often. All that for this!</p>
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


---

<!-- These are example components, inspire from them to add new content -->
{% include examples.md %}
