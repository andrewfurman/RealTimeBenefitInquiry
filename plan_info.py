## this python file should have a function that returns the plan information describing what is covered and not covered for specific health insurance plan. It's your return this information as a string.

def get_plan_info():
    return """

    ### Braven Medicare Choice (PPO) Region 1 Plan

    **Coverage Period:** Jan 1, 2024 – Dec 31, 2024  
    **Service Area:** Bergen, Essex, Hudson, Middlesex, Monmouth, Ocean, Passaic, and Union counties

    ---

    **Premium:** $0/month  
    **Annual Medical Deductible:** $0  
    **Max Out-of-Pocket:**  
    - **In-Network:** $7,050  
    - **Combined In/Out:** $11,500

    ---

    ### Covered Services & Costs

    - **Inpatient Hospital:** $350/day for days 1-5, $0 after day 6. Prior auth may be needed.  
    - **Outpatient Hospital/Observation:** $345 In-Network, $445 Out. Prior auth may be needed.  
    - **Ambulatory Surgery:** $275 In-Network, $375 Out. Prior auth may be needed.  
    - **Doctor Visits:** $0 for Primary, $30 for Specialist In-Network; $10 and $40 Out-Network. Prior auth may be needed.  
    - **Preventive Care:** $0 In-Network, $10 Out. No prior auth needed.  
    - **Emergency:** $100, covers worldwide up to $100,000/year.  
    - **Urgent Care:** $40 In-Network, $100 Out (Worldwide).  
    - **Diagnostics:**  
      - **Radiology:** $40/$175 In-Network; $60/$200 Out.  
      - **Lab:** $0 In-Network; $20/$50 Out.  
      - **Therapeutic Radiology:** 20% both In- and Out-Network.  
    - **Hearing:**  
      - **Diagnostic Exam:** $30 In, $40 Out.  
      - **Routine Exam:** $0 In, $40 Out.  
      - **Hearing Aids:** $299-$1,199 In; Not covered Out.  
    - **Dental:**  
      - **Routine:** $0 In (3 cleanings, exams, fluoride/year); Higher cost Out.  
      - **Comprehensive:** 50% In; Higher cost Out. $1,000 annual max.  
      - **Medicare-Covered Dental:** 20% both In and Out.  
    - **Vision:**  
      - **Routine Exam:** $0 In, 50% Out.  
      - **Lenses:** $0 In, 50% Out. $150 annual allowance for frames/contacts.  
      - **Post-Cataract:** $0 both In and Out.  
      - **Condition Exams:** $30 In, $40 Out.  
    - **Chiropractic:** $15 In, $30 Out. Prior auth may be needed.  
    - **SNF:** $0 for days 1-20, $203 for days 21-100 In-Network; 20% Out.  
    - **Ambulance:** $250 for Ground/Air both In and Out.  
    - **Home Health:** $0 In, $10 Out. Prior auth may be needed.  
    - **Physical Therapy:** $20 In, $30 Out. Prior auth may be needed.  
    - **Substance Use:** $40 In, $50 Out per session. Prior auth may be needed.  
    - **Rehabilitation:** $20 In, $30 Out. Prior auth may be needed.  
    - **Medicare Part B Drugs:** Up to 20% In and Out. Prior auth may be needed.

    ---

    ### Prescription Drugs

    - **Deductible:** $0 for Tiers 1, 2, 6; $200 for Tiers 3, 4, 5  
    - **Initial Coverage:**  
      - **Tier 1:** $0  
      - **Tier 2:** $8  
      - **Tier 3:** $47  
      - **Tier 4:** $100  
      - **Tier 5:** 30%  
      - **Tier 6:** $0  
    - **Coverage Gap:** 25% after $5,030 until $8,000  
    - **Catastrophic:** $0 after $8,000  
    - **Insulin:** $35 max per month  
    - **Enhanced Coverage:** Tier 2 copay for non-Medicare drugs (e.g., ED drugs, cough meds)

    ---

    ### Additional Benefits

    - **OTC Allowance:** $70/quarter  
    - **Flex Benefit:** $275/year (Weight Watchers, acupuncture, transport, etc.)  
    - **Fitness:** $200/year  
    - **Nurse Line:** $0  
    - **In-Home Support:** 36 hours/year

    ---

    ### Prior Authorization

    Required for services like inpatient/outpatient hospital stays, diagnostics, chiropractic, rehab, substance use services, and some Medicare Part B drugs.

    ---

    ### Contact Info

    Visit [BravenHealth.com/2024EOCChoiceA](https://BravenHealth.com/2024EOCChoiceA) or call 1-833-272-8360 (TTY: 711).
    
    """