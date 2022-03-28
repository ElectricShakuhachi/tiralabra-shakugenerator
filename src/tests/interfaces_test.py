import unittest
import dotenv
import os
from interfaces.interfaces import NonInteractive

class TestNonInteractive(unittest.TestCase):
    def setUp(self):
        self.interface = NonInteractive()
        dirname = os.path.dirname(__file__)
        dotenv.load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))

    def test_run_generates_correct_lenght_of_music(self):
        """This test provides proof that the application
        produces the requested amount of measures, with a
        possible extranneous marigin of the extra duration 
        of the last note"""
        for measure_count in [1, 3, 23, 121]:
            measure_lenght = int(os.getenv(("SHAKUGEN_MEASURE_LENGHT")))
            requested_lenght = measure_lenght * measure_count
            os.chdir("..")
            output = self.interface.run(measure_count)
            generated_lenght = sum(output["lenghts"])
            marigin = generated_lenght - requested_lenght
            self.assertGreaterEqual(marigin, 0)
            self.assertGreater(output["lenghts"][-1], marigin)
