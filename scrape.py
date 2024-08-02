import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/'
                   )
object = BeautifulSoup(res.text, 'html.parser')
links = object.select('.titleline a')
subtext = object.select('.subtext')


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom(links, subtext):
    hn = []
    for index, item in enumerate(links):
        text = links[index].getText()
        href = links[index].get('href', None)
        if index < len(subtext):
            vote = subtext[index].select('.score')
            if len(vote):
                points = int(vote[0].getText().replace(' points', ''))
                if points >= 100:
                    hn.append({'text': text, 'href': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom(links, subtext))
