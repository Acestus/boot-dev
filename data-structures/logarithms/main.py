import math


def get_influencer_score(num_followers, average_engagement_percentage):
    print(f"Logarithm base 2 of 16 is: {math.log(16, 2)}")
    print(f"Number of followers: {num_followers}")
    print(f"Average engagement percentage: {average_engagement_percentage}")
    influencer_score = math.log2(num_followers) * average_engagement_percentage
    print(f"Influencer score (before rounding): {influencer_score}")
    return influencer_score

get_influencer_score(40000, 0.3)