# gawker

## Pseudo code ##

```python
# Get list of article URLs
articles = []
for page_1 .. page_9469:
    for a in "section.main"
        articles.append(a["article.header.h1.a[href]"])
```

Keep in mind that all the URLs are relative.

```python
# Scrape all articles
json = {}
for a in articles:
    json.add({
        title: h1,
        pageviews: .meta__views
        date: time[datetime],
        content: .post-content (after <figure>),
        author: {
            name: .meta__byline,
            avatar: ".meta__avatar img[src]"
        }
        tags: [
            {name: ".first-tag span", slug: ""},
            {name: ".taglist li a.text()", slug: ".taglist li a.[href]"}
        ],
        image: {
            url: "figure img[src]",
            author: figcaption
        }
    })
```

On top of this, article headers, author avatars, and embedded article-body headers need to be backed up.

## Info ##

### Front page ###

#### Pagination ####

    First page: page_1
    Last page:  page_9469
    
#### HTML ####

```html
<body>
    <nav class="nav">
        <!-- etc -->
    </nav>
    <section class="main">
        <article>
            <header>
                <h1 class="headline">
                    <a href="{{ url.relative }}">{{ title }}</a>
                </h1>
                {{ author }} · {{ date }}
            </header>
            <div class="item__content">
                <div class="post-excerpt">
                    {{ excerpt }}
                </div>
            </div>
        </article>
        <article>
            <!-- etc -->
        </article>
<!-- etc -->
```

### Articles ###

```html
<div class="post">
    <article>
        <header>
            <h1>{{ post.title }}</h1>
            <div class="meta__views" title="{{ post.pageviews }} Pageviews">{{ post.pageviews }}</div>
            <div class="meta">
                <div class="meta__avatar">
                    <img src="{{ post.author.avatar }}" class="meta__avatar">
                </div>
                <div class="meta__text">
                    <div class="meta__byline">{{ post.author.name }}</div>
                    <time datetime="{{ post.date }}">{{ post.date | formatted }}</time>
                    <div class="tags-container">
                        <div class="first-tag">Filed to: <span>{{ post.tags[0].name }}</span></div>
                        <div class="taglist">
                            <ul>
                                <li><a href="/tag/{{ post.tags[1].slug }}">{{ post.tags[1].name }}</a></li>
                                <li><a href="/tag/{{ post.tags[2].slug }}">{{ post.tags[2].name }}</a></li>
                                <!-- etc -->
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
        </header>
        <div class="post-content">
            <figure class="align--bleed"><img src="{{ post.image.url }}">
                <figcaption>Illustration: {{ post.image.author }}</figcaption>
            </figure>
            {{ post.content }}
        </div>
    </article>
</div>
<!-- etc -->
```
