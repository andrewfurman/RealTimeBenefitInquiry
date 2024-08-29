from openai import OpenAI
import os

def process_transcript(transcript: str) -> str:
    # Set up the OpenAI client
    client = OpenAI(
        # This will use the OPENAI_API_KEY from environment variables
        api_key=os.environ.get("OPENAI_API_KEY")
    )

    # Prompt String (defines a multi paragraph string that can be used as the beginning of a prompt)
    background = """
    This is a conversation between a call-center agent that works for Horizon, Blue Cross Blue Shield of New Jersey and someone calling in that has the Horizon Braven Medicare advantage plan.

Based on their questions, please return the answer. format the answer so that there is a simple one sentence answer at the top and then include more details below if the person wants to read more.

Use emojis to call attention certain parts of emojis distinctly represent the sections of content that they are calling attention to.

Here are the details of what the Braven Medicare advantage plan covers:

**Braven Medicare Choice PPO Plan Overview (2024)**

**Service Area**:  
- R1: Bergen, Essex, Hudson, Middlesex, Monmouth, Ocean, Passaic, Union.  
- R2: Mercer, Morris, Somerset.  
- Freedom: Bergen, Essex, Hudson, Middlesex, Monmouth, Ocean, Passaic, Union.

**Premiums**:  
- R1: $0  
- R2: $0  
- Freedom: $35 (lower if eligible for Extra Help).

**Deductible**: $0 for medical.

**Max OOP**:  
- R1: $7,050 in-net, $11,500 combined.  
- R2: $7,300 in-net, $12,000 combined.  
- Freedom: $6,825 in-net, $9,500 combined.

**Preventive Care**:  
- **In-Net**: $0 copay.  
- **Out-Net**: R1 & R2: $10, Freedom: 30%.  
- **Services**: Annual wellness, cardiovascular screenings, cancer screenings (breast, cervical, colorectal, prostate), abdominal aortic aneurysm, diabetes screenings, lung cancer screening, glaucoma screening, HIV screening, vaccines (flu, pneumonia, hepatitis B, COVID-19), alcohol misuse counseling, obesity screening, smoking cessation, MDPP.

**Inpatient Hospital**:  
- **R1**: $350/day days 1-5, $0/day from day 6+.  
- **R2**: $345/day days 1-5, $0/day from day 6+.  
- **Freedom**: $325/day days 1-5 in-net, 30% out-net, $0/day from day 6+.

**Outpatient Hospital**:  
- **R1 & R2**: $345 in-net, $445 out-net.  
- **Freedom**: $290 in-net, 30% out-net.

**Ambulatory Surgical**:  
- **R1 & R2**: $275 in-net, $375 out-net.  
- **Freedom**: $220 in-net, 30% out-net.

**Doctor Visits**:  
- **Primary Care**: R1 & R2: $0 in-net, $10 out-net. Freedom: $0 in-net, 30% out-net.  
- **Specialist Care**: R1 & R2: $30 in-net, $40-$45 out-net. Freedom: $20 in-net, 30% out-net.

**Emergency Care**:  
- $100 copay (waived if admitted), $100k coverage outside U.S.

**Urgently Needed**:  
- **R1 & R2**: $40 U.S., $100 outside U.S.  
- **Freedom**: $40 U.S., 30% outside U.S.

**Diagnostics/Labs/Imaging**:  
- **R1 & R2**:  
  - **Radiology**: $40-$200 in-net, $60-$225 out-net.  
  - **Labs**: $0 in-net, $20-$50 out-net.  
  - **Tests**: $0-$50 in-net, $50-$110 out-net.  
  - **X-rays**: $0-$25 in-net, $40 out-net.  
- **Freedom**:  
  - **Radiology**: $40-$150 in-net, 30% out-net.  
  - **Labs**: $0 in-net, 30% out-net.  
  - **Tests**: $0-$50 in-net, 30% out-net.  
  - **X-rays**: $0-$25 in-net, 30% out-net.

**Hearing Services**:  
- **Exam**: R1 & R2: $0 in-net, $40-$45 out-net. Freedom: $0 in-net, 30% out-net.  
- **Hearing Aids**: $299-$1,199 in-net via HearUSA.

**Dental Services**:  
- **Routine**: $0 for cleaning (3/yr), exam (3/yr), fluoride (1/6mo), x-rays.  
- **Comprehensive**: 50% of allowed, $1k max/yr, out-net may cost more.

**Vision Services**:  
- **Exam**: $0 in-net (Davis Vision), 50% out-net.  
- **Lenses**: $0 in-net, 50% out-net.  
- **Frames/Contacts**: $150/yr, out-net costs beyond $150.  
- **Post-Cataract Surgery**: $0 in/out-net.

**Mental Health**:  
- **Inpatient**: $374-$385/day days 1-5, $0/day from day 6+, 190 days max in psych hospital.  
- **Outpatient Therapy**: $40-$50 in-net, 30% out-net (Freedom).

**SNF**:  
- $0/day days 1-20, $203/day days 21-100 in-net, 20%-30% out-net.

**Rehab Services**:  
- **PT/OT/Speech**: $20 in-net, $30 out-net (R1 & R2), 30% out-net (Freedom).

**Ambulance**:  
- $250 for ground/air in-net, 20%-30% out-net.

**Medicare Part B Drugs**:  
- 20% in-net, 20%-30% out-net.

**Fitness Benefit**:  
- $200/yr for gym/home fitness/virtual programs.

**Flex Benefit**:  
- $275/yr for Weight Watchers, acupuncture, transportation, etc.

**OTC Allowance**:  
- $70/quarter, $280/yr.

**Chronic Condition Benefit**:  
- $85/quarter, $340/yr for groceries at participating retailers (diabetes, CHF, cardiovascular).

**Home Health Care**:  
- $0 in-net, $10 out-net (R1 & R2), 30% out-net (Freedom).

**In-Home Support**:  
- $0 for up to 36 hrs/yr (grocery, transport, housekeeping).

**Telehealth**:  
- $0 copay for urgent/behavioral health via AmWell.

**Prescription Drugs**:  
- **Deductible**: $0 T1, T2, T6; $200 T3, T4, T5.  
- **Copays (1-Month)**:  
  - **T1**: $0  
  - **T2**: $5-$8  
  - **T3**: $47  
  - **T4**: $100  
  - **T5**: 30%  
  - **T6**: $0  
- **Mail-Order (3-Month)**:  
  - **T1**: $0  
  - **T2**: $7.50-$12  
  - **T3**: $141  
  - **T4**: $300  
  - **T5**: N/A  
  - **T6**: $0  
- **Coverage Gap**: 25% after $5,030 total drug cost until $8,000 OOP.  
- **Catastrophic**: $0 after $8,000 OOP.  
- **Insulin**: $35 max for 1-month supply.  
- **Enhanced Coverage**: Covers some non-Part D drugs (cough meds, ED drugs) at T2 copay.

**Not Covered**: Services not listed or non-Medicare-covered services may not be covered.

Refer to 2024 EOC or contact Member Services for full details.
    """

    # Joins the background string and the claim question together
    prompt = background + transcript

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