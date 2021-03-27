import unittest

import numpy as np
import pandas as pd
from integration.transport import transport


def test_dataframe(tested, expected):
    tested = tested.reset_index(drop=True).T.reset_index(drop=True)
    expected = expected.reset_index(
            drop=True).T.reset_index(drop=True).astype(float)
    # test_df = tested.T.reset_index(drop=True).T.astype(float)
    # expected_df = expected #.T.reset_index(drop=True).T.astype(float)
    # # exp_ref2_tam.index = expected_df.iloc[28:75, 0].astype(int).values
    # test_ref2_tam = test_dfs.ref2_tam.T.reset_index(drop=True).T
    pd.testing.assert_frame_equal(tested, expected, check_exact=False)


class TestTransport(unittest.TestCase):

    def test_transport(self):
        expected_df = pd.read_csv(
                'integration/transport/tests/expected_freight_adoption.csv', header=None, sep=';')

        test_pds1_df = transport.freight_adoption('pds1')
        test_pds2_df = transport.freight_adoption('pds2')
        test_pds3_df = transport.freight_adoption('pds3')

        self.assertIsNone(test_dataframe(
            test_pds1_df.iloc[:, 0:2], expected_df.iloc[0:49, 0:2]))

        self.assertIsNone(test_dataframe(
                test_pds2_df.iloc[:, 0:2], expected_df.iloc[49:98, 0:2]))

        self.assertIsNone(test_dataframe(
                    test_pds3_df.iloc[:, 0:2], expected_df.iloc[98:147, 0:2]))


if __name__ == "__main__":
    unittest.main()


# def test_final_co2_reduction()
#     # Test the final CO2 reduction output
#     exp_emissions_avoided = expected_df.iloc[[4, 7, 11], [13, 14]].reset_index(drop=True).T.reset_index(drop=True).T.astype(float)
#     test_emissions_avoided = pd.DataFrame([[test_dfs.emissions_avoided_lldc_period, test_dfs.emissions_avoided_lldc_full],
#                                         [test_dfs.emissions_avoided_mdc_period, test_dfs.emissions_avoided_mdc_full],
#                                         [test_dfs.emissions_avoided_total_period, test_dfs.emissions_avoided_total_full]])
#     pd.testing.assert_frame_equal(test_emissions_avoided, exp_emissions_avoided, check_exact=False, rtol=1e-2)

#     print("Test complete: clean cookstoves cluster")

# test_clean_cookstoves()
