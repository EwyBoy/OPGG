import webbrowser
import readline
import json


# VERSION: 1.1.0 #
# Made by Ewy 16.10.2018 #
# Last Update: 20.03.2019 #

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


lanelist = ["mid", "top", "jungle", "bot", "support"]


def getTabCompletion(list):
    completer = TabCompleter(list)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')
    for kw in list:
        readline.add_history(kw)


def getChamp():
    champions = open('champions.json')
    champion = json.load(champions)
    getTabCompletion(champion)
    global champ
    champ = raw_input('Champion: ')
    return champ


def getLane():
    getTabCompletion(lanelist)
    global lane
    lane = raw_input('Lane: ')
    return lane


def getLink():
    webbrowser.open('https://euw.op.gg/champion/' + getChamp() + '/statistics/' + getLane())
    print ''
    getLink()


if __name__ == '__main__':
    print 'OP.GG LOOKUP\n'
    getLink()
