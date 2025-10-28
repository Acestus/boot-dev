def decayed_followers(intl_followers, fraction_lost_daily, days):
    print(f"Initial international followers: {intl_followers}")
    return intl_followers * ((1 - fraction_lost_daily) ** days)


decayed_followers(200, 0.5, 1)