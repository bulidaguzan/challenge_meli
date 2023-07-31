from pydantic import BaseModel


# ---- Requests Models ----
class RequestIndex(BaseModel):
    tool: str
    body: str


class RequestId(RequestIndex):
    id: int
