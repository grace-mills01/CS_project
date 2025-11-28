import unittest
from persons import Participant
import main
class TestPersonFunctions(unittest.TestCase):
    def test_parse_screen_time(self):
        self.assertEqual(Participant.parse_screen_time("3.5 hours"), 3.5)
        self.assertEqual(Participant.parse_screen_time("7hr"), 7.0)
        self.assertEqual(Participant.parse_screen_time("32hrs"), 32.0)
        self.assertEqual(Participant.parse_screen_time("5 "), 5.0)
        self.assertEqual(Participant.parse_screen_time(""), 0.0)

    def test_calculate_depression(self):
        self.assertEqual(Participant.calculate_depression(["2", "3"]), 5)
        self.assertEqual(Participant.calculate_depression(["2", "3", "4"]), 9)
        self.assertEqual(Participant.calculate_depression(["2", "4", "2", "3","2","5","2","2","4"]), 26)

class TestMainFunctions(unittest.TestCase):
    def test_sort_by_screen_time(self):
        p1 = Participant(1, "Random 1", 2, 3)
        p2 = Participant(2, "Random 2", 4, 5)
        p3 = Participant(3, "Random 3", 5, 6)
        result = main.sort_by_screen_time([p1, p2, p3])
        self.assertEqual(result, [p1, p2, p3])

    def test_sort_by_depression(self):
        p1 = Participant(1, "Random 1", 2.0, 7)
        p2 = Participant(2, "Random 2", 8.0, 8)
        p3 = Participant(3, "Random 3", 5.0, 4)
        result = main.sort_by_depression_score([p1, p2, p3])
        self.assertEqual(result, [p3, p1, p2])

    def test_percentages_per_screen_time(self):
        p1 = Participant(1, "Random 1", 2, 3)
        p2 = Participant(2, "Random 2", 4, 5)
        p3 = Participant(3, "Random 3", 5, 6)
        p4 = Participant(4, "Random 4", 6, 14)
        p5 = Participant(5, "Random 5", 8, 20)
        p6 = Participant(6, "Random 6", 3, 2)

        groups = {
            "Screen time 0-2 hours":[p1],
            "Screen time 3-4 hours":[p2,p6],
            "Screen time 5-6 hours":[p3,p4],
            "Screen time 6+ hours":[p5]
        }
        result = main.percentages_per_screenTime(groups)

        self.assertEqual(result["Screen time 0-2 hours"],[100.0, 0.0, 0.0, 0.0, 0.0])

    def test_count_screen_time_groups(self):
        p1 = Participant(1, "A", 1, 3)
        p2 = Participant(2, "B", 3, 6)
        p3 = Participant(3, "C", 5, 8)
        p4 = Participant(4, "D", 7, 10)

        groups = {
            "Screen time 0-2 hours": [p1],
            "Screen time 3-4 hours": [p2],
            "Screen time 5-6 hours": [p3],
            "Screen time 6+ hours": [p4]
        }

        counts = main.count_screen_time_groups(groups)

        self.assertEqual(counts["Screen time 0-2 hours"], 1)
        self.assertEqual(counts["Screen time 3-4 hours"], 1)
        self.assertEqual(counts["Screen time 5-6 hours"], 1)
        self.assertEqual(counts["Screen time 6+ hours"], 1)

if __name__ == "__main__":
        unittest.main()