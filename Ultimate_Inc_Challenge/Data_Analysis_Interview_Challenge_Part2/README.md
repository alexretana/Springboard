# Part 2 - Experiment and metrics design

### Question:

The neighboring cities of Gotham and Metropolis have complementary circadian rhythms: on weekdays, Ultimate Gotham is most active at night, and Ultimate Metropolis is most active during the day. On weekends, there is reasonable activity in both cities.

However, a toll bridge, with a two way toll, between the two cities causes driver partners to tend to be exclusive to each city. The Ultimate managers of city operations for the two cities have proposed an experiment to encourage driver partners to be available in both cities, by reimbursing all toll costs.

 1. What would you choose as the key measure of success of this experiment in
    encouraging driver partners to serve both cities, and why would you choose this metric?

 2. Describe a practical experiment you would design to compare the effectiveness of the
    proposed change in relation to the key measure of success. Please provide details on:
    a. how you will implement the experiment

    b. what statistical test(s) you will conduct to verify the significance of the
       observation

    c. how you would interpret the results and provide recommendations to the city
       operations team along with any caveats.

### Answer:

1. In an attempt to quantify the success of encouraging drivers in Gotham and Metropolis to work in both cities, one could use the metric of percentage of drivers who are active in both citys compared to the weekday's average. That is:

####      **_Success Metric_ = (_DU<sub>f</sub>+)/(_U<sub>f</sub>_) - (_DU<sub>i</sub>_)/(_U<sub>i</sub>_) , ** 

      _Where:_

      **_DU<sub>f</sub>_** = _Number of Drivers active in both cities_

      **_U<sub>f</sub>_** = _Number of Drivers Active_

      **_DU<sub>i</sub>_** = _Average Number Of Drivers Active In Both City Averaged Over Weekday, Prior To Start Of Experiment_

      **_U<sub>i</sub>_** =  _Average Number Of Drivers Active Averaged Over Weekday, Prior To Start Of Experiment_


This is robust against false positives. With out using the percentage, an increase or decrease in users would not signify that users are encouraged to work in both cities, and without the second term, days like Friday would seem like there's a sudden increase in dual-city users.

2. a. To implement the test, it would be good to keep a control group. Thus, this offer of paying tolls could be offered randomly to 30% of the users to preform A/B testing. Once it launches, over time, compare the metric between the two       groups, to make the data more convincing that the toll-payments are the big influence for dual-city activity.
   b. To test for significance, a t-test would be done against the null hypothesis that the two metrics are equal for the comparison between the two groups. The significance level would be decided depending on how large the sample sizes       are.
   c. From the results, it would be useful to construct a confidence interval for the precent increase in dual-city users to project potential revenue and costs in the case of upscaling the offer to all users. Even if more users start          taking adventage of the toll compensation, it has to be taken into account if it would still be profitable.