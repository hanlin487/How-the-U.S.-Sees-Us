# The Project
The project is essentially a website. It takes in an image of a person, computes their demographics, finds the voter disparity of the corresponding demographics, and outputs the 
results. This project was made during the SD Hacks 2021 Hackathon.

Running server.py will launch the website, some python modules are needed before running such as pandas, flask, and requests. 
It's also where the layout of the website is.
census.py holds the methods for manipulating data from the electoral_data.csv file which holds the existing disparity data.
demoScript.py is the actual algorithm that's running to calculate demographics and format the output.