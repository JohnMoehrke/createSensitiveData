# Given the ValueSet-SlsSensitiveSDV.json as input of sensitive code values, create N FHIR Observation resources with a random sensitive code value, category of exam, a random date between 2000-01-01 and 2020-12-31, patient reference to Patient/1, and a valueString of "sensitive".
# The output is a FHIR Bundle with N Observation resources.
# Usage: python createData.py N
# N is the number of Observation resources to create.

import json
import random
import sys
from datetime import datetime, timedelta

# Load the sensitive code values from ValueSet-SlsSensitiveSDV.json
with open('ValueSet-SlsSensitiveSDV.json') as f:
    data = json.load(f)
    sensitiveCodes = data['expansion']['contains']

# Create N Observation resources
N = int(sys.argv[1])
bundle = {
    "resourceType": "Bundle",
    "type": "transaction",
    "entry": []
}
for i in range(N):

    # Randomly select a sensitive code value
    code = random.choice(sensitiveCodes)['code']

    # Randomly select a date between 2000-01-01 and 2020-12-31
    date = datetime(2000, 1, 1) + timedelta(days=random.randint(0, 7670))

    # Create an Observation resource
    observation = {
        "resource": {
            "resourceType": "Observation",
            "status": "final",
            "category": [{
                "coding": [{
                    "system": "http://terminology.hl7.org/CodeSystem/observation-category",
                    "code": "exam"
                }]  
            }],
            "code": {
                "coding": [{
                    "system": "http://loinc.org",
                    "code": code
                }]
            },
            "subject": {
                "reference": "Patient/1"
            },
            "effectiveDateTime": date.strftime('%Y-%m-%dT%H:%M:%S'),
            "valueString": "sensitive"
        },
        "request": {
            "method": "POST",
            "url": "Observation"
        }
    }
    bundle['entry'].append(observation)

# Output the FHIR Bundle
print(json.dumps(bundle, indent=2))

