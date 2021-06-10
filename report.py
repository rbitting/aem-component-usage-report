import os
import sys
import requests
from requests.auth import HTTPBasicAuth
import json
import csv

def clear_terminal_line(chars):
    padding = ""
    for i in range(chars):
        padding += " "
    print(padding, end='\r')

def generate_report(report_path, aem_path_to_search):
    with open(report_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["Component", "Path", "Page"])
        count = 1
        total =  "/" + str(len(components)) + " "
        length = len(total) + 1
        for path in components:
            print(str(count) + total + path, end='\r')
            url = "http://localhost:4502/bin/querybuilder.json?path=" + aem_path_to_search.replace("/","%2f") + "&property=sling%3aresourceType&p.limit=-1&property.value=" + path.replace("/","%2f")
            r = requests.get(url, auth=HTTPBasicAuth("admin", "admin"))
            results = json.loads(r.text)
            for res in results["hits"]:
                writer.writerow([path, res["path"], res["path"].split("/jcr:", 1)[0]])
            cur_length = len(path)
            if cur_length > length:
                length = cur_length
            else:
                clear_terminal_line(length + len(str(count) + total))
            count += 1
        clear_terminal_line(length + len(str(count) + total))
   
def get_path_list(file): 
    if os.path.isfile(file):
        f = open(file, "r")
        paths = f.read().splitlines()
        f.close()
        return paths
    else:
        print("Invalid file: " + file + ". Please try again.")
        exit()

components = []
has_argument = False

for arg in sys.argv[1:]:
    has_argument = True
    components = get_path_list(arg)

if not has_argument:
    print("Please include path to list of components as an argument.")
    exit(1)

total = str(len(components))

generate_report("report.csv","/content")
print(total + "/" + total + " Report is complete.")