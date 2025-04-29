---
layout: default
title: Portfolio
header_title: Portfolio
permalink: /portfolio/
sidebar_headers: false
number_per_row: 3
---
{% assign count = 0 %}

{%- for page in site.pages -%}
{%- if page.url contains 'portfolio' -%}
{%- if page.permalink != '/portfolio/' -%}
{% capture mod %}{% if count != 0 %}{{ count | modulo: page.number_per_row }}{% else %}0{% endif %}{% endcapture %}
<!-- MOD {{ mod }} COUNT {{ count }} -->
{% if mod == 0  %}
<div class="card-group">
{% endif %}
{% include card-one.html
card_type='portfolio-card'
card_image=page.card_image
header_txt=page.title
title_txt=page.title
card_txt=page.abstract
url=page.url
button=mod %}
{% capture count %}{{ count | plus:1 }}{% endcapture %}
{% capture mod %}{% if count > 0 %}{{ count | modulo: page.number_per_row }}{% else %}0{% endif %}{% endcapture %}
<!-- MOD {{ mod }} COUNT {{ count }} -->
{% if mod == page.number_per_row  %}
</div><!-- ./card-group -->
{% endif %}
{%- endif -%}
{%- endif -%}
{%- endfor -%}
