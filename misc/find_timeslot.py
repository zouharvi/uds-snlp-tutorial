#!/usr/bin/env python3

import sys
import csv
from collections import defaultdict

# index corresponds to the ordering in the original poll
slots_a = {1,2,4,6}
slots_j = {5,8,10,11}
slots_v = {3,7,9,12}

student_slots = defaultdict(lambda: set())
student_names = set()
data_loss = defaultdict(lambda: [])

# Input: cleaned exported csv file without the header (and without Vilém's vote which can't be removed)
with open(sys.argv[1], 'r', newline='') as f:
    reader = csv.reader(f, quotechar='"')
    _header = next(reader)
    _vilem_vote = next(reader)
    print("Skipping:", _header)
    print("Skipping:", _vilem_vote)
    for line in reader:
        # end of slots vote segment
        if len(line) == 0:
            break
        name, _email, slots = line
        slots = slots.strip('"').replace('.',',').split(',')
        for slot in slots:
            slot = int(slot)
            student_slots[slot].add(name)
        student_names.add(name)

# n^3 try all configurations and store the results
for slot_a in slots_a:
    for slot_j in slots_j:
        for slot_v in slots_v:
            covered_students = student_slots[slot_a].union(student_slots[slot_j]).union(student_slots[slot_v])
            loss = len(student_names) - len(covered_students)
            data_loss[loss].append({'awantee': slot_a,  'julius': slot_j, 'vilem':  slot_v, 'loss': loss})
            # 'loss_stud': student_names.difference(covered_students)

# print all configurations with minimal loss (number of student not covered)
min_loss = min(data_loss.keys())
for config in data_loss[min_loss]:
    print(config)
