#!/usr/bin/env python

import PriceGUI
import TypeGUI
import yelp
import json_format_parser
import noteWriter
import LocationFinder
import LocationChooser

PriceGUI.main()
rating = PriceGUI.get_rating_level()['level']
food_type = TypeGUI.get_food_type()['type']
print rating, food_type
#succesfully get input rating and food type! YAY


location = LocationFinder.getCity()
print location
#get city succesfully

json_response = yelp.query_api('food',location)
r_dict = json_format_parser.get_res_dict(json_response)
name_list = json_format_parser.get_name_list(r_dict)
#print "------------------------------\n----------------------------------\n"
chosen_res = LocationChooser.choose(name_list)
print chosen_res

note_dict = json_format_parser.get_name_note_dict(r_dict)
print note_dict

chosen_note = note_dict[chosen_res]

noteWriter.writeToNote(chosen_note)
