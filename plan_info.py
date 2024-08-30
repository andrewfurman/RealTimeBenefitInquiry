## this python file should have a function that returns the plan information describing what is covered and not covered for specific health insurance plan. It's your return this information as a string.

def get_plan_info():
    return """

    ### Healthfirst Gold Leaf Health Plan Summary (Coverage Period: 1/1/24 – 12/31/24)

    #### Overview:
    - **Plan Type**: HMO
    - **Coverage**: Individual and Family

    #### Premiums, Deductibles, and Out-of-Pocket Costs:
    - **Annual Deductible**: $600 Individual / $1,200 Family (In-Network)
      - *Exclusions*: Prescription drugs, preventive care visits.
    - **Out-of-Pocket Limit**: $5,900 Individual / $11,800 Family
      - *Exclusions*: Premiums, balance billing charges, non-covered services.

    #### Copayments and Coinsurance:
    - **Primary Care Visit**: $25 after deductible
    - **Specialist Visit**: $40 after deductible
    - **Preventive Care**: No charge
    - **Diagnostic Tests (X-ray, Blood Work)**: $25/$40 after deductible (Preauthorization required)
    - **Imaging (CT/PET/MRI)**: $40 after deductible (Preauthorization required)
    - **Emergency Room**: $150 after deductible (waived if admitted)
    - **Urgent Care**: $60 after deductible
    - **Hospital Stay**: $1,000 per admission after deductible (Preauthorization required)
    - **Outpatient Surgery**: $100 after deductible (Preauthorization required)
    - **Prescription Drugs**:
      - **Generic**: $10 (30-day), $25 (90-day mail)
      - **Preferred Brand**: $35 (30-day), $87.50 (90-day mail)
      - **Non-Preferred Brand**: $70 (30-day), $175 (90-day mail)
      - **Specialty**: $70 (30-day), $175 (90-day mail)

    #### Coverage Details:
    - **Mental Health Services**:
      - Outpatient: $25 after deductible (Preauthorization for select services)
      - Inpatient: $1,000 per admission after deductible (Preauthorization required)
    - **Pregnancy Care**:
      - Professional Services: $100 after deductible
      - Facility Services: $1,000 per admission after deductible
    - **Rehabilitation/Habilitation**: $30 after deductible, up to 60 visits/year (combined, preauthorization required)
    - **Skilled Nursing**: $1,000 per admission after deductible, up to 200 days/year (Preauthorization required)
    - **Durable Medical Equipment**: 20% coinsurance after deductible (Preauthorization required)
    - **Home Health Care**: $25 after deductible, up to 40 visits/year (Preauthorization required)
    - **Hospice**: $1,000 per admission after deductible (Inpatient); $25 after deductible (Outpatient); Preauthorization required.

    #### Excluded Services:
    - **Not Covered**: Acupuncture, cosmetic surgery, dental (adult), long-term care, non-emergency care outside the U.S., private-duty nursing, routine eye care (adult), routine foot care, weight loss programs.

    #### Other Covered Services:
    - **Covered with Limitations**: Bariatric surgery, chiropractic care, infertility treatment, abortion services, hearing aids.

    #### Important Notes:
    - **Network Providers**: Lower costs with network providers; higher costs or non-coverage with out-of-network providers.
    - **No Referrals Needed**: You can see specialists without a referral.

    #### Appeals and Grievances:
    - **Contact**: New York State Department of Financial Services, 800-342-3736.
    - **Assistance**: Community Health Advocates, 888-614-5400.

    #### Language Assistance:
    - Available in Spanish, Tagalog, Chinese, Navajo, and other languages.

    This summary is designed to provide you with a compact yet detailed overview of the Healthfirst Gold Leaf Plan, covering key benefits, costs, and exclusions.
    
    """