# Code 2: Safe Data Access
ai_model = {
    "model_name": "ChatGPT",
    "version": 4.0,
    "developer": "OpenAI"
}

# Tarika 1 (Risk wala):
print(ai_model["version"])

# Tarika 2 (Safe - Agar key na mile to error nahi aayega)
print(ai_model.get("release_date"))  # Ye "None" print karega

# Task: 'release_date' dictionary mein add karein aur fir check karein.