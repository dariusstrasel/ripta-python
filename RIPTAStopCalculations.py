# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 15:20:12 2016

@author: Silvi
"""

import requests
import json
import sys

routestops = requests.get("https://raw.githubusercontent.com/tbarmann/ripta-api/tb/add-stops-endpoint/static/route_stops.json")
routestopsdata = routestops.json()

vehiclepositions = requests.get("http://realtime.ripta.com:81/api/vehiclepositions?format=json")
vehicledata = vehiclepositions.json()

trips = requests.get("https://raw.githubusercontent.com/tbarmann/ripta-api/tb/add-stops-endpoint/static/trips.json")
tripsdata = trips.json()

# Get bus routes that pass by passenger_stop
def getRoutes(stop):
    print(stop)
    routes_list = []
    for routedict in routestopsdata:
        stopslist = routedict.get("stop_ids")
        if stop in stopslist:
            routes_list.append(routedict.get("route_id"))
    print(routes_list)        
    return routes_list
    
#get trips taken by bus routes
def getTrips(routes_list):
    print(routes_list)
    trips_list = []
    for tripdict in tripsdata:
        route_id = tripdict.get("route_id")
        for route in routes_list:
            if str(route) == route_id:
                trips_list.append(tripdict.get("trip_id"))
    print(trips_list)
    return trips_list

#get list of trips currently active and their most recent stop ids
#known bug: Occasionally api shows two stop ids for same trip
def getActiveTripsAndStops(trips_list):
    print(trips_list)
    active_trips_list = []
    recent_stops_list = []
    route_ids_list = []
    entity = vehicledata.get("entity")
    for vehicledict in entity:
        vehicle = vehicledict.get("vehicle")
        stop_id = vehicle.get("stop_id")
        trip = vehicle.get("trip")
        route_id = trip.get("route_id")
        trip_id = trip.get("trip_id")
        if trip_id in trips_list:
            active_trips_list.append(trip_id)
            recent_stops_list.append(stop_id)
            route_ids_list.append(route_id)
    trips_stops_list = []
    for i in range(len(route_ids_list)):
        dct = {'route': route_ids_list[i], 'stop': recent_stops_list[i], 'trip': active_trips_list[i]}
        trips_stops_list.append(dct)
    print(trips_stops_list)
    return trips_stops_list
    
#calculates distance from passenger to bus measured in number of bus stops
#compares index values in json arrays
def getStopsDistance(trips_stops_list, passenger_stop):
    print(trips_stops_list)
    text_msg = ''
    closest_stop = 500 #initialize arbitarily large value
    for trip_dct in trips_stops_list:
        stop = int(trip_dct.get('stop'))
        route = str(trip_dct.get('route'))
        for route_dct in routestopsdata:
            if str(route_dct.get('route_id')) == route:
                stop_ids_list = route_dct.get("stop_ids")
                bus_idx = stop_ids_list.index(stop)
                passen_idx = stop_ids_list.index(passenger_stop)
                if bus_idx <= passen_idx and (passen_idx - bus_idx) < closest_stop:
                    closest_stop = passen_idx - bus_idx
                    text_msg = "Bus "+str(route)+" is "+str(passen_idx - bus_idx)+" stops away. "
    
    print(text_msg)
    if text_msg == '':
        return "There are no buses arriving at your stop soon."
        #if stop is not valid, user will get this message
    else:
        return text_msg


def smsReply(passenger_stop):
    passenger_routes = getRoutes(passenger_stop)
    bus_trips = getTrips(passenger_routes)
    active_trips_and_stops = getActiveTripsAndStops(bus_trips)
    return getStopsDistance(active_trips_and_stops, passenger_stop)
#if bus is sitting at origin point, function will return value for that bus even if trip hasn't started


def main():
    pass
        
if __name__ == '__main__':
    main()

print(smsReply(18475))
    
# old test values for functions
# print(getRoutes(6335))
# print(getTrips([12]))
# print(getActiveTripsAndStops(['2390233', '2390236', '2356020', '2356003', '2395173', '2356376']))
# print(getsStopsDistance([{'stop': '1155', 'route': '66', 'trip': '2356003'}], 50725))