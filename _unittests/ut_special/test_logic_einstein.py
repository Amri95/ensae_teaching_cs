"""
@brief      test log(time=3s)
"""
import os
import sys
import unittest
from pyquickhelper.loghelper import fLOG

try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

from src.ensae_teaching_cs.special.einstein_prolog import Enigma


class TestSpecialLogic(unittest.TestCase):

    def test_einstein_prolog(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        en = Enigma()
        en.solve(logf=fLOG)
        sol = str(en)
        assert "jaune     , norvegien , eau       , Dunhill   , chats" in sol


if __name__ == "__main__":
    unittest.main()
