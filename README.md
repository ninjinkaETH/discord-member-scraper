# discord-member-count
Scrapes Discord servers for their member counts just using invites.

## Scraping OpenSea

To scrape OpenSea for Discord links and other useful information, do:

`go run opensea/main.go`

## Scraping Twitter

To scrape Twitter every 5 minutes for Discord links, run `twitter/twitter.py`. You will also need a file in the `twitter` directory named `twitter_api.txt` that contains your Twitter API bearer token.

## Scraping Discord

To run the scraping file, make a CSV named `serverlinks.csv` of format:

`server_name,server_invite_link,notes`

You can omit the name and notes as long as you keep the commas:

```
Bankless DAO,https://discord.gg/pqQhCb6kRE,
,https://discord.gg/pqQhCb6kRE,
Bankless DAO,https://discord.gg/pqQhCb6kRE,uses the BANK token
```
Then run:

`go run main.go`

This will scrape the servers you have in `serverlinks.csv` and write the results to a file called `servers.jl` (a JSONLines file).

## Analytics

This part has just begun development, but if you want to plot out the results of the scrape you can run `analytics.py` and it will plot out the results of the scrapes, like below: 

![Bankless DAO results](https://i.imgur.com/9oTpPLF.png)
