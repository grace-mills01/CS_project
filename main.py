import persons
from persons import Participant

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

        depression_values = data[3:12]
        depression_index = Participant.calculate_depression(depression_values)

        screen_time_raw = data[-1]
        screen_time = Participant.parse_screen_time(screen_time_raw)

        name = "Person_"+ str(n)

        p = Participant (n, name, screen_time, depression_index)
        participants.append(p)
        n= n+1
    file.close()
    return participants

def sort_by_screen_time(participants):
    n = len (participants)
    i = 0
    while i < n-1:
        j = 0
        while j < n-1-i:
            if participants[j].screen_time > participants[j + 1].screen_time:
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
    result = {"Screen time 0-2 hours":[["0-4", 0], ["5-9", 0], ["10-14", 0], ["15-19", 0], ["20-27", 0]],
            "Screen time 3-4 hours": [["0-4", 0], ["5-9", 0], ["10-14", 0], ["15-19", 0], ["20-27", 0]],
            "Screen time 5-6 hours": [["0-4", 0], ["5-9", 0], ["10-14", 0], ["15-19", 0], ["20-27", 0]],
            "Screen time 6+ hours": [["0-4", 0], ["5-9", 0], ["10-14", 0], ["15-19", 0], ["20-27", 0]]}

    total_per_st = {"Screen time 0-2 hours": len(dict_st["Screen time 0-2 hours"]),
            "Screen time 3-4 hours": len(dict_st["Screen time 3-4 hours"]),
            "Screen time 5-6 hours": len(dict_st["Screen time 5-6 hours"]),
            "Screen time 6+ hours": len(dict_st["Screen time 6+ hours"])}


    for x in range (4):
        if x == 0 :
            key = "Screen time 0-2 hours"
        elif x == 1:
            key = "Screen time 3-4 hours"
        elif x == 2:
            key = "Screen time 5-6 hours"
        elif x == 3:
            key = "Screen time 6+ hours"

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

    totals_02 = [result["Screen time 0-2 hours"][0][1] / total_per_st["Screen time 0-2 hours"],
                 result["Screen time 0-2 hours"][1][1] / total_per_st["Screen time 0-2 hours"],
                 result["Screen time 0-2 hours"][2][1] / total_per_st["Screen time 0-2 hours"],
                 result["Screen time 0-2 hours"][3][1] / total_per_st["Screen time 0-2 hours"],
                 result["Screen time 0-2 hours"][4][1] / total_per_st["Screen time 0-2 hours"]]

    totals_34 = [result["Screen time 3-4 hours"][0][1] / total_per_st["Screen time 3-4 hours"],
                 result["Screen time 3-4 hours"][1][1] / total_per_st["Screen time 3-4 hours"],
                 result["Screen time 3-4 hours"][2][1] / total_per_st["Screen time 3-4 hours"],
                 result["Screen time 3-4 hours"][3][1] / total_per_st["Screen time 3-4 hours"],
                 result["Screen time 3-4 hours"][4][1] / total_per_st["Screen time 3-4 hours"]]

    totals_56 = [result["Screen time 5-6 hours"][0][1] / total_per_st["Screen time 5-6 hours"],
                result["Screen time 5-6 hours"][1][1] / total_per_st["Screen time 5-6 hours"],
                result["Screen time 5-6 hours"][2][1] / total_per_st["Screen time 5-6 hours"],
                result["Screen time 5-6 hours"][3][1] / total_per_st["Screen time 5-6 hours"],
                result["Screen time 5-6 hours"][4][1] / total_per_st["Screen time 5-6 hours"]]

    totals_6 = [result["Screen time 6+ hours"][0][1] / total_per_st["Screen time 6+ hours"],
                result["Screen time 6+ hours"][1][1] / total_per_st["Screen time 6+ hours"],
                result["Screen time 6+ hours"][2][1] / total_per_st["Screen time 6+ hours"],
                result["Screen time 6+ hours"][3][1] / total_per_st["Screen time 6+ hours"],
                result["Screen time 6+ hours"][4][1] / total_per_st["Screen time 6+ hours"]]

    total_precents = {"Screen time 0-2 hours": [totals_02[0]*100,
                                                totals_02[1]*100,
                                                totals_02[2]*100,
                                                totals_02[3]*100,
                                                totals_02[4]*100],
            "Screen time 3-4 hours": [totals_34[0]*100,
                                    totals_34[1]*100,
                                    totals_34[2]*100,
                                    totals_34[3]*100,
                                    totals_34[4]*100],
            "Screen time 5-6 hours": [totals_56[0]*100,
                                    totals_56[1]*100,
                                    totals_56[2]*100,
                                    totals_56[3]*100,
                                    totals_56[4]*100],
            "Screen time 6+ hours": [totals_6[0]*100,
                                    totals_6[1]*100,
                                    totals_6[2]*100,
                                    totals_6[3]*100,
                                    totals_6[4]*100]}

    return total_precents

def main():
    dict_participants_screen_time = {"Screen time 0-2 hours": [],
                                     "Screen time 3-4 hours": [],
                                     "Screen time 5-6 hours": [],
                                     "Screen time 6+ hours": [],}
    dict_participants_depression_index = {"Index of 0-4 (None-minimal)": [],
                                          "Index of 5-9 (Mild)": [],
                                          "Index of 10-14 (Moderate)": [],
                                          "Index of 15-19 (Moderately Severe)": [],
                                          "Index of 20-27 (Severe)": [],}

    participants = load_participants("Screen_Time_Inputs.txt")

    for person in participants:
        screen_time = person.screen_time

        if screen_time >= 0 and screen_time <= 2:
            dict_participants_screen_time["Screen time 0-2 hours"].append(person)
        elif screen_time > 2 and screen_time <= 4:
            dict_participants_screen_time["Screen time 3-4 hours"].append(person)
        elif screen_time > 4 and screen_time <= 6:
            dict_participants_screen_time["Screen time 5-6 hours"].append(person)
        elif screen_time > 6:
            dict_participants_screen_time["Screen time 6+ hours"].append(person)

    for person in participants:
        depression_index = person.depression_index

        if depression_index > 0 and depression_index <= 4:
            dict_participants_depression_index["Index of 0-4 (None-minimal)"].append(person)
        elif depression_index >= 5 and depression_index <= 9:
            dict_participants_depression_index["Index of 5-9 (Mild)"].append(person)
        elif depression_index >= 10 and depression_index <= 14:
            dict_participants_depression_index["Index of 10-14 (Moderate)"].append(person)
        elif depression_index >= 15 and depression_index <= 19:
            dict_participants_depression_index["Index of 15-19 (Moderately Severe)"].append(person)
        elif depression_index >= 20 and depression_index <= 27:
            dict_participants_depression_index["Index of 20-27 (Severe)"].append(person)

    #overall output
    print ("We surveyed 18 people with a general form surveying for screen time, mood, and depression.","\n",
    "Our results are displayed below with insights into why some correlations appear")

    #percentage output
    percents = percentages_per_screenTime(dict_participants_screen_time)
    #counts how many people in each screen time group
    counts = count_screen_time_groups(dict_participants_screen_time)

    print("\nNumber of participants by screen time:")
    print("0–2 hours:", counts["Screen time 0-2 hours"])
    print("3–4 hours:", counts["Screen time 3-4 hours"])
    print("5–6 hours:", counts["Screen time 5-6 hours"])
    print("6+ hours:", counts["Screen time 6+ hours"])

    print ("\nScreen time 0-2 hours:","\n",
           "Percent at 0-4 depression index", percents["Screen time 0-2 hours"][0], "\n"
           "Percent at 5-9 depression index", percents["Screen time 0-2 hours"][1], "\n"
           "Percent at 10-14 depression index", percents["Screen time 0-2 hours"][2], "\n"
           "Percent at 15-19 depression index", percents["Screen time 0-2 hours"][3], "\n"
           "Percent at 20-27 depression index", percents["Screen time 0-2 hours"][4])

    print("Screen time 3-4 hours:", "\n",
        "Percent at 0-4 depression index", percents["Screen time 3-4 hours"][0], "\n"
        "Percent at 5-9 depression index",percents["Screen time 3-4 hours"][1], "\n"
        "Percent at 10-14 depression index", percents["Screen time 3-4 hours"][2], "\n"
        "Percent at 15-19 depression index", percents["Screen time 3-4 hours"][3], "\n"
        "Percent at 20-27 depression index",percents["Screen time 3-4 hours"][4])

    print("Screen time 5-6 hours:", "\n",
        "Percent at 0-4 depression index", percents["Screen time 5-6 hours"][0], "\n"
        "Percent at 5-9 depression index",percents["Screen time 5-6 hours"][1], "\n"
        "Percent at 10-14 depression index",percents["Screen time 5-6 hours"][2], "\n"
        "Percent at 15-19 depression index",percents["Screen time 5-6 hours"][3], "\n"
        "Percent at 20-27 depression index", percents["Screen time 5-6 hours"][4])

    print("Screen time 6+ hours:", "\n",
        "Percent at 0-4 depression index", percents["Screen time 6+ hours"][0], "\n"
        "Percent at 5-9 depression index",percents["Screen time 6+ hours"][1], "\n"
        "Percent at 10-14 depression index",percents["Screen time 6+ hours"][2], "\n"
        "Percent at 15-19 depression index",percents["Screen time 6+ hours"][3], "\n"
        "Percent at 20-27 depression index",percents["Screen time 6+ hours"][4])

def count_screen_time_groups(dict_st):
    return {
        "Screen time 0-2 hours": len(dict_st["Screen time 0-2 hours"]),
        "Screen time 3-4 hours": len(dict_st["Screen time 3-4 hours"]),
        "Screen time 5-6 hours": len(dict_st["Screen time 5-6 hours"]),
        "Screen time 6+ hours": len(dict_st["Screen time 6+ hours"])
    }

if __name__ == "__main__":
    main()


