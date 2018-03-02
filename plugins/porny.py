import requests
from cloudbot import hook
from cloudbot.util import web, formatting

@hook.command('porny', 'phc')
def porny_comments(text):
	"""porny <id> -- Get's you the porny comment <id>"""
	if text:
		r = requests.get('https://porny.blny.me/api.php?id={}&format=json'.format(text))
		j = r.json()
		status = j['status']
		if status == "fail":
			error = j['error']
			return "{}".format(error)
		else:
			text = j['text']
			return '{}'.format(text)