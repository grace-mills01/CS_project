#Holds our participant Class and all functions
'''
When creating a participant object the depression index needs to be read from the file
so first create a variable of the depression index and that adds the desired values together and
then pass that into the participants parameters

mood index and productivity also need to be read from the text file but nothing needs to be added
the id should correspond to which number entry the participant is in the text file
'''


class Participants:

    def __init__(self, id, name, screen_time, depression_index, mood_index, productivity_index):
        self.id = id
        self.name = name
        self.screen_time = screen_time
        self.depression_index = depression_index
        self.mood_index = mood_index
        self.productivity_index = productivity_index

    def __repr__(self):
        return ("The participants name and id is {},{} with the following stats: screen time: {}, ",
                "depression index: {}, ",
                "mood index: {}, ",
                "productivity index: {}". format(self.name, self.id, self.screen_time, self.depression_index,))

    def __eq__(self, other):
        return (self is other or
                type(self) == type(other) and
                self.screen_time == other.screen_time and
                self.depression_index == other.depression_index and
                self.mood_index == other.mood_index and
                self.productivity_index == other.productivity_index and
                self.id == other.id and
                self.name == other.name)


def overall_score(self):
    return self.depression_index - self.mood_index - self.productivity_index
def parse_screen_time(raw):
    raw = raw.lower()
    raw = raw.replace("hours", "")
    raw = raw.replace("hour", "")
    raw = raw.replace("hrs", "")
    raw = raw.replace("hr", "")
    raw = raw.replace("or", "")
    raw = raw.strip()
    number_str = ""
    for ch in raw:
        if (ch>= "0" and ch ,+ "9") or ch == ".":
            number_str = number_str + ch
    if number_str == "":
        return 0.0

    return float(number_str)
def calculate_depression(values):
    total = 0
    i = 0
    while i < len(values):
        total = total + int(values[i])
        i = i + 1
    return total

