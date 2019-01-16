from abc import ABCMeta, abstractmethod
from datetime import datetime as dt, date
import logging
from typing import Optional, Union

from hyo2.soundspeed.base.geodesy import Geodesy
from hyo2.soundspeed.profile.profilelist import ProfileList

logger = logging.getLogger(__name__)


class AbstractAtlas(metaclass=ABCMeta):
    """Common abstract atlas"""

    def __init__(self, data_folder: str, prj: 'hyo2.soundspeed.soundspeed import SoundSpeedLibrary') -> None:
        self.name = self.__class__.__name__
        self.desc = "Abstract atlas"  # a human-readable description
        self.data_folder = data_folder
        self.prj = prj
        self.g = Geodesy()

    @abstractmethod
    def is_present(self) -> bool:
        pass

    @abstractmethod
    def query(self, lat: Optional[float], lon: Optional[float], datestamp: Union[date, dt, None],
              server_mode: bool = False) -> Optional[ProfileList]:
        pass

    @abstractmethod
    def download_db(self) -> bool:
        pass

    def __repr__(self) -> str:
        msg = "  <%s>\n" % self.__class__.__name__
        msg += "      <desc: %s>\n" % self.desc
        return msg
