---
layout: default
title: "<i class='bi bi-tags'></i> Tags"
header_title: Tags Cloud
exclude_search: true
nav_display: true
permalink: /tags/
sidebar_headers: false
---
<script>
    $(document).ready(function () {    
        var tags = [];
        {%- for tag in site.tags -%}
            {% assign tag_slug = tag[0] | sluggify %}                    
            {% assign weight = site.tags[tag_slug] | size %}
            {% assign title = tag[0] | downcase %}
            tags.push({
                text: "{{ title }}",
                weight: '{{ weight }}',
                link: '{% include tag_url.html tag=title %}'
            });
        {%- endfor %}

        $('.wordcloud').jQCloud(tags, {
            'shape': 'rectangular'
        });    
    });    
</script>
<div class="wordcloud"></div>