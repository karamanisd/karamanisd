# ------------------------ question 1
# Set up virtual env, import and parse json data from url, show me how many bikes are there
import requests

req = requests.get('http://interview-external.citymapper.com/bike_status.json')
data = req.json()
# print(data.keys())
count=0
count2=0
for x in data['vehicles']:
    count+=1
print('all bikes:',count)

# ------------------------ question 2
# Show me how many of them are available
for x in data['vehicles']:
    if x['status'] == 'AVAILABLE':
        # print(x)
        count2 += 1
print('available bikes', count2)


# ------------------------ question 3
# Show me how many out of them have location data
count3=0
for x in data['vehicles']:  
    if 'location' in x:
        if 'lat' in x['location']:
            if x['status'] == 'AVAILABLE':
                # print(x)
                count3 += 1
print('available bikes with location data:', count3)


# ------------------------ question 4
# Remove duplicate entries
ids = []
count4=0
for x in data['vehicles']:  
    if 'location' in x:
        if 'lat' in x['location']:
            if x['status'] == 'AVAILABLE':
                if x['id'] not in ids:
                    ids.append(x['id'])
                    # print(x)
                    count4+=1
print('available bikes with location data, removed duplicates:', count4)


# ------------------------ question 5
# Show me how many of them are electric
ids = []
count5=0
count6=0
for x in data['vehicles']:  
    if 'location' in x:
        if 'lat' in x['location']:
            if x['status'] == 'AVAILABLE':
                if x['id'] not in ids:
                    ids.append(x['id'])
                    count4+=1
                    if 'battery_remaining' in x:
                        # print(x)
                        count5+=1
                    else:
                        count6+=1
print('available bikes with location data, removed duplicates, with battery:', count5)
print('available bikes with location data, removed duplicates, NO battery:', count6)


# ------------------------ question 6
# Given a second url, say its data produced one hour later for the same list of bikes.
# Show me the total distance they covered
req2 = requests.get('http://interview-external.citymapper.com/bike_status_2.json')
data2 = req2.json()
# print(data2.keys())
from geopy import distance

ids2 = []
sum=0

for x in data2['vehicles']:  
    if 'location' in x:
        if 'lat' in x['location']:
            if x['id'] not in ids2:
                ids2.append(x['id'])
                lat1=x['location']['lat']
                lng1=x['location']['lng']
                for y in data['vehicles']: 
                    if y['id'] == x['id']:
                        lat2=y['location']['lat']
                        lng2=y['location']['lng']
                        point1 = (lat1,lng1)
                        point2 = (lat2,lng2)
                        # print('distance:',distance.distance(point1, point2).km)
                        sum += distance.distance(point1, point2).km
                    
print('Sum of distances:',sum,'km')


## NOTES
# Google allowed, cam and share screen on, friendly people giving advices. 
# They didn't know & didn't care about the results, they did care about how you think and work 
# If your code and results make sense, its ok
# Last question was considered 2nd, "expert" step. 