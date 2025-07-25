---
date: 2025-07-11 00:00:00
author: Pete
search_exclude: true
---
{%- assign double_quote = '"' -%}
{%- assign escaped_double_quote = '\"' -%}
{%- assign counter = 0 -%}

// This file is generated by Jekyll and contains all the documents that will be indexed by Lunr.
// This page was last updated at {{ "now" | date: "%Y-%m-%d %H:%M" }}.
//

var documents = [{% for page in site.pages %}{% if page.exclude_search or page.url contains '.xml' or page.url contains 'assets' or page.url contains '.txt' or page.url contains '404' or page.url contains 'blog' %} {% else %} {
  "if": "one",
  "id": "{{ counter }}",
  "url": "{{ site.url | append: site.baseurl | append: page.url | absolute_url }}",
  "title": "{{ page.title }}",
  "body": "{{ page.content | markdownify | strip_html | replace: '`', ' ' | replace: double_quote, ' ' | normalize_whitespace }}"{% assign counter = counter | plus: 1 %}
},{% endif %}{% endfor %}{% for page in site.without-plugin %}{
  "if": "two",
  "id": "{{ counter }}",
  "url": "{{ site.url | append: site.baseurl | append: page.url | absolute_url }}",
  "title": "{{ page.title }}",
  "body": "{{ page.content | markdownify | strip_html | replace: '`', ' ' | replace: double_quote, ' ' | normalize_whitespace }}"{% assign counter = counter | plus: 1 %}
},{% endfor %}{% for page in site.posts %}{
  "if": "three",
  "id": "{{ counter }}",
  "url": "{{ site.url | append: site.baseurl | append: page.url | absolute_url }}",
  "title": "{{ page.title }}",
  "body": "{{ page.date | date: ' %Y/%m/%d' }} - {{ page.content | markdownify | strip_html |  replace: '`', ' ' | replace: double_quote, ' ' | normalize_whitespace }}"{% assign counter = counter | plus: 1 %}
} {% if forloop.last %} {% else %}, {% endif %} {% endfor %}];

//console.log("documents: ", documents);

var idx = lunr(function () {
  this.ref('id')
  this.field('title')
  this.field('body')

  documents.forEach(function (doc) {
    this.add(doc)
  }, this)
});