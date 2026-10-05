from pydantic import BaseModel, ConfigDict, Field


class CityBase(BaseModel):
    name: str = Field(min_length=1, max_length=100)
    additional_info: str | None = Field(default=None, max_length=500)


class CityCreate(CityBase):
    pass


class CityUpdate(CityBase):
    name: str | None = Field(default=None, min_length=1, max_length=100)
    additional_info: str | None = Field(default=None, max_length=500)


class City(CityBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
