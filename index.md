---
layout: default
title: "The Long Way Around"
---

An archive of projects, restorations and experiments 

## Projects

{% for project in site.pages %}
{% if project.path contains "projects/" and project.name == "index.md" and project.path != "projects/index.md" %}
- [{{ project.title }}]({{ project.url }})
{% endif %}
{% endfor %}

## Latest Posts 

{% for post in site.posts limit:5 %}
- {{ post.date | date: "%Y-%m-%d" }} — [{{ post.title }}]({{ post.url }})
{% endfor %}
