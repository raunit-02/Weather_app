from django.shortcuts import render
import json
import urllib.request


def index(request):
	if request.method == 'POST':
		city = request.POST['city']

		# source contain JSON data from API
		link_b=url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=1db02d732975aa1e12465725dae8b5da'.format(city)
		source = urllib.request.urlopen(link_b
			).read()
		print(source)
		# converting JSON data to a dictionary
		list_of_data = json.loads(source)

		# data for variable list_of_data
		data = {
			"country_code": str(list_of_data['sys']['country']),
			"coordinate": str(list_of_data['coord']['lon']) + ' '
						+ str(list_of_data['coord']['lat']),
			"temp": str(list_of_data['main']['temp']) + 'k',
			"pressure": str(list_of_data['main']['pressure'])+'Pa',
			"humidity": str(list_of_data['main']['humidity'])+'%',
		}
		print(data)
	else:
		data ={}
	return render(request, "index.html", data)

