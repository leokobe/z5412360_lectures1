from event_study import download, mk_rets, mk_events, mk_cars, test_hypo

def main(tic, update_csv=True):
    # Step 1: Download stock price and recommendation data for `tic`
    if update_csv is True:
        download.get_data(tic)
    else:
        print("Parameter `update_csv` set to False, skipping downloads...")

    # Step 2: Create a data frame with stock (tic) and market returns
    ret_df = mk_rets.mk_ret_df(tic)

    # Step 3: Create a data frame with the events
    event_df = mk_events.mk_event_df(tic)

    # Step 4: Calculate CARs for each event
    cars_df = mk_cars.mk_cars_df(ret_df, event_df)

    # Step 5: Hypothesis testing using t-statistics
    res = test_hypo.calc_tstats(cars_df)
    print(res)

if __name__ == "__main__":
    tic = 'TSLA'
    update_csv = False
    main(tic=tic, update_csv=update_csv)