# Create Data Python Script

This python script will create data given an expansion valueSet. To get the expansion in the ValueSet

- One method is to go to an IG that uses the ValueSet. The normal ValueSet in the IG will not have the expansions within it. BUT, there will be an expansions.json in the publication folder that is a Bundle of all of the ValueSets in the IG with expansion at the time of publication. Thus you just extract the ValueSet you need out, and use it.
  
This script is very simple, and uses a hardcoded patient "Patient/1"

> python createData.py 10 > out.json

Thus, given you have some normal test data, like from Synthia. Create an appropriate number of sensitive data with this script. Post both to your FHIR server.
