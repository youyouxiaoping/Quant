def run_formula(dv):
    factor4 = dv.add_formula('factor4',"-Correlation(Delta(Log(volume),1),(close-open)/open,6)+(-1 * Ts_Max(Corr(Ts_Rank(volume, 5), Ts_Rank(high, 5), 5), 3))",is_quarterly=False, add_data=True)
    return factor4
