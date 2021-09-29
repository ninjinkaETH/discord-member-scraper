import requests
import csv
import datetime
import time

discordLinks = {}

print("Starting...")
starttime = time.time()
# Run every 5 minutes
while True:
    print("Making request...")
    # Read in previous Discord links
    with open("out/serverlinks_twitter.csv", "r") as file:
        reader = csv.reader(file)
        for row in reader:
            discordLinks[row[1]] = True

    # Read in API key
    file = open("twitter/twitter_api.txt", "r")

    # Get the time 5 minutes ago
    currentDatetime = datetime.datetime.now()
    fiveMinutesAgo = currentDatetime - datetime.timedelta(minutes=5)
    fiveMinutesAgoString = fiveMinutesAgo.strftime('%Y-%m-%dT%H:%M:%SZ')

    # Set up request
    url = "https://api.twitter.com/2/tweets/search/recent?query=url:\"https://discord.gg\" has:links -is:retweet&start_time=" + \
        fiveMinutesAgoString+"&max_results=100&tweet.fields=entities,text"
    payload = {}
    headers = {
        'Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAACfqTwEAAAAAMRcWwUWjCNwFCDgoyuchxzDrPhw%3DD3brCXkZuVrQpOXdBFjFLdFkB93q9CpFuzSf8VnOqULuIF3ZeW',
        'Cookie': 'guest_id=v1%3A163271135500119327; personalization_id="v1_rkGujUjhyZMXfGa5EmJ7Lw=="'
    }

    # Do request
    response = requests.request("GET", url, headers=headers, data=payload)
    responseJSON = response.json()

    # Read response and get Discord URLs
    for tweet in responseJSON["data"]:
        urls = tweet["entities"]["urls"]
        for url in urls:
            if "discord.gg" in url["expanded_url"]:
                discordLinks[url["expanded_url"]] = True

    # Write unique Discord URLs
    with open("out/serverlinks_twitter.csv", "w", newline='') as file:
        writer = csv.writer(file)
        for discordLink in discordLinks:
            writer.writerow(["", discordLink, ""])
    time.sleep(300.0 - ((time.time() - starttime) % 60.0))
