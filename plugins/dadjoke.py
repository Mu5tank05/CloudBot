import requests
from cloudbot import hook
from cloudbot.util import web, formatting


@hook.command(autohelp=False)
def daddyjoke(text):
	"""NA"""
	if text:
		r = requests.get('https://dog.ceo/api/breed/{}/images/random'.format(text))
		j = r.json()
		image_url = j['message']
		if image_url == "Breed not found":
			return "Breed not found!"
		else:
			return '{}'.format(image_url)
	else:
		r = requests.get('https://icanhazdadjoke.com/slack')
		j = r.json()
		dad_joke = j['text']
		return '{}'.format(dad_joke)