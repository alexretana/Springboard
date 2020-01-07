Part 2 - Experiment and metrics design

1. In an attempt to quantify the success of encouraging drivers in Gotham and Metropolis to work in both cities, one could use the metric of percentage of drivers who are active in both citys compared to the weekday's average. That is:
    success metric = (Number of Drivers active in both cities)/(Number of Drivers Active) -  (Average number of Drivers active in both city averaged over weekday, prior to experiment start) / (Average number of Drivers Active averaged over weekday, prior to experiment start)

This is robust against false positives. With out using the percentage, an increase or decrease in users would not signify that users are encouraged to work in both cities, and without the second term, days like Friday would seem like there's a sudden increase in dual-city users.

2. a. To implement the test, it would be good to keep a control group. Thus, this offer of paying tolls could be offered randomly to 30% of the users to preform A/B testing. Once it launches, over time, compare the metric between the two groups, to make the data more convincing that the toll-payments are the big influence for dual-city activity.
   b. To test for significance, a t-test would be done against the null hypothesis that the two metrics are equal for the comparison between the two groups. The significance level would be decided depending on how large the sample sizes are.
   c. From the results, it would be useful to construct a confidence interval for the precent increase in dual-city users to project potential revenue and costs in the case of upscaling the offer to all users. Even if more users start taking adventage of the toll compensation, it has to be taken into account if it would still be profitable.