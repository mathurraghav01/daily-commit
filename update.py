import requests
from datetime import datetime

# get current date and time
now = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S UTC")

# Get random motivational quote
quote_resp = requests.get("https://api.quotable.io/random")
quote_data = quote_resp.json()
quote = f"💬 *{quote_data['content']}* — {quote_data['author']}"

# Get fun fact
fact_resp = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
fact_data = fact_resp.json()
fact = f"🎯 {fact_data['text']}"

# Prepare README content
readme_content = f"""
# 🌞 Daily Updates

📅 **Date:** {now}  
{quote}  
{fact}  

---
*Updated automatically every day using GitHub Actions.*
"""

# Write to README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)
