import sys

sys.path.append('..')

import numpy as np
import pandas as pd
import transport

# initial: scenario_PDS1 = ['PDS1-7p2050-Using ICCT/RMI', 'PDS1-58p2050-Avg EEOI', 'PDS1-5p2050-with UIC Electrification Rate']  
scenario_PDS1 = ['PDS1-6p2050-using ICCT/RMI', 'PDS1-57p2050-Avg_EEOI', 'PDS1-5p2050-with UIC Electrification Rate']  

# initial: scenario_PDS2 = ['PDS2-8p2050-Using ICCT Regional Data', 'PDS2-78p2050-1 St Dev bel. Mean EEOI', 'PDS2-8p2050-with IEA 2DS']  
scenario_PDS2 = ['PDS2-7p2050_based on ICCT', 'PDS2-78p2050-1StDev_below_Mean_EEOI', 'PDS2-8p2050-with IEA 2DS']  

# initial: scenario_PDS3 = ['PDS3-8p2050-Using IEA (Maximum)', 'PDS3-98p2050-Lowest EEOi', 'PDS3-11p2050-Complete Electrification']  
scenario_PDS3 = ['PDS3-7p2050_based on IEA (Maximum)', 'PDS3-97p2050-Lowest_EEOI', 'PDS3-9p2050-Complete Electrification']  


test_scenarios = [scenario_PDS1, scenario_PDS2, scenario_PDS3]
test_dfs = transport.freight_adoption(test_scenarios[0])

expected_df = pd.read_csv('expected_freight_adoption.csv', header=None, sep=';')
# expected_df = pd.read_excel('expected_freight.xlsx', header=None)

def test_dataframe(tested, expected):
    tested = tested.reset_index(drop=True).T.reset_index(drop=True)
    expected = expected.reset_index(drop=True).T.reset_index(drop=True).astype(float)
    # test_df = tested.T.reset_index(drop=True).T.astype(float)
    # expected_df = expected #.T.reset_index(drop=True).T.astype(float)
    # # exp_ref2_tam.index = expected_df.iloc[28:75, 0].astype(int).values
    # test_ref2_tam = test_dfs.ref2_tam.T.reset_index(drop=True).T
    result = pd.testing.assert_frame_equal(tested, expected, check_exact=False)
    if result is None:
        print("Test: Success!!! ✅")
    else:
        print("Test: Failure ⚠️")

t1 = test_dataframe(test_dfs.iloc[:, 0:2], expected_df.iloc[0:49, 0:2])
print(t1)

# def test_final_co2_reduction()
#     # Test the final CO2 reduction output
#     exp_emissions_avoided = expected_df.iloc[[4, 7, 11], [13, 14]].reset_index(drop=True).T.reset_index(drop=True).T.astype(float)
#     test_emissions_avoided = pd.DataFrame([[test_dfs.emissions_avoided_lldc_period, test_dfs.emissions_avoided_lldc_full],
#                                         [test_dfs.emissions_avoided_mdc_period, test_dfs.emissions_avoided_mdc_full],
#                                         [test_dfs.emissions_avoided_total_period, test_dfs.emissions_avoided_total_full]])
#     pd.testing.assert_frame_equal(test_emissions_avoided, exp_emissions_avoided, check_exact=False, rtol=1e-2)

#     print("Test complete: clean cookstoves cluster")

# test_clean_cookstoves()
