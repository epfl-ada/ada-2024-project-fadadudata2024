document.getElementById('burger1').addEventListener('mouseover', function () {
    let tempSrc = this.src;
    this.src = document.getElementById('burger2').src;
    document.getElementById('burger2').src = tempSrc;
});
document.getElementById('burger2').addEventListener('mouseover', function () {
    let tempSrc = this.src;
    this.src = document.getElementById('burger1').src;
    document.getElementById('burger1').src = tempSrc;
});


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

