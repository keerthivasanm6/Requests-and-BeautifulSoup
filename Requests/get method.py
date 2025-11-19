import requests

r=requests.get("https://www.geeksforgeeks.org/")
#This will return response code
print(r)

#This will return code alone
print(r.status_code)


#Below line will print the HTML page
#print(r.text)