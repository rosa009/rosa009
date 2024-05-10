import random

def get_daily_motivation(name):
    quotes = [
        "Believe in yourself and all that you are. Know that there is something inside you that is greater than any obstacle.",
        "Do not wait to strike till the iron is hot; but make it hot by striking.",
        "The only way to do great work is to love what you do. If you haven't found it yet, keep looking. Don't settle.",
        "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful.",
        "The best time to plant a tree was 20 years ago. The second best time is now.",
        "Your limitation—it's only your imagination.",
        "Push yourself, because no one else is going to do it for you.",
        "Great things never come from comfort zones.",
        "Dream it. Wish it. Do it.",
        "Success doesn’t just find you. You have to go out and get it."
    ]
    
    # Randomly select a quote
    quote = random.choice(quotes)
    
    # Personalize the message
    personalized_message = f"Hello {name}, here's your motivational quote for today: \n\n{quote}"
    
    return personalized_message

# Example usage
name = "Roger"  # You can change this to any name you want
print(get_daily_motivation(name))
