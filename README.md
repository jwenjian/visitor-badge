# visitor-badge

> **Warning**
>
> **The service is now deployed under a free version of glitch, so it will down if too many requests in the same time**
>
> Update at 2023-04-28: [CountAPI](https://countapi.xyz/) service is DOWN, looking for another alternative for now, but it takes time, you should consider using [hits](https://github.com/dwyl/hits) as alternative (more stable), see [issue #32](https://github.com/jwenjian/visitor-badge/issues/32)

---

A badge generator service to count visitors of your markdown file.

[The story of visitor badge](https://medium.com/@1link.fun/the-story-of-visitor-badge-1bded5ed56b4)

Examples:

- default style

```markdown
![visitor badge](https://visitor-badge.glitch.me/badge?page_id=jwenjian.visitor-badge)
```

![visitor badge](https://visitor-badge.glitch.me/badge?page_id=jwenjian.visitor-badge)

- customized left text (default is `visitors`)

```markdown
![visitor badge](https://visitor-badge.glitch.me/badge?page_id=jwenjian.visitor-badge&left_text=MyPageVisitors)
```
![visitor badge](https://visitor-badge.glitch.me/badge?page_id=jwenjian.visitor-badge&left_text=MyPageVisitors)

- customized left text with a space between words

```markdown
![visitor badge](https://visitor-badge.glitch.me/badge?page_id=jwenjian.visitor-badge&left_text=My%20Page%20Visitors)
```
![visitor badge](https://visitor-badge.glitch.me/badge?page_id=jwenjian.visitor-badge&left_text=My%20Page%20Visitors)

- customzied color

```markdown
![visitor badge](https://visitor-badge.glitch.me/badge?page_id=jwenjian.visitor-badge&left_color=red&right_color=green) 
```

![visitor badge](https://visitor-badge.glitch.me/badge?page_id=jwenjian.visitor-badge&left_color=red&right_color=green) (left_color=red, right_color=green)

- customized color and left text

```markdown
![visitor badge](https://visitor-badge.glitch.me/badge?page_id=jwenjian.visitor-badge&left_color=red&right_color=green&left_text=HelloVisitors)
```

![visitor badge](https://visitor-badge.glitch.me/badge?page_id=jwenjian.visitor-badge&left_color=red&right_color=green&left_text=HelloVisitors) (left_color=red, right_color=green, left_text=HelloVisitors)

- customized color and a space between words in left text

```markdown
![visitor badge](https://visitor-badge.glitch.me/badge?page_id=jwenjian.visitor-badge&left_color=red&right_color=green&left_text=Hello%20Visitors)
```

![visitor badge](https://visitor-badge.glitch.me/badge?page_id=jwenjian.visitor-badge&left_color=red&right_color=green&left_text=Hello%20Visitors) (left_color=red, right_color=green, left_text=Hello%20Visitors)

<a href="https://www.producthunt.com/posts/visitor-count-badge-for-your-github-repo?utm_source=badge-featured&utm_medium=badge&utm_souce=badge-visitor-count-badge-for-your-github-repo" target="_blank"><img src="https://api.producthunt.com/widgets/embed-image/v1/featured.svg?post_id=195146&theme=dark" alt="Visitor count badge for your Github Repo - A github badge to count visitor to your repository | Product Hunt Embed" style="width: 250px; height: 54px;" width="250px" height="54px" /></a>

---


If you deployed forked project to your stable server and want to provide a free, stable service, which is very kind, please raise an issue to tell me so I can list your service url here:

> Before you do that, **DO update the md5_key in .env file to `guess_what`** so that former users will not lose their count, otherwise the count will start from 1.

Other public services:

-  https://visitor-badge.laobi.icu 
-  ~~https://visitor-badge.deta.dev/ (By [@Amresh Prasad Sinha](https://github.com/AmreshSinha))~~ (NO LONGER AVAILABLE)
-  ~~https://page-views.glitch.me~~ (NOT WOKRING)

Other implementations:

> You can implement in other languages, if you has, please let me know and I will update this list.

- NodeJS: [Lete114/visitor-badge](https://github.com/Lete114/visitor-badge)
- Go: [Nathan13888/VisitorBadgeReloaded](https://github.com/Nathan13888/VisitorBadgeReloaded)

