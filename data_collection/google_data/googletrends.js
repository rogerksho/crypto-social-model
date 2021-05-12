const googleTrends = require('google-trends-api');
var fs = require('fs');

const START_TIME = new Date('2016-01-01')
const END_TIME = new Date(Date.now())

var finalDataObject = [];

async function fetchGoogleTrends(searchTermIn, startTimeIn, endTimeIn) {
    let results = await googleTrends.interestOverTime({keyword: searchTermIn, startTime: startTimeIn, endTime: endTimeIn,})

    var jsonResults;

    try {
        jsonResults = JSON.parse(results)
    } catch (err) {
        console.error(results)
    }
    
    //console.log(jsonResults['default']['timelineData'])
    finalDataObject = [...finalDataObject, jsonResults['default']['timelineData']]
}

// search params
let searchTerm = "bitcoin"
var currentStartTime = new Date(START_TIME)

var currentEndTime = new Date(START_TIME)
currentEndTime.setMonth(currentStartTime.getMonth() + 3)

// while
async function driverFunc() {
    while(currentEndTime < END_TIME) {
        console.log(`start: `, currentStartTime)
        console.log(`end: `, currentEndTime)
        
        await fetchGoogleTrends(searchTerm, currentStartTime, currentEndTime)
        .catch((e) => console.error(e))
    
        currentStartTime = new Date(currentEndTime.valueOf())
        currentStartTime.setMonth(currentStartTime.getMonth(), currentStartTime.getDay() + 1)
        currentEndTime.setMonth(currentStartTime.getMonth() + 6)
    }
}

async function printFile() {
    console.log(finalDataObject)
    let jsonString = JSON.stringify({...finalDataObject}, null, '\t')
    
    fs.writeFile("googletrends.json", jsonString, function(err) {
        if (err) {
            console.log(err);
        }
    });
}

driverFunc()
.then(printFile)
.catch(err => console.error(err))
