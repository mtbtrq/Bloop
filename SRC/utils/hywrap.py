import aiohttp

# Returns the entire API page of a given user
async def player(uuid : str = None, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    if uuid is None:
        print("Please specify a UUID!")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}') as profileRaw:
                player = await profileRaw.json()
                return player

# Returns the bedwars stats of a given user
async def bedwars(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    if uuid is None:
        print("Please specify a UUID!")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}') as bedwarsRaw:
                rawBW = await bedwarsRaw.json()
                bedwarsStats = rawBW["player"]["stats"]["Bedwars"]
                return bedwarsStats

# Returns the skywars stats of a given user
async def skywars(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    if uuid is None:
        print("Please specify a UUID!")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}') as skywarsRaw:
                rawSW = await skywarsRaw.json()
                skywarsStats = rawSW["player"]["stats"]["SkyWars"]
                return skywarsStats

# Returns the duel stats of a given user
async def duels(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    if uuid is None:
        print("Please specify a UUID!")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}') as duelsRaw:
                rawDuels = await duelsRaw.json()
                duelsStats = rawDuels["player"]["stats"]["Duels"]
                return duelsStats

# Returns the arcade stats of a given user
async def arcade(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    if uuid is None:
        print("Please specify a UUID!")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}') as arcadeRaw:
                rawArcade = await arcadeRaw.json()
                arcadeStats = rawArcade["player"]["stats"]["Arcade"]
                return arcadeStats

# Returns the build battle stats of a given user
async def buildBattle(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    if uuid is None:
        print("Please specify a UUID!")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}') as buildRaw:
                rawBuild = await buildRaw.json()
                buildBattleStats = rawBuild["player"]["stats"]["BuildBattle"]
                return buildBattleStats

# Returns the pit stats of a given user
async def pit(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    if uuid is None:
        print("Please specify a UUID!")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}') as pitRaw:
                rawPit = await pitRaw.json()
                pitStats = rawPit["player"]["stats"]["Pit"]
                return pitStats

# Returns Skyblock stats
async def skyblock(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    if uuid is None:
        print("Please specify a UUID!")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.hypixel.net/player?key={hypixelapikey}&uuid={uuid}') as sbraw:
                rawSB = await sbraw.json()
                skyblockStats = rawSB["player"]["stats"]["SkyBlock"]
                return skyblockStats

# Returns the booster information on the Hypixel Network
async def boosters(hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.hypixel.net/boosters?key={hypixelapikey}') as boosterRaw:
                rawBoosters = await boosterRaw.json()
                return rawBoosters

# Returns the player count across the Hypixel Network
async def playerCount(hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.hypixel.net/counts?key={hypixelapikey}') as playerCountRaw:
                count = await playerCountRaw.json()
                return count

# Returns the leaderboards across the Hypixel Network
async def leaderboards(hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.hypixel.net/leaderboards?key={hypixelapikey}') as leaderboardsRaw:
                leaderBoards = await leaderboardsRaw.json()
                return leaderBoards

# Returns the watchdog stats on the Hypixel Network
async def watchdogStats(hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.hypixel.net/punishmentstats?key={hypixelapikey}') as watchdogRaw:
                watchdog = await watchdogRaw.json()
                return watchdog

# Returns the entire Hypixel Guild API Page for a given user
async def guild(uuid : str, hypixelapikey : str = None):
    if hypixelapikey is None:
        print("Please Enter a Hypixel API Key!")
    if uuid is None:
        print("Please specify a UUID!")
    else:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(f'https://api.hypixel.net/guild?key={hypixelapikey}&player={uuid}') as guildRaw:
                guild = await guildRaw.json()
                return guild