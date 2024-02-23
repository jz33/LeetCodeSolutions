import re
import os

# Match like 888., not 80.6%
leetcodeQuestionPattern = re.compile(r"\d+\.(?!\d+)")

# Match T-123 or 123
filesPattern = re.compile(r"\d+ ")

# The file contains a rough string copy of finished LeetCode questions
with open('./finished_questions.txt', 'r') as f:
    leetcodeSolvedQuestionNumbers = leetcodeQuestionPattern.findall(f.read())
    # Remove .
    leetcodeSet = set([number[:-1] for number in leetcodeSolvedQuestionNumbers])
    
    filenames = os.listdir()
    myQuestionNumbers = []
    for name in filenames:
        matches = filesPattern.findall(name)
        if matches:
            # Convert to int then str to remove heading 0
            myQuestionNumbers.append(str(int(matches[0])))

    missing = sorted([mine for mine in myQuestionNumbers if mine not in leetcodeSet])
    print(missing)