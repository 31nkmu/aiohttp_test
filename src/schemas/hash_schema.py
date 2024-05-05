from pydantic import BaseModel


class HashSchema(BaseModel):
    string: str
