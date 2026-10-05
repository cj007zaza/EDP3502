import os

html_code = """<!DOCTYPE html>
<html lang="th">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>ผังความคิดเชื่อมโยง EDP3502: การช่วยเหลือและให้คำปรึกษาผู้เรียน (บทที่ 5 - 11)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Prompt:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Sarabun:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
  <style>
    :root {
      --primary: #2563eb;
      --primary-dark: #1d4ed8;
      --primary-light: #eff6ff;
      --accent: #6366f1;
      --accent-light: #e0e7ff;
      --teal: #0d9488;
      --teal-light: #f0fdfa;
      --amber: #d97706;
      --amber-light: #fffbeb;
      --rose: #e11d48;
      --rose-light: #fff1f2;
      --emerald: #059669;
      --emerald-light: #ecfdf5;
      --purple: #7c3aed;
      --purple-light: #f5f3ff;
      --bg: #0f172a;
      --surface: #1e293b;
      --surface-card: #273549;
      --surface-hover: #334155;
      --border: #334155;
      --border-light: #475569;
      --text: #f8fafc;
      --text-muted: #94a3b8;
      --text-dim: #64748b;
      --shadow-sm: 0 1px 3px rgba(0,0,0,0.3);
      --shadow-md: 0 4px 6px -1px rgba(0,0,0,0.4);
      --shadow-lg: 0 10px 25px -5px rgba(0,0,0,0.5);
      --radius: 12px;
      --radius-sm: 8px;
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      font-family: 'Sarabun', -apple-system, BlinkMacSystemFont, sans-serif;
      background-color: var(--bg);
      color: var(--text);
      line-height: 1.6;
      font-size: 15px;
      overflow-x: hidden;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }

    h1, h2, h3, h4, .font-heading {
      font-family: 'Prompt', sans-serif;
      font-weight: 600;
    }

    /* Top Navigation Bar */
    header.navbar {
      background: rgba(30, 41, 59, 0.95);
      backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border);
      position: sticky;
      top: 0;
      z-index: 100;
      padding: 12px 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 16px;
    }

    .brand-wrap {
      display: flex;
      align-items: center;
      gap: 12px;
    }

    .brand-badge {
      background: linear-gradient(135deg, var(--primary), var(--accent));
      color: #fff;
      font-family: 'Prompt', sans-serif;
      font-weight: 700;
      font-size: 0.85rem;
      padding: 4px 10px;
      border-radius: 6px;
      box-shadow: 0 2px 8px rgba(37, 99, 235, 0.4);
    }

    .brand-title {
      font-size: 1.15rem;
      color: #fff;
    }
    .brand-title span {
      color: #93c5fd;
      font-size: 0.9rem;
      font-weight: 400;
      margin-left: 6px;
    }

    /* View Switcher Tabs */
    .view-tabs {
      display: flex;
      background: #0f172a;
      padding: 4px;
      border-radius: 10px;
      border: 1px solid var(--border);
      gap: 4px;
    }

    .tab-btn {
      font-family: 'Prompt', sans-serif;
      background: transparent;
      border: none;
      color: var(--text-muted);
      padding: 6px 14px;
      border-radius: 6px;
      font-size: 0.88rem;
      cursor: pointer;
      transition: all 0.2s ease;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .tab-btn:hover {
      color: #fff;
    }

    .tab-btn.active {
      background: var(--primary);
      color: #fff;
      font-weight: 600;
      box-shadow: 0 2px 6px rgba(37, 99, 235, 0.4);
    }

    /* Main Container */
    main.main-content {
      flex: 1;
      padding: 24px;
      max-width: 1400px;
      width: 100%;
      margin: 0 auto;
    }

    /* Subheader Guidance Banner */
    .guidance-banner {
      background: linear-gradient(135deg, rgba(30, 58, 138, 0.4) 0%, rgba(79, 70, 229, 0.25) 100%);
      border: 1px solid rgba(59, 130, 246, 0.3);
      border-radius: var(--radius);
      padding: 16px 20px;
      margin-bottom: 24px;
      display: flex;
      align-items: center;
      justify-content: space-between;
      flex-wrap: wrap;
      gap: 12px;
    }

    .guidance-text {
      font-size: 0.95rem;
      color: #cbd5e1;
    }
    .guidance-text strong {
      color: #60a5fa;
    }

    .meta-tags {
      display: flex;
      gap: 8px;
      flex-wrap: wrap;
    }
    .meta-tag {
      background: rgba(15, 23, 42, 0.6);
      border: 1px solid var(--border);
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.8rem;
      color: #94a3b8;
    }

    /* ========================================================
       VIEW 1: MIND MAP VIEW (Interactive Tree / Visual Graph)
       ======================================================== */
    .mindmap-container {
      display: flex;
      flex-direction: column;
      gap: 24px;
    }

    /* Central Hub Card */
    .central-hub {
      background: linear-gradient(135deg, #1e3a8a, #312e81);
      border: 2px solid #60a5fa;
      border-radius: 16px;
      padding: 24px 28px;
      box-shadow: 0 10px 25px rgba(37, 99, 235, 0.25);
      text-align: center;
      max-width: 820px;
      margin: 0 auto 12px;
      position: relative;
    }

    .central-hub h2 {
      font-size: 1.55rem;
      color: #fff;
      margin-bottom: 6px;
    }
    .central-hub p {
      color: #cbd5e1;
      font-size: 0.98rem;
    }

    .central-hub .hub-metaphor {
      display: inline-block;
      margin-top: 10px;
      background: rgba(0, 0, 0, 0.3);
      border: 1px dashed rgba(255, 255, 255, 0.3);
      padding: 6px 14px;
      border-radius: 9999px;
      font-size: 0.85rem;
      color: #fde047;
    }

    /* 4 Primary Pillars Grid */
    .pillars-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(310px, 1fr));
      gap: 20px;
      margin-top: 10px;
    }

    .pillar-card {
      background: var(--surface);
      border-radius: var(--radius);
      border: 1.5px solid var(--border);
      padding: 20px;
      display: flex;
      flex-direction: column;
      gap: 14px;
      transition: all 0.25s ease;
      position: relative;
    }

    .pillar-card:hover {
      transform: translateY(-3px);
      box-shadow: var(--shadow-lg);
      border-color: var(--border-light);
    }

    /* Card Header Colors */
    .pillar-card.c-blue { border-top: 5px solid #3b82f6; }
    .pillar-card.c-teal { border-top: 5px solid #14b8a6; }
    .pillar-card.c-amber { border-top: 5px solid #f59e0b; }
    .pillar-card.c-purple { border-top: 5px solid #a855f7; }

    .pillar-header {
      display: flex;
      align-items: flex-start;
      gap: 12px;
    }

    .pillar-icon {
      font-size: 1.8rem;
      flex-shrink: 0;
      width: 44px;
      height: 44px;
      background: rgba(255, 255, 255, 0.05);
      border-radius: 10px;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid var(--border);
    }

    .pillar-title-wrap {
      flex: 1;
    }

    .pillar-badge {
      font-size: 0.75rem;
      font-family: 'Prompt', sans-serif;
      text-transform: uppercase;
      font-weight: 700;
      letter-spacing: 0.05em;
      margin-bottom: 2px;
      display: inline-block;
    }
    .c-blue .pillar-badge { color: #60a5fa; }
    .c-teal .pillar-badge { color: #2dd4bf; }
    .c-amber .pillar-badge { color: #fbbf24; }
    .c-purple .pillar-badge { color: #c084fc; }

    .pillar-title {
      font-size: 1.18rem;
      color: #fff;
      line-height: 1.3;
    }

    .pillar-metaphor {
      font-size: 0.85rem;
      color: #94a3b8;
      background: rgba(0,0,0,0.25);
      padding: 4px 10px;
      border-radius: 6px;
      display: inline-flex;
      align-items: center;
      gap: 6px;
    }

    .pillar-essence {
      font-size: 0.92rem;
      color: #cbd5e1;
      background: rgba(255,255,255,0.03);
      padding: 10px 12px;
      border-radius: 8px;
      border-left: 3px solid var(--border-light);
    }
    .pillar-essence strong {
      color: #f1f5f9;
    }

    /* Sub-branches List */
    .branch-list {
      display: flex;
      flex-direction: column;
      gap: 10px;
      flex: 1;
    }

    .branch-item {
      background: var(--surface-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 12px 14px;
      cursor: pointer;
      transition: all 0.2s ease;
      display: flex;
      flex-direction: column;
      gap: 4px;
    }

    .branch-item:hover {
      background: var(--surface-hover);
      border-color: #64748b;
      transform: translateX(4px);
    }

    .branch-item-head {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .branch-item-title {
      font-family: 'Prompt', sans-serif;
      font-size: 0.92rem;
      font-weight: 600;
      color: #f8fafc;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .branch-item-desc {
      font-size: 0.82rem;
      color: #94a3b8;
      line-height: 1.4;
    }

    .branch-click-hint {
      font-size: 0.72rem;
      color: #60a5fa;
      opacity: 0.8;
      margin-top: 4px;
      display: flex;
      align-items: center;
      gap: 4px;
    }

    /* Connection footer */
    .pillar-connection {
      margin-top: auto;
      padding-top: 10px;
      border-top: 1px solid var(--border);
      font-size: 0.8rem;
      color: #94a3b8;
      display: flex;
      align-items: center;
      gap: 6px;
    }
    .pillar-connection strong {
      color: #38bdf8;
    }

    /* ========================================================
       VIEW 2: WORKFLOW & CASE SIMULATION (Step-by-Step Flow)
       ======================================================== */
    .workflow-container {
      display: flex;
      flex-direction: column;
      gap: 24px;
      display: none;
    }

    .case-banner {
      background: linear-gradient(135deg, rgba(13, 148, 136, 0.2), rgba(15, 23, 42, 0.8));
      border: 1px solid #14b8a6;
      border-radius: var(--radius);
      padding: 18px 24px;
      display: flex;
      align-items: center;
      gap: 16px;
    }

    .case-banner .case-avatar {
      font-size: 2.4rem;
      width: 56px;
      height: 56px;
      background: rgba(20, 184, 166, 0.15);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      border: 1px solid #14b8a6;
      flex-shrink: 0;
    }

    .case-banner h3 {
      font-size: 1.15rem;
      color: #5eead4;
      margin-bottom: 4px;
    }
    .case-banner p {
      font-size: 0.92rem;
      color: #cbd5e1;
    }

    .workflow-timeline {
      position: relative;
      padding-left: 36px;
      display: flex;
      flex-direction: column;
      gap: 24px;
    }

    .workflow-timeline::before {
      content: "";
      position: absolute;
      left: 14px;
      top: 10px;
      bottom: 10px;
      width: 3px;
      background: linear-gradient(180deg, #3b82f6, #10b981, #a855f7, #64748b);
      border-radius: 9999px;
    }

    .timeline-step {
      position: relative;
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 20px 24px;
      transition: all 0.2s;
    }

    .timeline-step:hover {
      border-color: var(--border-light);
      box-shadow: var(--shadow-md);
    }

    .timeline-marker {
      position: absolute;
      left: -38px;
      top: 20px;
      width: 28px;
      height: 28px;
      background: #0f172a;
      border: 3px solid #3b82f6;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 0.75rem;
      font-weight: 700;
      color: #fff;
    }

    .step-header {
      display: flex;
      justify-content: space-between;
      align-items: center;
      flex-wrap: wrap;
      gap: 8px;
      margin-bottom: 12px;
    }

    .step-title {
      font-size: 1.1rem;
      color: #fff;
      display: flex;
      align-items: center;
      gap: 8px;
    }

    .step-badge {
      font-size: 0.75rem;
      padding: 3px 10px;
      border-radius: 9999px;
      background: rgba(59, 130, 246, 0.15);
      color: #93c5fd;
      border: 1px solid rgba(59, 130, 246, 0.3);
      font-family: 'Prompt', sans-serif;
    }

    .step-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
      gap: 14px;
      margin-top: 12px;
    }

    .step-subcard {
      background: var(--surface-card);
      border: 1px solid var(--border);
      border-radius: var(--radius-sm);
      padding: 14px;
    }

    .step-subcard h5 {
      font-size: 0.85rem;
      color: #38bdf8;
      margin-bottom: 6px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .step-subcard p {
      font-size: 0.88rem;
      color: #cbd5e1;
      line-height: 1.5;
    }

    /* ========================================================
       VIEW 3: VISUAL GLOSSARY (Flashcards & Mental Models)
       ======================================================== */
    .glossary-container {
      display: flex;
      flex-direction: column;
      gap: 20px;
      display: none;
    }

    .glossary-search-bar {
      display: flex;
      gap: 12px;
      background: var(--surface);
      border: 1px solid var(--border);
      padding: 10px 16px;
      border-radius: var(--radius);
      align-items: center;
    }

    .glossary-search-bar input {
      background: transparent;
      border: none;
      outline: none;
      color: #fff;
      font-size: 0.95rem;
      font-family: 'Sarabun', sans-serif;
      width: 100%;
    }
    .glossary-search-bar input::placeholder {
      color: var(--text-dim);
    }

    .glossary-grid {
      display: grid;
      grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
      gap: 18px;
    }

    .glossary-card {
      background: var(--surface);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 18px 20px;
      display: flex;
      flex-direction: column;
      gap: 12px;
      transition: all 0.2s;
    }

    .glossary-card:hover {
      border-color: #64748b;
      transform: translateY(-2px);
      box-shadow: var(--shadow-md);
    }

    .g-header {
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 10px;
    }

    .g-term {
      font-size: 1.05rem;
      color: #fff;
      font-family: 'Prompt', sans-serif;
    }

    .g-chapter-tag {
      font-size: 0.72rem;
      padding: 2px 8px;
      border-radius: 4px;
      background: rgba(255,255,255,0.06);
      color: #94a3b8;
      border: 1px solid var(--border);
      white-space: nowrap;
    }

    .g-human-lang {
      background: rgba(37, 99, 235, 0.12);
      border-left: 3px solid #3b82f6;
      padding: 8px 12px;
      border-radius: 0 6px 6px 0;
      font-size: 0.9rem;
      color: #bfdbfe;
    }

    .g-metaphor-box {
      background: rgba(245, 158, 11, 0.1);
      border: 1px dashed rgba(245, 158, 11, 0.35);
      padding: 10px 12px;
      border-radius: 8px;
    }

    .g-metaphor-title {
      font-size: 0.78rem;
      color: #fbbf24;
      font-weight: 600;
      margin-bottom: 4px;
      display: flex;
      align-items: center;
      gap: 4px;
    }

    .g-metaphor-desc {
      font-size: 0.88rem;
      color: #fde68a;
      line-height: 1.45;
    }

    .g-example {
      font-size: 0.85rem;
      color: #94a3b8;
      margin-top: auto;
      padding-top: 8px;
      border-top: 1px solid var(--border);
    }
    .g-example strong {
      color: #cbd5e1;
    }

    /* ========================================================
       MODAL / DETAIL DRAWER (Click-to-Inspect Concept)
       ======================================================== */
    .drawer-overlay {
      position: fixed;
      inset: 0;
      background: rgba(15, 23, 42, 0.75);
      backdrop-filter: blur(6px);
      z-index: 200;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 20px;
    }

    .drawer-overlay.active {
      display: flex;
    }

    .drawer-card {
      background: #1e293b;
      border: 1px solid #475569;
      border-radius: 16px;
      max-width: 680px;
      width: 100%;
      max-height: 85vh;
      overflow-y: auto;
      padding: 28px;
      box-shadow: 0 20px 30px rgba(0,0,0,0.6);
      display: flex;
      flex-direction: column;
      gap: 18px;
      position: relative;
      animation: modalFadeIn 0.2s ease;
    }

    @keyframes modalFadeIn {
      from { opacity: 0; transform: scale(0.96); }
      to { opacity: 1; transform: scale(1); }
    }

    .drawer-close-btn {
      position: absolute;
      top: 20px;
      right: 20px;
      background: rgba(255, 255, 255, 0.08);
      border: none;
      color: #cbd5e1;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      cursor: pointer;
      font-size: 1.2rem;
      transition: all 0.15s;
    }
    .drawer-close-btn:hover {
      background: rgba(255, 255, 255, 0.2);
      color: #fff;
    }

    .drawer-badge {
      display: inline-block;
      font-size: 0.78rem;
      padding: 3px 10px;
      border-radius: 6px;
      background: rgba(37, 99, 235, 0.2);
      color: #93c5fd;
      border: 1px solid rgba(37, 99, 235, 0.4);
      width: fit-content;
    }

    .drawer-title {
      font-size: 1.45rem;
      color: #fff;
      margin-top: 4px;
    }

    .drawer-block {
      background: #0f172a;
      border: 1px solid var(--border);
      border-radius: 10px;
      padding: 16px;
    }

    .drawer-block h4 {
      font-size: 0.9rem;
      color: #38bdf8;
      margin-bottom: 8px;
      display: flex;
      align-items: center;
      gap: 6px;
    }

    .drawer-block p {
      font-size: 0.92rem;
      color: #cbd5e1;
      line-height: 1.6;
    }

    .drawer-connections {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 4px;
    }

    .drawer-conn-tag {
      background: #334155;
      padding: 4px 10px;
      border-radius: 6px;
      font-size: 0.8rem;
      color: #e2e8f0;
      border: 1px solid #475569;
    }

    /* Footer */
    footer.app-footer {
      background: #0b1120;
      border-top: 1px solid var(--border);
      padding: 20px;
      text-align: center;
      font-size: 0.85rem;
      color: var(--text-dim);
      margin-top: auto;
    }

    @media print {
      header.navbar, .view-tabs, .drawer-overlay {
        display: none !important;
      }
      body {
        background: #fff !important;
        color: #000 !important;
      }
      .central-hub, .pillar-card, .timeline-step, .glossary-card {
        background: #fff !important;
        border: 1px solid #ccc !important;
        color: #000 !important;
        box-shadow: none !important;
      }
      h1, h2, h3, h4, p, span {
        color: #000 !important;
      }
    }
  </style>
</head>
<body>

  <!-- Top Sticky Navigation -->
  <header class="navbar">
    <div class="brand-wrap">
      <div class="brand-badge">EDP3502</div>
      <div class="brand-title">
        ผังความคิดและระบบเชื่อมโยง <span>บทที่ 5 – 11</span>
      </div>
    </div>

    <!-- View Switcher -->
    <div class="view-tabs">
      <button class="tab-btn active" id="tabMindmap" onclick="switchView('mindmap')">
        <span>🌳 ผังมโนทัศน์ (Mind Map)</span>
      </button>
      <button class="tab-btn" id="tabWorkflow" onclick="switchView('workflow')">
        <span>🔄 ผังกระบวนการตามเคสจริง</span>
      </button>
      <button class="tab-btn" id="tabGlossary" onclick="switchView('glossary')">
        <span>💡 การ์ดภาพจำศัพท์เฉพาะ</span>
      </button>
    </div>
  </header>

  <!-- Main Content Area -->
  <main class="main-content">
    
    <!-- Guidance Banner -->
    <div class="guidance-banner">
      <div class="guidance-text">
        💡 <strong>หลักคิดสำคัญ:</strong> อย่าจำแบบแยกบท! ให้มองว่า <strong>บทที่ 5</strong> คือแผนที่ <strong>บทที่ 6</strong> คือเครื่องมือช่าง <strong>บทที่ 7</strong> คือระบบป้องกันภัยของเด็ก และ <strong>บทที่ 8–11</strong> คือแว่น 4 อันในการวินิจฉัยและรักษา
      </div>
      <div class="meta-tags">
        <span class="meta-tag">🗺️ 4 ขั้นตอน</span>
        <span class="meta-tag">🛠️ 7+ ทักษะ</span>
        <span class="meta-tag">🛡️ 6 กลไกทางจิต</span>
        <span class="meta-tag">👓 4 ทฤษฎีใหญ่</span>
      </div>
    </div>

    <!-- ========================================================
         VIEW 1: MIND MAP VIEW (Interactive Pillars)
         ======================================================== -->
    <div class="mindmap-container" id="viewMindmap">
      
      <!-- Central Hub -->
      <div class="central-hub">
        <h2>กระบวนการช่วยเหลือและให้คำปรึกษาผู้เรียน</h2>
        <p>การผสมผสานระหว่าง "ศาสตร์แห่งการวินิจฉัยจิตใจ" และ "ศิลปะแห่งการรับฟังเพื่อเยียวยา"</p>
        <div class="hub-metaphor">
          🚗 ภาพจำเปรียบเทียบ: <strong>"คลินิก / อู่ซ่อมรถยนต์จิตใจ"</strong> ซ่อมจากภายนอกลึกสู่ภายใน
        </div>
      </div>

      <!-- 4 Core Pillars Grid -->
      <div class="pillars-grid">

        <!-- Pillar 1: Blue (Chapter 5) -->
        <div class="pillar-card c-blue">
          <div class="pillar-header">
            <div class="pillar-icon">🗺️</div>
            <div class="pillar-title-wrap">
              <span class="pillar-badge">บทที่ 5</span>
              <h3 class="pillar-title">ขั้นตอนการให้คำปรึกษา</h3>
            </div>
          </div>

          <div class="pillar-metaphor">
            📍 <strong>เปรียบเหมือน:</strong> "แผนที่เดินทาง 4 สถานี"
          </div>

          <div class="pillar-essence">
            <strong>ประเด็นหลักจริงๆ:</strong> การคุยไม่ใช่การนั่งคุยเรื่อยเปื่อย แต่ต้องเดินตามลำดับ 4 ขั้นตอน ไม่ข้ามขั้น
          </div>

          <div class="branch-list">
            <div class="branch-item" onclick="openDetail('c5_1')">
              <div class="branch-item-head">
                <span class="branch-item-title">1. เริ่มต้น & สร้างสัมพันธภาพ</span>
                <span>➔</span>
              </div>
              <p class="branch-item-desc">ทลายกำแพงความระแวง สร้างพื้นที่ปลอดภัย</p>
              <span class="branch-click-hint">คลิกดูรายละเอียด & สิ่งที่ต้องทำ</span>
            </div>

            <div class="branch-item" onclick="openDetail('c5_2')">
              <div class="branch-item-head">
                <span class="branch-item-title">2. สำรวจปัญหา & เข้าใจตนเอง</span>
                <span>➔</span>
              </div>
              <p class="branch-item-desc">ระบายอารมณ์ (Catharsis) + ขุดหาสาเหตุที่แท้จริง</p>
              <span class="branch-click-hint">คลิกดูรายละเอียด & ข้อพึงระวัง</span>
            </div>

            <div class="branch-item" onclick="openDetail('c5_3')">
              <div class="branch-item-head">
                <span class="branch-item-title">3. จัดการกับปัญหา (Working Through)</span>
                <span>➔</span>
              </div>
              <p class="branch-item-desc">เปลี่ยนความเข้าใจ (Insight) ให้กลายเป็นพฤติกรรมใหม่</p>
              <span class="branch-click-hint">คลิกดูจุดที่นำทฤษฎีมาลงมือแก้</span>
            </div>

            <div class="branch-item" onclick="openDetail('c5_4')">
              <div class="branch-item-head">
                <span class="branch-item-title">4. ยุติการปรึกษา (Termination)</span>
                <span>➔</span>
              </div>
              <p class="branch-item-desc">สรุปผล ปล่อยให้พึ่งพาตนเอง และนัดติดตามผล</p>
              <span class="branch-click-hint">คลิกดูข้อควรระวังเรื่องการติดพึ่งพา</span>
            </div>
          </div>

          <div class="pillar-connection">
            🔗 <strong>นำไปทำอะไร:</strong> เป็นกระดูกสันหลังคุมเวลาและทิศทางบทสนทนา
          </div>
        </div>

        <!-- Pillar 2: Teal (Chapter 6) -->
        <div class="pillar-card c-teal">
          <div class="pillar-header">
            <div class="pillar-icon">🛠️</div>
            <div class="pillar-title-wrap">
              <span class="pillar-badge">บทที่ 6</span>
              <h3 class="pillar-title">ทักษะการให้คำปรึกษา</h3>
            </div>
          </div>

          <div class="pillar-metaphor">
            🧰 <strong>เปรียบเหมือน:</strong> "กล่องเครื่องมือช่างในมือครู"
          </div>

          <div class="pillar-essence">
            <strong>ประเด็นหลักจริงๆ:</strong> ฟังให้ได้ยินสิ่งที่ไม่ได้พูด สะท้อนอารมณ์เหมือนกระจกเงา และท้าทายความย้อนแย้ง
          </div>

          <div class="branch-list">
            <div class="branch-item" onclick="openDetail('c6_1')">
              <div class="branch-item-head">
                <span class="branch-item-title">การใส่ใจ & ท่าทาง (SOLER)</span>
                <span>➔</span>
              </div>
              <p class="branch-item-desc">นั่งเผชิญหน้า เปิดท่าที โน้มตัว สบตา และผ่อนคลาย</p>
            </div>

            <div class="branch-item" onclick="openDetail('c6_2')">
              <div class="branch-item-head">
                <span class="branch-item-title">การฟัง 3 มิติ (Verbal)</span>
                <span>➔</span>
              </div>
              <p class="branch-item-desc">ฟังครบ 3 ด้าน: 1. พฤติกรรม 2. ความคิด 3. อารมณ์ความรู้สึก</p>
            </div>

            <div class="branch-item" onclick="openDetail('c6_3')">
              <div class="branch-item-head">
                <span class="branch-item-title">การสะท้อนความรู้สึก</span>
                <span>➔</span>
              </div>
              <p class="branch-item-desc">สูตร: "เธอรู้สึก [อารมณ์] เพราะ [สาเหตุ]" (ห้ามสั่งสอน)</p>
            </div>

            <div class="branch-item" onclick="openDetail('c6_4')">
              <div class="branch-item-head">
                <span class="branch-item-title">การท้าทาย (Challenging) & เงียบ</span>
                <span>➔</span>
              </div>
              <p class="branch-item-desc">ชี้ให้เห็นช่องว่างคำพูดกับการกระทำ + อดทนต่อความเงียบ</p>
            </div>
          </div>

          <div class="pillar-connection">
            🔗 <strong>เชื่อมกับ:</strong> หยิบไปใช้ตลอดขั้นตอนที่ 1, 2, และ 3 ของบทที่ 5
          </div>
        </div>

        <!-- Pillar 3: Amber (Chapter 7) -->
        <div class="pillar-card c-amber">
          <div class="pillar-header">
            <div class="pillar-icon">🛡️</div>
            <div class="pillar-title-wrap">
              <span class="pillar-badge">บทที่ 7</span>
              <h3 class="pillar-title">กลไกจิตใจ & การป้องกันตัว</h3>
            </div>
          </div>

          <div class="pillar-metaphor">
            🦺 <strong>เปรียบเหมือน:</strong> "ระบบ Safe Mode / ถุงลมนิรภัย"
          </div>

          <div class="pillar-essence">
            <strong>ประเด็นหลักจริงๆ:</strong> เมื่อจิตใจเจ็บปวด มนุษย์จะบิดเบือนความจริงอัตโนมัติ เพื่อปกป้องอีโก้ไม่ให้พังทลาย
          </div>

          <div class="branch-list">
            <div class="branch-item" onclick="openDetail('c7_1')">
              <div class="branch-item-head">
                <span class="branch-item-title">Repression (การกดเก็บ)</span>
                <span>➔</span>
              </div>
              <p class="branch-item-desc">กลไกแม่บท: กวาดขยะแผลใจลงใต้พรมจิตไร้สำนึก</p>
            </div>

            <div class="branch-item" onclick="openDetail('c7_2')">
              <div class="branch-item-head">
                <span class="branch-item-title">Projection (การฉายภาพ / โยนบาป)</span>
                <span>➔</span>
              </div>
              <p class="branch-item-desc">ตัวเองมีข้อเสียนั้น แต่ชี้นิ้วด่าว่าคนอื่นเป็นแทน</p>
            </div>

            <div class="branch-item" onclick="openDetail('c7_3')">
              <div class="branch-item-head">
                <span class="branch-item-title">Reaction Formation (กลับขั้ว)</span>
                <span>➔</span>
              </div>
              <p class="branch-item-desc">เกลียดมากแต่แสดงออกด้วยการกอดยิ้มหวานเอาใจสุดโต่ง</p>
            </div>

            <div class="branch-item" onclick="openDetail('c7_4')">
              <div class="branch-item-head">
                <span class="branch-item-title">Displacement (การเปลี่ยนที่ / เตะหมา)</span>
                <span>➔</span>
              </div>
              <p class="branch-item-desc">โกรธคนมีอำนาจแต่ไม่กล้าสู้ เลยไประบายใส่คนที่อ่อนแอกว่า</p>
            </div>
          </div>

          <div class="pillar-connection">
            🔗 <strong>นำไปทำอะไร:</strong> ช่วยให้ครูอ่านอาการออก ไม่โกรธเด็กเมื่อถูกพาลใส่
          </div>
        </div>

        <!-- Pillar 4: Purple (Chapters 8 - 11) -->
        <div class="pillar-card c-purple">
          <div class="pillar-header">
            <div class="pillar-icon">👓</div>
            <div class="pillar-title-wrap">
              <span class="pillar-badge">บทที่ 8 – 11</span>
              <h3 class="pillar-title">4 แว่นตาทฤษฎีในการรักษา</h3>
            </div>
          </div>

          <div class="pillar-metaphor">
            🔬 <strong>เปรียบเหมือน:</strong> "หมอเฉพาะทาง 4 สไตล์"
          </div>

          <div class="pillar-essence">
            <strong>ประเด็นหลักจริงๆ:</strong> เลือกมุมมองในการวินิจฉัยปัญหาของเด็กว่าเกิดจาก อดีต, สังคม, การไม่ยอมรับตน, หรือการค้างคา
          </div>

          <div class="branch-list">
            <div class="branch-item" onclick="openDetail('c8')">
              <div class="branch-item-head">
                <span class="branch-item-title">1. Freud: นักโบราณคดี (ขุดอดีต)</span>
                <span>➔</span>
              </div>
              <p class="branch-item-desc">Id-Ego-Superego, แผลวัยเด็ก, จิตไร้สำนึก, Transference</p>
            </div>

            <div class="branch-item" onclick="openDetail('c9')">
              <div class="branch-item-head">
                <span class="branch-item-title">2. Adler: โค้ชสังคม (แก้ปมด้อย)</span>
                <span>➔</span>
              </div>
              <p class="branch-item-desc">ปมด้อยสู่ปมเด่น, เป้าหมายผิด 4 ขั้น, ลำดับการเกิด, The Question</p>
            </div>

            <div class="branch-item" onclick="openDetail('c10')">
              <div class="branch-item-head">
                <span class="branch-item-title">3. Rogers: คนทำสวน (เมตตา-ไม่ชี้นำ)</span>
                <span>➔</span>
              </div>
              <p class="branch-item-desc">Real vs Ideal Self, ศักยภาพมนุษย์, 3 สภาวะ (จริงใจ-ยอมรับ-เข้าใจ)</p>
            </div>

            <div class="branch-item" onclick="openDetail('c11')">
              <div class="branch-item-head">
                <span class="branch-item-title">4. Gestalt: นักแสดงดึงสติ (ปัจจุบัน)</span>
                <span>➔</span>
              </div>
              <p class="branch-item-desc">Here & Now, Unfinished Business, เทคนิคเก้าอี้ว่าง (Empty Chair)</p>
            </div>
          </div>

          <div class="pillar-connection">
            🔗 <strong>เชื่อมกับ:</strong> เลือกหยิบมาใช้ในบทที่ 5 ขั้นที่ 2 (เข้าใจ) และขั้นที่ 3 (แก้ไข)
          </div>
        </div>

      </div>

    </div>

    <!-- ========================================================
         VIEW 2: WORKFLOW & CASE SIMULATION VIEW
         ======================================================== -->
    <div class="workflow-container" id="viewWorkflow">
      
      <!-- Case Banner -->
      <div class="case-banner">
        <div class="case-avatar">👦</div>
        <div>
          <h3>กรณีศึกษาจำลอง: "น้องน็อต ม.4 ผู้เงียบขรึม ไม่ส่งงาน และชอบพาลใส่ครู"</h3>
          <p>ดูการร้อยเรียงเนื้อหาทั้ง 7 บท (บทที่ 5–11) ผ่านสถานการณ์จริง ตั้งแต่ก้าวแรกจนจบเคส</p>
        </div>
      </div>

      <!-- Timeline -->
      <div class="workflow-timeline">

        <!-- Step 1 -->
        <div class="timeline-step">
          <div class="timeline-marker">1</div>
          <div class="step-header">
            <div class="step-title">
              <span>🚪 สถานีที่ 1: ต้อนรับและเปิดใจ (สร้างสัมพันธภาพ)</span>
            </div>
            <span class="step-badge">บทที่ 5 (ขั้น 1) + บทที่ 6 (ทักษะ) + บทที่ 10 (Rogers)</span>
          </div>
          <p style="color: #cbd5e1; font-size: 0.95rem;">
            น้องน็อตเดินเข้ามาด้วยสีหน้าบึ้งตึง กอดอก ไม่ยอมสบตา
          </p>
          <div class="step-grid">
            <div class="step-subcard">
              <h5>🛠️ สิ่งที่ครูลงมือทำ (บทที่ 6)</h5>
              <p>ใช้ท่าทาง <strong>SOLER</strong>: นั่งเอียง 45 องศา โน้มตัวไปข้างหน้า ไม่กอดอก สบตาเป็นมิตร ชวนคุยเรื่องทั่วไป ไม่เปิดประเด็นด่าเรื่องไม่ส่งงาน</p>
            </div>
            <div class="step-subcard">
              <h5>🌱 ทัศนคติของครู (บทที่ 10 Rogers)</h5>
              <p>ให้ <strong>Unconditional Positive Regard</strong>: สื่อสารให้เด็กสัมผัสได้ว่า แม้เขาจะทำผิดมา ที่นี่คือพื้นที่ปลอดภัย ครูไม่ตัดสินและพร้อมรับฟัง</p>
            </div>
          </div>
        </div>

        <!-- Step 2 -->
        <div class="timeline-step">
          <div class="timeline-marker">2</div>
          <div class="step-header">
            <div class="step-title">
              <span>🔍 สถานีที่ 2: สำรวจปัญหา & จับไต๋ระบบป้องกันตัว</span>
            </div>
            <span class="step-badge">บทที่ 5 (ขั้น 2) + บทที่ 6 (ฟัง/สะท้อน) + บทที่ 7 (กลไกจิต)</span>
          </div>
          <p style="color: #cbd5e1; font-size: 0.95rem;">
            น็อตเริ่มระบายอารมณ์เสียงดัง: <em>"ครูประจำวิชาเขาจงใจแกล้งผม สั่งการบ้านยากๆ ให้ผมทำไม่ได้ เขาเกลียดผม!"</em>
          </p>
          <div class="step-grid">
            <div class="step-subcard">
              <h5>🛡️ วิเคราะห์กลไกทางจิต (บทที่ 7)</h5>
              <p>น็อตกำลังใช้ <strong>Projection (การโยนบาป)</strong> เพราะจิตใจยอมรับไม่ได้ว่าตัวเองขี้เกียจ จึงโทษว่าครูเป็นฝ่ายเกลียดตนเอง</p>
            </div>
            <div class="step-subcard">
              <h5>🛠️ ครูสะท้อนความรู้สึก (บทที่ 6)</h5>
              <p><em>"น็อตรู้สึกอึดอัดและน้อยใจใช่ไหม ที่รู้สึกเหมือนพยายามทำแล้วแต่ครูไม่เข้าใจ"</em> (น็อตเริ่มน้ำตาซึมและคลายเกราะกำบังลง)</p>
            </div>
          </div>
        </div>

        <!-- Step 3 -->
        <div class="timeline-step">
          <div class="timeline-marker">3</div>
          <div class="step-header">
            <div class="step-title">
              <span>🔬 สถานีที่ 3: สวมแว่นตาวินิจฉัยและลงมือรักษา (Working Through)</span>
            </div>
            <span class="step-badge">บทที่ 5 (ขั้น 3) + บทที่ 8, 9, 10, 11 (เลือกแว่นทฤษฎี)</span>
          </div>
          <p style="color: #cbd5e1; font-size: 0.95rem;">
            เมื่อขุดลึกลงไป ครูสามารถเลือกใช้มุมมองทฤษฎีต่างๆ มาอธิบายและบำบัด ดังนี้:
          </p>
          <div class="step-grid">
            <div class="step-subcard">
              <h5>🏺 มุมมอง Freud (บทที่ 8)</h5>
              <p>พบว่าในวัยเด็ก พ่อชอบตีและด่าว่า <em>"ไอ้เด็กโง่"</em> น็อตจึงเกิด <strong>Transference (ถ่ายโยงอารมณ์)</strong> เอาความโกรธพ่อมาพาลใส่ครูผู้ชายทุกคนในโรงเรียน</p>
            </div>
            <div class="step-subcard">
              <h5>🎯 มุมมอง Adler (บทที่ 9)</h5>
              <p>มองว่าน็อตมี <strong>ปมด้อย (Inferiority)</strong> จากการเรียนไม่ทันเพื่อน จึงมีเป้าหมายผิดขั้นที่ 1 คือ <strong>เรียกร้องความสนใจ</strong> ด้วยการทำตัวเกเรเพื่อชดเชย</p>
            </div>
            <div class="step-subcard">
              <h5>🌱 มุมมอง Rogers (บทที่ 10)</h5>
              <p>เกิด <strong>Incongruence</strong> ระหว่าง Real Self (เด็กที่เรียนไม่ทัน) กับ Ideal Self (อยากเป็นลูกที่พ่อภูมิใจ) จึงเกิดความทุกข์ ครูช่วยให้เขายอมรับตนเอง</p>
            </div>
            <div class="step-subcard">
              <h5>⚡ ลงมือรักษาด้วย Gestalt (บทที่ 11)</h5>
              <p>จัด <strong>เทคนิคเก้าอี้ว่าง (Empty Chair)</strong> สมมุติให้พ่อนั่งอยู่ แล้วให้น็อตพูดระบายความอัดอั้นในอดีตออกมาในปัจจุบัน (Here & Now) เพื่อสะสาง <strong>Unfinished Business</strong></p>
            </div>
          </div>
        </div>

        <!-- Step 4 -->
        <div class="timeline-step">
          <div class="timeline-marker">4</div>
          <div class="step-header">
            <div class="step-title">
              <span>🏁 สถานีที่ 4: สรุปบทเรียน วางแผน และส่งกลับ (ยุติการปรึกษา)</span>
            </div>
            <span class="step-badge">บทที่ 5 (ขั้น 4) + ประเมินผล</span>
          </div>
          <p style="color: #cbd5e1; font-size: 0.95rem;">
            น็อตเกิดความเข้าใจตนเองอย่างลึกซึ้ง (Insight) ว่าพฤติกรรมเกเรของตนไม่ได้ช่วยแก้ปัญหา
          </p>
          <div class="step-grid">
            <div class="step-subcard">
              <h5>📝 วางแผนพฤติกรรมรูปธรรม</h5>
              <p>ร่วมกันตั้งเป้าหมาย: ขอส่งการบ้านวันละ 1 วิชา และขอคำปรึกษาครูผู้สอนเมื่อทำไม่ได้</p>
            </div>
            <div class="step-subcard">
              <h5>🤝 จากลาอย่างสร้างสรรค์</h5>
              <p>ครูชมเชยความกล้าหาญ นัดติดตามผลในอีก 2 สัปดาห์ และไม่ปล่อยให้เด็กเกิดการติดพึ่งพาครู</p>
            </div>
          </div>
        </div>

      </div>

    </div>

    <!-- ========================================================
         VIEW 3: VISUAL GLOSSARY (Flashcards)
         ======================================================== -->
    <div class="glossary-container" id="viewGlossary">
      
      <!-- Search Input -->
      <div class="glossary-search-bar">
        <span>🔎</span>
        <input type="text" id="glossarySearchInput" onkeyup="filterGlossary()" placeholder="พิมพ์ค้นหาคำศัพท์เฉพาะ เช่น Catharsis, Transference, The Question, Here and Now...">
      </div>

      <!-- Flashcards Grid -->
      <div class="glossary-grid" id="glossaryGrid">

        <!-- Card: Catharsis -->
        <div class="glossary-card" data-tags="catharsis ระบายอารมณ์ บทที่5 บทที่8 freud">
          <div class="g-header">
            <h4 class="g-term">Catharsis (การระบายอารมณ์)</h4>
            <span class="g-chapter-tag">บทที่ 5 & 8</span>
          </div>
          <div class="g-human-lang">
            🗣️ <strong>ภาษาคน:</strong> ร้องไห้โฮ หรือระบายความอัดอั้นตันใจที่เก็บไว้นานจนหมดก๊อก
          </div>
          <div class="g-metaphor-box">
            <div class="g-metaphor-title">🖼️ ภาพจำในชีวิตจริง</div>
            <p class="g-metaphor-desc"><strong>"หม้อต้มน้ำเดือดที่แง้มฝาเปิดระบายไอน้ำ"</strong> รู้สึกโล่งเบาสบายตัวทันที แต่หม้อยังตั้งอยู่บนเตา (ยังไม่ได้แก้ปัญหาที่ต้นตอ)</p>
          </div>
          <div class="g-example">
            ⚠️ <strong>ข้อควรระวัง:</strong> อย่าเพิ่งรีบยุติการปรึกษาหลังเด็กร้องไห้เสร็จ เพราะนั่นแค่ขั้นระบาย ยังไม่ได้ลงมือแก้ปัญหา
          </div>
        </div>

        <!-- Card: Id Ego Superego -->
        <div class="glossary-card" data-tags="id ego superego โครงสร้างจิต จิตวิเคราะห์ บทที่8 freud">
          <div class="g-header">
            <h4 class="g-term">Id, Ego, Superego</h4>
            <span class="g-chapter-tag">บทที่ 8 Freud</span>
          </div>
          <div class="g-human-lang">
            🗣️ <strong>ภาษาคน:</strong> พลังขับ 3 ฝ่ายที่แย่งกันคุมพฤติกรรมมนุษย์ตลอดเวลา
          </div>
          <div class="g-metaphor-box">
            <div class="g-metaphor-title">🖼️ ภาพจำในชีวิตจริง</div>
            <p class="g-metaphor-desc">
              • <strong>Id</strong> = <em>เด็กเอาแต่ใจ:</em> "กูจะเอาเดี๋ยวนี้! โดดเรียนไปเล่นเกมกัน!"<br>
              • <strong>Superego</strong> = <em>แม่ชีเจ้าระเบียบ:</em> "ทำแบบนั้นชั่วร้าย ตกนรก!"<br>
              • <strong>Ego</strong> = <em>ผู้จัดการคนกลาง:</em> "ทำการบ้าน 1 ชม. ก่อน แล้วค่อยไปเล่นเกม"
            </p>
          </div>
          <div class="g-example">
            🎯 <strong>ประเด็นสอบ:</strong> ปัญหาสุขภาพจิตเกิดจาก Ego อ่อนแอ ไม่สามารถไกล่เกลี่ย Id กับ Superego ได้
          </div>
        </div>

        <!-- Card: Transference -->
        <div class="glossary-card" data-tags="transference การถ่ายโยงความรู้สึก บทที่8 freud">
          <div class="g-header">
            <h4 class="g-term">Transference (การถ่ายโยง)</h4>
            <span class="g-chapter-tag">บทที่ 8 Freud</span>
          </div>
          <div class="g-human-lang">
            🗣️ <strong>ภาษาคน:</strong> เอาความรู้สึกที่เคยมีต่อคนสำคัญในอดีต (เช่น พ่อ/แม่) มาสวมทับที่ตัวครู
          </div>
          <div class="g-metaphor-box">
            <div class="g-metaphor-title">🖼️ ภาพจำในชีวิตจริง</div>
            <p class="g-metaphor-desc"><strong>"เห็นหน้าครูแล้วนึกถึงพ่อขี้โมโห"</strong> เด็กเกลียดพ่อ พอครูแค่พูดเสียงเข้ม เด็กระเบิดอารมณ์ด่าครูทันที เพราะจิตใต้สำนึกมองเห็นภาพพ่อซ้อนอยู่ที่ครู</p>
          </div>
          <div class="g-example">
            💡 <strong>การนำไปใช้:</strong> ครูต้องรู้ทัน ไม่โกรธตอบ และใช้จังหวะนี้ชี้ให้เด็กเห็นว่าเขากำลังสับสนกับอดีต
          </div>
        </div>

        <!-- Card: Reaction Formation -->
        <div class="glossary-card" data-tags="reaction formation กลไกป้องกันตนเอง บทที่7 บทที่8">
          <div class="g-header">
            <h4 class="g-term">Reaction Formation</h4>
            <span class="g-chapter-tag">บทที่ 7 & 8</span>
          </div>
          <div class="g-human-lang">
            🗣️ <strong>ภาษาคน:</strong> แสดงพฤติกรรมใน "ขั้วตรงข้ามอย่างสุดโต่ง" เพื่อกลบความรู้สึกจริง
          </div>
          <div class="g-metaphor-box">
            <div class="g-metaphor-title">🖼️ ภาพจำในชีวิตจริง</div>
            <p class="g-metaphor-desc"><strong>"เกลียดเข้าไส้ แต่เข้าไปกอด ยิ้มหวาน เอาใจผิดปกติ"</strong> เพราะจิตใจรู้สึกผิดถ้าจะยอมรับว่าตัวเองเกลียด เลยแกล้งทำเป็นรักเว่อร์ๆ เพื่อปกปิด</p>
          </div>
          <div class="g-example">
            🔍 <strong>จุดสังเกต:</strong> พฤติกรรมจะดูประดิษฐ์ ไม่เป็นธรรมชาติ และล้นเกินความเป็นจริง
          </div>
        </div>

        <!-- Card: The Question -->
        <div class="glossary-card" data-tags="the question คำถามสมมุติ adler บทที่9">
          <div class="g-header">
            <h4 class="g-term">The Question (คำถามสมมุติ)</h4>
            <span class="g-chapter-tag">บทที่ 9 Adler</span>
          </div>
          <div class="g-human-lang">
            🗣️ <strong>ภาษาคน:</strong> คำถามดักจับว่า "เด็กป่วยจริง หรือป่วยเพื่อหนีปัญหา"
          </div>
          <div class="g-metaphor-box">
            <div class="g-metaphor-title">🖼️ ภาพจำในชีวิตจริง</div>
            <p class="g-metaphor-desc"><em>"ถ้าพรุ่งนี้ตื่นมา อาการปวดหัวหายเป็นปลิดทิ้ง เธอจะทำอะไรเป็นอย่างแรก?"</em><br>ถ้าเด็กตอบว่า: <em>"หนูก็ต้องไปสอบคณิตศาสตร์สิคะ"</em> $\rightarrow$ ชัดเจนว่า ปวดหัวเพื่อ <strong>หนีสอบ!</strong></p>
          </div>
          <div class="g-example">
            🎯 <strong>ประเด็นสอบ:</strong> Adler เชื่อว่าพฤติกรรมทุกอย่างของมนุษย์มี "เป้าหมาย (Goal)" แอบแฝงเสมอ
          </div>
        </div>

        <!-- Card: Real vs Ideal Self -->
        <div class="glossary-card" data-tags="real self ideal self incongruence rogers บทที่10">
          <div class="g-header">
            <h4 class="g-term">Real Self vs. Ideal Self</h4>
            <span class="g-chapter-tag">บทที่ 10 Rogers</span>
          </div>
          <div class="g-human-lang">
            🗣️ <strong>ภาษาคน:</strong> สิ่งที่เราเป็นจริงๆ กับ สิ่งที่เราเพ้อฝันอยากจะเป็น
          </div>
          <div class="g-metaphor-box">
            <div class="g-metaphor-title">🖼️ ภาพจำในชีวิตจริง</div>
            <p class="g-metaphor-desc"><strong>"วงกลม 2 วงที่ไม่ยอมซ้อนทับกัน"</strong> ตัวจริงเรียนได้เกรด 2 (Real) แต่อยากสอบติดหมอตามที่แม่สั่ง (Ideal) ช่องว่างระหว่างสองวงนี้คือ <strong>ความเครียดและโรคซึมเศร้า</strong></p>
          </div>
          <div class="g-example">
            🌱 <strong>เป้าหมายการบำบัด:</strong> ช่วยให้เด็กยอมรับความจริงและรักตัวเอง เพื่อให้วงกลมสองวงเลื่อนมาซ้อนกัน
          </div>
        </div>

        <!-- Card: Unfinished Business -->
        <div class="glossary-card" data-tags="unfinished business เรื่องค้างคาใจ gestalt perls บทที่11">
          <div class="g-header">
            <h4 class="g-term">Unfinished Business</h4>
            <span class="g-chapter-tag">บทที่ 11 Gestalt</span>
          </div>
          <div class="g-human-lang">
            🗣️ <strong>ภาษาคน:</strong> เรื่องค้างคาใจในอดีตที่ไม่ได้เคลียร์ แล้วตามมาหลอกหลอนปัจจุบัน
          </div>
          <div class="g-metaphor-box">
            <div class="g-metaphor-title">🖼️ ภาพจำในชีวิตจริง</div>
            <p class="g-metaphor-desc"><strong>"เสี้ยนหนามที่ตำคานิ้วจนเป็นหนอง"</strong> เช่น ความโกรธที่ไม่ได้ด่าพ่อ หรือคำขอโทษที่ไม่ได้พูดก่อนเพื่อนย้ายโรงเรียน มันคอยกัดกินใจตลอดเวลา</p>
          </div>
          <div class="g-example">
            ⚡ <strong>วิธีแก้:</strong> ใช้ <strong>เก้าอี้ว่าง (Empty Chair)</strong> ให้ผู้เรียนพูดสะสางความรู้สึกนั้นออกมาให้จบ
          </div>
        </div>

        <!-- Card: Topdog Underdog -->
        <div class="glossary-card" data-tags="topdog underdog gestalt perls บทที่11">
          <div class="g-header">
            <h4 class="g-term">Topdog vs. Underdog</h4>
            <span class="g-chapter-tag">บทที่ 11 Gestalt</span>
          </div>
          <div class="g-human-lang">
            🗣️ <strong>ภาษาคน:</strong> ตัวเราฝ่ายสั่งการ vs ตัวเราฝ่ายดื้อเงียบ
          </div>
          <div class="g-metaphor-box">
            <div class="g-metaphor-title">🖼️ ภาพจำในชีวิตจริง</div>
            <p class="g-metaphor-desc">
              • <strong>Topdog (หมาตัวบน):</strong> สั่งการ เจ้าระเบียบ <em>"ต้องตื่นตี 5 อ่านหนังสือเดี๋ยวนี้!"</em><br>
              • <strong>Underdog (หมาตัวล่าง):</strong> แสร้งทำเป็นอ่อนแอ ขอโทษ แต่ <em>"ผัดวันประกันพรุ่ง ดื้อเงียบ นอนต่อ"</em>
            </p>
          </div>
          <div class="g-example">
            🎯 <strong>ประเด็นสอบ:</strong> Underdog ควบคุมสถานการณ์ด้วยการแกล้งทำเป็นไร้ความสามารถ
          </div>
        </div>

      </div>

    </div>

  </main>

  <!-- ========================================================
       DETAIL DRAWER MODAL
       ======================================================== -->
  <div class="drawer-overlay" id="detailDrawer" onclick="closeDrawer(event)">
    <div class="drawer-card" onclick="event.stopPropagation()">
      <button class="drawer-close-btn" onclick="closeDrawer()">✕</button>
      
      <div>
        <span class="drawer-badge" id="modalBadge">หมวดหมู่</span>
        <h3 class="drawer-title" id="modalTitle">ชื่อหัวข้อ</h3>
      </div>

      <div class="drawer-block">
        <h4>🎯 ประเด็นหลักจริงๆ (Core Essence)</h4>
        <p id="modalEssence">เนื้อหาสาระสำคัญ</p>
      </div>

      <div class="drawer-block">
        <h4>🛠️ นำไปทำอะไรในการช่วยเหลือผู้เรียน?</h4>
        <p id="modalAction">แนวทางการนำไปปฏิบัติจริงของครู</p>
      </div>

      <div class="drawer-block">
        <h4>🔗 เชื่อมโยงกับบทไหนและอย่างไร?</h4>
        <div class="drawer-connections" id="modalConnections">
          <!-- Connection badges -->
        </div>
      </div>
    </div>
  </div>

  <!-- Footer -->
  <footer class="app-footer">
    EDP3502 การช่วยเหลือและให้คำปรึกษาผู้เรียน | ผังความคิดมโนทัศน์ช่วยจำ บทที่ 5 – 11
  </footer>

  <script>
    // Detailed concept database
    const conceptDB = {
      c5_1: {
        badge: "บทที่ 5 : ขั้นตอนที่ 1",
        title: "เริ่มต้นและสร้างสัมพันธภาพ (Establishing Relationship)",
        essence: "สร้างบรรยากาศที่อบอุ่น ไว้วางใจ ปลอดภัย และไม่ตัดสิน เพื่อให้ผู้เรียนกล้าเปิดปากเล่าความจริงโดยไม่กลัวถูกลงโทษ",
        action: "จัดที่นั่งให้ผ่อนคลาย, กล่าวทักทาย, อธิบายบทบาทและ 'การรักษาความลับ (Confidentiality)', หลีกเลี่ยงการเปิดประเด็นด้วยการจับผิดหรือตำหนิ",
        connections: ["บทที่ 6: ใช้ทักษะท่าทาง SOLER และการใส่ใจ", "บทที่ 10: สวมวิญญาณ Carl Rogers (Unconditional Positive Regard)"]
      },
      c5_2: {
        badge: "บทที่ 5 : ขั้นตอนที่ 2",
        title: "สำรวจปัญหาเพื่อเข้าใจตนเอง (Exploration & Catharsis)",
        essence: "ช่วยให้ผู้เรียนได้ระบายอารมณ์ความอัดอั้น (Catharsis) และสำรวจความคิด ความรู้สึก พฤติกรรม เพื่อให้เห็น 'สาเหตุที่แท้จริง' ไม่ใช่แค่ปัญหาผิวเผิน",
        action: "ตั้งคำถามเปิด, สะท้อนความรู้สึก, ฟังให้ครบ 3 มิติ, ระวังอย่าเพิ่งด่วนสรุปหรือสั่งสอนในขั้นนี้",
        connections: ["บทที่ 6: ใช้การสะท้อนความรู้สึก (Reflection) และทักษะเงียบ", "บทที่ 7: จับตาดูว่าเด็กกำลังใช้ Defense Mechanism แบบไหน", "บทที่ 8: ใช้ขุดหาความขัดแย้งใต้จิตสำนึก"]
      },
      c5_3: {
        badge: "บทที่ 5 : ขั้นตอนที่ 3",
        title: "จัดการกับปัญหา (Working Through & Action Plan)",
        essence: "หัวใจสำคัญของการรักษา! เมื่อเข้าใจสาเหตุ (Insight) แล้ว ต้องนำความเข้าใจนั้นมาฝึกฝน วางแผน และเปลี่ยนเป็นพฤติกรรมใหม่ในชีวิตจริง",
        action: "ช่วยผู้เรียนกำหนดเป้าหมายเชิงพฤติกรรมที่ทำได้จริง, ฝึกทักษะใหม่, ใช้เทคนิคการท้าทายความคิดย้อนแย้ง, ติดตามการฝึกฝน",
        connections: ["บทที่ 9: ปรับเปลี่ยนเป้าหมายชีวิตและเอาชนะปมด้อย (Adler)", "บทที่ 11: สะสางเรื่องค้างคาใจด้วย Empty Chair (Gestalt)"]
      },
      c5_4: {
        badge: "บทที่ 5 : ขั้นตอนที่ 4",
        title: "ยุติการปรึกษาและประเมินผล (Termination & Evaluation)",
        essence: "การจากลาอย่างสร้างสรรค์ สรุปบทเรียนที่ผู้เรียนค้นพบ ให้กำลังใจ และส่งเสริมให้ผู้เรียนสามารถ 'พึ่งพาตนเองได้' ในอนาคต",
        action: "เตือนล่วงหน้าเรื่องการยุติ, สรุปความก้าวหน้า, ทบทวนแผนเผชิญปัญหาหากอาการกำเริบ, นัดหมายติดตามผล (Follow-up)",
        connections: ["ป้องกันภาวะติดพึ่งพาครู (Dependence)", "ประเมินว่าบรรลุเป้าหมายที่ตั้งไว้ในขั้นที่ 3 หรือไม่"]
      },
      c6_1: {
        badge: "บทที่ 6 : ทักษะพื้นฐาน",
        title: "การใส่ใจและการแสดงท่าที (Attending Behavior & SOLER)",
        essence: "ภาษากาย (Non-verbal) มีพลังมากกว่าคำพูด ภาษากายที่เปิดรับจะส่งสัญญาณว่าครูอยู่ตรงนี้เพื่อรับฟังเธออย่างแท้จริง",
        action: "สูตร SOLER: Squarely (นั่งตรง/เยื้องเล็กน้อย), Open (เปิดท่าที ไม่กอดอก), Lean (โน้มตัวไปข้างหน้าเล็กน้อย), Eye contact (สบตาเป็นมิตร), Relax (ผ่อนคลาย)",
        connections: ["บทที่ 5: ใช้เป็นรากฐานตั้งแต่ขั้นที่ 1 จนถึงขั้นที่ 4", "บทที่ 10: แสดงถึงความจริงแท้ (Congruence)"]
      },
      c6_2: {
        badge: "บทที่ 6 : ทักษะการฟัง",
        title: "การฟังภาษาพูดครบ 3 มิติ (Verbal Listening)",
        essence: "การฟังที่ดีไม่ใช่แค่ได้ยินเสียง แต่ต้องเก็บข้อมูลให้ครบ 3 องค์ประกอบของจิตใจมนุษย์",
        action: "เก็บข้อมูล: 1. พฤติกรรม (เขาทำอะไรมา) 2. ความคิด (เขาตีความอย่างไร) 3. อารมณ์ความรู้สึก (ข้างในใจรู้สึกอย่างไร)",
        connections: ["ช่วยให้ครูสะท้อนความรู้สึกในบทที่ 6 ได้ตรงจุด", "ช่วยตรวจจับความไม่สอดคล้อง (Incongruence) ในบทที่ 10"]
      },
      c6_3: {
        badge: "บทที่ 6 : ทักษะแกนกลาง",
        title: "การสะท้อนความรู้สึก (Reflection of Feeling)",
        essence: "ทำหน้าที่เป็น 'กระจกเงา' สะท้อนอารมณ์ที่ซ่อนอยู่ใต้คำพูดกลับไปให้ผู้เรียนเห็นชัดขึ้น โดยครูต้องไม่ตัดสิน ไม่แนะนำ และไม่สั่งสอน",
        action: "โครงสร้างมาตรฐาน: 'หนูกำลังรู้สึก [ระบุคำบอกอารมณ์] เพราะ [ระบุเหตุการณ์/สาเหตุ]'",
        connections: ["บทที่ 5: ขับเคลื่อนขั้นสำรวจปัญหาให้ลึกซึ้ง", "บทที่ 10: เป็นเครื่องมือแสดง Empathy ของ Carl Rogers"]
      },
      c6_4: {
        badge: "บทที่ 6 : ทักษะขั้นสูง",
        title: "การท้าทาย (Challenging) และ การใช้ความเงียบ (Silence)",
        essence: "การท้าทาย = ชี้ให้เห็นช่องว่างความย้อนแย้งระหว่างคำพูดกับการกระทำ ส่วนความเงียบ = พื้นที่ทรงพลังให้ผู้เรียนใคร่ครวญตนเอง",
        action: "ท้าทายอย่างสุภาพ เช่น 'ครูสังเกตว่าหนูบอกว่าอยากสอบติดหมอมาก แต่หนูก็เล่าว่าเล่นเกมวันละ 8 ชั่วโมง หนูกำลังคิดอย่างไรกับสองสิ่งนี้?'",
        connections: ["บทที่ 5: ขับเคลื่อนขั้นจัดการปัญหา (Working through)", "บทที่ 11: ทลายหน้ากากข้ออ้าง (Topdog/Underdog)"]
      },
      c7_1: {
        badge: "บทที่ 7 & 8 : กลไกป้องกันตนเอง",
        title: "Repression (การกดเก็บ)",
        essence: "กลไกป้องกันตัวแม่บทที่จิตใจใช้มากที่สุด คือการกดความทรงจำ ความเจ็บปวด หรือความปรารถนาที่น่าละอายลงไปขังไว้ในจิตไร้สำนึก",
        action: "ครูต้องเข้าใจว่าเด็กไม่ได้แกล้งลืม แต่จิตใต้สำนึกสั่งให้ลืมเพื่อไม่ให้เจ็บปวด ต้องสร้างความปลอดภัยสูงมากเด็กจึงจะกล้าเปิดเผย",
        connections: ["บทที่ 8: รากฐานของจิตวิเคราะห์ Freud", "บทที่ 5: อุปสรรคสำคัญในขั้นสำรวจปัญหา"]
      },
      c7_2: {
        badge: "บทที่ 7 & 8 : กลไกป้องกันตนเอง",
        title: "Projection (การฉายภาพ / โยนความผิด)",
        essence: "การไม่ยอมรับข้อเสียหรือความรู้สึกด้านลบของตนเอง แล้วโยนบาปไปกล่าวหาว่าคนอื่นเป็นคนทำหรือเป็นคนรู้สึกแบบนั้น",
        action: "เมื่อเด็กบอกว่า 'เพื่อนทุกคนเกลียดหนู' หรือ 'ครูแกล้งหนู' ให้ครูตั้งข้อสังเกตว่าแท้จริงเด็กกำลังรู้สึกเกลียดตัวเองหรือไม่",
        connections: ["บทที่ 11: เกสตอลต์มองว่า Projection คือการผลักตัวตนบางส่วนออกไป ต้องเรียกคืนมาด้วย Enactment"]
      },
      c7_3: {
        badge: "บทที่ 7 & 8 : กลไกป้องกันตนเอง",
        title: "Reaction Formation (การกระทำตรงข้าม)",
        essence: "การแสดงออกพฤติกรรมในขั้วตรงข้ามกับความรู้สึกจริงอย่างสุดโต่ง เพื่อป้องกันไม่ให้จิตสำนึกรู้สึกผิดบาป",
        action: "สังเกตความผิดปกติ: ถ้าเด็กทำดีเว่อร์ เอาใจผิดปกติ หรือสุภาพจนแข็งทื่อ อาจกำลังกลบเกลื่อนความโกรธหรือความเกลียดที่รุนแรง",
        connections: ["บทที่ 8: การทำงานของ Ego ในการรับมือกับ Superego"]
      },
      c7_4: {
        badge: "บทที่ 7 & 8 : กลไกป้องกันตนเอง",
        title: "Displacement (การเปลี่ยนที่ / เตะหมา)",
        essence: "การย้ายอารมณ์โกรธหรือคับข้องใจจากบุคคลที่มีอำนาจเหนือกว่า ไปลงกับบุคคลหรือสิ่งของที่อ่อนแอกว่าและไม่มีทางสู้",
        action: "เมื่อเห็นเด็กแกล้งเพื่อนที่อ่อนแอกว่า หรือพังโต๊ะเก้าอี้ อย่าเพิ่งลงโทษทันที ให้สืบค้นว่าเขาเพิ่งโดนใครกดขี่หรือทำร้ายมา",
        connections: ["บทที่ 9: อาจสะท้อนความรู้สึกไร้พลัง (Inferiority) ที่ต้องการหาอำนาจชดเชย"]
      },
      c8: {
        badge: "บทที่ 8 : ทฤษฎีจิตวิเคราะห์",
        title: "ทฤษฎีจิตวิเคราะห์ของ Sigmund Freud (Psychoanalysis)",
        essence: "มนุษย์ถูกควบคุมโดยพลังจิตไร้สำนึกและประสบการณ์ในวัยเด็ก 5 ขวบปีแรก ปัญหาสุขภาพจิตเกิดจากความขัดแย้งของ Id-Ego-Superego",
        action: "ใช้สืบค้นแผลเก่าในอดีต, ระวังภาวะ Transference (ถ่ายโยงอารมณ์ใส่ครู), ช่วยให้ผู้เรียนเกิดความเข้าใจตนเองอย่างลึกซึ้ง (Insight)",
        connections: ["เป็นต้นกำเนิดของกลไกในบทที่ 7", "เป็นขั้วตรงข้ามของบทที่ 11 (Freud เน้นอดีต แต่ Gestalt เน้นปัจจุบัน)"]
      },
      c9: {
        badge: "บทที่ 9 : ทฤษฎีแอดเลอร์",
        title: "ทฤษฎีจิตวิทยาเดี่ยวของ Alfred Adler (Individual Psychology)",
        essence: "มนุษย์ไม่ได้ถูกกำหนดโดยอดีต แต่ถูกขับเคลื่อนด้วย 'เป้าหมายสู่อนาคต' เพื่อเอาชนะ 'ปมด้อย (Inferiority)' สู่ 'ความรู้สึกมีคุณค่า (Superiority)'",
        action: "วิเคราะห์เป้าหมายพฤติกรรมผิด 4 ขั้น (เรียกร้องความสนใจ, แย่งอำนาจ, แก้แค้น, แกล้งยอมแพ้), วิเคราะห์ลำดับการเกิด, ใช้เทคนิค 'The Question'",
        connections: ["เหมาะมากกับการแก้พฤติกรรมเด็กดื้อในห้องเรียน", "ช่วยต่อยอดบทที่ 5 ในการกำหนดเป้าหมายใหม่"]
      },
      c10: {
        badge: "บทที่ 10 : ทฤษฎีโรเจอร์ส",
        title: "ทฤษฎีตัวผู้เรียนเป็นศูนย์กลางของ Carl Rogers (Person-Centered)",
        essence: "มนุษย์ทุกคนมีศักยภาพในการชี้นำตนเองและอยากเติบโตเป็นคนดี ครูไม่ต้องคอยสั่งสอน แค่ให้ 'ดิน น้ำ แดด' (3 สภาวะ) แล้วต้นไม้จะโตเอง",
        action: "สร้าง 3 สภาวะ: 1. Congruence (จริงแท้) 2. Unconditional Positive Regard (ยอมรับไร้เงื่อนไข) 3. Empathy (เข้าใจลึกซึ้ง)",
        connections: ["เป็น Mindset คลุมทุกขั้นตอนในบทที่ 5", "ขับเคลื่อนทักษะการฟังและสะท้อนความรู้สึกในบทที่ 6"]
      },
      c11: {
        badge: "บทที่ 11 : ทฤษฎีเกสตอลต์",
        title: "ทฤษฎีเกสตอลต์ของ Fritz Perls (Gestalt Therapy)",
        essence: "หยุดคร่ำครวญถึงอดีต ให้ตระหนักรู้กับปัจจุบัน 'ที่นี่และเดี๋ยวนี้ (Here & Now)' ร่างกายไม่เคยโกหก สะสางเรื่องค้างคาใจ (Unfinished Business)",
        action: "ใช้ 'เทคนิคเก้าอี้ว่าง (Empty Chair)', ให้แสดงบทบาทสมมติเพื่อดึงตัวตนที่ฉายภาพกลับคืนมา, เปลี่ยนคำพูด 'ฉันทำไม่ได้' เป็น 'ฉันเลือกที่จะไม่ทำ'",
        connections: ["ตอบโจทย์ขั้นที่ 3 (จัดการปัญหา) ของบทที่ 5", "ช่วยปลดล็อกความโกรธที่ค้างคาจากวัยเด็กของ Freud (บทที่ 8)"]
      }
    };

    // Switch View function
    function switchView(viewName) {
      document.getElementById('viewMindmap').style.display = viewName === 'mindmap' ? 'flex' : 'none';
      document.getElementById('viewWorkflow').style.display = viewName === 'workflow' ? 'flex' : 'none';
      document.getElementById('viewGlossary').style.display = viewName === 'glossary' ? 'flex' : 'none';

      document.getElementById('tabMindmap').classList.toggle('active', viewName === 'mindmap');
      document.getElementById('tabWorkflow').classList.toggle('active', viewName === 'workflow');
      document.getElementById('tabGlossary').classList.toggle('active', viewName === 'glossary');

      window.scrollTo({ top: 0, behavior: 'smooth' });
    }

    // Modal Drawer functions
    function openDetail(key) {
      const data = conceptDB[key];
      if (!data) return;

      document.getElementById('modalBadge').textContent = data.badge;
      document.getElementById('modalTitle').textContent = data.title;
      document.getElementById('modalEssence').textContent = data.essence;
      document.getElementById('modalAction').textContent = data.action;

      const connContainer = document.getElementById('modalConnections');
      connContainer.innerHTML = '';
      data.connections.forEach(conn => {
        const span = document.createElement('span');
        span.className = 'drawer-conn-tag';
        span.textContent = conn;
        connContainer.appendChild(span);
      });

      document.getElementById('detailDrawer').classList.add('active');
    }

    function closeDrawer(e) {
      if (!e || e.target.id === 'detailDrawer' || e.target.classList.contains('drawer-close-btn')) {
        document.getElementById('detailDrawer').classList.remove('active');
      }
    }

    // Glossary Filter function
    function filterGlossary() {
      const query = document.getElementById('glossarySearchInput').value.toLowerCase().trim();
      const cards = document.querySelectorAll('.glossary-card');

      cards.forEach(card => {
        const text = (card.textContent + ' ' + card.getAttribute('data-tags')).toLowerCase();
        if (text.includes(query)) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    }
  </script>
</body>
</html>
"""

# Destination paths
path_work = r"c:\Users\chinj\OneDrive\ปี3\EDP3502-ช่วยเหลือ\งาน\ผังความคิด_EDP3502_บทที่5-11.html"
path_root = r"c:\Users\chinj\OneDrive\ปี3\EDP3502-ช่วยเหลือ\ผังความคิด_EDP3502_บทที่5-11.html"

with open(path_work, "w", encoding="utf-8") as f:
    f.write(html_code)
print(f"Generated work file: {path_work} ({len(html_code)} bytes)")

with open(path_root, "w", encoding="utf-8") as f:
    f.write(html_code)
print(f"Generated root file: {path_root} ({len(html_code)} bytes)")
