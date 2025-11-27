#Holds our participant Class and all functions
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

