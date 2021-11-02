import json
import webbrowser
import readline


# VERSION: 2.1.0
# Made by Ewy 16.10.2018
# Last Update: 02.11.2021

class TabCompleter(object):

    def __init__(self, options):
        self.options = sorted(options)

    def complete(self, text, state):
        if state == 0:  # on first trigger, build possible matches
            if text:  # cache matches (entries that start with entered text)
                self.matches = [s for s in self.options if s and s.startswith(text)]
            else:  # no text entered, all matches possible
                self.matches = self.options[:]

        # return match indexed by state
        try:
            return self.matches[state]
        except IndexError:
            return None


LANE_LIST = ['aram', 'mid', 'top', 'jungle', 'bot', 'support']


def getTabCompletion(champions):
    completer = TabCompleter(champions)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')

    for champion in champions:
        readline.add_history(champion)


def getChamp():
    getTabCompletion(json.load(open('champions.json')))
    champ = input('Champion: ')
    return champ


def getLane():
    getTabCompletion(LANE_LIST)
    lane = input('Lane: ')
    return lane


def getLink(champ, lane):
    if lane == 'aram':
        return 'https://euw.op.gg/aram/' + champ + '/statistics/450/build'
    else:
        return 'https://euw.op.gg/champion/' + champ + '/statistics/' + lane


def openLink(url):
    webbrowser.open(url)


if __name__ == '__main__':
    print('OP.GG LOOKUP\n')

    while True:
        openLink(getLink(getChamp(), getLane()))
        print('')
