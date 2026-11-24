import json

with open(r'C:\Users\user\.gemini\antigravity\brain\76ce6bd4-8b6a-4d0f-86db-9a655ef20cd0\.system_generated\logs\transcript_full.jsonl', 'r', encoding='utf-8') as f:
    for line in f:
        if '"step_index":14121' in line:
            data = json.loads(line)
            with open(r'C:\Users\user\Downloads\websites\templatemo_633_celadon\prompt_dump.txt', 'w', encoding='utf-8') as out:
                out.write(data['content'])
            print("Successfully extracted prompt. Length:", len(data['content']))
            break
