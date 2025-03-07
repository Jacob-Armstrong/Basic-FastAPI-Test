from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from ..routers.games import Game, bg3, starfield, terraria, skyrim

router = APIRouter()

class Publisher(BaseModel):
    title: str
    description: str
    games: list[Game]

bethesda = Publisher(
    title="Bethesda Game Studios",
    description=("Bethesda Game Studios is an American video game developer and a studio of ZeniMax Media based in Rockville, Maryland. It is best known for its action role-playing franchises, "
                 "including The Elder Scrolls, Fallout, and Starfield."),
    games=[starfield, skyrim]
)

larian = Publisher(
    title="Larian Studios",
    description="Larian Studios is a Belgian independent video game developer and publisher founded in 1996 by Swen Vincke. It is best known for developing the Divinity series and Baldur's Gate 3.",
    games=[bg3]
)

relogic = Publisher(
    title="Re-Logic",
    description=("Re-Logic is an American independent game developer and publisher based in Indiana in the USA. It was founded by Andrew Spinks in 2011. The company is best known for developing and publishing Terraria, "
                 "a 2D action-adventure sandbox video game."),
    games=[terraria]
)

publisherList = [bethesda, larian, relogic]

@router.get("/publishers", response_model=list[Publisher])
def get_publishers():
    return publisherList

@router.get("/publishers/{title}", response_model=Publisher)
def get_publisher(title: str):
    publisher = next(publisher for publisher in publisherList if publisher.title == title)

    if publisher is None:
        raise HTTPException(status_code=404, detail=f"{title} was not in the list of publishers.")
    else:
        return publisher