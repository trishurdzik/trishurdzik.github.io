---
layout: page
title: "<i class='bi bi-pen'></i> Blog"
permalink: /blog/
---
{% if site.paginate %}
    {% assign posts = paginator.posts %}
  {% else %}
    {% assign posts = site.posts %}
{% endif %}
{% include blog.html %}
