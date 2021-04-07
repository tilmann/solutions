import os

import pandas as pd


def average_tam(*scenarios):

    TAM_PATH = os.path.join("integration", "transport", "tam" + "/")
    df = pd.DataFrame()

    for scenario in scenarios:
        csv_df = pd.read_csv(filepath_or_buffer=TAM_PATH +
                             scenario + ".csv", index_col=0)
        csv_df.rename(columns={"World": "World - " + scenario}, inplace=True)

        df = pd.concat([df, csv_df.iloc[:, 0:1]], axis=1)

    df["Average of Baseline TAMs"] = df.mean(axis=1)
    # print(df)
    # tam_ETP_2016_URBAN_2_DS_Nonmotorized_Travel_Adjustment.csv
    # tam_ETP_2016_URBAN_4_DS_Nonmotorized_Travel_Adjustment.csv
    # tam_ETP_2016_URBAN_6_DS_Nonmotorized_Travel_Adjustment.csv
    # tam_ICCT_2012_Global_Transportation_Roadmap_Model_Nonmotorized_Travel_Adjustment.csv
    return(df["Average of Baseline TAMs"])


average_tam("tam_ETP_2016_URBAN_6_DS_Nonmotorized_Travel_Adjustment",
            "tam_ICCT_2012_Global_Transportation_Roadmap_Model_Nonmotorized_Travel_Adjustment")
