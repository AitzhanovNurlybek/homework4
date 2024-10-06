
input_file = 'class_scores.txt'
output_file = 'scores2.txt'

with open(input_file, 'r') as infile:
    lines = infile.readlines()

updated_scores = []

for line in lines:
    username, score = line.split()
    new_score = int(score) + 5 
    updated_scores.append(f"{username} {new_score}\n")

with open(output_file, 'w') as outfile:
    outfile.writelines(updated_scores)

print("Scores updated and saved to scores2.txt.")
