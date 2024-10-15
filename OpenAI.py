from openai import OpenAI

import os
from dotenv import load_dotenv

load_dotenv(".env") #loads environ vars from .venv file (hidden on mac bc start with .)
# Set your OpenAI API key
api_key = os.environ.get("openai_api_key")

prompt = """You are a neurosurgeon at one of the top universities in the United States. Please summarize the following medical case as it would appear on an electronic medical record:
X is a 16-year-old male who grew up on a rice
farm near Freetown, Sierra Leone, with his
mother, father, and two siblings. His family has
traditionally engaged in subsistence farming, but
since the Ebola epidemic in 2014-15, which
disrupted the rural labor market, X’s parents have
also been informally employed as retail workers in
Freetown. Their combined income is
approximately 2000 USD per year, which is about
the mean for a Sierra Leonean household. X and
his siblings now attend school in Freetown under
the government’s new scheme for fee-free
primary education.
This case is based on the clinical course of a real patient who presented to
Connaught Hospital (Sierra Leone) in 2019. Some details were changed to anonymize
the patient, and some fictional but representative context was added.

On January 5th, 2019, X was at a beach in Freetown with some friends. He dove headfirst into
the ocean but unfortunately struck a rock, briefly losing consciousness. He was brought to
shore by his friends, who noticed that he was unable to move his lower limbs or sit upright. An
ambulance was called, and X was immobilized in a C-collar and transported to the Accident &
Emergency Department (A&E) at Connaught Hospital, the main public referral hospital in
Freetown.

Upon arrival in A&E, X was found to be conscious and alert. However, he exhibited reduced
sensation, muscle tone, and power (0/5) in his lower limbs. A Foley catheter was placed to aid
with voiding, and X was administered IV fluids. He was admitted to medical ward 3 with a
suspected injury of the C3-C4 vertebrae and placed under the supervision of Dr. A.K.,
Connaught Hospital’s only pediatric orthopedic consultant. (There are no neurosurgeons at
Connaught Hospital.) X was prescribed continuous neck immobilization via rigid C-collar, bed
rest with water bag application to pressure-prone areas, physiotherapy to strengthen his lower
limbs, blood thinners, IV fluids, a liquid diet, and pain management with NSAIDs. He required
intermittent catheterization and manual fecal evacuation in order to pass urine and stool,
respectively.

Six days into his admission, X was undergoing a routine log roll maneuver (as he did
every two hours) when his nurse spotted a sacral pressure ulcer. These ulcers would
be monitored closely over X’s hospital course, but they would nonetheless progress
despite appropriate precautionary measures, wound care, and antibiotics.

Two and a half weeks after admission, X’s hemoglobin dropped suddenly without an
attributable source of bleeding. His hemoglobin rebounded successfully after several
blood transfusions.

On February 16th (over a month after the incident), X began to notice a heightened
sensation of numbness, along with paresthesias, in his hands and feet. His symptoms
were deemed to be consistent with peripheral neuritis, and Dr. A.K. revised X’s
diagnosis to cervical cord contusion, secondary to spinal fracture.

X continued to improve under medical management. As of March 24, 2019, X was alert
and oriented, with a Glasgow Coma Score of 15, but he still retained severe motor
deficits. He was discharged from Connaught Hospital to his home, with referrals for
physiotherapy to train his bladder/rectal tone and a skin graft for his sacral pressure
ulcer.
"""
def process(prompt=prompt):
    client = OpenAI(
        # This is the default and can be omitted
        api_key=api_key,
    )
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
    )
    
    response = chat_completion.model_dump()["choices"][0]["message"]["content"]
    return response

