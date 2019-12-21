# Capstone Project for Springboard: Consumer Financial Complaint Resolution Predictor

As a final Project for the Springboard Machine Learning Bootcamp course, a Complaint Resolution Predictor for complaints submitted to the Consumer Financial Protection Bureau. The context of their Complaint database is an submission process to the Government Bureau is accepted and then sent to the company specified, to monitor and investigate if companies are addressing their consumers' complaints. The data is anonymized, but keeps information about general locations with ZIP code being the most specific identifier. Each complaint is assigned a unique ID, which can be used to reference back the status. Companies are expected to respond in a timely manner (within 14 days) and can be audited if they show a pattern of not responding within the time frame. Consumers are to fill out the form to the best of their knowledge, including information about what Product and what kind of Issue is troubling them.



The process for this project follows an outline as such:

1. Data Exploration

   i. Exploring How Many Empty/Null Values Reside in each Column

   ii. Determining number of Unique Values of each Non-numeric Column, and Corresponding Value Counts

   iii. Cleaning Numeric Columns and Imputing Values

   iv. Create Visualization of above Investigations

   v. Filtering Out Unlabeled Data

   vi. Create Preprocessing Pipeline for Training and Testing models

   vii. Create Dimensionally Reduced Visualization of Data

2. Binary Resolution Classifier

   i. Random Forest Classier

   ii. Logistic Regression

   iii. Gradient Boosting Classifier

   iv. Resampling: Logistic Regression | Gradient Boosting Classifier 

   v. Truncated Singular Value Decomposition

   ​	a. Support Vector Classifier

   ​	b. SGDClassifier

   vi. Deep Neural Network Classifier

3. Multi-class Resolution Classifier

   i. Logistic Regression

   ii. Bernoulli Naive Bayes

   iii. Deep Neural Network Classifier

4. Full Categorized Classifier

   i. Head-To-Head Comparison of Logistic Regression Classifier

   ii. Deep Neural Network Classifier Head-To-Head Comparison

5. Natural Language Processing Classifier

   i. Beautiful Soup

   ii. Natural Language Toolkit

   iii. Text-frequency Inverse Document-frequency Vectorizer

   vi. Logistic Regression

   v. Bernoulli Naive Bayes

   vi. Truncated Singular Decomposition

   vii. Deep Neural Network (Inconclusive)

6. Refine Logistic Regression Model

   i. Remove Low-Weighted Columns