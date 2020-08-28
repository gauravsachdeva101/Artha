# Artha
A web crawler that fetches daily energy generation and error logs for the given months. Script that automatically fetches data and store it in the database

It fetches data for January and February 2020 but script can be used to fetch daily energy generation and error logs for other months also. 

Technology used: python, selenium

Database: mysql

Run: main.py file

other files: 

datafetch.py for fetching the data from the website
It login to the website, target various elements to get the required months and download the files that contain data.

storedata.py for storing the data in the database
It creates tables in the #arthadatabase and then stores the data from csv files to mysql database


