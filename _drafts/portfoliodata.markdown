---
layout: page
dropdown: true
navbar: false
title: Portfolio
nav_display: false
---
<article>
  {% for project in site.data.portfolio %}
    <h3>
      <a href="{{ project.url | relative_link }}">{{ Battlefield Simulation Tests Wearable Tourniquet }}</a>
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
<article>
  {% for project in site.data.portfolio %}
    <h3>
      <a href="{{ project.url | relative_link }}">{{ Discovering the Perfect Moving App }}</a>
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
<article>
  {% for project in site.data.portfolio %}
    <h3>
      <a href="{{ project.url | relative_link }}">{{ Do Customers Understand Our Loyalty Program? }}</a>
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
<article>
  {% for project in site.data.portfolio %}
    <h3>
      <a href="{{ project.url | relative_link }}">{{ Implementing Accessibility via Design System }}</a>
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
<article>
  {% for project in site.data.portfolio %}
    <h3>
      <a href="{{ project.url | relative_link }}">{{ Investigating Employee Knowledge of Digital Application Uses Across Enterprise }}</a>
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
<article>
  {% for project in site.data.portfolio %}
    <h3>
      <a href="{{ project.url | relative_link }}">{{ Finding Vulnerabilities to Prevent Fraud }}</a>
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
<article>
  {% for project in site.data.portfolio %}
    <h3>
      <a href="{{ project.url | relative_link }}">{{ Investigating Boston Bike Mapping App Need }}</a>
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