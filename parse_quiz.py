import re
import json

with open('step_96_content.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract answers from markdown table
table_matches = re.findall(r'\|\s*\*\*(\d+)\*\*\s*\|\s*\*\*([ก-ง])\*\*\s*\|\s*(.*?)\s*\|', text)
print(f'Answer table matches count: {len(table_matches)}')
answers = {int(m[0]): {'key': m[1], 'exp': m[2]} for m in table_matches}

# Split text before the answer tables
content_parts = re.split(r'### เฉลยตอนที่ 1', text)
questions_text = content_parts[0]

# Each question starts with ### <number>.
q_blocks = re.findall(r'###\s+(\d+)\.\s+(.*?)(?=(?:\n###\s+\d+\.|\Z))', questions_text, re.DOTALL)
print(f'q_blocks found: {len(q_blocks)}')

parsed_questions = []
for q_num_str, q_body in q_blocks:
    q_num = int(q_num_str)
    lines = [l.strip() for l in q_body.strip().split('\n') if l.strip() and l.strip() != '---']
    
    q_lines = []
    choices = {}
    current_choice = None
    
    for line in lines:
        m = re.match(r'^([ก-ง])\.\s*(.*)', line)
        if m:
            current_choice = m.group(1)
            choices[current_choice] = m.group(2)
        elif current_choice:
            choices[current_choice] += ' ' + line
        else:
            q_lines.append(line)
            
    q_text = ' '.join(q_lines)
    
    ans_info = answers.get(q_num, {})
    parsed_questions.append({
        'id': q_num,
        'part': 1 if q_num <= 20 else 2,
        'part_name': 'ตอนที่ 1: ข้อสอบเน้นความจำและหลักการสำคัญ' if q_num <= 20 else 'ตอนที่ 2: ข้อสอบเชิงสถานการณ์และการประยุกต์ใช้',
        'question': q_text,
        'choices': choices,
        'answer': ans_info.get('key', ''),
        'explanation': ans_info.get('exp', '')
    })

print(f'Parsed {len(parsed_questions)} questions.')
errors = 0
for q in parsed_questions:
    if len(q['choices']) != 4:
        print(f"Error Q{q['id']}: has {len(q['choices'])} choices")
        errors += 1
    if not q['answer']:
        print(f"Error Q{q['id']}: missing answer")
        errors += 1
    if not q['explanation']:
        print(f"Error Q{q['id']}: missing explanation")
        errors += 1

if errors == 0:
    print("ALL 35 QUESTIONS PARSED PERFECTLY!")
    with open('quiz_data.json', 'w', encoding='utf-8') as out:
        json.dump(parsed_questions, out, ensure_ascii=False, indent=2)
    print("Saved to quiz_data.json")
