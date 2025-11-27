import Participant

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

        if len(data) < 13:
            continue
        mood = int(data[1])
        productivity = int(data[2])

        depression_values = data[3:12]
        depression_index = Participant.calculate_depression(depression_values)

        screen_time_raw = data[3:12]
        screen_time = Participant.parse_screen_time(screen_time_raw)

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

def sort_by_depression_score(participants):
    n = len (participants)
    i = 0
    while i < n-1:
        j = 0
        while j < n-1-i:
            if participants[j].depression_index > participants[j + 1].depression_index:
                temp = participants[j]
                participants[j] = participants [j+1]
                participants[j + 1] = temp
            j = j + 1
        i = i + 1
    return participants

def percentages_per_screenTime(dict_st):
    result = {"Screen Time 0-2 hours":[["0-4", 0], ["5-9", 0], ["10-14", 0], ["15-19", 0], ["20-27", 0]],
            "Screen Time 4-2 hours": [["0-4", 0], ["5-9", 0], ["10-14", 0], ["15-19", 0], ["20-27", 0]],
            "Screen Time 4-6 hours": [["0-4", 0], ["5-9", 0], ["10-14", 0], ["15-19", 0], ["20-27", 0]],
            "Screen Time 6+ hours": [["0-4", 0], ["5-9", 0], ["10-14", 0], ["15-19", 0], ["20-27", 0]]}

    total_per_st = {"Screen Time 0-2 Hours": len(dict_st["Screen Time 0-2 Hours"]),
            "Screen Time 4-2 Hours": len(dict_st["Screen Time 2-4 Hours"]),
            "Screen Time 4-6 Hours": len(dict_st["Screen Time 4-6 Hours"]),
            "Screen Time 6+ Hours": len(dict_st["Screen Time 6+ Hours"])}


    for x in range (4):
        if x == 0 :
            key = "Screen Time 0-2 Hours"
        elif x == 1:
            key = "Screen Time 2-4 Hours"
        elif x == 2:
            key = "Screen Time 4-6 Hours"
        elif x == 3:
            key = "Screen Time 6+ Hours"

        for i in dict_st[key]:
            index = i.depression_index
            if index > 0 and index <= 4:
                result[key][0][1] += 1
            elif index >= 5 and index <= 9:
                result[key][1][1] += 1
            elif index >= 10 and index <= 14:
                result[key][2][1] += 1
            elif index >= 15 and index <= 19:
                result[key][3][1] += 1
            elif index >= 20 and index <= 27:
                result[key][4][1] += 1

    totals_02 = [result["Screen Time 0-2 hours"][0][1] / total_per_st["Screen Time 0-2 Hours"],
                 result["Screen Time 0-2 hours"][1][1] / total_per_st["Screen Time 0-2 Hours"],
                 result["Screen Time 0-2 hours"][2][1] / total_per_st["Screen Time 0-2 Hours"],
                 result["Screen Time 0-2 hours"][3][1] / total_per_st["Screen Time 0-2 Hours"],
                 result["Screen Time 0-2 hours"][4][1] / total_per_st["Screen Time 0-2 Hours"]]

    totals_24 = [result["Screen Time 2-4 hours"][0][1] / total_per_st["Screen Time 2-4 Hours"],
                 result["Screen Time 2-4 hours"][1][1] / total_per_st["Screen Time 2-4 Hours"],
                 result["Screen Time 2-4 hours"][2][1] / total_per_st["Screen Time 2-4 Hours"],
                 result["Screen Time 2-4 hours"][3][1] / total_per_st["Screen Time 2-4 Hours"],
                 result["Screen Time 2-4 hours"][4][1] / total_per_st["Screen Time 2-4 Hours"]]

    totals_46 = [result["Screen Time 4-6 hours"][0][1] / total_per_st["Screen Time 4-6 Hours"],
                result["Screen Time 4-6 hours"][1][1] / total_per_st["Screen Time 4-6 Hours"],
                result["Screen Time 4-6 hours"][2][1] / total_per_st["Screen Time 4-6 Hours"],
                result["Screen Time 4-6 hours"][3][1] / total_per_st["Screen Time 4-6 Hours"],
                result["Screen Time 4-6 hours"][4][1] / total_per_st["Screen Time 4-6 Hours"]]

    totals_6 = [result["Screen Time 6+ hours"][0][1] / total_per_st["Screen Time 6+ Hours"],
                result["Screen Time 6+ hours"][1][1] / total_per_st["Screen Time 6+ Hours"],
                result["Screen Time 6+ hours"][2][1] / total_per_st["Screen Time 6+ Hours"],
                result["Screen Time 6+ hours"][3][1] / total_per_st["Screen Time 6+ Hours"],
                result["Screen Time 6+ hours"][4][1] / total_per_st["Screen Time 6+ Hours"]]

    total_precents = {"Screen Time 0-2 hours": [totals_02[0]*100,
                                                totals_02[1]*100,
                                                totals_02[2]*100,
                                                totals_02[3]*100,
                                                totals_02[4]*100],
            "Screen Time 4-2 hours": [totals_24[0],
                                                totals_24[1]*100,
                                                totals_24[2]*100,
                                                totals_24[3]*100,
                                                totals_24[4]*100],
            "Screen Time 4-6 hours": [totals_46[0],
                                                totals_46[1]*100,
                                                totals_46[2]*100,
                                                totals_46[3]*100,
                                                totals_46[4]*100],
            "Screen Time 6+ hours": [totals_6[0],
                                                totals_6[1]*100,
                                                totals_6[2]*100,
                                                totals_6[3]*100,
                                                totals_6[4]*100]}

    return total_precents

def main():
    dict_participants_screen_time = {"Screen time 0-2 hours": [],
                                     "Screen time 2-4 hours": [],
                                     "Screen time 4-6 hours": [],
                                     "Screen time 6+ hours": [],}
    dict_participants_depression_index = {"Index of 0-4 (None-minimal)": [],
                                          "Index of 5-9 (Mild)": [],
                                          "Index of 10-14 (Moderate)": [],
                                          "Index of 15-19 (Moderately Severe)": [],
                                          "Index of 20-27 (Severe)": [],}

    participants = load_participants("Screen_Time_Inputs.txt")
    participants_screenTime = sort_by_screen_time(participants)

    for person in participants_screenTime:
        screen_time = person.screen_time

        if screen_time > 0 and screen_time <= 2:
            dict_participants_screen_time["Screen time 0-2 hours"].append(person.name)
        elif screen_time > 2 and screen_time <= 4:
            dict_participants_screen_time["Screen time 2-4 hours"].append(person.name)
        elif screen_time > 4 and screen_time <= 6:
            dict_participants_screen_time["Screen time 4-6 hours"].append(person.name)
        elif screen_time > 6:
            dict_participants_screen_time["Screen time 6+ hours"].append(person.name)

    participants_depressionIndex = sort_by_depression_score(participants)

    for person in participants_depressionIndex:
        depression_index = person.depression_index

        if depression_index > 0 and depression_index <= 4:
            dict_participants_depression_index["Index of 0-4 (None-minimal)"].append(person.name)
        elif depression_index >= 5 and depression_index <= 9:
            dict_participants_depression_index["Index of 5-9 (Mild)"].append(person.name)
        elif depression_index >= 10 and depression_index <= 14:
            dict_participants_depression_index["Index of 10-14 (Moderate)"].append(person.name)
        elif depression_index >= 15 and depression_index <= 19:
            dict_participants_depression_index["Index of 15-19 (Moderately Severe)"].append(person.name)
        elif depression_index >= 20 and depression_index <= 27:
            dict_participants_depression_index["Index of 20-27 (Severe)"].append(person.name)

    #overall output
    print ("We surveyed 18 people with a general form surveying for screen time, mood, and depression."
           "Our results are displayed below with insights into why some correlations appear")

    #screen time output
    for i in range (len(dict_participants_screen_time)):
        key = dict_participants_screen_time.key()
        print (key, dict_participants_screen_time[key])
        print("There are ", dict_participants_screen_time[key].length,
              "number of participants with a screen time within", key)

    #depression index output
    for i in range(len(dict_participants_depression_index)):
        key = dict_participants_depression_index.key()
        print(key, dict_participants_depression_index[key])
        print("There are ", dict_participants_depression_index[key].length,
              "number of participants with a depression index within", key)

    #percentage output
    percents = percentages_per_screenTime(dict_participants_screen_time)

    print ("Screen Time 0-2 hours:","\n",
           "Percent at 0-4 depression index", percents["Screen Time 0-2 hours"][0], "\n"
           "Percent at 5-9 depression index", percents["Screen Time 0-2 hours"][1], "\n"
           "Percent at 10-14 depression index", percents["Screen Time 0-2 hours"][2], "\n"
           "Percent at 15-19 depression index", percents["Screen Time 0-2 hours"][3], "\n"
           "Percent at 20-27 depression index", percents["Screen Time 0-2 hours"][4])

    print("Screen Time 2-4 hours:", "\n",
        "Percent at 0-4 depression index", percents["Screen Time 2-4 hours"][0], "\n"
        "Percent at 5-9 depression index",percents["Screen Time 2-4 hours"][1], "\n"
        "Percent at 10-14 depression index", percents["Screen Time 2-4 hours"][2], "\n"
        "Percent at 15-19 depression index", percents["Screen Time 2-4 hours"][3], "\n"
        "Percent at 20-27 depression index",percents["Screen Time 2-4 hours"][4])

    print("Screen Time 4-6 hours:", "\n",
        "Percent at 0-4 depression index", percents["Screen Time 4-6 hours"][0], "\n"
        "Percent at 5-9 depression index",percents["Screen Time 4-6 hours"][1], "\n"
        "Percent at 10-14 depression index",percents["Screen Time 4-6 hours"][2], "\n"
        "Percent at 15-19 depression index",percents["Screen Time 4-6 hours"][3], "\n"
        "Percent at 20-27 depression index", percents["Screen Time 4-6 hours"][4])

    print("Screen Time 4-6 hours:", "\n",
        "Percent at 0-4 depression index", percents["Screen Time 4-6 hours"][0], "\n"
        "Percent at 5-9 depression index",percents["Screen Time 4-6 hours"][1], "\n"
        "Percent at 10-14 depression index",percents["Screen Time 4-6 hours"][2], "\n"
        "Percent at 15-19 depression index",percents["Screen Time 4-6 hours"][3], "\n"
        "Percent at 20-27 depression index",percents["Screen Time 4-6 hours"][4])

if __name__ == "__main__":
    main()


    