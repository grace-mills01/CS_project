def load_participants(filename):
    participants = []
    file = open(filename, "r")
    header = file.readline()

    n = 1
    for line in file:
        line = line.strip()
        if line == "":
            continue
        data = line.split(",")

        if len(data) < 13
            continue
        mood = int(data[1])
        productivity = int(data[2])

        depression_values = data[3:12]
        depression_index = calculate_depression(depression_values)

        screen_time_raw = data[3:12]
        screen_time = parse_screen_time(screen_time_raw)

        name = "Person_"+ str(n)

        p = Participant (n, name, screen_time, depression_index, mood, participants.append(p))

        n= n+1
    file.close()
    return participants
def sort_by_screen_time(participants):
    n = len (participants)
    i = 0
    while i < n-1:
        j = 0
        while j < n-1-i:
            if participants[j].screentime > participants[j + 1].screen_time:
                temp = participants[j]
                participants[j] = participants [j+1]
                participants[j + 1] = temp
            j = j + 1
        i = i + 1
    return participants

def sort_by_overall_score(participants):
    n = len (participants)
    i = 0
    while i < n-1:
        j = 0
        while j < n-1-i:
            if participants[j].overall_score > participants[j + 1].overall_score:
                temp = participants[j]
                participants[j] = participants [j+1]
                participants[j + 1] = temp
            j = j + 1
        i = i + 1
    return participants

def main():
    