from openai import OpenAI
import os

from plan_info import get_plan_info

def process_transcript(transcript: str) -> str:
    # Set up the OpenAI client
    client = OpenAI(
        # This will use the OPENAI_API_KEY from environment variables
        api_key=os.environ.get("OPENAI_API_KEY")
    )

    # Prompt String (defines a multi paragraph string that can be used as the beginning of a prompt)
    background = """
    This is a conversation between a call-center agent that works for Horizon, Blue Cross Blue Shield of New Jersey and someone calling in that has the Horizon Braven Medicare advantage plan.

Based on their questions in the transcript, please return the answer. format the answer so that there is a simple one sentence answer at the top and then include more details below if the person wants to read more.

Use emojis to call attention certain parts of emojis distinctly represent the sections of content that they are calling attention to.

Please also note to not include information clearly addressed in previous responses. Instead focus on the new information that is being asked.

Question Tips:
- If there is a $0 copay, it will be specifically listed as $0. If no coapy is mentioned, do not say "there is a $0 co-pay", but instead say that there is not a copay for that specific service and talk about whetther or not the service is covered.

Here are the details of what the plan covers:

    """
    planinfo = get_plan_info()
    
    # Joins the background string and the claim question together
    prompt = background + planinfo + "here's the transcript where questions are being asked about the plan: " + transcript

    # Send the question to ChatGPT and save the answer
    chat_completion = client.chat.completions.create(
        model="gpt-4o-mini",  # or whichever model you prefer
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions about claims."},
            {"role": "user", "content": prompt}
        ]
    )

    # Extract the answer from the API response
    answer = chat_completion.choices[0].message.content

    return answer