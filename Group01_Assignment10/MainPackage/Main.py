# Name:Cassidy Hook & Kelly Roden
# email:hookcx@mail.uc.edu & rodenky@mail.uc.edu
# Assignment Title: Assignment 10
# Due Date: 11/09/23
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: This project demonstrates that we can find a public API &
                    #import the data into a python dictionary & print interesting data from the dictionary
# Citations: https://stackoverflow.com/questions/26306448/extract-values-by-key-from-a-nested-dictionary

import json
import requests

if __name__ == "__main__":   
    response = requests.get('https://eonet.gsfc.nasa.gov/api/v2.1/events/EONET_6440')   
    #Pulling data from a NASA EONET(Earth Observatory Natural Event Tracker) API that gives data
    #about the recent Hurricane Tammy in the Atlantic Ocean
    json_string = response.content
    
    parsed_json = json.loads(json_string) # Now we have a python dictionary
    
    #print everything as a dictionary
    print(parsed_json)
    
#We want to display the dates & coordinates data captured by the NASA EONET for Hurricane Tammy 
    print('Dates & Coordinates from NASA EONET for Hurricane Tammy:')

#extract the date & coordinate data from the JSON, and store in a variable, then print data
#https://stackoverflow.com/questions/26306448/extract-values-by-key-from-a-nested-dictionary
    for geometries in parsed_json['geometries']:
        print ('date:', geometries['date'],',coordinates:', geometries['coordinates'])