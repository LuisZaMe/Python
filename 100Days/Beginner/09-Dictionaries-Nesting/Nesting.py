# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
# dict = {
#     "a": 1,
#     "b": 2,
#     "c": 3,
# }
# dict["c"] = [1 ,2 ,3]

# for key in dict:
#     print(key)
#     print(dict[key])

# Nesting a List in a Dictionary
travel_log = {
    "France": {"cities_visited" :["Paris", "Lille", "Dijon"], "total_visits" : 12},
    "Germany": {"cities_visited" :["Berlin", "hamburg", "Stuttgart"], "total_visits" : 105},
}

print(travel_log["Germany"]["cities_visited"])  # Accesses the list ['Berlin', 'hamburg', 'Stuttgart']
print(travel_log["Germany"]["cities_visited"][1]) # Accesses the list hamburg
print(f"{travel_log['Germany']['total_visits']}")  # Accesses the list 105

# Nesting Dictionary in a List 
travel_log02 = [
   {
       "country": "France",
       "cities_visited" :["Paris", "Lille", "Dijon"],
       "total_visits" : 12
   },
   {
       "country": "Germany",
       "cities_visited" :["Berlin", "hamburg", "Stuttgart"],
       "total_visits" : 5
   },
]

country = input() # Add Country
visits = int(input()) # Number of visits
list_of_cities = eval(input()) #Create list formatted

def add_new_country(country, visits, list_of_cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = list_of_cities
    travel_log02.append(new_country)

add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log02[2]['country']} {travel_log02[2]['visits']} times.")
print(f"My favorite city was {travel_log02[2]['cities'][0]}.")