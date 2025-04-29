---
layout: default
title: Portfolio
header_title: Portfolio
permalink: /portfolio/
sidebar_headers: false
number_per_row: 3
---
{% assign count = 0 %}
{% assign number_per_row_as_int = page.number_per_row %}

{%- for eachPage in site.pages -%}
{%- if eachPage.url contains 'portfolio' -%}
{%- if eachPage.permalink != '/portfolio/' -%}

<!-- 1     COUNT {{ count }} NUM {{ number_per_row_as_int }} -->

{% if count != 0 %}
{% assign mod =  count | modulo: number_per_row_as_int %}
<!-- 2A MOD {{ mod }} COUNT {{ count }} -->
{% else %}
{%  assign mod = 0 %}
<!-- 2B MOD {{ mod }} COUNT {{ count }} -->
{% endif %}

{% if mod == 0 %}
<div class="card-group">
{% endif %}

{% include card-one.html
card_type='portfolio-card'
card_image=eachPage.card_image
header_txt=eachPage.title
title_txt=eachPage.title
card_txt=eachPage.abstract
url=eachPage.url
button=mod
%}
{% assign count = count | plus: 1 %}
<!-- 3  MOD {{ mod }} COUNT {{ count }} -->

{% if count != 0 %}
{% assign mod = count | modulo: number_per_row_as_int %}
{% else %}
{% assign mod = number_per_row_as_int %}
{% endif %}
<!-- 4  MOD {{ mod }} COUNT {{ count }} -->

{% if mod == 0 %}
</div><!-- ./card-group -->
{% endif %}

{% endif %}
{% endif %}
{% endfor %}
