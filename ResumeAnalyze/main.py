
import yaml

with open('./config/main.yaml', 'r') as f:
    cnf = yaml.load(f, Loader=yaml.SafeLoader)

print ("Resume Analyzer - ", cnf["ver"])

from pyresparser import ResumeParser
data = ResumeParser('D:/wspc3/github/TextAnalysers/samples/resumes/KalashJindal-ML.pdf').get_extracted_data()

import json
print(json.dumps(data, indent=2))