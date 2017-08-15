#-*- coding: utf-8 -*-
"""
@brief      test log(time=23s)
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
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor, add_missing_development_version


class TestNotebookRunner2a_csharp (unittest.TestCase):

    def setUp(self):
        add_missing_development_version(["pymyinstall", "pyensae", "pymmails", "jyquickhelper"],
                                        __file__, hide=True)

    def test_notebook_runner_2a(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            # too long for appveyor
            # not available on linux
            return

        if not sys.platform.startswith("win"):
            return

        from src.ensae_teaching_cs.automation.notebook_test_helper import ls_notebooks, execute_notebooks, clean_function_1a
        temp = get_temp_folder(__file__, "temp_notebook2a_sharp")
        keepnote = ls_notebooks("2a")
        execute_notebooks(temp, keepnote, (lambda i, n: "csharp" in n),
                          clean_function=clean_function_1a,
                          fLOG=fLOG, dump=src.ensae_teaching_cs)

        #~ if len(fails) > 0:
        #~ e = str(fails[0][1][-1])
        #~ if "Audio device error encountered" in str(e):
        #~ # maybe the script is running on a virtual machine (no Audia
        #~ # device)
        #~ if os.environ["USERNAME"] == "ensaestudent" or \
        #~ os.environ["USERNAME"] == "vsxavierdupre" or \
        #~ "paris" in os.environ["COMPUTERNAME"].lower() or \
        #~ "2016" in os.environ["COMPUTERNAME"].lower() or \
        #~ os.environ["USERNAME"].endswith("$"):  # anonymous Jenkins configuration
        #~ # I would prefer to catch a proper exception
        #~ # it just exclude one user only used on remotre machines
        #~ fLOG("no audio")
        #~ return
        #~ elif "<class 'int'>-" in str(e):
        #~ # issue with conversion from 3 to double
        #~ return

        #~ fLOG(str(e).replace("\n", " EOL "))
        #~ raise Exception(
        #~ "*** {0} *** {1} ***".format(os.environ["COMPUTERNAME"], e)) from fails[0][1][-1]
        #~ else:
        #~ fLOG("success")


if __name__ == "__main__":
    unittest.main()
