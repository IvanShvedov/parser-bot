from tkinter.messagebox import NO
from models.base import Base


class ChannelDTO(Base):
    id: str = None
    channel: str = None