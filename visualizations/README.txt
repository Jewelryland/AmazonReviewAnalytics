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
  
	To get the average rating over time:   
	Run the cumulaiveaveragrescore.py in the same folder the above score files were created. Create a folder data which has the file cumulaiveaveragrescore.py before running the code.  

	To plot the trends:  
	Download and copy the index2.html file to the above data folder. Go the Terminal to the path to the data folder. Start the python 
	html server using python -m SimpleHTTPServer. Go to the browser enter the address for the localhost. Open the index2.html.  
