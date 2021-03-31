import unittest

import numpy as np
import pandas as pd
from integration.transport import transport


def test_dataframe(tested, expected):
    tested = tested.reset_index(drop=True).T.reset_index(drop=True)
    expected = expected.reset_index(
            drop=True).T.reset_index(drop=True).astype(float)
    pd.testing.assert_frame_equal(tested, expected, check_exact=False)


class TestTransport(unittest.TestCase):

    def test_transport_urban_pass(self):
        # expected_df = pd.read_csv(
        #        'integration/transport/tests/expected_urban_pass.csv', header=None, sep=';')
        test_pds1_df = transport.nonurban_pass_adoption('pds1')

        self.assertIsInstance(test_pds1_df, pd.DataFrame)

        # self.assertIsNone(test_dataframe(
        #    test_pds1_df.iloc[:, 0:2], expected_df.iloc[0:49, 0:2]))

    def test_transport_freight_adoption(self):
        expected_df = pd.read_csv(
                'integration/transport/tests/expected_freight_adoption.csv', header=None, sep=';')

        test_pds1_df = transport.freight_adoption('pds1')
        self.assertIsNone(test_dataframe(
            test_pds1_df.iloc[:, 0:2], expected_df.iloc[0:49, 0:2]))

        test_pds2_df = transport.freight_adoption('pds2')
        self.assertIsNone(test_dataframe(
                test_pds2_df.iloc[:, 0:2], expected_df.iloc[49:98, 0:2]))

        test_pds3_df = transport.freight_adoption('pds3')
        self.assertIsNone(test_dataframe(
                    test_pds3_df.iloc[:, 0:2], expected_df.iloc[98:147, 0:2]))


if __name__ == "__main__":
    unittest.main()
