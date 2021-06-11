from urllib.request import urlopen
import re
import pickle
from rawData.localData import data as localData

# Initialize variables
completeList = []
i = 1

# Loop through 5 pages of website [www.behindthename.com]
while i <= 5:
    # Data request actions
    if i == 1:
        url = "https://www.behindthename.com/submit/names/usage/nigerian".format(i)
    else:
        url = "https://www.behindthename.com/submit/names/usage/nigerian/" + str(i)
    page = urlopen(url)
    html = page.read().decode("utf-8")

    # Regex actions
    pattern = "\"nll\">.*?</a>"
    match_results = re.findall(pattern, html, re.IGNORECASE)
    for index, item in enumerate(match_results):
        temp = item.replace("\"nll\">", "").replace("</a>", "") # Remove HTML tags
        match_results[index] = temp[0].lower() + temp[1:] # decapitalize first letter
    completeList = [*completeList, *match_results]
    print(i)
    i += 1
completeList = [*completeList, *localData]


#Store data in picle
with open('rawData/completePickleData.pkl', 'wb') as f:
  pickle.dump(completeList, f)





