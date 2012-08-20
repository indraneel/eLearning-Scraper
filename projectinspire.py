from bs4 import BeautifulSoup
import requests
import json
from pprint import pprint
import re
import operator
import datetime

# FUNCTIONS
def strip_tags(value):
    """Returns the given HTML with all tags stripped."""
    #magic regex
    return re.sub(r'<[^>]*?>', '', str(value))


def get_votes(value):
    #less magic regex, also casts to an int
    return int(''.join(c for c in value if c.isdigit()))

    # PARSING
def jsonVotes():

    now = datetime.datetime.now()
    timestamp = str(now.month)+ "/" + str(now.day) +  " " + str(now.hour)+ ":" +str(now.minute)

    #payload is all the stuff you have to POST(?) to the website
    payload = {'coupon' : '170529', 'last' : '0', 'params' : '%2FContest.psp%3Fc%3D170529%26u%3D45692%26a%3DNone%26p%3DNone%26rest%3D0', 'ajax' : '1' , 'searchfilter' : '' }
    #r is the request result
    r = requests.get("https://offerpop.com/ContestGrid.psp", params=payload)

    #take the response, r, get it in the form of a json object
    #then get the content and throw it into BeautifulSoup
    soup = BeautifulSoup(r.json['content'])

    #go through the soup'd html, find the project name
    names = soup.findAll("div", { "class" : "CThumbName" })
    votes = soup.findAll("div", { "class" : "CThumbAction" })

    # if (choice is 1):
    #     JSON_output = []
    #     for i in range(len(names)):
    #         # [{'n':asdfjkl,'d':[{'x':t, 'y':v}.{'x':t, 'y':v}]},
    #         temp = {}
    #         tempList = []
    #         tempList.append({'x':timestamp, 'y':get_votes(strip_tags(votes[i]))})
    #         temp["name"] = strip_tags(names[i])
    #         temp["data"] = tempList
    #         JSON_output.append(temp)
    #     # for project in names:
    #     write_file = open("leaders.json", "w")
    #     JSON_output_final = json.dumps(JSON_output)
    #     write_file.write(JSON_output_final)

    # else:
    JSON_output_final = []
    JSON_output_final.append({"time" : timestamp})

    for i in range(len(names)):
        an_item = {}
        an_item["name"] = strip_tags(names[i])
        an_item["votes"] = get_votes(strip_tags(votes[i]))
        JSON_output_final.append(an_item)

    return JSON_output_final


#mongodb---->
# import pymongo
import sys

def main(args):
    # json_list = json.loads(jsonVotes())
    # for project in json_list:
    #     pprint(project['name'])
    #     for info in project['data']:
    #         pprint(info['x'])
    #         pprint(info['y'])
            


    pprint(jsonVotes())
        # If your database server is running in auth mode, you will need user and
    # database info. Ex:
    #    mongodb_uri = 'mongodb://username:password@localhost:27017/dbname'
    #
    # mongodb_uri = "mongodb://<ip132@scarletmail.rutgers.edu>:<mitiswhereibe>@alex.mongohq.com:10036/inspire"
    # db_name = "inspire"

    # # pymongo.Connection creates a connection directly from the URI, performing
    # # authentication using the provided user components if necessary.
    # #
    # try:
    #     connection = pymongo.Connection(mongodb_uri)
    #     database = connection[db_name]
    # except:
    #     print('Error: Unable to connect to database.')
    #     connection = None

    # if connection is not None:
        #loop through json objects and add to db

if __name__ == '__main__': 
    main(sys.argv[1:])


#next: create a graph of this
#after: make this run on its own