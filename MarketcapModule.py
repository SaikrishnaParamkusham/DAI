class MarketCapEligibility():
    def __init__(self, input_dataframe):
        self.input_dataframe = input_dataframe

    def filter_marketcap(self, field_str, threshold_num):
        if field_str == "" and threshold_num == 0:
            return None
        df_eligible = self.input_dataframe[self.input_dataframe[field_str].astype(int) >= threshold_num]
        df_ineligible = self.input_dataframe[self.input_dataframe[field_str].astype(int) < threshold_num]
        return df_eligible, df_ineligible
