# Task 1 — Process the Scores
def process_scores(students):
    averages = {}

    for name, scores in students.items():
        avg = round(sum(scores) / len(scores), 2)
        averages[name] = avg

    return averages


# Task 2 — Classify Grades
def classify_grades(averages):
    classified = {}

    # grading thresholds (inside function)
    A = 90
    B = 75
    C = 60

    for name, avg in averages.items():
        if avg >= A:
            grade = "A"
        elif avg >= B:
            grade = "B"
        elif avg >= C:
            grade = "C"
        else:
            grade = "F"

        classified[name] = (avg, grade)

    return classified


# Task 3 — Generate Report
def generate_report(classified, passing_avg=70):
    total = len(classified)
    passed = 0
    failed = 0

    print("===== Student Grade Report =====")

    for name, (avg, grade) in classified.items():
        if avg >= passing_avg:
            status = "PASS"
            passed += 1
        else:
            status = "FAIL"
            failed += 1

        print(f"{name} | Avg: {avg:.2f} | Grade: {grade} | Status: {status}")

    print("===============================")
    print("Total Students :", total)
    print("Passed         :", passed)
    print("Failed         :", failed)

    return passed


# ----- Main Program -----
students_data = {
    "Alice": [85, 90, 84],
    "Bob": [60, 65, 62],
    "Clara": [95, 97, 97]
}

averages = process_scores(students_data)
classified = classify_grades(averages)
generate_report(classified)