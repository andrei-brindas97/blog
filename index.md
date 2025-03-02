---
layout: home
title: Home
---

Welcome to my blog! Here you'll find my latest posts about DevOps.

## Recent Posts

{% for post in site.posts limit:5 %}
* [{{ post.title }}]({{ post.url }}) - {{ post.date | date: "%B %d, %Y" }}
{% endfor %} 