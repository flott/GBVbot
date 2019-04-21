#!/usr/bin/env python3

# Markovify
# https://github.com/jsvine/markovify
# https://github.com/jsvine/markovify/blob/master/markovify/text.py
import markovify
import random
import tweepy
from secrets import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET

with open("gbvtitles.txt") as f:
    text = f.read()

text_model = markovify.NewlineText(text)


def make_title():
    if random.random() <= 0.05:
        # add a parentheses suffix to the title
        first_len = random.randrange(20, 120)
        second_len = random.randrange(16, 140 - first_len)
        first_part = text_model.make_short_sentence(first_len, tries=100)
        second_part = text_model.make_short_sentence(second_len, tries=100)
        title = first_part + " (" + second_part + ")"
        return title
    else:
        return text_model.make_short_sentence(
            20 + random.randrange(20, 120), tries=100)


def send_msg(api, msg):
    try:
        status = api.update_status(status=msg)
    except tweepy.error.TweepError as e:
        print(repr(e))


def main():
    # Twitter API setup
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    api = tweepy.API(auth)
    title = make_title()
    send_msg(api, title)


if __name__ == '__main__':
    main()
