from pydantic import BaseModel

class Tokens(BaseModel):
    """
    Schema representing tokens
    """
    access_token: str
    refresh_token: str
    token_type: str