# -*- coding: utf-8 -*-
"""
Script to generate the complete 60 questions, 40 flashcards, and summary dataset for EDP3502
"""

import json

# Q6 was missing in build_full_data.py, let's include it and ensure all 60 are pristine!
q6 = {
    "id": 6,
    "chapter": 6,
    "chapter_name": "บทที่ 6: ตัวอย่างกระบวนการปรึกษา",
    "part": 1,
    "part_name": "ตอนที่ 1: ประเด็นหลักและแก่นทฤษฎี",
    "type": "concept",
    "question": "การส่งต่อ (Referral) ผู้รับการปรึกษาไปยังผู้เชี่ยวชาญอื่น ควรเกิดขึ้นในกรณีใด และมีหลักการปฏิบัติอย่างไร",
    "choices": {
        "ก": "ส่งต่อทันทีที่ผู้รับการปรึกษาเริ่มร้องไห้เพื่อไม่ให้ผู้ให้คำปรึกษาต้องรับแรงกดดันทางอารมณ์",
        "ข": "ส่งต่อเมื่อประเมินแล้วพบว่าปัญหาเกินขอบเขตความรู้ความสามารถ ประสบการณ์ หรือขัดกับจริยธรรม โดยต้องชี้แจงเหตุผลและได้รับความยินยอมจากผู้รับการปรึกษา",
        "ค": "ส่งต่อไปยังฝ่ายปกครองหรือผู้ปกครองเพื่อลงโทษทางวินัยโดยไม่ต้องแจ้งให้นักเรียนทราบล่วงหน้า",
        "ง": "ไม่ควรส่งต่อในทุกกรณีเพราะถือเป็นการละทิ้งหน้าที่และขาดความรับผิดชอบวิชาชีพ"
    },
    "answer": "ข",
    "explanation": "<strong>หลักการส่งต่อ (Referral):</strong> ผู้ให้คำปรึกษาต้องตระหนักถึงข้อจำกัดและความเชี่ยวชาญของตน หากปัญหาเกินขอบเขต (เช่น ภาวะซึมเศร้าขั้นรุนแรง เสี่ยงฆ่าตัวตาย โรคจิตเภท สารเสพติดรุนแรง) ต้องส่งต่อแพทย์หรือจิตแพทย์ โดยต้องอธิบายเหตุผลและได้รับความยินยอมจากผู้รับบริการเพื่อประโยชน์สูงสุดของเขา"
}

with open("all_60_questions.json", "r", encoding="utf-8") as f:
    qs = json.load(f)

# Insert Q6
qs.append(q6)
qs.sort(key=lambda x: x["id"])

print(f"Total questions now: {len(qs)}")
assert len(qs) == 60, f"Expected 60 questions, got {len(qs)}"

# Check parts and chapters
part1 = [q for q in qs if q["part"] == 1]
part2 = [q for q in qs if q["part"] == 2]
print(f"Part 1 (Concepts): {len(part1)}")
print(f"Part 2 (Situations): {len(part2)}")

from collections import Counter
print("Chapters:", Counter([q["chapter"] for q in qs]))

with open("all_60_questions.json", "w", encoding="utf-8") as f:
    json.dump(qs, f, ensure_ascii=False, indent=2)
print("Updated all_60_questions.json successfully!")
