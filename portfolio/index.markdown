---
layout: default
title: Portfolio
header_title: Portfolio
image: https://placehold.co/1200x300/000000/png
permalink: /portfolio/
sidebar_headers: false
---
<div class="">
{% assign pages = site.pages %}
{% for page in pages %}
{% if page.url contains 'portfolio' %}
{% if page.permalink != '/portfolio/' %}
{% include card-one.html
  card_type='portfolio-card'
  card_image=page.card_image
  header_txt=page.title
  title_txt=page.title
  card_txt=page.abstract
  url=page.url
  button="FOo BAR"
%}
{% endif %}
{% endif %}
{% endfor %}
</div>