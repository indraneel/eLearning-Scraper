Scraper/Leaderboard — eLearning for Change
==========================================
What it is
----------
My friend spent the summer of 2012 working on a educational initiative/project in India, and entered it in a contest to win a hefty sum of money.  Part of the contest involved an online vote, which was hosted on Facebook via a site called OfferPop.

My friend hated that website. Since I wanted to learn more about site scraping, I decided to scrape the contents of the page and dump it into a nicely formatted page, showing my friend exactly where his project was on a leaderboard.

What I did
----------
OfferPop served up HTML via jQuery/AJAX (ew), so this became a bigger challenge to scrape.  I picked up Python, since it has BeautifulSoup, the greatest HTML scraping library in all the land.  And then I used Flask + Bootstrap to render the page with all the data.

![You can see a screenshot of it here](http://i.imgur.com/XgLqr.png)
