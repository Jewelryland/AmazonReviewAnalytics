==================================================================================================================================
CLUSTERING
==================================================================================================================================
##Kmeans using the TFIDF features##
----------------------------------------------------------------------------------------------------------------------------------
	To run the kmeans using the tfidf features:

	In the file kmeans_tfidf.py:
	Replace the path to data with training data file path in this line
	line 28: g = open('/path/to/test_data_file', 'r')

----------------------------------------------------------------------------------------------------------------------------------
##Kmeans using the vaderSentiment features##
----------------------------------------------------------------------------------------------------------------------------------
	To run the kmeans using the tfidf features:

	In the file kmeans_tfidf.py:
	Replace the path to data with training data file path in this line
	line 27: g = open('/path/to/test_data_file', 'r')

==================================================================================================================================
CLASSIFICATION
==================================================================================================================================
##Classification Using the TFIDF features##
----------------------------------------------------------------------------------------------------------------------------------
	To run the Naive Bayes classifier for gathering sentiment scores:

	In the file review_analysis.py:
	Replace the path to data with training data file path in this line
	line 5: train_reviews_labels_rdd = formatData(sc, '/path/to/training_data_file')

	Replace the path to test data with the actual path in this line:
	line 22: test_reviews_labels_rdd = formatData(sc,'/path/to/test_data_file')

	To run the program:
	./home/path/to/spark-1.5.2-bin-hadoop2.6/bin/spark-submit --master local[*] ~/project_directory/review_analysis.py

	The results are saved in a directory called nb_pred

----------------------------------------------------------------------------------------------------------------------------------
##Classification Using the vaderSentiment##
----------------------------------------------------------------------------------------------------------------------------------
	To get the VaderSentiment scores:

	In the file VaderSentiment_analysis.py:
	Replace the path to results file with the actual path in this line
	line 8: with open("/path/to/sentiment_results_file", "a") as f:

	Replace the path to data with the actual path in this line:
	line 14: path = "/home/path/to/review_file"

	Execute using:
	./home/path/tp/spark-1.5.2-bin-hadoop2.6/bin/spark-submit --master local[*] ~/project_folder/VaderSentiment_analysis.py

==================================================================================================================================
TREND ANALYSIS
==================================================================================================================================
	To get the trend data:

	In the file trends.py:
	Replace the path to data with training data file path in this line
	line 15: path = "/home/path/to/data"

	Replace the path with the project folder:
	line 23: with open("/project/folder/" + product_id + "_scores.tsv", "w") as f:

	To run the program:
	./home/path/to/spark-1.5.2-bin-hadoop2.6/bin/spark-submit --master local[*] ~/project_directory/trends.py