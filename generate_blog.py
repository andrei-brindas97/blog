import os
import openai
import datetime

# Configuration
TOPIC = "DevOps"
POSTS_PER_DAY = 3
OUTPUT_DIR = "posts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Set OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")  # Set this in GitHub Secrets

# Function to generate a blog post
def generate_post():
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"You are a tech blogger writing about {TOPIC}."},
            {"role": "user", "content": f"Write an insightful blog post on {TOPIC}."}
        ]
    )
    
    return response["choices"][0]["message"]["content"]

# Generate posts
for i in range(POSTS_PER_DAY):
    post_content = generate_post()
    date_str = datetime.datetime.now().strftime("%Y-%m-%d")
    filename = f"{OUTPUT_DIR}/{date_str}-post-{i+1}.md"
    
    with open(filename, "w") as file:
        file.write(f"# {TOPIC} - {date_str}\n\n{post_content}")

print(f"Generated {POSTS_PER_DAY} posts for {TOPIC}.")
