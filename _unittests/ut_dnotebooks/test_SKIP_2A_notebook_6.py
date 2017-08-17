"""
@brief      test log(time=15s)
"""

import sys
import os
import unittest


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

try:
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import pyquickhelper as skip_

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, add_missing_development_version


class TestNotebookRunner2a_6 (unittest.TestCase):

    def setUp(self):
        fLOG("add missing dependencing")
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails"],
                                        __file__, hide=True)

    def test_notebook_runner(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks
        temp = get_temp_folder(__file__, "temp_notebook2a_6")
        keepnote = ls_notebooks("td2a")
        execute_notebooks(temp, keepnote, lambda i, n: "_6" in n,
                          fLOG=fLOG, dump=src.ensae_teaching_cs)


if __name__ == "__main__":
    unittest.main()
