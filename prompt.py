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
    This is a conversation between a call-center agent that works for a health insurance company and someone calling in that wants to know more about their health insurance coverage.

Based on their questions in the transcript, please return the answer. 

Format the answer so that it starts with an emoji disinctly representing the topic, followed by a bolded title, followed by a susinct answer with any key amounts bolded.

Do NOT include information clearly addressed in previous responses. Instead focus on the new information that is being asked.  If all questions have been adequirely answered, please respond with "No Major Update"

Question Tips:
- If there is a $0 copay, it will be specifically listed as $0. If no coapy is mentioned, do not say "there is a $0 co-pay", but instead say that there is not a copay for that specific service and talk about whetther or not the service is covered.

Here are the details of what the plan covers:

    """
    planinfo = get_plan_info()
    
    # Joins the background string and the claim question together
    prompt = background + planinfo + " here's the transcript where questions are being asked about the plan: " + transcript

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