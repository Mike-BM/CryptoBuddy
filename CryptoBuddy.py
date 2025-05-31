
# crypto_chatbot.py

# Sample crypto dataset
crypto_db = {
    "Bitcoin": {
        "price_trend": "rising",
        "market_cap": "high",
        "energy_use": "high",
        "sustainability_score": 3 / 10
    },
    "Ethereum": {
        "price_trend": "stable",
        "market_cap": "high",
        "energy_use": "medium",
        "sustainability_score": 6 / 10
    },
    "Cardano": {
        "price_trend": "rising",
        "market_cap": "medium",
        "energy_use": "low",
        "sustainability_score": 8 / 10
    }
}

# Step 1: Personality
def welcome():
    print("👋 Hello! I'm CryptoBuddy — your friendly AI crypto sidekick!")
    print("💡 Ask me questions like:")
    print("   - Which crypto is trending up?")
    print("   - What’s the most sustainable coin?")
    print("   - Which coin should I buy for long-term growth?")
    print("   - Which coin uses the least energy?")
    print("   - Is Bitcoin a good investment?")
    print("🔚 Type 'exit' to leave anytime.\n")

# Step 2–4: Logic based on simple if-else rules
def respond_to_query(query):
    query = query.lower()

    if "sustainable" in query:
        recommend = max(crypto_db, key=lambda x: crypto_db[x]["sustainability_score"])
        print(f"CryptoBuddy: 🌱 Invest in {recommend}! It’s eco-friendly and has long-term potential!")

    elif "energy" in query:
        lowest_energy = min(crypto_db, key=lambda x: crypto_db[x]["energy_use"])
        print(f"CryptoBuddy: ⚡ {lowest_energy} uses the least energy — great for green investing!")

    elif "trending" in query or "rising" in query:
        trending = [coin for coin, data in crypto_db.items() if data["price_trend"] == "rising"]
        print(f"CryptoBuddy: 🚀 These are trending up: {', '.join(trending)}")

    elif "long-term" in query or "buy" in query or "best" in query:
        for coin, data in crypto_db.items():
            if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                print(f"CryptoBuddy: 📈 {coin} is trending up and has a top-tier sustainability score! 🚀")
                return
        print("CryptoBuddy: 🤔 No perfect long-term picks at the moment. Check back soon!")

    elif "market cap" in query:
        high_caps = [coin for coin, data in crypto_db.items() if data["market_cap"] == "high"]
        print(f"CryptoBuddy: 💰 Coins with high market cap: {', '.join(high_caps)}")

    elif "bitcoin" in query:
        coin = "Bitcoin"
        data = crypto_db[coin]
        advice = "not very sustainable but still popular" if data["sustainability_score"] < 0.5 else "a decent option for now"
        print(f"CryptoBuddy: 🤔 {coin} is currently {data['price_trend']} with a high market cap, but it's {advice}. DYOR!")

    elif "exit" in query:
        print("CryptoBuddy: 👋 Thanks for chatting! Remember, crypto is risky—always do your own research!")
        return False

    else:
        print("CryptoBuddy: 🤖 I didn’t understand that. Try asking about trends or sustainability.")

    return True

# Step 5: Run chatbot
def run_chatbot():
    welcome()
    active = True
    while active:
        user_query = input("You: ")
        active = respond_to_query(user_query)

if __name__ == "__main__":
    run_chatbot()


