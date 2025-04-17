def determine_personality(scores):
    max_score = max(scores.values())
    top_traits = [k for k, v in scores.items() if v == max_score]

    if "A" in top_traits:
        return "The Adventurer - You love trying new things and taking risks."
    elif "B" in top_traits:
        return "The Thinker - You enjoy deep thoughts and analyzing situations."
    elif "C" in top_traits:
        return "The Helper - You are compassionate and love supporting others."
    elif "D" in top_traits:
        return "The Leader - You are confident, assertive, and like to take charge."
    else:
        return "A Balanced Personality - You have a mix of different traits."