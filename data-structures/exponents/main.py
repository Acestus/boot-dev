def get_estimated_spread(audiences_followers):
    if not audiences_followers:
        return 0
    average_followers = sum(audiences_followers) / len(audiences_followers)
    print(f"Average followers: {average_followers}")
    estimated_spread = average_followers * (len(audiences_followers) ** 1.2)
    print(f"Estimated spread (before rounding): {estimated_spread}")
    return estimated_spread