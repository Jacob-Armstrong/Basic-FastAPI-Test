from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

class Game(BaseModel):
    title: str
    description: str
    rating: float

bg3 = Game(
    title="Baldur's Gate 3", 
    description=("Baldur’s Gate 3 is a story-rich, party-based RPG set in the universe of Dungeons & Dragons, " 
                 "where your choices shape a tale of fellowship and betrayal, survival and sacrifice, and the lure of absolute power."),
    rating=4.8
)

starfield = Game(
    title="Starfield",
    description="Starfield is the first new universe in 25 years from Bethesda Game Studios, the award-winning creators of The Elder Scrolls V: Skyrim and Fallout 4.",
    rating=2.9
)

terraria = Game(
    title="Terraria",
    description="Dig, fight, explore, build! Nothing is impossible in this action-packed adventure game. Four Pack also available!",
    rating=4.85
)

skyrim = Game(
    title="The Elder Scrolls V: Skyrim",
    description="The next chapter in the highly anticipated Elder Scrolls saga arrives from the makers of the 2006 and 2008 Games of the Year, Bethesda Game Studios.",
    rating=4.7
)

gameList = [bg3, starfield, terraria, skyrim]

@router.get("/games", response_model=list[Game])
def get_games():
    return gameList

@router.get("/games/{title}", response_model=Game)
def get_game(title: str):

    game = next((game for game in gameList if game.title == title), None)

    if game is None:
        raise HTTPException(status_code=404, detail=f"{title} could not be found.")
    
    return game

@router.post("/games")
def post_game(game: Game):
    gameList.append(game)
    return gameList

@router.delete("/games/{title}")
def delete_Game(title: str):
    for game in gameList:
        if game.title == title:
            gameList.remove(game)
            return gameList
    raise HTTPException(status_code=404, detail=f"{title} does not exist or has already been deleted.")