# Analyzing-baseball-data
This project does some basic analyses on Baseball statistics by reading several CSV files. 

This is an assignend project on the MOOC "Python Data Analysis" by Rice university on Coursera.
https://www.coursera.org/learn/python-analysis?utm_medium=sem&utm_source=gg&utm_campaign=b2c_apac_x_multi_ftcof_career-academy_cx_dr_bau_gg_pmax_pr_s3_en_m_hyb_25-04_x&campaignid=22420706570&adgroupid=&device=c&keyword=&matchtype=&network=x&devicemodel=&creativeid=&assetgroupid=6566756439&targetid=&extensionid=&placement=&gad_source=1&gad_campaignid=22424263906&gbraid=0AAAAADdKX6bPFobg3dJ4ucMiivY5PpKvD&gclid=CjwKCAjwl_XBBhAUEiwAWK2hzhd4Dp73SXugQqubLEoqqu5Yafjr7e8nCItUA81H_khI1okwqoI-IBoCVGkQAvD_BwE

The first project in this course is to develop code for reading and writing CSV files using dictionaries:
read_write_cvsfile.py

For the main project, a several CSV files are provided that contain data on the performance of 
Major League Baseball (MLB) player over a span of more than a century. The Python program, project.py, statistically analyzes this data. This historical baseball data can be found at seanlehman.com in his baseball archive. The archive includes the raw data (stored in CSV files) used in computing most important baseball statistics.

http://seanlahman.com/files/database/baseballdatabank-2017.1.zip
This zip file includes a collection of CSV files from this archive with data that spans the years 1871-2016. The zip files includes two CSV files "Master.csv" and "Batting.csv" that contain player information and batting statistics. Since this data is being updated regularly, we ask that you use the 2016 versions of this two files linked here: 
Master_2016.csv and  Batting_2016.csv. Using our provided version of the files allows us all to work from the same raw data.
https://storage.googleapis.com/codeskulptor-isp/course3/Master_2016.csv
https://storage.googleapis.com/codeskulptor-isp/course3/Batting_2016.csv


Each line in the file Master.csv (and Master_2016.csv) is indexed by a unique field, "playerID", that corresponds to each player that has played in Major League Baseball.  Other fields in the file include the player's first and last names.  The file Batting.csv (and Batting_2016.csv) includes season-by-season batting data for each player. The first field identifies the player via his ID while the rightmost fields contain integers that correspond to the player's performance in various basic statistical categories.

This project will focus on writing code that will compute several common batting statistics from the data in these CSV files.