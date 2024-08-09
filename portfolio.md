---
layout: page
dropdown: true
navbar: false
title: Portfolio
---
<article>
  {% for project in site.data.portfolio %}
    <h3>
      <a href="{{ project.url | relative_link }}">{{ project.name }}</a>
    </h3>
    <p>
      {{ project.description }}  
    </p>
    <ul>Images
    {% for img in project.images %}
        <li><img src="{{img}}"/></li>
    {% endfor %}
    </ul>
  {% endfor %}
</article>