medalResults = [
    {
        "sport": "cycling",
        "podium": ["1.China", "2.Germany", "3.ROC"]
    },
    {
        "sport": "fencing",
        "podium": ["1.ROC", "2.France", "3.Italy"]
    },
    {
        "sport": "high jump",
        "podium": ["1.Italy", "1.Qatar", "3.Belarus"]
    },
    {
        "sport": "swimming",
        "podium": ["1.USA", "2.France", "3.Brazil"]
    }
]

def createMedalTable(results):

    table = {}
    
    for event in results: #iterates over all the events
        for result in event['podium']: # looks at each podium result (sport doesn't matter)
            country = result[2:] #gets the name of the country
            if country in table:
                table[country] += 4 - int(result[0]) # adds 3points if result starts with 1., 2points if country starts with 2. etc...
            else:
                table[country] = 4 - int(result[0]) # adds country to table and its points for this event
   
    return table

createMedalTable(medalResults)

def test_function():
    #This it the test function, please don't change me
    medalTable = createMedalTable(medalResults)
    expectedTable = {
        "Italy": 4,
        "France": 4,
        "ROC": 4,
        "USA": 3,
        "Qatar": 3,
        "China": 3,
        "Germany": 2,
        "Brazil": 1,
        "Belarus": 1,
    }
    assert medalTable == expectedTable