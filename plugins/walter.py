import time
from cloudbot import hook
from cloudbot.util import http
import requests
import random


@hook.command
def piglatin(text):
    """piglatin - returns word in pig latin format"""
    word = text.lower()
    vowels = 'aeiou'
    pig = 'ay'
    first = word[0]
    if first in vowels:
        newword = word + pig
    else:
        newword = word[1:] + first + pig
    return "{} becomes {}".format(word, newword)


@hook.command
def palindrome(text):
    """palindrome - checks if textut is a palindrome"""
    string = text.lower()
    if string == string[::-1]:
        return "{} is a palindrome".format(string)
    else:
        return "{} is not a palindrome".format(string)


@hook.regex(r'\#(SWAG|swag|Swag)')
@hook.regex(r'\#(YOLO|yolo|Yolo)')
def refrainyoself(match, nick=None, message=None):
    if nick == "Mu5tank05" or "Mu5tank05-mc":
        return
    else:
        matchword = match.group().encode('utf-8')
        message("{} please refrain from saying {}".format(nick, matchword))


@hook.regex(r'\#(fourtwenty|420)')
def fourtwenty(nick=None, message=None):
    if nick == "Mu5tank05" or nick == "nathanblaney" or nick == "Mu5tank05-mc":
        message("{} loves to blaze".format(nick))
		
@hook.regex(r'\:pepe:')
def pepe(nick=None, message=None):
	message(":pepe:")
		
@hook.regex(r'(?i)(Hello|Hi) (w|W)alter(!| |\\.|\?)*')
def helloregex(match, nick=None, message=None):
    if match.group(3) == "?":
        message("Hi {}, what's your question?".format(nick))
    else:
        message("Hello {}!".format(nick))

@hook.command
def poke(text, nick, action=None):
    if nick == "Sam":
        return
    else:
        action("pokes " + text)


@hook.regex(r'.*(?i)cloud.*')
def clouds(message=None, nick=None):
    message("{} is talking about clouds".format(nick))
	
@hook.regex(r'.*(?i)database.*')
def db(message=None, nick=None):
	num = random.randint(0,10)
	if num >= 5:
		message("fuck off {} you gimp".format(nick))
	elif num >=10:
		message("confirmed {} is a fuckpig".format(nick))
	else:
		message("{} loves to fisted by ten database engineers".format(nick))


@hook.command(autohelp=False)
def wtc():
    target_url = "http://whatthecommit.com/index.txt"
    for line in http.open(target_url):
        return "{}".format(http.unescape(line))
		
@hook.regex(r'(?i)(I|i)s (J|j)amii (.*)(!| |\\.|\?)*')
def jamii(match, nick=None, message=None):
	message("He certainly is {} old mate ".format(match.group(3)))
