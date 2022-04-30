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
hypothesis_edg_path = os.path.join(folderName, "_".join([summaryFileName, "EdgeSumm", summaryNStr]))
reference_path = os.path.join("Summary", "Human Generated", "_".join([summaryFileName, summaryNStr, "Human"]))

if os.path.exists(hypothesis_ext_path):
    raise Exception("ExtendedSumm summary could not be found at {}".format(hypothesis_ext_path))
if os.path.exists(hypothesis_edg_path):
    raise Exception("EdgeSumm summary could not be found at {}".format(hypothesis_edg_path))
if os.path.exists(reference_path):
    raise Exception("Human summary could not be found at {}".format(reference_path))

hypothesis_ext_path += ".txt"
hypothesis_edg_path += ".txt"
reference_path += ".txt"

with open(hypothesis_ext_path, 'r', encoding='utf-8') as inputExtFile:
    hypothesis_ext = inputExtFile.read().replace('\n', ' ')

with open(hypothesis_edg_path, 'r', encoding='utf-8') as inputEdgFile:
    hypothesis_edg = inputEdgFile.read().replace('\n', ' ')

with open(reference_path, 'r', encoding='utf-8') as referenceFile:
    reference = referenceFile.read().replace('\n', ' ')


rogue_summary = ""
# Note: "f" stands for f1_score, "p" stands for precision, "r" stands for recall.
rouge = Rouge()

rogue_summary += "EdgeSumm Rouge Scores\nFilename: {}\n".format(hypothesis_edg_path)
scores = rouge.get_scores(hypothesis_edg, reference)
print("EdgeSumm Rouge Scores")
print(scores)
rogue_summary += str(scores) + "\n\n"

print()

rogue_summary += "Extended Rouge Scores\nFilename: {}\n".format(hypothesis_ext_path)
scores = rouge.get_scores(hypothesis_ext, reference)
print("ExtendedSumm Rouge Scores")
print(scores)
rogue_summary += str(scores)


with open(output_path, 'w') as outputfile:
    outputfile.write(rogue_summary)