import json
import re
import os

with open('quiz_data.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

# Helper function to clean markdown and LaTeX in text
def clean_format(text):
    if not text:
        return ''
    # Replace LaTeX arrows
    text = text.replace(r'$\rightarrow$', '➔')
    text = text.replace(r'\rightarrow', '➔')
    # Bold **text**
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Italic *text*
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    return text

# Pre-format questions
formatted_questions = []
for q in questions:
    clean_choices = {}
    for k, v in q['choices'].items():
        clean_choices[k] = clean_format(v)
    formatted_questions.append({
        'id': q['id'],
        'part': q['part'],
        'part_name': q['part_name'],
        'question': clean_format(q['question']),
        'choices': clean_choices,
        'answer': q['answer'],
        'explanation': clean_format(q['explanation'])
    })

questions_json_str = json.dumps(formatted_questions, ensure_ascii=False)

html_template = f"""<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>แบบทดสอบจำลอง EDP3502: การช่วยเหลือและให้คำปรึกษาผู้เรียน (บทที่ 5 - 11)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Prompt:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Sarabun:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
  <style>
    :root {{
      --primary: #2563eb;
      --primary-dark: #1d4ed8;
      --primary-light: #eff6ff;
      --secondary: #0f172a;
      --accent: #6366f1;
      --accent-light: #e0e7ff;
      --success: #10b981;
      --success-light: #ecfdf5;
      --success-border: #6ee7b7;
      --danger: #ef4444;
      --danger-light: #fef2f2;
      --danger-border: #fca5a5;
      --warning: #f59e0b;
      --warning-light: #fffbeb;
      --flagged: #d97706;
      --bg: #f8fafc;
      --card-bg: #ffffff;
      --border: #e2e8f0;
      --text-main: #1e293b;
      --text-muted: #64748b;
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.06);
      --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.08), 0 2px 4px -2px rgba(0,0,0,0.05);
      --shadow-lg: 0 10px 20px -3px rgba(0,0,0,0.1), 0 4px 6px -4px rgba(0,0,0,0.05);
      --radius: 12px;
    }}

    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      font-family: 'Sarabun', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg);
      color: var(--text-main);
      line-height: 1.6;
      font-size: 16px;
      -webkit-font-smoothing: antialiased;
    }}

    h1, h2, h3, h4, .font-heading {{
      font-family: 'Prompt', sans-serif;
      font-weight: 600;
    }}

    /* Top Hero Header */
    header.hero-header {{
      background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 55%, #4f46e5 100%);
      color: #ffffff;
      padding: 40px 20px 32px;
      box-shadow: var(--shadow-md);
      position: relative;
      overflow: hidden;
    }}

    header.hero-header::before {{
      content: "";
      position: absolute;
      top: -60px;
      right: -60px;
      width: 240px;
      height: 240px;
      background: radial-gradient(circle, rgba(255,255,255,0.12) 0%, rgba(255,255,255,0) 70%);
      border-radius: 50%;
    }}

    .header-content {{
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 12px;
      position: relative;
      z-index: 1;
    }}

    .badge-course {{
      display: inline-flex;
      align-items: center;
      gap: 8px;
      background: rgba(255, 255, 255, 0.18);
      backdrop-filter: blur(10px);
      padding: 6px 16px;
      border-radius: 9999px;
      font-size: 0.88rem;
      font-weight: 600;
      width: fit-content;
      border: 1px solid rgba(255, 255, 255, 0.28);
      letter-spacing: 0.02em;
    }}

    .hero-header h1 {{
      font-size: 1.95rem;
      line-height: 1.3;
      letter-spacing: -0.02em;
      text-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }}

    .hero-header p {{
      color: #e0e7ff;
      font-size: 1.02rem;
      max-width: 850px;
      line-height: 1.6;
    }}

    .meta-bar {{
      display: flex;
      flex-wrap: wrap;
      gap: 16px;
      margin-top: 10px;
      font-size: 0.92rem;
      color: #bfdbfe;
    }}

    .meta-item {{
      display: flex;
      align-items: center;
      gap: 6px;
      background: rgba(0,0,0,0.12);
      padding: 4px 12px;
      border-radius: 6px;
    }}

    /* Main Container */
    .app-container {{
      max-width: 1200px;
      margin: 28px auto 90px;
      padding: 0 16px;
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 26px;
      align-items: start;
    }}

    @media (max-width: 992px) {{
      .app-container {{
        grid-template-columns: 1fr;
      }}
      .sticky-sidebar {{
        position: static !important;
        margin-bottom: 24px;
      }}
    }}

    /* Controls Bar */
    .controls-card {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 16px 20px;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border);
      margin-bottom: 22px;
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
      align-items: center;
      justify-content: space-between;
    }}

    .tabs-group {{
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }}

    .tab-btn {{
      font-family: 'Prompt', sans-serif;
      padding: 8px 15px;
      border-radius: 8px;
      border: 1px solid var(--border);
      background: #f1f5f9;
      color: var(--text-main);
      cursor: pointer;
      font-size: 0.88rem;
      font-weight: 500;
      transition: all 0.18s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }}

    .tab-btn:hover {{
      background: #e2e8f0;
      border-color: #cbd5e1;
    }}

    .tab-btn.active {{
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
      box-shadow: 0 2px 4px rgba(37, 99, 235, 0.25);
    }}

    .tab-btn.tab-wrong {{
      background: var(--danger-light);
      color: #991b1b;
      border-color: var(--danger-border);
    }}
    .tab-btn.tab-wrong.active {{
      background: var(--danger);
      color: #ffffff;
      border-color: var(--danger);
    }}

    .mode-switch-container {{
      display: flex;
      align-items: center;
      background: #f1f5f9;
      border-radius: 9999px;
      padding: 4px;
      border: 1px solid var(--border);
    }}

    .mode-btn {{
      font-family: 'Prompt', sans-serif;
      padding: 6px 14px;
      border-radius: 9999px;
      border: none;
      background: transparent;
      color: var(--text-muted);
      cursor: pointer;
      font-size: 0.85rem;
      font-weight: 500;
      transition: all 0.2s;
      display: inline-flex;
      align-items: center;
      gap: 5px;
    }}

    .mode-btn.active {{
      background: #ffffff;
      color: var(--primary-dark);
      font-weight: 600;
      box-shadow: 0 1px 3px rgba(0,0,0,0.1);
    }}

    /* Questions List */
    .questions-wrapper {{
      display: flex;
      flex-direction: column;
      gap: 22px;
    }}

    .question-card {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 24px;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border);
      transition: all 0.2s ease;
      scroll-margin-top: 90px;
      position: relative;
    }}

    .question-card:hover {{
      box-shadow: var(--shadow-md);
      border-color: #cbd5e1;
    }}

    .q-header {{
      display: flex;
      align-items: flex-start;
      gap: 14px;
      margin-bottom: 16px;
    }}

    .q-num-badge {{
      flex-shrink: 0;
      background: #e0e7ff;
      color: #3730a3;
      font-family: 'Prompt', sans-serif;
      font-weight: 700;
      font-size: 1rem;
      width: 40px;
      height: 40px;
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid #c7d2fe;
    }}

    .q-title-wrap {{
      flex-grow: 1;
    }}

    .q-meta-top {{
      display: flex;
      align-items: center;
      justify-content: space-between;
      margin-bottom: 6px;
    }}

    .q-part-label {{
      font-size: 0.78rem;
      font-family: 'Prompt', sans-serif;
      color: #4f46e5;
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.04em;
      background: #eef2ff;
      padding: 2px 8px;
      border-radius: 4px;
      width: fit-content;
    }}

    .flag-btn {{
      background: transparent;
      border: none;
      cursor: pointer;
      font-size: 1.15rem;
      opacity: 0.35;
      transition: all 0.15s;
      padding: 2px 6px;
      border-radius: 4px;
    }}
    .flag-btn:hover {{
      opacity: 0.8;
      background: #f1f5f9;
    }}
    .flag-btn.flagged {{
      opacity: 1;
      filter: drop-shadow(0 1px 2px rgba(217, 119, 6, 0.4));
    }}

    .q-text {{
      font-size: 1.1rem;
      font-weight: 600;
      color: var(--text-main);
      line-height: 1.55;
    }}

    /* Choices List */
    .choices-list {{
      display: flex;
      flex-direction: column;
      gap: 10px;
      margin-top: 16px;
    }}

    .choice-item {{
      display: flex;
      align-items: flex-start;
      gap: 12px;
      padding: 12px 16px;
      border-radius: 10px;
      border: 1.5px solid var(--border);
      cursor: pointer;
      background: #ffffff;
      transition: all 0.18s ease;
      user-select: none;
      position: relative;
    }}

    .choice-item:hover {{
      background: #f8fafc;
      border-color: #94a3b8;
    }}

    .choice-key {{
      flex-shrink: 0;
      font-family: 'Prompt', sans-serif;
      font-weight: 600;
      width: 30px;
      height: 30px;
      border-radius: 50%;
      background: #f1f5f9;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.92rem;
      border: 1px solid var(--border);
      transition: all 0.18s;
    }}

    .choice-text {{
      font-size: 1rem;
      line-height: 1.55;
      padding-top: 3px;
      flex-grow: 1;
    }}

    /* Selected state */
    .choice-item.selected {{
      background: var(--primary-light);
      border-color: var(--primary);
    }}

    .choice-item.selected .choice-key {{
      background: var(--primary);
      color: #ffffff;
      border-color: var(--primary);
    }}

    /* Correct Choice Feedback */
    .choice-item.is-correct {{
      background: var(--success-light) !important;
      border-color: var(--success) !important;
    }}
    .choice-item.is-correct .choice-key {{
      background: var(--success) !important;
      color: #ffffff !important;
      border-color: var(--success) !important;
    }}

    /* Wrong Choice Feedback */
    .choice-item.is-wrong {{
      background: var(--danger-light) !important;
      border-color: var(--danger) !important;
    }}
    .choice-item.is-wrong .choice-key {{
      background: var(--danger) !important;
      color: #ffffff !important;
      border-color: var(--danger) !important;
    }}

    /* Explanation Box */
    .explanation-box {{
      margin-top: 18px;
      padding: 16px 20px;
      background: #f8fafc;
      border-left: 4px solid var(--accent);
      border-radius: 8px;
      font-size: 0.96rem;
      color: #334155;
      display: none;
      animation: fadeIn 0.25s ease;
      line-height: 1.6;
    }}

    .explanation-box.show {{
      display: block;
    }}

    .explanation-title {{
      font-family: 'Prompt', sans-serif;
      font-weight: 600;
      color: #4338ca;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 8px;
    }}

    /* Right Sticky Sidebar */
    .sticky-sidebar {{
      position: sticky;
      top: 24px;
      display: flex;
      flex-direction: column;
      gap: 20px;
    }}

    .sidebar-card {{
      background: var(--card-bg);
      border-radius: var(--radius);
      padding: 22px;
      box-shadow: var(--shadow-sm);
      border: 1px solid var(--border);
    }}

    .card-title {{
      font-size: 1.05rem;
      font-weight: 600;
      color: var(--text-main);
      margin-bottom: 14px;
      display: flex;
      align-items: center;
      justify-content: space-between;
    }}

    .stat-row {{
      display: flex;
      justify-content: space-between;
      margin-bottom: 8px;
      font-size: 0.92rem;
      color: var(--text-muted);
    }}
    .stat-row strong {{
      color: var(--text-main);
    }}

    .progress-bar-bg {{
      width: 100%;
      height: 10px;
      background: #e2e8f0;
      border-radius: 9999px;
      overflow: hidden;
      margin: 10px 0 16px;
    }}

    .progress-bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, #3b82f6, #10b981);
      width: 0%;
      transition: width 0.3s ease;
    }}

    /* Navigator Grid */
    .q-grid {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 6px;
      margin-top: 10px;
    }}

    .grid-btn {{
      aspect-ratio: 1;
      border: 1px solid var(--border);
      background: #f8fafc;
      color: var(--text-main);
      border-radius: 6px;
      font-family: 'Prompt', sans-serif;
      font-size: 0.86rem;
      font-weight: 500;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      transition: all 0.15s ease;
      position: relative;
    }}

    .grid-btn:hover {{
      background: #e2e8f0;
    }}

    .grid-btn.answered {{
      background: #dbeafe;
      border-color: #93c5fd;
      color: #1e40af;
      font-weight: 600;
    }}

    .grid-btn.flagged::after {{
      content: "";
      position: absolute;
      top: 2px;
      right: 2px;
      width: 6px;
      height: 6px;
      background: var(--warning);
      border-radius: 50%;
    }}

    .grid-btn.correct {{
      background: #d1fae5 !important;
      border-color: #6ee7b7 !important;
      color: #065f46 !important;
      font-weight: 700;
    }}

    .grid-btn.wrong {{
      background: #fee2e2 !important;
      border-color: #fca5a5 !important;
      color: #991b1b !important;
      font-weight: 700;
    }}

    /* Action Buttons */
    .btn {{
      font-family: 'Prompt', sans-serif;
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 8px;
      width: 100%;
      padding: 12px 18px;
      border-radius: 8px;
      font-size: 0.95rem;
      font-weight: 600;
      cursor: pointer;
      border: none;
      transition: all 0.2s ease;
    }}

    .btn-primary {{
      background: var(--primary);
      color: #ffffff;
      box-shadow: 0 4px 6px rgba(37, 99, 235, 0.25);
    }}
    .btn-primary:hover {{
      background: var(--primary-dark);
      transform: translateY(-1px);
    }}

    .btn-outline {{
      background: transparent;
      color: var(--text-muted);
      border: 1px solid var(--border);
      margin-top: 8px;
    }}
    .btn-outline:hover {{
      background: #f1f5f9;
      color: var(--text-main);
    }}

    /* Score Result Modal */
    .modal-overlay {{
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.65);
      backdrop-filter: blur(5px);
      display: none;
      align-items: center;
      justify-content: center;
      z-index: 1000;
      padding: 20px;
      animation: fadeIn 0.25s ease;
    }}

    .modal-overlay.active {{
      display: flex;
    }}

    .modal-card {{
      background: #ffffff;
      border-radius: 18px;
      max-width: 520px;
      width: 100%;
      padding: 34px 28px;
      box-shadow: var(--shadow-lg);
      text-align: center;
      position: relative;
      animation: scaleUp 0.25s ease;
    }}

    .modal-icon {{
      width: 76px;
      height: 76px;
      margin: 0 auto 16px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 2.4rem;
      background: #eff6ff;
    }}

    .score-big {{
      font-family: 'Prompt', sans-serif;
      font-size: 3.2rem;
      font-weight: 700;
      color: var(--primary-dark);
      line-height: 1;
      margin: 12px 0 6px;
    }}

    .score-percent {{
      font-size: 1.05rem;
      color: var(--text-muted);
      margin-bottom: 22px;
      line-height: 1.5;
    }}

    .score-breakdown {{
      background: #f8fafc;
      border-radius: 12px;
      padding: 16px;
      margin-bottom: 24px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
      text-align: left;
      border: 1px solid var(--border);
    }}

    .breakdown-box {{
      padding: 12px 14px;
      border-radius: 8px;
      background: #ffffff;
      border: 1px solid var(--border);
    }}
    .breakdown-box h4 {{
      font-size: 0.82rem;
      color: var(--text-muted);
      margin-bottom: 4px;
    }}
    .breakdown-box .val {{
      font-family: 'Prompt', sans-serif;
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--text-main);
    }}

    .modal-actions {{
      display: flex;
      flex-direction: column;
      gap: 10px;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; }}
      to {{ opacity: 1; }}
    }}

    @keyframes scaleUp {{
      from {{ opacity: 0; transform: scale(0.95); }}
      to {{ opacity: 1; transform: scale(1); }}
    }}

    /* Print styles */
    @media print {{
      header.hero-header, .sticky-sidebar, .controls-card, .btn, .flag-btn {{
        display: none !important;
      }}
      .app-container {{
        display: block !important;
        max-width: 100% !important;
        margin: 0 !important;
        padding: 0 !important;
      }}
      .question-card {{
        break-inside: avoid;
        box-shadow: none !important;
        border: 1px solid #cbd5e1 !important;
        margin-bottom: 20px !important;
        padding: 16px !important;
      }}
      .explanation-box {{
        display: block !important;
        border-left: 3px solid #6366f1 !important;
      }}
    }}
  </style>
</head>
<body>

  <!-- Top Hero Header -->
  <header class="hero-header">
    <div class="header-content">
      <div class="badge-course">
        <span>📖</span> EDP3502 การช่วยเหลือและให้คำปรึกษาผู้เรียน
      </div>
      <h1>แบบทดสอบวัดผลการเรียนรู้และจำลองสถานการณ์</h1>
      <p>ครอบคลุมสาระสำคัญบทที่ 5 ถึง บทที่ 11: ลำดับขั้นตอนการให้คำปรึกษา, ทักษะสำคัญในการสื่อสาร, ทฤษฎีจิตวิเคราะห์ (Freud), ทฤษฎีแอดเลอร์ (Adler), ทฤษฎีตัวผู้เรียนเป็นศูนย์กลาง (Rogers) และทฤษฎีเกสตอลต์ (Gestalt)</p>
      
      <div class="meta-bar">
        <div class="meta-item"><span>📝</span> ทั้งหมด 35 ข้อ (ปรนัย 4 ตัวเลือก)</div>
        <div class="meta-item"><span>🎯</span> ตอนที่ 1: ความจำและหลักการสำคัญ (ข้อ 1 – 20)</div>
        <div class="meta-item"><span>🧩</span> ตอนที่ 2: เชิงสถานการณ์และการประยุกต์ใช้ (ข้อ 21 – 35)</div>
        <div class="meta-item"><span>⏱️</span> ระบบจับเวลา & เฉลยเชิงวิชาการละเอียดทุกข้อ</div>
      </div>
    </div>
  </header>

  <!-- Main Container -->
  <div class="app-container">
    
    <!-- Left Column: Questions List -->
    <main>
      <!-- Controls Card -->
      <div class="controls-card">
        <div class="tabs-group" id="tabsFilterGroup">
          <button class="tab-btn active" onclick="setFilter('all', this)">ทั้งหมด (35 ข้อ)</button>
          <button class="tab-btn" onclick="setFilter('part1', this)">ตอนที่ 1: หลักการ (1-20)</button>
          <button class="tab-btn" onclick="setFilter('part2', this)">ตอนที่ 2: สถานการณ์ (21-35)</button>
          <button class="tab-btn" id="tabFlaggedBtn" onclick="setFilter('flagged', this)" style="display: none;">🚩 ที่ปักหมุด (<span id="flaggedCountSpan">0</span>)</button>
          <button class="tab-btn tab-wrong" id="tabWrongBtn" onclick="setFilter('wrong', this)" style="display: none;">❌ ดูเฉพาะข้อที่ผิด (<span id="wrongCountSpan">0</span>)</button>
        </div>

        <div class="mode-switch-container" title="สลับโหมดการทดสอบ">
          <button class="mode-btn active" id="modePracticeBtn" onclick="setMode('practice')">💡 โหมดฝึกฝน (เฉลยทันที)</button>
          <button class="mode-btn" id="modeExamBtn" onclick="setMode('exam')">⏱️ โหมดสอบจริง</button>
        </div>
      </div>

      <!-- Question Cards -->
      <div class="questions-wrapper" id="questionsContainer">
        <!-- Injected via JavaScript -->
      </div>
    </main>

    <!-- Right Column: Sidebar -->
    <aside class="sticky-sidebar">
      <!-- Status & Progress -->
      <div class="sidebar-card">
        <div class="card-title">
          <span>📊 ความคืบหน้า</span>
          <span id="timerDisplay" style="font-family: 'Prompt', monospace; font-size: 1rem; color: var(--primary); font-weight: 600;">00:00</span>
        </div>
        
        <div class="stat-row">
          <span>ทำเสร็จแล้ว:</span>
          <strong id="answeredCountText">0 / 35 ข้อ</strong>
        </div>
        
        <div class="progress-bar-bg">
          <div class="progress-bar-fill" id="progressBar"></div>
        </div>

        <div id="liveScoreCard" style="background: #ecfdf5; border: 1px solid #a7f3d0; border-radius: 8px; padding: 10px; margin-bottom: 12px; text-align: center;">
          <div style="font-size: 0.85rem; color: #065f46; font-weight: 500;">คะแนนฝึกฝนขณะนี้</div>
          <div style="font-size: 1.45rem; font-family: 'Prompt'; font-weight: 700; color: #047857;" id="liveScoreText">0 / 0 (0%)</div>
        </div>

        <button class="btn btn-primary" id="submitExamBtn" onclick="submitExam()">
          <span>📤 ส่งคำตอบ / ตรวจคะแนน</span>
        </button>

        <button class="btn btn-outline" onclick="resetQuiz()">
          <span>🔄 รีเซ็ตทำใหม่</span>
        </button>

        <button class="btn btn-outline" onclick="window.print()" style="margin-top: 6px;">
          <span>🖨️ พิมพ์ข้อสอบ / บันทึก PDF</span>
        </button>
      </div>

      <!-- Navigator Grid -->
      <div class="sidebar-card">
        <div class="card-title">
          <span>📑 แผนผังข้อสอบ</span>
          <span style="font-size: 0.8rem; color: var(--text-muted);">คลิกเพื่อไปยังข้อนั้น</span>
        </div>
        <div class="q-grid" id="navigatorGrid">
          <!-- Injected via JavaScript (1 - 35) -->
        </div>

        <div style="margin-top: 14px; font-size: 0.78rem; color: var(--text-muted); display: flex; flex-direction: column; gap: 4px;">
          <div style="display: flex; align-items: center; gap: 6px;">
            <span style="width: 12px; height: 12px; background: #dbeafe; border-radius: 3px; display: inline-block;"></span>
            <span>ตอบแล้ว (สีฟ้า)</span>
          </div>
          <div style="display: flex; align-items: center; gap: 6px;">
            <span style="width: 12px; height: 12px; background: #d1fae5; border-radius: 3px; display: inline-block;"></span>
            <span>ถูกต้อง (สีเขียว)</span>
          </div>
          <div style="display: flex; align-items: center; gap: 6px;">
            <span style="width: 12px; height: 12px; background: #fee2e2; border-radius: 3px; display: inline-block;"></span>
            <span>ผิดพลาด (สีแดง)</span>
          </div>
          <div style="display: flex; align-items: center; gap: 6px;">
            <span style="width: 8px; height: 8px; background: var(--warning); border-radius: 50%; display: inline-block;"></span>
            <span>จุดสีส้ม = ปักหมุดไว้ทบทวน (🚩)</span>
          </div>
        </div>
      </div>
    </aside>

  </div>

  <!-- Score Summary Modal -->
  <div class="modal-overlay" id="scoreModal">
    <div class="modal-card">
      <div class="modal-icon" id="modalEmoji">🎉</div>
      <h2 id="modalTitle" style="font-size: 1.55rem; margin-bottom: 4px;">ผลการทดสอบของคุณ</h2>
      <p id="modalSubtitle" style="color: var(--text-muted); font-size: 0.95rem;">ตรวจประเมินผลคะแนนตามมาตรฐานวิชาชีพ</p>
      
      <div class="score-big" id="modalScore">32 / 35</div>
      <div class="score-percent" id="modalPercent">คิดเป็น 91.4% (ระดับ: ยอดเยี่ยมมาก!)</div>

      <div class="score-breakdown">
        <div class="breakdown-box">
          <h4>ตอนที่ 1 (หลักการ)</h4>
          <div class="val" id="scorePart1">18 / 20</div>
        </div>
        <div class="breakdown-box">
          <h4>ตอนที่ 2 (สถานการณ์)</h4>
          <div class="val" id="scorePart2">14 / 15</div>
        </div>
      </div>

      <div class="modal-actions">
        <button class="btn btn-primary" onclick="closeModalAndReview()">
          <span>🔍 ตรวจดูเฉลยละเอียดทุกข้อ</span>
        </button>
        <button class="btn btn-outline" id="reviewWrongModalBtn" onclick="closeModalAndFilterWrong()" style="color: #b91c1c; border-color: #fca5a5;">
          <span>❌ ดูเฉพาะข้อที่ตอบผิด</span>
        </button>
        <button class="btn btn-outline" onclick="resetQuiz(); closeModal();">
          <span>🔄 รีเซ็ตทำใหม่อีกรอบ</span>
        </button>
      </div>
    </div>
  </div>

  <script>
    // Quiz Dataset
    const questionsData = {questions_json_str};

    // Application State
    let userAnswers = {{}}; // id -> 'ก' | 'ข' | 'ค' | 'ง'
    let flaggedQuestions = new Set();
    let currentFilter = 'all'; // 'all' | 'part1' | 'part2' | 'flagged' | 'wrong'
    let currentMode = 'practice'; // 'practice' | 'exam'
    let isSubmitted = false;
    let timerSeconds = 0;
    let timerInterval = null;

    // Initialization
    window.addEventListener('DOMContentLoaded', () => {{
      renderQuestions();
      renderNavigator();
      updateStats();
      startTimer();
    }});

    // Timer functions
    function startTimer() {{
      if (timerInterval) clearInterval(timerInterval);
      timerInterval = setInterval(() => {{
        timerSeconds++;
        const mins = String(Math.floor(timerSeconds / 60)).padStart(2, '0');
        const secs = String(timerSeconds % 60).padStart(2, '0');
        document.getElementById('timerDisplay').textContent = `${{mins}}:${{secs}}`;
      }}, 1000);
    }}

    // Switch Testing Mode
    function setMode(mode) {{
      currentMode = mode;
      document.getElementById('modePracticeBtn').classList.toggle('active', mode === 'practice');
      document.getElementById('modeExamBtn').classList.toggle('active', mode === 'exam');

      const liveScoreCard = document.getElementById('liveScoreCard');
      if (mode === 'practice') {{
        liveScoreCard.style.display = 'block';
      }} else {{
        liveScoreCard.style.display = isSubmitted ? 'block' : 'none';
      }}

      renderQuestions();
      renderNavigator();
      updateStats();
    }}

    // Filter questions view
    function setFilter(filter, el) {{
      currentFilter = filter;
      document.querySelectorAll('.tab-btn').forEach(btn => btn.classList.remove('active'));
      if (el) el.classList.add('active');

      document.querySelectorAll('.question-card').forEach(card => {{
        const qid = parseInt(card.getAttribute('data-qid'));
        const part = card.getAttribute('data-part');
        const ans = userAnswers[qid];
        const q = questionsData.find(item => item.id === qid);
        const isWrong = ans !== undefined && ans !== q.answer;

        let visible = false;
        if (filter === 'all') {{
          visible = true;
        }} else if (filter === 'part1' && part === '1') {{
          visible = true;
        }} else if (filter === 'part2' && part === '2') {{
          visible = true;
        }} else if (filter === 'flagged' && flaggedQuestions.has(qid)) {{
          visible = true;
        }} else if (filter === 'wrong' && isWrong) {{
          visible = true;
        }}

        card.style.display = visible ? 'block' : 'none';
      }});
    }}

    // Toggle Flagging
    function toggleFlag(qid, e) {{
      if (e) e.stopPropagation();
      if (flaggedQuestions.has(qid)) {{
        flaggedQuestions.delete(qid);
      }} else {{
        flaggedQuestions.add(qid);
      }}

      // Update flag button in card
      const flagBtn = document.getElementById(`flag-btn-${{qid}}`);
      if (flagBtn) {{
        flagBtn.classList.toggle('flagged', flaggedQuestions.has(qid));
        flagBtn.title = flaggedQuestions.has(qid) ? 'ยกเลิกการปักหมุด' : 'ปักหมุดข้อนี้ไว้ทบทวน';
      }}

      // Update Tab count
      const tabFlaggedBtn = document.getElementById('tabFlaggedBtn');
      const count = flaggedQuestions.size;
      document.getElementById('flaggedCountSpan').textContent = count;
      tabFlaggedBtn.style.display = count > 0 ? 'inline-flex' : 'none';

      renderNavigator();
    }}

    // Render All Questions
    function renderQuestions() {{
      const container = document.getElementById('questionsContainer');
      container.innerHTML = '';

      questionsData.forEach(q => {{
        const card = document.createElement('div');
        card.className = 'question-card';
        card.id = `q-card-${{q.id}}`;
        card.setAttribute('data-part', q.part);
        card.setAttribute('data-qid', q.id);

        const isUserAnswered = userAnswers[q.id] !== undefined;
        const selectedChoice = userAnswers[q.id];
        const reveal = (currentMode === 'practice' && isUserAnswered) || isSubmitted;

        let choicesHtml = '';
        ['ก', 'ข', 'ค', 'ง'].forEach(key => {{
          const choiceText = q.choices[key] || '';
          let itemClass = 'choice-item';
          
          if (selectedChoice === key) {{
            itemClass += ' selected';
          }}

          if (reveal) {{
            if (key === q.answer) {{
              itemClass += ' is-correct';
            }} else if (selectedChoice === key && selectedChoice !== q.answer) {{
              itemClass += ' is-wrong';
            }}
          }}

          choicesHtml += `
            <div class="${{itemClass}}" onclick="selectChoice(${{q.id}}, '${{key}}')">
              <div class="choice-key">${{key}}</div>
              <div class="choice-text">${{choiceText}}</div>
            </div>
          `;
        }});

        // Explanation Box
        let expClass = 'explanation-box';
        if (reveal) expClass += ' show';

        const resultBadge = reveal ? (
          selectedChoice === q.answer 
            ? '<span style="color: #10b981; font-weight: 700;">✅ ตอบถูกต้อง</span>' 
            : '<span style="color: #ef4444; font-weight: 700;">❌ ตอบผิด (เฉลยที่ถูกต้องคือ ข้อ ' + q.answer + ')</span>'
        ) : '';

        const isFlagged = flaggedQuestions.has(q.id);

        card.innerHTML = `
          <div class="q-header">
            <div class="q-num-badge">${{q.id}}</div>
            <div class="q-title-wrap">
              <div class="q-meta-top">
                <span class="q-part-label">${{q.part_name}}</span>
                <button class="flag-btn ${{isFlagged ? 'flagged' : ''}}" id="flag-btn-${{q.id}}" onclick="toggleFlag(${{q.id}}, event)" title="${{isFlagged ? 'ยกเลิกการปักหมุด' : 'ปักหมุดข้อนี้ไว้ทบทวน'}}">🚩</button>
              </div>
              <div class="q-text">${{q.question}}</div>
            </div>
          </div>
          <div class="choices-list">
            ${{choicesHtml}}
          </div>
          <div class="${{expClass}}" id="exp-${{q.id}}">
            <div class="explanation-title">
              <span>💡 คำอธิบายเชิงวิชาการ</span>
              ${{resultBadge}}
            </div>
            <div>${{q.explanation}}</div>
          </div>
        `;

        container.appendChild(card);
      }});

      // Re-apply current filter
      if (currentFilter !== 'all') {{
        setFilter(currentFilter, document.querySelector(`.tab-btn[onclick*="${{currentFilter}}"]`));
      }}
    }}

    // Select Choice
    function selectChoice(qid, choiceKey) {{
      if (isSubmitted && currentMode === 'exam') return; // Locked in exam mode after submission
      
      userAnswers[qid] = choiceKey;
      renderSingleQuestion(qid);
      renderNavigator();
      updateStats();
    }}

    function renderSingleQuestion(qid) {{
      const card = document.getElementById(`q-card-${{qid}}`);
      if (!card) return;

      const q = questionsData.find(item => item.id === qid);
      if (!q) return;

      const selectedChoice = userAnswers[qid];
      const isUserAnswered = selectedChoice !== undefined;
      const reveal = (currentMode === 'practice' && isUserAnswered) || isSubmitted;

      const choicesList = card.querySelector('.choices-list');
      choicesList.innerHTML = '';

      ['ก', 'ข', 'ค', 'ง'].forEach(key => {{
        const choiceText = q.choices[key] || '';
        let itemClass = 'choice-item';
        
        if (selectedChoice === key) {{
          itemClass += ' selected';
        }}

        if (reveal) {{
          if (key === q.answer) {{
            itemClass += ' is-correct';
          }} else if (selectedChoice === key && selectedChoice !== q.answer) {{
            itemClass += ' is-wrong';
          }}
        }}

        const item = document.createElement('div');
        item.className = itemClass;
        item.onclick = () => selectChoice(qid, key);
        item.innerHTML = `
          <div class="choice-key">${{key}}</div>
          <div class="choice-text">${{choiceText}}</div>
        `;
        choicesList.appendChild(item);
      }});

      const expBox = card.querySelector('.explanation-box');
      if (reveal) {{
        expBox.classList.add('show');
        const resultBadge = selectedChoice === q.answer 
          ? '<span style="color: #10b981; font-weight: 700;">✅ ตอบถูกต้อง</span>' 
          : '<span style="color: #ef4444; font-weight: 700;">❌ ตอบผิด (เฉลยที่ถูกต้องคือ ข้อ ' + q.answer + ')</span>';
        expBox.querySelector('.explanation-title').innerHTML = `<span>💡 คำอธิบายเชิงวิชาการ</span>${{resultBadge}}`;
      }} else {{
        expBox.classList.remove('show');
      }}
    }}

    // Render Navigator Grid
    function renderNavigator() {{
      const grid = document.getElementById('navigatorGrid');
      grid.innerHTML = '';

      questionsData.forEach(q => {{
        const btn = document.createElement('button');
        btn.className = 'grid-btn';
        btn.textContent = q.id;
        btn.title = `ข้ามไปข้อ ${{q.id}}`;

        const ans = userAnswers[q.id];
        const isAnswered = ans !== undefined;
        const reveal = (currentMode === 'practice' && isAnswered) || isSubmitted;

        if (reveal) {{
          if (ans === q.answer) {{
            btn.classList.add('correct');
          }} else {{
            btn.classList.add('wrong');
          }}
        }} else if (isAnswered) {{
          btn.classList.add('answered');
        }}

        if (flaggedQuestions.has(q.id)) {{
          btn.classList.add('flagged');
        }}

        btn.onclick = () => scrollToQuestion(q.id);
        grid.appendChild(btn);
      }});
    }}

    // Scroll to question
    function scrollToQuestion(qid) {{
      const q = questionsData.find(item => item.id === qid);
      if (q) {{
        // Ensure visible if filtered out
        const card = document.getElementById(`q-card-${{qid}}`);
        if (card && card.style.display === 'none') {{
          setFilter('all', document.querySelectorAll('.tab-btn')[0]);
        }}
      }}

      const target = document.getElementById(`q-card-${{qid}}`);
      if (target) {{
        target.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
        target.style.transition = 'background 0.3s ease';
        target.style.backgroundColor = '#f0f9ff';
        setTimeout(() => {{
          target.style.backgroundColor = 'var(--card-bg)';
        }}, 800);
      }}
    }}

    // Update Progress and Stats
    function updateStats() {{
      const answeredTotal = Object.keys(userAnswers).length;
      const totalQuestions = questionsData.length;
      
      document.getElementById('answeredCountText').textContent = `${{answeredTotal}} / ${{totalQuestions}} ข้อ`;
      const pct = Math.round((answeredTotal / totalQuestions) * 100);
      document.getElementById('progressBar').style.width = `${{pct}}%`;

      let correctCount = 0;
      let wrongCount = 0;
      Object.entries(userAnswers).forEach(([qid, ans]) => {{
        const q = questionsData.find(item => item.id === parseInt(qid));
        if (q) {{
          if (q.answer === ans) correctCount++;
          else wrongCount++;
        }}
      }});

      const scoreRate = answeredTotal ? Math.round((correctCount / answeredTotal) * 100) : 0;
      document.getElementById('liveScoreText').textContent = `${{correctCount}} / ${{answeredTotal}} (ถูก ${{scoreRate}}%)`;

      // Update Wrong Tab
      const tabWrongBtn = document.getElementById('tabWrongBtn');
      document.getElementById('wrongCountSpan').textContent = wrongCount;
      if (isSubmitted || (currentMode === 'practice' && wrongCount > 0)) {{
        tabWrongBtn.style.display = wrongCount > 0 ? 'inline-flex' : 'none';
      }} else {{
        tabWrongBtn.style.display = 'none';
      }}
    }}

    // Submit Exam
    function submitExam() {{
      const answeredTotal = Object.keys(userAnswers).length;
      const totalQuestions = questionsData.length;

      if (!isSubmitted && answeredTotal < totalQuestions) {{
        const confirmSubmit = confirm(`คุณตอบไปแล้ว ${{answeredTotal}} จากทั้งหมด ${{totalQuestions}} ข้อ (ยังเหลือ ${{totalQuestions - answeredTotal}} ข้อ)\n\nต้องการส่งกระดาษคำตอบและตรวจผลคะแนนเลยหรือไม่?`);
        if (!confirmSubmit) return;
      }}

      isSubmitted = true;

      // Calculate score
      let scoreTotal = 0;
      let scorePart1 = 0;
      let scorePart2 = 0;

      questionsData.forEach(q => {{
        const userChoice = userAnswers[q.id];
        if (userChoice === q.answer) {{
          scoreTotal++;
          if (q.part === 1) scorePart1++;
          else scorePart2++;
        }}
      }});

      const percentage = Math.round((scoreTotal / totalQuestions) * 100);
      document.getElementById('modalScore').textContent = `${{scoreTotal}} / ${{totalQuestions}}`;
      
      let evalText = '';
      let emoji = '🎉';
      if (percentage >= 80) {{
        evalText = `คิดเป็น ${{percentage}}% (ระดับ: ยอดเยี่ยมมาก! 🌟 ความรู้แม่นยำ พร้อมสอบเก็บ A)`;
        emoji = '🏆';
      }} else if (percentage >= 70) {{
        evalText = `คิดเป็น ${{percentage}}% (ระดับ: ดีมาก 👍 เข้าใจสาระสำคัญและทฤษฎีส่วนใหญ่)`;
        emoji = '🎯';
      }} else if (percentage >= 50) {{
        evalText = `คิดเป็น ${{percentage}}% (ระดับ: ผ่านเกณฑ์ 💡 ควรทบทวนข้อที่พลาดเพื่อความแม่นยำ)`;
        emoji = '📚';
      }} else {{
        evalText = `คิดเป็น ${{percentage}}% (ระดับ: ควรทบทวนเนื้อหาเพิ่มเติม 🔄 ลองอ่านชีทสรุปแล้วกลับมาทำใหม่นะ)`;
        emoji = '💪';
      }}

      document.getElementById('modalEmoji').textContent = emoji;
      document.getElementById('modalPercent').textContent = evalText;
      document.getElementById('scorePart1').textContent = `${{scorePart1}} / 20 ข้อ`;
      document.getElementById('scorePart2').textContent = `${{scorePart2}} / 15 ข้อ`;

      const wrongTotal = totalQuestions - scoreTotal;
      const reviewWrongBtn = document.getElementById('reviewWrongModalBtn');
      if (wrongTotal > 0) {{
        reviewWrongBtn.style.display = 'inline-flex';
        reviewWrongBtn.querySelector('span').textContent = `❌ ดูเฉพาะข้อที่ตอบผิด (${{wrongTotal}} ข้อ)`;
      }} else {{
        reviewWrongBtn.style.display = 'none';
      }}

      document.getElementById('scoreModal').classList.add('active');

      renderQuestions();
      renderNavigator();
      updateStats();
    }}

    function closeModalAndReview() {{
      document.getElementById('scoreModal').classList.remove('active');
      setFilter('all', document.querySelectorAll('.tab-btn')[0]);
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function closeModalAndFilterWrong() {{
      document.getElementById('scoreModal').classList.remove('active');
      setFilter('wrong', document.getElementById('tabWrongBtn'));
      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    function closeModal() {{
      document.getElementById('scoreModal').classList.remove('active');
    }}

    // Reset Quiz
    function resetQuiz() {{
      if (confirm('คุณต้องการรีเซ็ตคำตอบทั้งหมดเพื่อเริ่มทำข้อสอบใหม่ใช่หรือไม่?')) {{
        userAnswers = {{}};
        flaggedQuestions.clear();
        isSubmitted = false;
        timerSeconds = 0;
        startTimer();
        setFilter('all', document.querySelectorAll('.tab-btn')[0]);
        renderQuestions();
        renderNavigator();
        updateStats();
        window.scrollTo({{ top: 0, behavior: 'smooth' }});
      }}
    }}
  </script>
</body>
</html>
"""

# Save to destination paths
target_dir = r"c:\Users\chinj\OneDrive\ปี3\EDP3502-ช่วยเหลือ\งาน"
target_file_1 = os.path.join(target_dir, "แบบทดสอบ_EDP3502_บทที่5-11.html")
target_file_root = r"c:\Users\chinj\OneDrive\ปี3\EDP3502-ช่วยเหลือ\แบบทดสอบ_EDP3502_บทที่5-11.html"

with open(target_file_1, "w", encoding="utf-8") as f:
    f.write(html_template)
print(f"Generated: {target_file_1} ({len(html_template)} chars)")

with open(target_file_root, "w", encoding="utf-8") as f:
    f.write(html_template)
print(f"Generated: {target_file_root} ({len(html_template)} chars)")
