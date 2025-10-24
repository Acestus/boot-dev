def get_follower_prediction(follower_count, influencer_type, num_months):
    print(f"Initial follower count: {follower_count}")
    growth_rates = {
        "fitness": 4,
        "cosmetic": 3
    }
    growth_rate = growth_rates.get(influencer_type, 2)
    print(f"Growth rate for {influencer_type}: {growth_rate}")
    predicted_followers = follower_count * (growth_rate ** (num_months))
    print(f"Predicted followers after {num_months} months: {predicted_followers}")
    return predicted_followers

get_follower_prediction(10, "fitness", 2) 