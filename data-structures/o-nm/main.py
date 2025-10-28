def get_avg_brand_followers(all_handles, brand_name):
    print(f"Calculating average followers for brand: {brand_name}")
    total_followers = 0
    brand_count = 0
    for handles in all_handles:
        brand_count += 1
        for handle in handles:
            if brand_name in handle:
                total_followers += 1
    return total_followers / brand_count if brand_count > 0 else 0


get_avg_brand_followers([
    ["cosmofan1010", "cosmogirl", "billjane321"],
    ["cosmokiller", "gr8", "cosmojane3"],
    ["iloveboots", "paperthin"]
], "cosmo")
