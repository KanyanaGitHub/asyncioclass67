import aiofiles
import asyncio
import json
from pathlib import Path

pokemonapi_directory = './assignment07/pokemon/pokemonapi'
pokemonmove_directory = './assignment07/pokemon/pokemonmove'

async def seach(path_file):
    # read the contents of the json file.
    async with aiofiles.open(path_file, mode='r') as f:
        contents = await f.read()

    # Load it into a dictionary and create a list of move.
    pokemon = json.loads(contents)
    name = pokemon['name']
    moves = [move['move']['name'] for move in pokemon['moves']]
    
    # open a new file to wirte the list of moves into.
    async with aiofiles.open(f'{pokemonmove_directory}/{name}_move.txt', mode='w') as f :
        await f.write('\n'.join(moves))

async def main():
    pathlist = Path(pokemonapi_directory).glob('*.json')

    # Iterate through all json files in the directory.
    # for path in pathlist:
    #     print(path)
    tasks = [asyncio.create_task(seach(Path)) for Path in pathlist]
    await asyncio.gather(*tasks)

asyncio.run(main())