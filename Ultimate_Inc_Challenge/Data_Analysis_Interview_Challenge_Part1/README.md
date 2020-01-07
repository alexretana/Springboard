# Part 1 - Exploratory data analysis

## Question:

The attached logins.json file contains (simulated) timestamps of user logins in a particular geographic location. Aggregate these login counts based on 15minute time intervals, and visualize and describe the resulting time series of login counts in ways that best characterize the underlying patterns of the demand. Please report/illustrate important features of the demand, such as daily cycles. If there are data quality issues, please report them.

## Answer:

### Weekly Averages

From the aggregation displayed on the plot below, there's a pattern that Ultimate's transportation services are used more on the weekends than the weekdays, where there is a steady increase of use from Monday to Saturday, and small drop on Sunday, and a significant drop on Monday.

![Average Logins/15-Minutes Throughout Week (by Weekday)](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/Average-Logins-Thru-Weekdays.png)

### Daily Trend

Looking at the graph below, the average daily trend is a high amough of use from the early morning until about 5:00, then a drop of a activity with a second peak centered around 11:00. After the peak, there's a quick drop again, not as low, followed by another end of the day peak. It should be suspected that transportation use differs depending on the day of the week, and by extension, the login rate.

![Average Logins Throughout Day](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/Average-Logins-Thru-Day.png)

### Weekday vs Weekend Trends

Below are the average daily logins traffic by day of the week:

![Average Logins Throughout Day (Monday)](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/Average-Logins-Monday.png)
![Average Logins Throughout Day (Tuesday)](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/Average-Logins-Tuesday.png)
![Average Logins Throughout Day (Wednesday)](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/Average-Logins-Wednesday.png)
![Average Logins Throughout Day (Thursday)](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/Average-Logins-Thursday.png)
![Average Logins Throughout Day (Friday)](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/Average-Logins-Friday.png)
![Average Logins Throughout Day (Saturday)](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/Average-Logins-Saturday.png)
![Average Logins Throughout Day (Sunday)](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/Average-Logins-Sunday.png)

There is a significantly different trend between the weekends and the weekdays. 

On weekdays, there is decent use from the 12:00 which steadily decreases until hitting a low at about 6:00. From there, the login rate dramatically increases until a little pass 11:00, perhaps this is caused by people who are working going to lunch. After this peak, the rate slows down, but not as slow as the morning's lowpoint. Then at the end of the day, around 22:00, a final peak of logins come through.

On weekends however, there's a steady rise from 12:00 until the first peak at 5:00. It drops down drastically, has a small pick up around noon, but then steadys out for the rest of the day.

### Monthly Trends

From the basic bar graph below, it is apparent that there was an increase of traffic between January and March, and then a small decrease from March to April.

![Average Logins/15-Minutes (by Month)](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/Average-Login-by-Month.png)

### Daily Traffic Depending on Month

Making a similar analysis before, the plots above show the average daily highs and lows depending on month. There does not seem to be significant differences between months.

![Average Logins Throughout Day (Jan)](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/Average-Logins-Jan.png)
![Average Logins Throughout Day (Feb)](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/Average-Logins-Feb.png)
![Average Logins Throughout Day (Mar)](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/Average-Logins-Mar.png)
![Average Logins Throughout Day (April)](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/Average-Logins-April.png)


