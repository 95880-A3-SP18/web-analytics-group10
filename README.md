
# Python for Developers (95-880) - Group 10

## Web Analytics Startup for Restaurants Recommendation

### Team: Arunabha Sen, Rohan Parikh, Venkatesh Bhattad

### Project Deliverables

#### Who are your customers?

Our business is mainly to serve the general public looking for a place to eat given a particular location. Our product is going to serve residents and tourists to determine the best place to spend their money on a meal.

#### What are their needs? 

Everyone's gotta eat. A resident of a city/town often spends time on deciding where to eat. Our product will help our customer by recommending the best restaurant based on the location they search. This recommendation will purely be based on the reviews provided by the customers.

#### What specific problem(s) will you solve?

The problem of time spent by our customers to decide a restaurant is what we are looking to solve by our product. We believe everyone spends plenty of time looking for restaurants and deciding on where to eat. Based on exhaustive analytics on the reviews, we plan to provide our customers with instant recommendations.

#### Why do these problems need solved?

There are many applications out there which provide all restaurants at a location. But, a person still spends time choosing one. We can save time of every individual by our instant recommendation. Because, "time saved is time earned".

#### Where are you going to pull the data from?

Our major data source will be from the readily available APIs from Yelp and Google Places API's.


## Instructions on how to run the project

To run the project, please make sure you have the following libraries installed.

1. textblob - http://textblob.readthedocs.io/en/dev/install.html
2. WordCloud - https://github.com/amueller/word_cloud (For windows machine, you might have to download the wheel (.whl) as per your python version and install it manually.)
3. Pillow - https://pypi.python.org/pypi/Pillow/2.2.1
4. Make sure these are installed os, sys, csv, requests,time, pandas, numpy, io, json, bs4, matplotlib, warnings
5. Make sure this package works as well IPython.display

Once you have all the libraries installed. 

* Start Jupyter Notebook
* Navigate to the project folder
* Navigate to the src folder
* Start "Project_Group10.ipynb" and run all cells. The menu is displayed in the last cell. It takes couple of minutes to download all the data for the first time for both searching restaurants and then couple of minutes for extracting reviews. It will be fast once the data is loaded, since the program saves cache.


