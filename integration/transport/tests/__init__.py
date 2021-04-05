import unittest

import numpy as np
import pandas as pd
from integration.transport import transport


def test_dataframe(tested, expected):

    tested = tested.reset_index(drop=True).T.reset_index(drop=True)
    expected = expected.reset_index(
            drop=True).T.reset_index(drop=True).astype(float)
    pd.testing.assert_frame_equal(
        tested, expected, check_exact=False, rtol=1e-2)


class TestTransport(unittest.TestCase):

    def test_transport_urban_pass(self):
        expected_df = pd.read_csv(
                'integration/transport/tests/expected_nonurban_pass_pds3.csv', header=None)

        test_pds1_df = transport.nonurban_pass_adoption('pds1')
        self.assertIsInstance(test_pds1_df, pd.DataFrame)
        print('⚠️ Only asserts that it return a valid dataframe')
        # self.assertIsNone(test_dataframe(
        #         test_pds1_df.iloc[:, 0:13], expected_df.iloc[0:49, 0:13]))

        test_pds2_df = transport.nonurban_pass_adoption('pds2')
        self.assertIsInstance(test_pds2_df, pd.DataFrame)
        print('⚠️ Only asserts that it return a valid dataframe')
        # TODO assert the test_dataframe for pds2
        # currently the df is exported for the
        # self.assertIsNone(test_dataframe(
        #        test_pds1_df.iloc[:, 0:13], expected_df.iloc[49:98, 0:13]))

        test_pds3_df = transport.nonurban_pass_adoption('pds3')
        self.assertIsInstance(test_pds3_df, pd.DataFrame)

        # Test the percentages and data from scenario
        self.assertIsNone(test_dataframe(
                   test_pds3_df.iloc[0:49, 3:13], expected_df.iloc[0:49, 3:13]))

        # Test the calculations for the first three columnos
        self.assertIsNone(test_dataframe(
                  test_pds3_df.iloc[3:49, 0:3], expected_df.iloc[3:49, 0:3]))

    def test_transport_freight_adoption(self):
        expected_df = pd.read_csv(
                'integration/transport/tests/expected_freight_adoption.csv', header=None)

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
