---
layout: page
title: "Blog"
image: /assets/images/blog_image_01.jpg
permalink: /blog/
nav_display: false
---
{% if site.paginate %}
    {% assign posts = paginator.posts %}
  {% else %}
    {% assign posts = site.posts %}
{% endif %}
{% include blog.html %}
