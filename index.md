---
layout: home
title: Home
---

Welcome to my DevOps blog! Here you'll find articles about DevOps practices, tools, and culture.

{% for post in site.posts %}
  <article>
    <h2><a href="{{ post.url }}">{{ post.title }}</a></h2>
    <time datetime="{{ post.date | date: "%Y-%m-%d" }}">{{ post.date | date_to_long_string }}</time>
    {{ post.excerpt }}
  </article>
{% endfor %} 