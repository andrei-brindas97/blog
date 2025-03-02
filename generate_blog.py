import os
import openai
import datetime
import logging

# Configure logging
LOG_FILE = "blog_generator.log"
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Configuration
TOPIC = "DevOps"
POSTS_PER_DAY = 3
OUTPUT_DIR = "_posts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Initialize OpenAI client
API_KEY = os.getenv("OPENAI_API_KEY")

if not API_KEY:
    logging.error("OPENAI_API_KEY is not set. Make sure it's configured in GitHub Secrets.")
    raise ValueError("OPENAI_API_KEY is missing.")

client = openai.OpenAI(api_key=API_KEY)

def generate_post():
    """Generates a blog post using OpenAI API."""
    try:
        logging.info(f"Generating a blog post on {TOPIC}...")

        response = client.chat.completions.create(
            model="gpt-4.5-preview",
            messages=[
                {"role": "system", "content": f"You are a tech blogger writing about {TOPIC}."},
                {"role": "user", "content": f"Write an insightful blog post on {TOPIC}."}
            ],
            max_tokens=800
        )
        
        post_content = response.choices[0].message.content.strip()
        logging.info("Blog post generated successfully.")
        return post_content

    except openai.APIError as e:
        logging.error(f"OpenAI API error: {e}")
        return None
    except Exception as e:
        logging.error(f"Unexpected error while generating post: {e}")
        return None

# Generate multiple posts
for i in range(POSTS_PER_DAY):
    logging.info(f"Starting generation of post {i+1}/{POSTS_PER_DAY}...")
    
    post_content = generate_post()
    if post_content:
        date_str = datetime.datetime.now().strftime("%Y-%m-%d")
        filename = f"{OUTPUT_DIR}/{date_str}-post-{i+1}.md"

        try:
            # Add front matter to the post
            front_matter = f"""---
layout: post
title: "{TOPIC} - Post {i+1}"
date: {date_str}
categories: 
  - {TOPIC}
tags:
  - DevOps
  - Technology
---

"""
            with open(filename, "w", encoding="utf-8") as file:
                file.write(front_matter + post_content)
            logging.info(f"Post {i+1} saved to {filename}.")
        
        except IOError as e:
            logging.error(f"Error saving post {i+1}: {e}")

print(f"Generated {POSTS_PER_DAY} posts for {TOPIC}. Check {LOG_FILE} for details.")
