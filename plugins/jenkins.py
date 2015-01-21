# Thanks to @md-5 for the base of this
from cloudbot import hook

import requests


@hook.command("jenkins", "ci")
def jenkins(text):
    """-- Gets the latest build number for a project on Jenkins"""

    try:
        request = requests.get("http://ci.blny.me/job/{}/lastBuild/buildNumber".format(text))
        request.raise_for_status()
    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
        return "I couldn't find the latest build number for {}, please make sure this project exists".format(text)

    latest = request.text
    url = text + "/" + latest
    return "The latest build for {} is #{}, and can be downloaded from http://ci.blny.me/job/{}".format(text, latest, url)
