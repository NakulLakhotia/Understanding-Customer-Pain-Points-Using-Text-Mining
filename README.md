# NLP-Projects - UNDERSTANDING CUSTOMER PAIN POINTS USING TEXT MINING

The project is divided into two parts. 

1.	The first part is the web scraping part where extractions of reviews for the top healthcare industries in USA are done using web scraping libraries available in Python.

2.	The second part is the Sentiment Analysis part where the data (text reviews) extracted from scraping is cleaned and processed in order to extract various features from the dataset and then apply sentiment analysis to obtain key insights like – which company has got the most negative/positive reviews, what are the topics of liking/disliking among the customers, most frequently used words in the review etc.

PROBLEM STATEMENT

Online product/service reviews are a great source of information for consumers. From the seller’s point of view, online reviews can be used to record the consumer’s feedback on the products or services they are selling. However, since these online reviews are quite often overwhelming in terms of numbers and information, an intelligent system, capable of finding key insights (topics) from these reviews, will be of great help for both the consumers and the sellers. This project will serve two purposes:

•	Enable consumers to quickly extract the key topics covered by the reviews without having to go through all of them

•	Help the sellers/retailers get consumer feedback in the form of topics (extracted from the consumer reviews)

SCRAPING TASK

Steps to scrape data

1.	We will first extract the reviews, rating from the first page of the website and store it in separate lists since the URL for this page is unique.

2.	Using a ‘for loop’ we request the other pages and extract the data. This extracted data gets stored in a 2D list where each list contains reviews & corresponding ratings from different pages. 

3.	Place the data from 2D list to 1D list containing all the reviews in one list and their corresponding rating in a different list. Then merge the review, rating list of first page and other pages. Finally create a dataframe with columns ‘Reviews’, ‘Rating’ & ‘Company’

4.	A similar kind of data frame is created for other companies by following the same steps explained previously.

5.	Then we concatenate the data frames for other companies and export it as csv. This csv file is then used for the ‘Sentiment Analysis’ of reviews by applying the concepts of Natural Language Processing (NLP)

SENTIMENT ANALYSIS

1. Importing the dataset obtained after scraping project – dataset.csv

2. View the dataset to get basic insights – shape, descriptive statistics, dataset head

3. Add a column of ‘text length’ for each review to check if it can be a helpful feature for our model

4. For better decision-making visualize the distribution of text-length for each rating using histograms and box-plots

5. Create a new dataset  which contains data only with rating ‘1’ (negative) or ‘5’ (positive)

6. Text Pre-processing

      6.1. Convert the ratings into binary format : Rating 5="1"  ,  Rating 1="0“ using label encoder
      
      6.2. Using regular expressions replace text like email addresses with ‘emailaddr’ and similarly for others      
      
      6.3. Remove stopwords and then lemmatize each review text
      
      6.4. Find the most common and rare words
      
      6.5. Create a new dataset with the processed reviews and corresponding encoded rating for feature extraction 

7. Feature Engineering
      
      7.1. Use Vader to find the polarity score for each review of our pre-processed dataset
      
      7.2. Adding ‘word-count’ & ‘character-count’ columns to the dataset to see the reduction in dataset
      
      7.3. Extract vector representation of every review using doc2vec of genism package
      
      7.4. Add TF-IDF columns for every word and document

8. Print the wordcloud from available reviews

9. Find the highest sentiment positive reviews 

10. Plot sentiment distribution for positive and negative reviews

11. Building Model & Model Evaluation

12. Insights from project (Please view the notebook for they key insights obtained)

