class DataCollectorAgent:
    def __init__(self):
        print("✅ DataCollectorAgent initialized")

    def collect(self):
        print("📥 Collecting sample data...")
        return {
  "user_feedback": [
    "The app is slow sometimes.",
    "I love the new dashboard!",
    "Too many notifications."
  ]
}