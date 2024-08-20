---
title: Search Results
---

<ul id="search-results"></ul>
<script>
  window.store = {
      {{ range where .Site.Pages "Section" "blog" }}
      "{{ .Permalink }}": {
          "title": "{{ .Title  }}",
          "author": [{{ range .Params.authors }}"{{ . }}",{{ end }}],
         "category": [{{ range .Params.categories }}"{{ . }}",{{ end }}],
          "content": {{ .Content | plainify }},
          "url": "{{ .Permalink }}"
      },
      {{ end }}
  }
</script>

<!-- Import lunr.js from unpkg.com -->
<script src="https://unpkg.com/lunr/lunr.js"></script>
<!-- Custom search script which we will create below -->
<script src="/js/search.js"></script>
```
