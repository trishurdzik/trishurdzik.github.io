---
layout: default
title: "<i class='bi bi-file-code'></i> Htmx "
permalink: /htmx_example/
image: "https://placeholder.co/900x300/dddddd/ffffff/?text=HTMX"
header_title: "HTMX Example Page"
image_alt: "Htmx Examle page image"
nav_display: false
show_top_link: false
htmx_enabled: true
sidebar_headers: false
---
## What's HTMX

HTMX is an HTML variant that can dynamicaly update your web pages without the need coding javascript simply by using some special html attributes.

### HTMX Button Example 

<pre class="bg-light" id="res-div"></pre>

#### Get the site robots.txt

<button class="btn-sm btn-secondary" id="btn1" hx-get="{{ '/robots.txt' | relative_url }}" hx-trigger="click" hx-target="#res-div">Update robots.txt</button>

#### Get the sitemap.xml

<button class="btn-sm btn-secondary" id="btn2" hx-get="{{ '/sitemap.xml' | relative_url }}" hx-trigger="click" hx-target="#res-div">Update sitemap.xml</button>

### JSON Ajax data retrieval

Using data from here: [https://github.com/fawazahmed0/exchange-api](https://github.com/fawazahmed0/exchange-api) the form below will give up to date currency exchange rates with the US Dollar.

The form retrieves the data from this json api: [https://latest.currency-api.pages.dev/v1/currencies/usd.json](https://latest.currency-api.pages.dev/v1/currencies/usd.json) Grabbing only the relavant data. 

This JSON based problem required some special code via a python based [Google Cloud Function](https://cloud.google.com/functions) to over come some of HTMX's json limitations. See the code in the the file `htmx-get-json-cloud-function.py`.

{% include htmx_examples.html %}

