# Part 3 - Predictive Modeling


Ultimate is interested in predicting rider retention. To help explore this question, we have provided a sample dataset of a cohort of users who signed up for an Ultimate account in January 2014. The data was pulled several months later; we consider a user retained if they were “active” (i.e. took a trip) in the preceding 30 days. 
We would like you to use this data set to help understand what factors are the best predictors for retention, and offer suggestions to operationalize those insights to help Ultimate.
The data is in the attached file ultimate_data_challenge.json. See below for a detailed description of the dataset. Please include any code you wrote for the analysis and delete the dataset when you have finished with the challenge.

## Sub-section 1

### Question:
Perform any cleaning, exploratory analysis, and/or visualizations to use the provided data for this analysis (a few sentences/plots describing your approach will suffice). What fraction of the observed users were retained?

### Answer:

The data clean up steps started out by transforming string columns to pandas' categorical dtype, while numerical and boolean columns were changed to numpy float-64 dtype. After looking at the .info method, it is revealed that there are 3 columns with NULL/missing data: phone, avg_rating_of_driver, and avg_rating_by_driver.

![DataFrame Info](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/Info.PNG)

Starting with the phone columns, which records what type of phone the user is pirmarily using to accesss the app as either IPhone or Android. There were 396 values that were null, but since there aren't too many, it should be suffice to convert null values with a new category, "Unknown"

Moving on to the avg_rating_of_driver and avg_rating_by_driver, the histogram below shows the distribution of average ratings given by the user and average ratings received by drivers:

![Count of Avg Score Given by rider](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/Count-of-Avg-Score-Given-by-rider.png)
![Count of Avg Score Recieved by rider](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/Count-of-Avg-Score-Recieved-by-rider.png)

Both have a strongly skewed left distribution, and therefore, the median values will be imputed for missing data in each column, respectively.

Since some algorithms, such as logisitc regression, make assumptions of linear independence, it best to avoid columns of redundancy. The plot below is a correlation grid for all the columns. 

![correlation grid](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/correlation-grid.png)

The columns are all quite independent with the exception of avg_surge to surge_pct. It should make sense that the percent of trips taken at a surge multipler > 1x and the average surge price are correlated since the majority of users use the service only when at 1x pricing. Since the average has more information, the percent column will be dropped.

Finally, the fraction of users from the January Cohort that were retained is 37.61%

## Sub-section 2

### Question:

Build a predictive model to help Ultimate determine whether or not a user will be active in their 6th month on the system. Discuss why you chose your approach, what alternatives you considered, and any concerns you have. How valid is your model? Include any key indicators of model performance.

### Answer:

Due to the limited size of the dataset, despite it being quite clean, simple standard binary classification algorithms should be used. In my experience, Logistic Regression, Random Forest, and Gradient Boosted Trees are great general purpose classifiers. A big advantage of these algorithm is their interpretability. The Logisitc Regression uses a linear equation with coefficients to split the high-dimensional space in half, where these cofficients express how relevant a feature is. For Radom Forest and Gradient Boosted Trees, they have feature importance, a measure of how significant features are for the decision trees that are built.

Each model was trained using a Grid Search Cross Validation, a method where several models are trained using different hyper parameters, and then a score is given using k-fold cross validation.

Out of these three models, the Gradient Boosted Tree yielded the best accuracy, as well as the best f1-scores. The accuracy was 0.778 when predicting values from the test data.

Although the best model to predict with is the Gradient Boosted Tree, there is value in looking at the feature importance for all three models.

## Sub-section 3

### Question:

Briefly discuss how Ultimate might leverage the insights gained from the model to improve its longterm rider retention (again, a few sentences will suffice).

### Answer:

As mentioned before, one of the great advantages of the three models that were trained is their interpretable decision making parameters. Below are the three plots, one for each model trained:

![Feature Importance for LogisiticRegression](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/Feature-importance-for-logistic-regression.png)
![Feature Importance for RandomForestClassifer](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/feature-importance-for-random-forest-classifier.png)
![Feature Importance for GradientBoostingForest](https://github.com/alexretana/Springboard/blob/master/Ultimate_Inc_Challenge/Images/feature-imortance-for-gradient-boosting-forest.png)

From the Logistic Regression coefficients, it seems like users from King's Landing are much more likely to be retained, and for whatever reason, android users don't seem to be retained.

Looking toward the forest classifer, they both seem to be in agreement that the biggest deciding factors are the average rating by the drivers, being in King's Landing, the precentage of trips taken during the weekday, and the average surge multiplier.

From this information, it could be recommended that King's Landing users can be used to further investigate what makes that location more successful. The precentage of trips taken during the weekday being a deciding feature indicates that retained users are those who need use it on the weekday, likely traveling for work. Assuming this, the marketing department could be told to focus more on demographic of employees who travel for work. Lastly, the surge multiplier affecting the decision indicates that users are less likely to be retained if they have a bad experience of high surge multipliers. A further cost analysis go be done to determine if it would be profitable to offer a discount to users who have higher than normal surge multiplier averages, to incentivize them to stay.
