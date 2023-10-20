# Data Visualization: 2023 US Women's Gymnastics Championships

## Motivation
Since I learned gymnastics growing up, I have always been interested in watching the sport at the professional level. Though Women's gymnastics has fairly high viewership in Olympic years, this dwindles in the off-years, leading to very limited available data analysis. I began this analysis of the 2023 US Championships with two main goals:
1. to visualize the rankings of gymnasts on each event and the magnitude of their score differences
2. to determine which gymnasts have the potential to be on a highest-scoring 5 member team

The first goal is more straightforward. Women's gymnastics has four events: vault, uneven bars, balance beam, and floor exercise. In addition to the comparison of these event scores, there is also an All-Around ranking which compares the sum of each gymnast's four events. This championship had two days of competition, so the rankings are calculated for each day and on average.</br>
The second goal requires additional context. While this competition was not directly used to select athletes for the World Championships a few weeks later, it did provide a first look at all routines for the 2023 year and a baseline for score analysis. Using these scores, I calculated team scores for every possible combination of 5 athletes for comparison. The intention was not necessarily to predict the World's team, because other factors that are not quantified also go into consideration; rather, it was meant to provide insight into which athletes were "in the mix" for selection based on this competition and promote discussion among the viewership community.

## Features
### Visualization of All-Around Scores
There are three different ways to view All-Around scores:
1. bar chart of the top 10 average AA performances with hatches differentiating scores from each event and colors differentiating athletes (gym/figures/AA/Top 10 Average AA Performances) 
2. slope chart of the top 10 average AA performances to highlight trends across the two days with colors differentiating athletes (gym/figures/AA/Top 10 Average AA Performances Across Days)
3. bar charts of the top 10 AA performances for each day of competition with hatches differentiating scores from each event and colors differentiating athletes (gym/figures/AA/Top 10 AA Performances by Day)
### Visualization of Event Scores
There are two different ways to view event scores:
1. bar chart of the top 10 average event performances with colors differentiating athletes and error bars denoting their score range across the days (gym/figures/[EVENT]/Top 10 Average [EVENT] Performances)
2. bar charts of the top 10 event performances from each day with colors differentiating athletes (gym/figures/[EVENT]/Top 10 [EVENT] Performances Across Days)
### 3-up, 3-count Algorithm
An international team final competition allows for 3 team members to compete on each event, with all 12 event scores counting towards the team score. Assuming the strategy would be to use the 3 highest scoring routines out of the 5 members for each event, the developed algorithm calculates a presumptive "team score" to simulate a 3-up, 3-count competition format. This is executed for every combination of 5 athletes.
### Visualization of Highest Scoring Teams
For Day 1, Day 2, and on average, a pair of bar charts and tables display the highest-scoring teams among all possible teams. Bar charts have hatches differentiating scores from each event and colors differentiating athletes. (gym/figures/Team/)

## How to Use
The notebook (US_Champs.ipynb) explains why each chart was created and insights gleaned from these charts, as well as background information to contextualize the data.
1. Clone repository
2. Run all cells in US_Champs.ipynb

*NOTE:* The tables corresponding to the highest-scoring teams won't display on the GitHub notebook preview.
### Accessibility
With the number of athletes, it was challenging to find a unique combination of colors to represent them. This challenge was compounded in trying to find a discernible palette of colors that was also color-blind friendly. To account for this, the colors used are easily accessible and editable to customize user experience. 
To change the colors:
1. Open the Excel file 2023 US Championships Results. (path: gym/data/)
2. On the day 1 sheet, edit individual athlete [color names](https://matplotlib.org/stable/gallery/color/named_colors.html) (or HEX codes).
3. Delete all pre-existing figures. (path: gym/figures/)
4. Run all cells in US_Champs.ipynb
5. Access new figures in gym/figures/.

## Methods
All code was executed in Python, with the following libraries utilized:
- pandas
- numpy
- matplotlib
- itertools
- openpyxl
- plotly

## Conclusions
The primary purpose of this analysis was simply to create visuals that make the scores easier to comprehend and compare. The created visualizations show who has the highest scoring potential among the athletes for each event as well as the consistency in hitting that score potential across multiple days. </br>
However, my underlying goal was to provide the highest-scoring team data in order to make predictions about the World Championships team (predictions for fun, not a Data Science sense). Using the average highest-scoring team data, my ideal team was Simone Biles, Shilese Jones, Skye Blakely, Kaliya Lincoln, and Leanne Wong. The first 4 mentioned athletes are frequently on the highest-scoring teams, while Leanne was a personal pick based on the consistency of her scores and her ability to fill in on any event in case of emergency. The team ended up being the same, except Joscelyn Roberson in place of Kaliya Lincoln. This slightly reduced the team scoring potential (~0.2), but was likely based on factors outside the scope of this analysis. Gymnastics as a sport is a balance of risk and reward, and I speculate that Kaliya was left off the team due to her lack of prior international experience. With the increased mental pressure of international competitions, some athletes tend to falter in their consistency. Since Team USA didn't need an additional +0.2 to win gold, they didn't take the risk in this case.

## Future Applications
I tried to make this code as generalized as possible, such that its visualization methods and algorithms can easily be applied to other events. </br>
Potentially expanding the scope, I have been thinking about trying to train a predictive model for future team building. However, this would likely necessitate the integration of more historical data, which presents a challenge, as data within the sport is not well documented. Additionally, there are many categorical factors, such as prior international experience and injury history. While I haven't decided on whether to pursue this application yet, this code would be foundational to do so. 
