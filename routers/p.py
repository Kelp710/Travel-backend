import requests

# url = "https://cost-of-living-and-prices.p.rapidapi.com/prices"

# querystring = {"city_name":"Kathmandu","country_name":"napal"}

# headers = {
# 	"X-RapidAPI-Key": "996ae8ab49msh8c991b4e71c0891p14d285jsn295dad829477",
# 	"X-RapidAPI-Host": "cost-of-living-and-prices.p.rapidapi.com"
# }

# response = requests.request("GET", url, headers=headers, params=querystring)

# print(response.text)

unsplash_key = "BIWkxve6hsoQNq7zoauikNAOXOH03SEKh1futEFtnRA"
url = f"https://api.unsplash.com/photos/random/?client_id={unsplash_key}&query=Japan&per_page=4&order_by=popular&orientation=landscape&count=1&content_filter=high"
r_2 = requests.get(url) 
print(r_2)
pic_data = r_2.json()[0]["urls"]["raw"]
print(pic_data)