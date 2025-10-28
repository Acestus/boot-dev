class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"


# dont touch above this line


def vanity(influencer):
    print(f"Calculating vanity for influencer: {influencer}")
    score = (influencer.num_selfies) + (influencer.num_bio_links * 5)
    print(f"Vanity score: {score}")
    return score


def vanity_sort(influencers):
    print(f"Sorting influencers: {influencers}")
    sorted_influencers = sorted(influencers, key=vanity)
    print(f"Sorted influencers: {sorted_influencers}")
    return sorted_influencers


vanity(Influencer(10, 5))  # should return (10, -5)

items = [1, 5, 3]
print(sorted(items)) # [1, 3, 5]

theprimeagen = Influencer(100, 1)
pokimane = Influencer(800, 2)
spambot = Influencer(0, 200)
lane = Influencer(10, 2)
badcop = Influencer(1, 2)
vanity_sort([badcop, lane, pokimane, theprimeagen, spambot])