# Data Visualization: 2023 US Women's Gymnastics Championships

## Motivation
After learning gymnastics growing up, I have always been interested in watching the sport at the professional level. Though Women's gymnastics has fairly high viewership in Olympic years, this dwindles in the off-years, leading to very limited available data analysis. I began this analysis of the 2023 US Championships with two main goals:
1. to visuzlize the rankings of gymnasts on each event and the magnitude of their score differences
2. to determine which gymnasts have the potential to be on a highest-scoring 5 member team

The first goal is more straightforward. Women's gymnastics has four events: vault, uneven bars, balance beam, and floor exercise. In addition to the comparison of these event scores, there is also an All-Around ranking which compares the sum of each gymnasts's four events. </br>
The second goal requires additional context. While this competition was not directly used to select athletes for the World Championships a few weeks later, it did provide a first look at all routines for the 2023 year and a baseline for score analysis. Using these scores, I calculated team scores for every possible combination of 5 athletes for comparison. The intention was not necessarily to predict the World's team, because other factors that are not quantified also go into consideration; rather, it was meant to provide insight into which athletes were "in the mix" for selection based on this competition and promote discussion among the viewership community.

## Features
### Visualization of All-Around Scores

### Visualization of Event Scores

### 3-up, 3-count Algorithm
An international team final competition allows for 3 team members to compete on each event, with all 12 event scores counting towards the team score. Assuming the strategy would be to use the 3 highest scoring routines out of the 5 members for each event, the developed algorithm calculates a presumptive "team score" to simulate a 3-up, 3-count competition format. This is executed for every combination of 5 athletes.
### Visualization of Highest Scoring Teams
From this 

## How to Run
1. Clone respository
2. Run all cells in US_Champs.ipynb
### Accessibility
With the number of athletes, it was challenging to find a unique combination of colors to represent them. This challenge was compounded in trying to find a discernible palette of colors that was also color-blind friendly. To account for this, the colors used are easily accessible and editable to customize user experience. 
To change the colors, 
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

## Future Applications
I tried to make this code as generalized as possible, such that its visualization methods and algorithms can easily applied to other events. If you have interest in generating these graphs for other competitions, email me at zoeekimm@gmail.com. </br>
Expanding the scope, I have been thinking about trying to train a predictive model for future team building. However, this would likely necessitate the integration of more historical data, which presents a challenge, as data within the sport is not well documented. Additionally, there are many categorical factors, such as prior international experience and injury history. While I haven't decided on whether to pursue this application yet, this code would be foundational to do so. 
