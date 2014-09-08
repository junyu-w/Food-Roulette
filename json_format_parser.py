#!/usr/bin/env python

import yelp
import json
import PriceGUI
import TypeGUI


class Restaurant(object):
    #code
    
    def __init__(self, name, category, rate, phone_number, image, location, url):
        self.name = name
        self.category = category
        self.rate = rate
        self.phone_number = phone_number
        self.image_url = image
        self.location = location
        self.url = url
        
    def get_name(self):
        return self.name
    
    def get_category(self):
        return self.category
    
    def get_rate_level(self):
        return self.rate
    
    def get_phone_number(self):
        return self.phone_number
    
    def get_image_url(self):
        return self.image_url
    
    def get_location(self):
        return self.location
    
    def get_url(self):
        return self.url
    

#build a restaurant dict: {name: restaurant_obj}
def get_res_dict(json_input):
    r_dict = {}
    r_list = json_input['businesses']
    for r in r_list:
        r_key = r['name']
        r_obj = Restaurant(r['name'], r['categories'], r['rating'], r['display_phone'], r['image_url'], r['location']['address'], r['url'])
        r_dict[r_key]=r_obj
    return r_dict


def get_name_list(r_dict):
    name_list = [];
    for a in r_dict:
        r_obj = r_dict[a]
        name = r_obj.get_name()
        name_list.append(name)
    return name_list

def get_name_location_dict(r_dict):
    location_dict = {}
    for a in r_dict:
        r_obj = r_dict[a]
        r_name = r_obj.get_name()
        location_dict[r_name] = r_object['location'][0]
    return location_dict

def get_name_rating_dict(r_dict):
    rating_dict = {}
    for a in r_dict:
        r_obj = r_dict[a]
        r_name = r_obj.get_name()
        rating_dict[r_name] = r_object['rating']
    return rating_dict

def note_generator(r_obj):
    info = ""
    info += "<span>Name: </span><span style='font-weight:bold'>"+r_obj.get_name()+"</span><br/>\n"
    info += "<span>Location: </span><span style='font-weight:bold'>"+r_obj.get_location()[0]+"</span><br/>\n"
    info += "<span>Phone: </span><span style='font-weight:bold'>"+r_obj.get_phone_number()+"</span><br/>\n"
    info += "<span>Rating: </span><span style='font-weight:bold'>"+str(r_obj.get_rate_level())+"</span><br/>\n"
    info += "<span>URL: </span><span style='font-weight:bold'>"+r_obj.get_url()+"</span><br/>\n"
    info += "<div><br /></div>"
    return info
    
def get_name_note_dict(r_dict):
    note_dict = {}
    for a in r_dict:
        r_obj = r_dict[a]
        r_name = r_obj.get_name()
        note_dict[r_name] = note_generator(r_obj)
    return note_dict


def main():
    inputValue = yelp.query_api("food", "Berkeley")
    r_dict = get_res_dict(inputValue)
    for a in r_dict:
        r_obj = r_dict[a]
        #print r_obj.get_location()[0]
        note_generator(r_obj)
    
    
if __name__ == '__main__':
    main()