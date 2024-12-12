---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---
# Comparative analysis between USA and European comedy 

# START COMMAND : bundle exec jekyll serve --l


Some base text in here

## Part xghfhgcfhgfhgf

Some other text here.

Here is how to add a plot :

<!-- ATTENTION il faut que 'basic-plot' corresponde à l'argument de newPlot() dans basic_plot.js !! -->
<div id="basic-plot" style="width: 620px; height: 420px;"></div>
<script src="{{ '/assets/js/basic_plot.js' | relative_url }}"></script>


## Movie carousel

<div class="container-fluid">
  <div class="row justify-content-center">
    <div class="col-8">
      <p>Some text here</p>
    </div>
    <div class="col-4">
      {% include carousel.html %}
    </div>
  </div>
</div>

Here is how to add simple tabs :

<div class="container mt-2 mb-2">
  <ul class="nav nav-underline" id="sampleTabs" role="tablist">
    <li class="nav-item" role="presentation">
      <button class="nav-link active" id="europe-wordcloud-tab" data-bs-toggle="tab" data-bs-target="#europe-wordcloud" type="button" role="tab" aria-controls="europe-wordcloud" aria-selected="true">
        Europe
      </button>
    </li>
    <li class="nav-item" role="presentation">
      <button class="nav-link" id="america-wordcloud-tab" data-bs-toggle="tab" data-bs-target="#america-wordcloud" type="button" role="tab" aria-controls="america-wordcloud" aria-selected="false">
        North America
      </button>
    </li>
  </ul>

  <div class="tab-content mt-3" id="sampleTabsContent">
    <div class="tab-pane fade show active" id="europe-wordcloud" role="tabpanel" aria-labelledby="europe-wordcloud-tab">
      <div class="card w-25">
        <img src="{{ '/assets/img/test1.jpg' | relative_url }}" alt="Image 1" class="card-img-top">
        <div class="card-body">
          <h4 class="card-title">Some more text here </h4>
          <p class="card-text">Description</p>
        </div>
      </div>
    </div>
    <div class="tab-pane fade" id="america-wordcloud" role="tabpanel" aria-labelledby="america-wordcloud-tab">
      <div class="card w-25">
      <img src="{{ '/assets/img/test2.jpg' | relative_url }}" alt="Image 2" class="card-img-top">
        <div class="card-body">
          <h4 class="card-title">Some more text here </h4>
          <p class="card-text">Description</p>
        </div>
      </div>
    </div>
  </div>
</div>

Exemple : pour réajouter une "IMPACT IMAGE" (toute la largeur, ici c'est la banner mais il suffit de changer src)

<div class="big-image-wrapper">
  <img src="{{ '/assets/img/banner.jpg' | relative_url }}" alt="Alternative text" class="big-image">
</div>
<div class="big-image-spacer"></div>


## Wordclouds

### Now, presenting a star of the comedy data scene… give it up for the one, the only… WORDCLOUD! 🎭

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
<div class="container-fluid">
  <div class="row" id="wordclouds">
    <div class="col align-content-center">
      <div class="btn-group  w-100">
        <button type="button" class="btn btn-info dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
          Region
        </button>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#wordclouds" onclick="on_wordcloud_filter_change({key: 'region', value: 'Europe'})">Europe</a></li>
          <li><a class="dropdown-item" href="#wordclouds" onclick="on_wordcloud_filter_change({key: 'region', value: 'America'})">America</a></li>
          <li><hr class="dropdown-divider"></li>
          <li><a class="dropdown-item" href="#wordclouds" onclick="on_wordcloud_filter_change({key: 'region', value: 'Both'})">Both</a></li>
        </ul>
      </div>
    </div>
    <div class="col align-content-center">
      <div class="btn-group  w-100">
        <button type="button" class="btn btn-info dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
          Subsets
        </button>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#wordclouds" onclick="on_wordcloud_filter_change({key: 'subset', value: 'Biggest_America'})">Biggest_America</a></li>
          <li><a class="dropdown-item" href="#wordclouds" onclick="on_wordcloud_filter_change({key: 'subset', value: 'Biggest_Both'})">Biggest_Both</a></li>
          <li><a class="dropdown-item" href="#wordclouds" onclick="on_wordcloud_filter_change({key: 'subset', value: 'Biggest_Europe'})">Biggest_Europe</a></li>
          <li><a class="dropdown-item" href="#wordclouds" onclick="on_wordcloud_filter_change({key: 'subset', value: 'Biggest_Gap_diff_Eu_Am'})">Biggest_Gap_diff_Eu_Am</a></li>
          <li><a class="dropdown-item" href="#wordclouds" onclick="on_wordcloud_filter_change({key: 'subset', value: 'Smallest_Gap_diff_Eu_Am'})">Smallest_Gap_diff_Eu_Am</a></li>
          <li><a class="dropdown-item" href="#wordclouds" onclick="on_wordcloud_filter_change({key: 'subset', value: 'None'})">No subset</a></li>
        </ul>
      </div>
    </div>
    <div class="col align-content-center">
      <div class="btn-group  w-100">
        <button type="button" class="btn btn-info dropdown-toggle" data-bs-toggle="dropdown" aria-expanded="false">
          Part-Of-Speech
        </button>
        <ul class="dropdown-menu">
          <li><a class="dropdown-item" href="#wordclouds" onclick="on_wordcloud_filter_change({key: 'pos_tag', value: 'NN'})">Nouns</a></li>
          <li><a class="dropdown-item" href="#wordclouds" onclick="on_wordcloud_filter_change({key: 'pos_tag', value: 'VB'})">Verbs</a></li>
          <li><a class="dropdown-item" href="#wordclouds" onclick="on_wordcloud_filter_change({key: 'pos_tag', value: 'JJ'})">Adjectives</a></li>
        </ul>
      </div>
    </div>
    <div class="col align-content-center">
      <label for="ngram-range" class="form-label text-center">N-gram size</label>
      <input type="range" class="form-range" style="height: 12px" min="1" max="3" step="1" 
      value="1" id="ngram-range" onchange="on_wordcloud_filter_change({key: 'ngram', value: this.value})">
    </div>
  </div>
  <div class="row justify-content-center">
    <div class="col-5 border border-secondary rounded">
        <img src="{{ site.baseurl }}/assets/img/wordclouds/America__None__VB__1.jpg" class="wordcloud-image" alt="Wordcloud" id="wordcloud"
        onload="this.classList.remove('wordcloud-image-hidden')"/>
    </div>
    <!-- Secret Button Below the Wordcloud -->
    <div class="col-5 text-center mt-2">
        <button type="button" class="btn btn-secondary secret-button" onclick="void(0);">
            🕵️‍♀️ Secret Button
        </button>
    </div>
</div>

Another one some text