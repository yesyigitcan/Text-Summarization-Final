from rouge import Rouge
import os
import datetime
#hypothesis_ext_path = "Auto Summaries\Document_1_GeneratedExtended_2022-04-20_21-49.txt"
#hypothesis_edg_path = "Auto Summaries\Document_1_GeneratedEdgeSumm_2022-04-20_22-00.txt"
#hypothesis_ext_path = "Latest Auto Summaries\Document_1_GeneratedExtended.txt"
#hypothesis_edg_path = "Latest Auto Summaries\Document_1_GeneratedEdgeSumm.txt"

summaryFileName = "Document_5"
outputfileName = "Evaluation.txt"
summaryN = 12
summaryNStr = str(summaryN)

output_path = os.path.join("Evaluation", "_".join([summaryFileName, summaryNStr, outputfileName]) )

folderName = os.path.join("Summary", "Auto Generated")

hypothesis_ext_path = os.path.join(folderName, "_".join([summaryFileName, "ExtendedSumm", summaryNStr]))

'''
hypothesis_ext2_path = os.path.join(folderName, "_".join([summaryFileName, "ExtendedSumm2", summaryNStr]))
'''

hypothesis_edg_path = os.path.join(folderName, "_".join([summaryFileName, "EdgeSumm", summaryNStr]))
reference_path = os.path.join("Summary", "Human Generated", "_".join([summaryFileName, summaryNStr, "Human"]))

if os.path.exists(hypothesis_ext_path):
    raise Exception("ExtendedSumm summary could not be found at {}".format(hypothesis_ext_path))
'''
if os.path.exists(hypothesis_ext2_path):
    raise Exception("ExtendedSumm2 summary could not be found at {}".format(hypothesis_ext_path))
'''
if os.path.exists(hypothesis_edg_path):
    raise Exception("EdgeSumm summary could not be found at {}".format(hypothesis_edg_path))
if os.path.exists(reference_path):
    raise Exception("Human summary could not be found at {}".format(reference_path))

hypothesis_ext_path += ".txt"
# hypothesis_ext2_path += ".txt"
hypothesis_edg_path += ".txt"
reference_path += ".txt"

with open(hypothesis_ext_path, 'r', encoding='utf-8') as inputExtFile:
    hypothesis_ext = inputExtFile.read().replace('\n', ' ')

'''
with open(hypothesis_ext2_path, 'r', encoding='utf-8') as inputExtFile:
    hypothesis_ext2 = inputExtFile.read().replace('\n', ' ')
'''

with open(hypothesis_edg_path, 'r', encoding='utf-8') as inputEdgFile:
    hypothesis_edg = inputEdgFile.read().replace('\n', ' ')

with open(reference_path, 'r', encoding='utf-8') as referenceFile:
    reference = referenceFile.read().replace('\n', ' ')


rogue_summary = ""
table_summary = "|"
# Note: "f" stands for f1_score, "p" stands for precision, "r" stands for recall.
rouge = Rouge()

rogue_summary += "EdgeSumm Rouge Scores\nFilename: {}\n".format(hypothesis_edg_path)
scores = rouge.get_scores(hypothesis_edg, reference)
print("EdgeSumm Rouge Scores")
print(scores)
print(scores[0])
table_summary += str(round(scores[0]["rouge-1"]["r"], 5)) + "|"
table_summary += str(round(scores[0]["rouge-1"]["p"], 5)) + "|"
table_summary += str(round(scores[0]["rouge-1"]["f"], 5)) + "|"
table_summary += str(round(scores[0]["rouge-2"]["r"], 5)) + "|"
table_summary += str(round(scores[0]["rouge-2"]["p"], 5)) + "|"
table_summary += str(round(scores[0]["rouge-2"]["f"], 5)) + "|"
table_summary += str(round(scores[0]["rouge-l"]["r"], 5)) + "|"
table_summary += str(round(scores[0]["rouge-l"]["p"], 5)) + "|"
table_summary += str(round(scores[0]["rouge-l"]["f"], 5)) + "|"
table_summary += "\n"
rogue_summary += str(scores) + "\n\n"

print()

table_summary += "|"
rogue_summary += "Extended Rouge Scores\nFilename: {}\n".format(hypothesis_ext_path)
scores = rouge.get_scores(hypothesis_ext, reference)
print("ExtendedSumm Rouge Scores")
print(scores)
table_summary += str(round(scores[0]["rouge-1"]["r"], 5)) + "|"
table_summary += str(round(scores[0]["rouge-1"]["p"], 5)) + "|"
table_summary += str(round(scores[0]["rouge-1"]["f"], 5)) + "|"
table_summary += str(round(scores[0]["rouge-2"]["r"], 5)) + "|"
table_summary += str(round(scores[0]["rouge-2"]["p"], 5)) + "|"
table_summary += str(round(scores[0]["rouge-2"]["f"], 5)) + "|"
table_summary += str(round(scores[0]["rouge-l"]["r"], 5)) + "|"
table_summary += str(round(scores[0]["rouge-l"]["p"], 5)) + "|"
table_summary += str(round(scores[0]["rouge-l"]["f"], 5)) + "|"
rogue_summary += str(scores)
'''
print()

rogue_summary += "Extended 2 Rouge Scores\nFilename: {}\n".format(hypothesis_ext2_path)
scores = rouge.get_scores(hypothesis_ext2, reference)
print("ExtendedSumm2 Rouge Scores")
print(scores)
rogue_summary += str(scores)
'''
rogue_summary += "\n\n" + table_summary

with open(output_path, 'w') as outputfile:
    outputfile.write(rogue_summary)
    