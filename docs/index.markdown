---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: default
---
# Comparative analysis between USA and European comedy 

Some base text in here

## Part x

Some other text here.

Here is how to add a plot :

<!-- ATTENTION il faut que 'basic-plot' corresponde à l'argument de newPlot() dans basic_plot.js !! -->
<div id="basic-plot" style="width: 620px; height: 420px;"></div>
<script src="{{ '/assets/js/basic_plot.js' | relative_url }}"></script>

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

## Conclusion

Exemple : pour réajouter une "IMPACT IMAGE" (toute la largeur, ici c'est la banner mais il suffit de changer src)

<div class="big-image-wrapper">
  <img src="/assets/img/banner.jpg" alt="Alternative text" class="big-image">
</div>
<div class="big-image-spacer"></div>




Another one some text