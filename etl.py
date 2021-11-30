import asyncio
import aiohttp

async def main():

    hostserver = "https://statsapi.web.nhl.com"
    seasons = [20182019,20192020,20202021]
    async with aiohttp.ClientSession() as session:
        for season in seasons:
            url = f'{hostserver}/api/v1/schedule?season={season}'
            async with session.get(url) as resp:
                data = await resp.json()
                for date in data['dates']:
                    games = [game for game in date['games'] if game['gameType'] == "A"]
                    if len(games) > 0:
                        games = [games[-1]]
                        break
                    

                games.append(data['dates'][-1]["games"][-1])
                print(games)
                # print(games)
                for game in games:
                    if game['gameType'] == "A": # No Team Data
                        print("All-Star Game")
                    else:
                        print("Playoffs Final")
                    print(game["gameDate"])
                    teams = []
                    for k,val in game['teams'].items():
                        teams.append(val['team']['id'])
                    # async with session.get() as teamresp:
                        # print(teams)

                        print(str(k) + "   " +str(val['team']['name'] + "  id   " + str(val['team']['id'])))
                # print(teams)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())