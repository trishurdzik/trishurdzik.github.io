---
layout: default
title: Portfolio
header_title: Portfolio
permalink: /portfolio/
sidebar_headers: false
---
<div class="row row-cols-1 row-cols-sm-2 row-cols-md-3 row-cols-lg-4 g-3">
{%- for eachPage in site.pages -%}
{%- if eachPage.url contains 'portfolio' -%}
{%- if eachPage.permalink != '/portfolio/' -%}
<div class="col">
{% include card-one.html
card_type='portfolio-card h-150'
card_image=eachPage.card_image
header_txt=eachPage.title
title_txt=eachPage.title
card_txt=eachPage.abstract
url=eachPage.url
button=mod
%}
</div><!-- ./col -->
{%- endif -%}
{%- endif -%}
{%- endfor -%}
</div><!-- ./row -->
