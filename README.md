<h1>What can you do with this scraper?</h1>

With a little Python magic, anything is possible. After developing the scraper, I did some basic data visualization on the following topics - scoring breakdown by position,
most prevalant colleges represented in the NBA, and LeBron James' performance (in terms of FG%) against various teams throughout his career. The possibilities are endless,
provided you can get the data you need, of course. These are just some examples:

<h3>Scoring Breakdown by Position</h3>

I was curious about the scoring breakdown by position over time. More recently, basketball has seen kind of a shift towards lobbing 3's every time it's feasible to get a shot off
...but are point and shooting guards truly dominating scoring over forwards and centers across the league? Here are some bar charts showing scoring breakdown with total points 
across the league using each players most frequently played position in the 1986-1987, 1999-2000, 2006-2007, and 2016-2017 seasons:

![](https://github.com/nawal786/Basketball-Reference-Scraper/blob/master/examples/PointsByPosition_1986-87.png)
![](https://github.com/nawal786/Basketball-Reference-Scraper/blob/master/examples/PointsByPosition_1999-2000.png)
![](https://github.com/nawal786/Basketball-Reference-Scraper/blob/master/examples/PointsByPosition_2006-07.png)
![](https://github.com/nawal786/Basketball-Reference-Scraper/blob/master/examples/PointsByPosition_2016-17.png)

Comparing the 1986-87 and 1999-2000 seasons, scoring from point guards increased by an impressive 20%, while scoring from shooting guards decreased 17%. Scoring from forwards
stayed just about the same, and centers scored 5% less in the 1999-2000 season.

Looking at 1999-2000 and and 2006-07, the scoring increases are even more drastic. Between these two seasons, scoring from shooting guards increased an amazing <strong>52%</strong>.
Point guards scored 9% more, and power forwards and centers saw 31% and 30% increases, respectively. Small forwards scored 5% less, but overall the league scoring increased
drastically.

The upward trend continues between 2006-07 and 2016-17, with all positions seeing increases or essentially staying the same (within 1% of total points).

<h3>Which colleges send the most players to the NBA?</h3>

College basketball is fairly popular among Americans. Over the decades of growing NCAA popularity, several schools have gained a reputation of "basketball powerhouses," 
winning championships, producing top-tier players, and sending away high basketball IQ individuals to franchises that will pay them millions of dollars. 
Since 2000, let's see which schools have produced the most NBA draftees:

![](https://github.com/nawal786/Basketball-Reference-Scraper/blob/master/examples/CollegesByDraftees.png)

Kentucky and Duke are probably the two most popular colleges for basketball, so it makes sense that they lead all colleges in players drafted in to the NBA since 2000. Personally, 
I'm surprised to see Stanford in the Top 30...

<h3>LeBron James' Performance vs. Various Teams</h3>

There's no denying that LeBron has been a dominant force in the league since he was drafted by the Cavs in 2003. He's frequently touted as the G.O.A.T. (greatest of all time)
and definitely the bestin the league as it exists today. Over LeBron's career, he's been to the NBA finals 10 times and has won a championship 4 times with three different
teams - the Miami Heat, Cleveland Cavaliers, and most recently, the Los Angeles Lakers. Here is a heatmap of LeBron's regular season field goal percentage against every team 
in every year he's played against them in his career:

![](https://github.com/nawal786/Basketball-Reference-Scraper/blob/master/examples/LBJ_HeatMap_Career.png)

In the early portion of LeBron's career, (2004- ~2008), there are much more sub-50% performances. As he continued to evolve as a player, LeBron's performance seems to have
improved, with more >50% FG performances in 2009 and 2010. From 2011-2014, however, LeBron seems to have hit the prime of his career, with incredibly efficient
performances against many of the teams in the league. Coincidentally, this is also the period of time where he joined Dwyane Wade and Chris Bosh to form "The Big Three" in
Miami to win his first championship. Looking at the heatmap, transitioning to the Miami Heat was a good move for LeBron, as he now had a reliable cast in Wade and Bosh and
no longer needed to shoulder the burden of scoring to keep his team's season alive. LeBron went to the finals four times with the Heat, winning two championships.
