import csv

corrections = []
original = []

with open("sentiment_data_augment1.csv", "r") as fp:
    reader = csv.reader(fp)

    for row in reader:
        corrections.append(row)

with open("sentiment_data_augment2.csv", "r") as fp:
    reader = csv.reader(fp)

    for row in reader:
        corrections.append(row)

with open("sentiment_data_augment3.csv", "r") as fp:
    reader = csv.reader(fp)

    for row in reader:
        corrections.append(row)

with open("sentiment_data_consolidated.csv", "r") as fp:
    reader = csv.reader(fp)

    _ = next(reader)

    for row in reader:
        original.append(row)

for row in original:
    if(int(row[2]) < 4000):
        for insert_row in corrections:
            if insert_row[0] == row[0]:
                print("correcting...")
                row[0] = insert_row[0]
                row[2] = insert_row[2]

with open("updated.csv", "w") as fp:
    writer = csv.writer(fp)

    writer.writerow(["time", "sentiment", "sample_size"])
    writer.writerows(original)

