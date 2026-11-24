import os
import re

DIR = r"C:\Users\user\Downloads\websites\templatemo_633_celadon"
how_path = os.path.join(DIR, "how-it-works.html")

with open(how_path, "r", encoding="utf-8") as f:
    how = f.read()

# Update hero subtext
how = how.replace(
    '<p class="sub rv d2">Virtual Human does not generate superficial platitudes. We combine verified human frameworks, episodic conversational memory, and adaptive cognitive calibration to create digital identities that challenge your thinking and guide your execution.</p>',
    '<p class="sub rv d2">Virtual Human does not generate superficial platitudes or generic responses. Whether you are creating a personal companion (father, mother, spouse, confidant) or engaging an expert mentor, our system combines persistent episodic memory, grounded narrative context, and adaptive emotional calibration to build meaningful, lasting relationships.</p>'
)

# Update Step 1 in Track
step1_old = '<p>Knowledge owners upload original frameworks, recorded insights, essays, and methodologies. Our indexing system builds semantic knowledge clusters without retraining open models.</p>'
step1_new = '<p>Define any identity: upload expert frameworks and articles, or impart personal backstories, family traditions, and life memories. Our indexing system anchors dialogue in your actual context without retraining open models.</p>'
how = how.replace(step1_old, step1_new)

# Update Step 2 in Track
step2_old = '<p>As you converse, the platform extracts key decisions, goals, and recurring dilemmas into a persistent episodic memory graph. Each subsequent session recognizes your evolving context.</p>'
step2_new = '<p>As you converse, the platform extracts personal milestones, recurring challenges, shared humor, and past decisions into a persistent episodic memory graph. Each session builds naturally on the last.</p>'
how = how.replace(step2_old, step2_new)

# Update Step 3 in Track
step3_old = '<p>Your companion sends personalized follow-ups via email and in-app alerts referencing your exact conversation. It suggests actionable challenges and measures your progress.</p>'
step3_new = '<p>Your companion sends personalized follow-ups via email referencing your exact discussions—like a caring father checking on your new home or a mentor reviewing your pricing model. Zero generic template spam.</p>'
how = how.replace(step3_old, step3_new)

with open(how_path, "w", encoding="utf-8") as f:
    f.write(how)

print("Updated how-it-works.html successfully")
