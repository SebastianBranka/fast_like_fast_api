from pydantic import BaseModel, Field

class Creature(BaseModel):
    name: str = Field(..., min_length=2)
    country: str
    area: str
    description: str
    aka: str

thing = Creature(
    name="Yeti",
    country="CN",
    area="Himalayas",
    description="Hirsute Himalayan",
    aka="Abominable Snowman"
)

print("Nazwa to", thing.name)