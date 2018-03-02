import requests
from cloudbot import hook
from cloudbot.util import web, formatting

@hook.command('dogpic', autohelp=False)
def dogpic(text):
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
		r = requests.get('https://dog.ceo/api/breeds/image/random'.format(text))
		j = r.json()
		image_url = j['message']
		return '{}'.format(image_url)
		
@hook.regex(r'.*(?i)doge.*')
def dogepic_regex():
	"""NA"""
	r = requests.get('https://dog.ceo/api/breed/shiba/images/random')
	j = r.json()
	image_url = j['message']
	return '{}'.format(image_url)				