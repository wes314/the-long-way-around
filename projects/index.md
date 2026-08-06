---
layout: default
title: Projects
---

# Projects

{% for page in site.pages %}
{% if page.path contains "projects/" and page.name == "index.md" and page.path != "projects/index.md" %}
- [{{ page.title }}]({{ page.url | relative_url }})
{% endif %}
{% endfor %}
