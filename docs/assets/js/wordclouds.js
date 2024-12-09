
var filters = {
    pos_tag: "VB",
    region: "America",
    subset: "None",
    ngram: 1
}

var filename = `{{ /assets/img/wordclouds/${filters.region}__${filters.subset}__${filters.pos_tag}__${filters.ngram}.jpg | relative_url}}`

function on_wordcloud_filter_change(new_filter) {
    filters[new_filter.key] = new_filter.value
    filename = `{{ /assets/img/wordclouds/${filters.region}__${filters.subset}__${filters.pos_tag}__${filters.ngram}.jpg | relative_url}}`
    const wc_image = document.getElementById("wordcloud")
    wc_image.classList.add("wordcloud-image-hidden")
    // small transition
    setTimeout(() => {  
        // load the image after 500 ms
        wc_image.src = filename
    }, 300)
}
