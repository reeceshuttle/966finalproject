import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("survey_responses.csv")
# index refers to number of people getting correct for (question-1)
num_correct = []
for q_num in range(1,7):
    correct_q = 0
    for person_num in range(len(df)):
        if df['PDDL Experience'][person_num]<=5: # edit this constraint if desired
            correct_q += df[f'Problem {q_num} Evaluation'][person_num]
    num_correct.append(correct_q)

averages = [val/len(df) for val in num_correct]

# Making plot:

barWidth = 0.25
fig = plt.subplots(figsize = (12, 8))

generic_averages = averages[:3]
generic_averages = [val+0.004 for val in generic_averages] # for visual effect
descriptive_averages = averages[3:]

br1 = np.arange(len(generic_averages))
br2 = [x + barWidth for x in br1]

plt.bar(br1, generic_averages, color ='b', width = barWidth,
        label ='Generic')
plt.bar(br2, descriptive_averages, color ='r', width = barWidth,
        label ='Descriptive')

plt.xlabel('Survey Problems', fontweight ='bold', fontsize = 15)
plt.ylabel('Proportion Correct', fontweight ='bold', fontsize = 15)
plt.xticks([r + (barWidth/2) for r in range(len(generic_averages))],
        ['Problem 1', 'Problem 2', 'Problem 3'])

plt.ylim([0,1])
plt.text(0.18, averages[3]+0.01, round(averages[3], 4))
plt.text(1.18, averages[4]+0.01, round(averages[4], 4))
plt.text(2.18, averages[5]+0.01, round(averages[5], 4))
plt.text(-0.06, 0.01, '0.00')
plt.text(0.96, 0.01, '0.00')
plt.text(1.96, 0.01, '0.00')
plt.legend()
plt.show()
