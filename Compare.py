import csv
from sys import argv

# Check if arguments are valid
if len(argv) != 5:
    print(
        "Грешка! Използвай така: Compare.py (CSV) (ОЦЕНКА 1) (ОЦЕНКА 2) (ОЦЕНКА 3)"
    )
    exit()

# Open CSV file
with open(argv[1], "r", encoding="utf-8") as ocenki:

    reader = csv.DictReader(ocenki)

    # Def variables
    avg_grade1 = 0.0
    avg_grade2 = 0.0
    avg_grade3 = 0.0
    count_all = 0
    count_disqualified = 0
    better_1 = 0
    better_2 = 0
    better_3 = 0
    better_avg = 0

    # Оценки на потребителя
    user_grade1 = float(argv[2])
    user_grade2 = float(argv[3])
    user_grade3 = float(argv[4])
    user_avg = (user_grade1 + user_grade2 + user_grade3) / 3

    # Събиране на всички оценки
    for row in reader:
        if (float(row["grade1"]) >= 2 and float(row["grade2"]) >= 2
                and float(row["grade3"]) >= 2):
            avg_grade1 += float(row["grade1"])
            avg_grade2 += float(row["grade2"])
            avg_grade3 += float(row["grade3"])
            count_all += 1
            avg_row = (float(row["grade1"]) + float(row["grade2"]) +
                       float(row["grade3"])) / 3

            if (float(row["grade1"]) > user_grade1):
                better_1 += 1
            if (float(row["grade2"]) > user_grade2):
                better_2 += 1
            if (float(row["grade3"]) > user_grade3):
                better_3 += 1
            if (avg_row > user_avg):
                better_avg += 1
        else:
            count_disqualified += 1

    # Пресмятане на средни оценки на явилите се
    avg_grade1 = avg_grade1 / count_all
    avg_grade2 = avg_grade2 / count_all
    avg_grade3 = avg_grade3 / count_all
    avg_all = (avg_grade1 + avg_grade2 + avg_grade3) / 3

    #Брой на явили се на всички изпити
    print(f"\nБрой на явили се на всички изпити: {count_all}\n")

    # Броя на неявили се
    print(f"Броя на неявили се: {count_disqualified}\n")

    # Принтиране на средните оценки на явилите се
    print("Средни оценки на явилите се:")
    print(f"Средна от трите: {round(avg_all,2)}")
    print(f"Рисунка 1: {round(avg_grade1,2)}")
    print(f"Рисунка 2: {round(avg_grade2,2)}")
    print(f"Рисунка 3: {round(avg_grade3,2)}\n")

    # Броя на хората справили се по-добре от потребителя
    print("Броя на явилите се, които са се справили по-добре:")
    print(f"Средна оценка: {better_avg}")
    print(f"Рисунка 1: {better_1}")
    print(f"Рисунка 2: {better_2}")
    print(f"Рисунка 3: {better_3}\n")

    # Показва в ТОП кой процент е потребителя
    print(
        f"Ти си в ТОП {round((better_avg/count_all)*100,2)} процента от явилите се!\n"
    )
