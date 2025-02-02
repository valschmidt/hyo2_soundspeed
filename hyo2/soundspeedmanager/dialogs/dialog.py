import os

from PySide2 import QtCore, QtGui, QtWidgets

import logging

logger = logging.getLogger(__name__)

from hyo2.abc.app.qt_progress import QtProgress
from hyo2.soundspeed.soundspeed import SoundSpeedLibrary


class AbstractDialog(QtWidgets.QDialog):
    here = os.path.abspath(os.path.join(os.path.dirname(__file__)))  # to be overloaded
    media = os.path.abspath(os.path.join(here, os.pardir, "media"))

    def __init__(self, main_win, lib, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        if not isinstance(lib, SoundSpeedLibrary):
            raise RuntimeError("Passed invalid project object: %s" % type(lib))
        self.main_win = main_win
        self.lib = lib

        self.setWindowFlags(self.windowFlags() & ~QtCore.Qt.WindowContextHelpButtonHint)

        # progress dialog
        self.progress = QtProgress(parent=self)
