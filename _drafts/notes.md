---
layout: default
exclude_search: true
sidebar_headers: false
nav_display: false
title: NOTES
permalink: /notes/
accordian:
    - id: one
      header: This is the header one 
      content: This is the content of the first accordian <a href="/link">Link</a> foo flim flam.
    - id: two
      header: This is the header two
      content: This is the content of the second accordian. This is a second sentence
    - id: three
      header: This is the header three
      content: This is the content of the <b>third</b> accordian
---

### Accordians Example
<!-- Use this to include the Accordian on a page: -->
{% include accordian-one.html %}

<!-- 
```html
 include h-card.html card-header="This is the optional header" card-title='This is the Title' card-content="This is the content of this horizontal card" img-src='/assets/images/forks.jpg' img-alt-txt='Forks' card-button-txt='Contact Me' card-button-href='/contact'

include v-card.html card-header="This is the optional header" card-title='This is the Title' card-content="This is the content of this vertical card" img-src='/assets/images/forks.jpg' img-alt-txt='Forks' card-button-txt='Contact Me' card-button-href='/contact'
```
-->