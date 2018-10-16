import webbrowser
import readline


# VERSION: 1.0.1 #
# Made by Ewy 16.10.2018 #

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


champlist = [
    "aatrox", "ahri", "akali", "alistar", "amumu", "anivia", "annie", "ashe", "aurelion sol", "azir", "bard",
    "blitzcrank", "brand", "braum", "caitlyn", "camille", "cassiopeia", "chogath", "corki", "darius", "diana",
    "drmundo", "draven", "ekko", "elise", "evelynn", "ezreal", "fiddlesticks", "fiora", "fizz", "galio",
    "gangplank", "garen", "gnar", "gragas", "graves", "hecarim", "heimerdinger", "illaoi", "ivern", "irelia",
    "janna", "jarvaniv", "jax", "jayce", "jhin", "jinx", "kaisa", "kalista", "karma", "karthus", "kassadin",
    "katarina", "kayle", "kayn", "kennen", "khazix", "kindred", "kled", "kogmaw", "leblanc", "leesin", "leona",
    "lissandra", "lucian", "lulu", "lux", "malphite", "malzahar", "maokai", "masteryi", "miss fortune",
    "mordekaiser", "morgana", "nami", "nasus", "nautilus", "nidalee", "nocturne", "nunu", "olaf", "orianna",
    "ornn", "pantheon", "poppy", "pyke", "quinn", "rakan", "rammus", "reksai", "renekton", "rengar", "riven",
    "rumble", "ryze", "sejuani", "shaco", "shen", "shyvana", "singed", "sion", "sivir", "skarner", "sona",
    "soraka", "swain", "syndra", "tahmkench", "taliyah", "talon", "taric", "teemo", "thresh", "tristana",
    "trundle", "tryndamere", "twistedfate", "twitch", "udyr", "urgot", "varus", "vayne", "veigar", "velkoz",
    "vi", "viktor", "vladimir", "volibear", "warwick", "wukong", "xayah", "xerath", "xinzhao", "yasuo",
    "yorick", "zac", "zed", "ziggs", "zilean", "zoe"
]

lanelist = ["mid", "top", "jungle", "bot", "support"]


def getTabCompletion(list):
    completer = TabCompleter(list)
    readline.set_completer(completer.complete)
    readline.parse_and_bind('tab: complete')
    for kw in list:
        readline.add_history(kw)


def getChamp():
    getTabCompletion(champlist)
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
