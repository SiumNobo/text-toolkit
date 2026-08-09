from pydantic import BaseModel, field_validator


class ChunkConfig(BaseModel):
    size: int
    overlap: int

    @field_validator("overlap")
    @classmethod
    def overlap_must_be_smaller(cls, overlap: int, info):
        size = info.data.get("size")
        if size is not None and overlap >= size:
            raise ValueError("overlap must be smaller than size")
        return overlap