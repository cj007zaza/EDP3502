# -*- coding: utf-8 -*-
"""
HTML Portal Generator for EDP3502: การช่วยเหลือและให้คำปรึกษาผู้เรียน
Generates the complete 3-in-1 interactive web app:
- 60 Questions (30 Core Concepts + 30 Situations)
- 40 Knowledge Flashcards (3D flip, tracker, filters)
- Comprehensive Summary for Chapters 5-11 + Comparison Table
"""

import json

with open("all_60_questions.json", "r", encoding="utf-8") as f:
    questions_json_str = f.read()

with open("all_40_flashcards.json", "r", encoding="utf-8") as f:
    flashcards_json_str = f.read()

# Build HTML template
html_content = f'''<!DOCTYPE html>
<html lang="th" data-theme="sage">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>EDP3502 การช่วยเหลือและให้คำปรึกษาผู้เรียน | คลังข้อสอบ 60 ข้อ • แฟลชการ์ด • สรุปบทที่ 5-11</title>
  
  <!-- Google Fonts: Prompt for headers & Sarabun for comfortable body reading -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Prompt:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&family=Sarabun:ital,wght@0,300;0,400;0,500;0,600;0,700;1,400&display=swap" rel="stylesheet">
  
  <style>
    /* ==========================================================================
       CSS Variables & Themes (Soothing, Eye-friendly Color Palettes)
       ========================================================================== */
    :root {{
      /* 🌿 Theme 1: Sage Serenity (Default soothing palette) */
      --bg-body: #f5f8f5;
      --bg-card: #ffffff;
      --bg-card-subtle: #f9fbf9;
      --bg-header: rgba(255, 255, 255, 0.88);
      --bg-pill: #eaf2ec;
      --bg-pill-hover: #dfebe2;
      --bg-code: #edf4ef;
      
      --text-main: #213328;
      --text-secondary: #4d6355;
      --text-muted: #6b8273;
      --text-light: #899e91;

      --border-color: #e0ece3;
      --border-subtle: #ebf3ed;
      --border-focus: #3d7054;

      --primary: #3d7054;
      --primary-hover: #315c44;
      --primary-light: #eaf3ed;
      --primary-border: #b8d9c5;

      --accent: #c86d51;
      --accent-light: #fbeee9;
      --accent-border: #f2c7b8;

      --warning: #c28322;
      --warning-light: #fef8eb;
      --warning-border: #f9e2b4;

      --success: #2e7d58;
      --success-light: #eaf6ef;
      --success-border: #a8dfc2;

      --danger: #cf4e4e;
      --danger-light: #fdf0f0;
      --danger-border: #f7bebe;

      --shadow-sm: 0 2px 6px rgba(33, 51, 40, 0.04);
      --shadow-md: 0 6px 18px rgba(33, 51, 40, 0.06);
      --shadow-lg: 0 14px 34px rgba(33, 51, 40, 0.09);
      --shadow-card: 0 4px 16px -2px rgba(33, 51, 40, 0.05);

      --radius-sm: 8px;
      --radius-md: 14px;
      --radius-lg: 20px;
      --radius-full: 9999px;

      --font-heading: 'Prompt', -apple-system, BlinkMacSystemFont, sans-serif;
      --font-body: 'Sarabun', -apple-system, BlinkMacSystemFont, sans-serif;

      --base-font-size: 16px;
      --transition-smooth: all 0.25s cubic-bezier(0.2, 0.8, 0.2, 1);
    }}

    /* 🌾 Theme 2: Warm Sand & Earth Tone */
    [data-theme="warm"] {{
      --bg-body: #faf7f2;
      --bg-card: #ffffff;
      --bg-card-subtle: #fcfaf6;
      --bg-header: rgba(255, 255, 255, 0.90);
      --bg-pill: #f3ece1;
      --bg-pill-hover: #ebd9c5;
      --bg-code: #f5eee4;

      --text-main: #332a22;
      --text-secondary: #635245;
      --text-muted: #826e5f;
      --text-light: #a38f80;

      --border-color: #ede4d8;
      --border-subtle: #f5ede1;
      --border-focus: #7a5e43;

      --primary: #6b5038;
      --primary-hover: #543e2a;
      --primary-light: #f5ede4;
      --primary-border: #dbc4b0;

      --accent: #b86236;
      --accent-light: #fdf0e9;
      --accent-border: #f4cbbb;

      --shadow-sm: 0 2px 6px rgba(51, 42, 34, 0.04);
      --shadow-md: 0 6px 18px rgba(51, 42, 34, 0.06);
      --shadow-lg: 0 14px 34px rgba(51, 42, 34, 0.09);
      --shadow-card: 0 4px 16px -2px rgba(51, 42, 34, 0.05);
    }}

    /* 🌙 Theme 3: Soft Forest Night (Reading Dark Mode) */
    [data-theme="night"] {{
      --bg-body: #141d17;
      --bg-card: #1c2720;
      --bg-card-subtle: #18231c;
      --bg-header: rgba(28, 39, 32, 0.92);
      --bg-pill: #26362d;
      --bg-pill-hover: #314439;
      --bg-code: #223128;

      --text-main: #e2ede5;
      --text-secondary: #b1c7ba;
      --text-muted: #8ca395;
      --text-light: #6e8477;

      --border-color: #2b3d32;
      --border-subtle: #243329;
      --border-focus: #5fa47e;

      --primary: #5fa47e;
      --primary-hover: #75b893;
      --primary-light: #22362b;
      --primary-border: #3b5746;

      --accent: #d88167;
      --accent-light: #362521;
      --accent-border: #5a3a32;

      --warning: #d99f43;
      --warning-light: #332817;
      --warning-border: #574121;

      --success: #4ea87d;
      --success-light: #1b3527;
      --success-border: #2e5942;

      --danger: #e26f6f;
      --danger-light: #381f1f;
      --danger-border: #633030;

      --shadow-sm: 0 2px 6px rgba(0, 0, 0, 0.25);
      --shadow-md: 0 6px 18px rgba(0, 0, 0, 0.35);
      --shadow-lg: 0 14px 34px rgba(0, 0, 0, 0.45);
      --shadow-card: 0 4px 16px -2px rgba(0, 0, 0, 0.30);
    }}

    /* ==========================================================================
       Global Reset & Base Typography
       ========================================================================== */
    *, *::before, *::after {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    html {{
      font-size: var(--base-font-size);
      scroll-behavior: smooth;
    }}

    body {{
      font-family: var(--font-body);
      background-color: var(--bg-body);
      color: var(--text-main);
      line-height: 1.7;
      -webkit-font-smoothing: antialiased;
      -moz-osx-font-smoothing: grayscale;
      transition: background-color 0.3s ease, color 0.3s ease;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
    }}

    h1, h2, h3, h4, h5, h6 {{
      font-family: var(--font-heading);
      color: var(--text-main);
      line-height: 1.35;
      font-weight: 600;
    }}

    p {{
      margin-bottom: 0.85rem;
    }}

    a {{
      color: var(--primary);
      text-decoration: none;
      transition: var(--transition-smooth);
    }}

    a:hover {{
      color: var(--primary-hover);
      text-decoration: underline;
    }}

    /* ==========================================================================
       Top Header & Navigation Bar
       ========================================================================== */
    .site-header {{
      position: sticky;
      top: 0;
      z-index: 1000;
      background: var(--bg-header);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-bottom: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
      transition: var(--transition-smooth);
    }}

    .header-container {{
      max-width: 1280px;
      margin: 0 auto;
      padding: 0.75rem 1.25rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      flex-wrap: wrap;
    }}

    .brand-area {{
      display: flex;
      align-items: center;
      gap: 0.85rem;
      text-decoration: none;
    }}

    .brand-logo-icon {{
      width: 44px;
      height: 44px;
      background: linear-gradient(135deg, var(--primary), var(--accent));
      color: white;
      border-radius: var(--radius-md);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.4rem;
      box-shadow: 0 4px 10px rgba(61, 112, 84, 0.25);
    }}

    .brand-titles {{
      display: flex;
      flex-direction: column;
    }}

    .brand-course {{
      font-size: 0.78rem;
      font-weight: 600;
      letter-spacing: 0.05em;
      color: var(--accent);
      text-transform: uppercase;
      font-family: var(--font-heading);
    }}

    .brand-main {{
      font-size: 1.12rem;
      font-weight: 600;
      color: var(--text-main);
      font-family: var(--font-heading);
    }}

    /* Nav Tabs */
    .nav-tabs {{
      display: flex;
      gap: 0.4rem;
      background: var(--bg-pill);
      padding: 0.3rem;
      border-radius: var(--radius-full);
      border: 1px solid var(--border-color);
    }}

    .nav-tab-btn {{
      font-family: var(--font-heading);
      font-size: 0.88rem;
      font-weight: 500;
      padding: 0.5rem 1rem;
      border-radius: var(--radius-full);
      border: none;
      background: transparent;
      color: var(--text-secondary);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.45rem;
      transition: var(--transition-smooth);
      white-space: nowrap;
    }}

    .nav-tab-btn:hover {{
      color: var(--text-main);
      background: var(--bg-pill-hover);
    }}

    .nav-tab-btn.active {{
      background: var(--bg-card);
      color: var(--primary);
      font-weight: 600;
      box-shadow: var(--shadow-sm);
    }}

    .badge-count {{
      font-size: 0.72rem;
      padding: 0.15rem 0.45rem;
      border-radius: var(--radius-full);
      background: var(--primary-light);
      color: var(--primary);
      font-weight: 600;
      border: 1px solid var(--primary-border);
    }}

    /* Utilities in header */
    .header-actions {{
      display: flex;
      align-items: center;
      gap: 0.6rem;
    }}

    .theme-select {{
      font-family: var(--font-heading);
      font-size: 0.82rem;
      padding: 0.4rem 0.75rem;
      border-radius: var(--radius-full);
      border: 1px solid var(--border-color);
      background: var(--bg-card);
      color: var(--text-main);
      cursor: pointer;
      outline: none;
      transition: var(--transition-smooth);
    }}

    .theme-select:hover {{
      border-color: var(--primary);
    }}

    .font-size-btn {{
      width: 32px;
      height: 32px;
      display: flex;
      align-items: center;
      justify-content: center;
      border-radius: 50%;
      border: 1px solid var(--border-color);
      background: var(--bg-card);
      color: var(--text-secondary);
      cursor: pointer;
      font-size: 0.85rem;
      font-weight: 600;
      transition: var(--transition-smooth);
    }}

    .font-size-btn:hover {{
      color: var(--primary);
      border-color: var(--primary);
    }}

    /* ==========================================================================
       Main Layout & Section Wrappers
       ========================================================================== */
    .main-container {{
      max-width: 1280px;
      margin: 1.5rem auto 3rem;
      padding: 0 1.25rem;
      width: 100%;
      flex: 1;
    }}

    .view-panel {{
      display: none;
      animation: fadeIn 0.3s ease;
    }}

    .view-panel.active {{
      display: block;
    }}

    @keyframes fadeIn {{
      from {{ opacity: 0; transform: translateY(6px); }}
      to {{ opacity: 1; transform: translateY(0); }}
    }}

    /* Hero Banner for Each View */
    .hero-banner {{
      background: linear-gradient(135deg, var(--bg-card), var(--bg-card-subtle));
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 1.75rem 2rem;
      margin-bottom: 1.75rem;
      box-shadow: var(--shadow-card);
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1.5rem;
      flex-wrap: wrap;
    }}

    .hero-content h1 {{
      font-size: 1.65rem;
      margin-bottom: 0.4rem;
      color: var(--text-main);
    }}

    .hero-content p {{
      color: var(--text-secondary);
      margin-bottom: 0;
      font-size: 0.98rem;
      max-width: 680px;
    }}

    .hero-badges {{
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
      margin-top: 0.6rem;
    }}

    .chip-badge {{
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      font-size: 0.78rem;
      padding: 0.25rem 0.65rem;
      border-radius: var(--radius-full);
      background: var(--primary-light);
      color: var(--primary);
      font-weight: 500;
      border: 1px solid var(--primary-border);
      font-family: var(--font-heading);
    }}

    .chip-badge.accent {{
      background: var(--accent-light);
      color: var(--accent);
      border-color: var(--accent-border);
    }}

    /* ==========================================================================
       TAB 1: QUIZ SECTION (60 Questions)
       ========================================================================== */
    .quiz-layout {{
      display: grid;
      grid-template-columns: 1fr 340px;
      gap: 1.5rem;
      align-items: start;
    }}

    @media (max-width: 960px) {{
      .quiz-layout {{
        grid-template-columns: 1fr;
      }}
    }}

    /* Controls Bar */
    .controls-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      margin-bottom: 1.25rem;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }}

    .control-row {{
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 0.75rem;
    }}

    /* Mode Switcher Buttons */
    .mode-switch-group {{
      display: flex;
      background: var(--bg-pill);
      padding: 0.25rem;
      border-radius: var(--radius-full);
      border: 1px solid var(--border-color);
    }}

    .mode-btn {{
      font-family: var(--font-heading);
      font-size: 0.85rem;
      font-weight: 500;
      padding: 0.45rem 1rem;
      border-radius: var(--radius-full);
      border: none;
      background: transparent;
      color: var(--text-secondary);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.4rem;
      transition: var(--transition-smooth);
    }}

    .mode-btn.active {{
      background: var(--primary);
      color: white;
      font-weight: 600;
      box-shadow: var(--shadow-sm);
    }}

    /* Filters: Chapter & Type */
    .filters-cluster {{
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      align-items: center;
    }}

    .filter-select {{
      font-family: var(--font-heading);
      font-size: 0.85rem;
      padding: 0.45rem 0.85rem;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
      background: var(--bg-card);
      color: var(--text-main);
      outline: none;
      cursor: pointer;
      transition: var(--transition-smooth);
    }}

    .filter-select:hover, .filter-select:focus {{
      border-color: var(--primary);
    }}

    .search-box-wrap {{
      position: relative;
      flex: 1;
      min-width: 200px;
    }}

    .search-input {{
      width: 100%;
      font-family: var(--font-body);
      font-size: 0.9rem;
      padding: 0.5rem 0.85rem 0.5rem 2.2rem;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
      background: var(--bg-card-subtle);
      color: var(--text-main);
      outline: none;
      transition: var(--transition-smooth);
    }}

    .search-input:focus {{
      border-color: var(--primary);
      background: var(--bg-card);
      box-shadow: 0 0 0 3px var(--primary-light);
    }}

    .search-icon {{
      position: absolute;
      left: 0.75rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-muted);
      pointer-events: none;
      font-size: 0.95rem;
    }}

    /* Stats Bar in Controls */
    .quiz-stats-summary {{
      display: flex;
      gap: 1rem;
      align-items: center;
      flex-wrap: wrap;
      font-size: 0.88rem;
      color: var(--text-secondary);
      padding-top: 0.5rem;
      border-top: 1px dashed var(--border-color);
    }}

    .stat-pill {{
      display: flex;
      align-items: center;
      gap: 0.35rem;
    }}

    .stat-pill strong {{
      color: var(--text-main);
      font-family: var(--font-heading);
    }}

    /* Question Card */
    .question-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      margin-bottom: 1.25rem;
      box-shadow: var(--shadow-card);
      transition: var(--transition-smooth);
      position: relative;
    }}

    .question-card:hover {{
      border-color: var(--border-focus);
    }}

    .question-card.flagged {{
      border-left: 4px solid var(--warning);
    }}

    .q-header {{
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      margin-bottom: 0.85rem;
      gap: 0.75rem;
    }}

    .q-meta {{
      display: flex;
      gap: 0.45rem;
      align-items: center;
      flex-wrap: wrap;
    }}

    .q-number-badge {{
      font-family: var(--font-heading);
      font-size: 0.85rem;
      font-weight: 700;
      color: var(--primary);
      background: var(--primary-light);
      padding: 0.2rem 0.65rem;
      border-radius: var(--radius-sm);
      border: 1px solid var(--primary-border);
    }}

    .q-chapter-tag {{
      font-size: 0.76rem;
      color: var(--text-secondary);
      background: var(--bg-pill);
      padding: 0.2rem 0.6rem;
      border-radius: var(--radius-full);
      font-family: var(--font-heading);
    }}

    .q-type-tag {{
      font-size: 0.74rem;
      padding: 0.18rem 0.55rem;
      border-radius: var(--radius-full);
      font-family: var(--font-heading);
      font-weight: 500;
    }}

    .q-type-tag.concept {{
      background: var(--primary-light);
      color: var(--primary);
      border: 1px solid var(--primary-border);
    }}

    .q-type-tag.situation {{
      background: var(--accent-light);
      color: var(--accent);
      border: 1px solid var(--accent-border);
    }}

    .flag-btn {{
      background: transparent;
      border: none;
      cursor: pointer;
      font-size: 1.15rem;
      color: var(--text-light);
      padding: 0.2rem 0.4rem;
      border-radius: var(--radius-sm);
      transition: var(--transition-smooth);
    }}

    .flag-btn:hover {{
      color: var(--warning);
      background: var(--warning-light);
    }}

    .flag-btn.active {{
      color: var(--warning);
    }}

    .q-text {{
      font-size: 1.05rem;
      color: var(--text-main);
      font-weight: 500;
      line-height: 1.7;
      margin-bottom: 1.25rem;
    }}

    .q-text em {{
      font-style: normal;
      background: var(--bg-pill);
      padding: 0.4rem 0.75rem;
      border-radius: var(--radius-sm);
      display: block;
      border-left: 3px solid var(--accent);
      margin: 0.4rem 0 0.75rem 0;
      font-size: 0.98rem;
      color: var(--text-main);
    }}

    /* Choices List */
    .choices-list {{
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      margin-bottom: 1rem;
    }}

    .choice-item {{
      display: flex;
      align-items: flex-start;
      gap: 0.75rem;
      padding: 0.85rem 1rem;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
      background: var(--bg-card);
      cursor: pointer;
      transition: var(--transition-smooth);
      font-size: 0.98rem;
      color: var(--text-main);
      line-height: 1.55;
    }}

    .choice-item:hover {{
      background: var(--bg-card-subtle);
      border-color: var(--primary);
      transform: translateX(2px);
    }}

    .choice-key {{
      display: inline-flex;
      align-items: center;
      justify-content: center;
      width: 28px;
      height: 28px;
      min-width: 28px;
      border-radius: 50%;
      background: var(--bg-pill);
      color: var(--text-secondary);
      font-family: var(--font-heading);
      font-size: 0.85rem;
      font-weight: 600;
      border: 1px solid var(--border-color);
      transition: var(--transition-smooth);
    }}

    .choice-item.selected {{
      border-color: var(--primary);
      background: var(--primary-light);
    }}

    .choice-item.selected .choice-key {{
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }}

    /* Choice states in Practice / Checked mode */
    .choice-item.correct {{
      border-color: var(--success);
      background: var(--success-light);
      color: var(--text-main);
    }}

    .choice-item.correct .choice-key {{
      background: var(--success);
      color: white;
      border-color: var(--success);
    }}

    .choice-item.wrong {{
      border-color: var(--danger);
      background: var(--danger-light);
      color: var(--text-main);
    }}

    .choice-item.wrong .choice-key {{
      background: var(--danger);
      color: white;
      border-color: var(--danger);
    }}

    /* Explanation Box */
    .explanation-box {{
      display: none;
      margin-top: 1rem;
      padding: 1rem 1.25rem;
      border-radius: var(--radius-md);
      background: var(--bg-card-subtle);
      border-left: 4px solid var(--primary);
      font-size: 0.94rem;
      line-height: 1.65;
      color: var(--text-secondary);
      animation: fadeIn 0.25s ease;
    }}

    .explanation-box.show {{
      display: block;
    }}

    .explanation-title {{
      font-family: var(--font-heading);
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--primary);
      margin-bottom: 0.4rem;
      display: flex;
      align-items: center;
      gap: 0.35rem;
    }}

    /* Sidebar Navigator */
    .quiz-sidebar {{
      position: sticky;
      top: 5rem;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      box-shadow: var(--shadow-card);
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }}

    .sidebar-header {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .sidebar-title {{
      font-family: var(--font-heading);
      font-size: 1rem;
      font-weight: 600;
    }}

    .progress-bar-wrap {{
      width: 100%;
      height: 8px;
      background: var(--bg-pill);
      border-radius: var(--radius-full);
      overflow: hidden;
    }}

    .progress-bar-fill {{
      height: 100%;
      background: linear-gradient(90deg, var(--primary), var(--accent));
      width: 0%;
      transition: width 0.3s ease;
    }}

    .q-nav-grid {{
      display: grid;
      grid-template-columns: repeat(6, 1fr);
      gap: 0.4rem;
      max-height: 380px;
      overflow-y: auto;
      padding: 0.25rem;
    }}

    .q-nav-btn {{
      font-family: var(--font-heading);
      font-size: 0.78rem;
      font-weight: 600;
      aspect-ratio: 1;
      border-radius: var(--radius-sm);
      border: 1px solid var(--border-color);
      background: var(--bg-card-subtle);
      color: var(--text-secondary);
      cursor: pointer;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: var(--transition-smooth);
      position: relative;
    }}

    .q-nav-btn:hover {{
      border-color: var(--primary);
      background: var(--primary-light);
    }}

    .q-nav-btn.answered {{
      background: var(--primary);
      color: white;
      border-color: var(--primary);
    }}

    .q-nav-btn.correct {{
      background: var(--success);
      color: white;
      border-color: var(--success);
    }}

    .q-nav-btn.wrong {{
      background: var(--danger);
      color: white;
      border-color: var(--danger);
    }}

    .q-nav-btn.flagged::after {{
      content: '';
      position: absolute;
      top: 3px;
      right: 3px;
      width: 6px;
      height: 6px;
      border-radius: 50%;
      background: var(--warning);
    }}

    .sidebar-actions {{
      display: flex;
      flex-direction: column;
      gap: 0.6rem;
    }}

    .btn-submit-exam {{
      width: 100%;
      font-family: var(--font-heading);
      font-size: 0.95rem;
      font-weight: 600;
      padding: 0.75rem;
      border-radius: var(--radius-md);
      border: none;
      background: linear-gradient(135deg, var(--primary), var(--primary-hover));
      color: white;
      cursor: pointer;
      box-shadow: 0 4px 12px rgba(61, 112, 84, 0.25);
      transition: var(--transition-smooth);
    }}

    .btn-submit-exam:hover {{
      transform: translateY(-2px);
      box-shadow: 0 6px 16px rgba(61, 112, 84, 0.35);
    }}

    .btn-reset-quiz {{
      width: 100%;
      font-family: var(--font-heading);
      font-size: 0.85rem;
      padding: 0.5rem;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
      background: transparent;
      color: var(--text-muted);
      cursor: pointer;
      transition: var(--transition-smooth);
    }}

    .btn-reset-quiz:hover {{
      color: var(--danger);
      border-color: var(--danger);
      background: var(--danger-light);
    }}

    /* Score Report Modal / Box */
    .score-modal-backdrop {{
      position: fixed;
      top: 0;
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(0, 0, 0, 0.6);
      backdrop-filter: blur(4px);
      z-index: 2000;
      display: none;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
    }}

    .score-modal-backdrop.show {{
      display: flex;
    }}

    .score-modal {{
      background: var(--bg-card);
      border-radius: var(--radius-lg);
      border: 1px solid var(--border-color);
      max-width: 650px;
      width: 100%;
      max-height: 90vh;
      overflow-y: auto;
      padding: 2rem;
      box-shadow: var(--shadow-lg);
      position: relative;
      animation: scaleIn 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }}

    @keyframes scaleIn {{
      from {{ transform: scale(0.92); opacity: 0; }}
      to {{ transform: scale(1); opacity: 1; }}
    }}

    .score-summary-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 1rem;
      margin: 1.25rem 0;
      text-align: center;
    }}

    .score-card-item {{
      background: var(--bg-card-subtle);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1rem;
    }}

    .score-val {{
      font-family: var(--font-heading);
      font-size: 1.8rem;
      font-weight: 700;
      color: var(--primary);
    }}

    .score-lbl {{
      font-size: 0.8rem;
      color: var(--text-muted);
      margin-top: 0.2rem;
    }}

    /* ==========================================================================
       TAB 2: FLASHCARDS SECTION (40 Cards)
       ========================================================================== */
    .flashcards-container {{
      max-width: 800px;
      margin: 0 auto;
    }}

    .fc-controls {{
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 1.5rem;
      background: var(--bg-card);
      padding: 1rem 1.25rem;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
      box-shadow: var(--shadow-sm);
    }}

    /* Flashcard 3D Scene */
    .fc-scene {{
      perspective: 1200px;
      width: 100%;
      height: 380px;
      margin-bottom: 1.5rem;
      cursor: pointer;
    }}

    .fc-card {{
      width: 100%;
      height: 100%;
      position: relative;
      transform-style: preserve-3d;
      transition: transform 0.6s cubic-bezier(0.4, 0.2, 0.2, 1);
      border-radius: var(--radius-lg);
    }}

    .fc-card.flipped {{
      transform: rotateY(180deg);
    }}

    .fc-face {{
      position: absolute;
      width: 100%;
      height: 100%;
      backface-visibility: hidden;
      -webkit-backface-visibility: hidden;
      border-radius: var(--radius-lg);
      padding: 2rem;
      box-shadow: var(--shadow-md);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      border: 1px solid var(--border-color);
    }}

    .fc-front {{
      background: linear-gradient(135deg, var(--bg-card), var(--bg-card-subtle));
    }}

    .fc-back {{
      background: linear-gradient(135deg, var(--bg-card-subtle), var(--bg-card));
      transform: rotateY(180deg);
      overflow-y: auto;
    }}

    .fc-top-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}

    .fc-ch-badge {{
      font-size: 0.78rem;
      padding: 0.2rem 0.6rem;
      border-radius: var(--radius-full);
      background: var(--primary-light);
      color: var(--primary);
      font-weight: 600;
      border: 1px solid var(--primary-border);
      font-family: var(--font-heading);
    }}

    .fc-progress-num {{
      font-family: var(--font-heading);
      font-size: 0.85rem;
      color: var(--text-muted);
    }}

    .fc-center-content {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      text-align: center;
      margin: auto 0;
    }}

    .fc-term {{
      font-size: 1.55rem;
      font-weight: 700;
      color: var(--text-main);
      margin-bottom: 0.65rem;
      line-height: 1.4;
    }}

    .fc-hint {{
      font-size: 0.96rem;
      color: var(--text-secondary);
      max-width: 500px;
    }}

    .fc-bottom-tap {{
      text-align: center;
      font-size: 0.8rem;
      color: var(--text-muted);
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 0.4rem;
    }}

    /* Back details */
    .fc-back-title {{
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--primary);
      margin-bottom: 0.75rem;
    }}

    .fc-definition {{
      font-size: 0.96rem;
      color: var(--text-main);
      line-height: 1.7;
      margin-bottom: 1rem;
    }}

    .fc-takeaway-box {{
      background: var(--primary-light);
      border-left: 3px solid var(--primary);
      padding: 0.6rem 0.85rem;
      border-radius: var(--radius-sm);
      font-size: 0.88rem;
      color: var(--primary);
      margin-bottom: 0.65rem;
    }}

    .fc-exam-box {{
      background: var(--accent-light);
      border-left: 3px solid var(--accent);
      padding: 0.6rem 0.85rem;
      border-radius: var(--radius-sm);
      font-size: 0.85rem;
      color: var(--accent);
    }}

    /* Bottom Flashcard Navigation */
    .fc-nav-bar {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 0.75rem;
      margin-top: 1rem;
    }}

    .fc-btn {{
      font-family: var(--font-heading);
      font-size: 0.92rem;
      font-weight: 600;
      padding: 0.65rem 1.25rem;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
      background: var(--bg-card);
      color: var(--text-main);
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 0.45rem;
      transition: var(--transition-smooth);
    }}

    .fc-btn:hover {{
      border-color: var(--primary);
      background: var(--primary-light);
      color: var(--primary);
    }}

    .fc-status-group {{
      display: flex;
      gap: 0.5rem;
    }}

    .fc-btn-memorized {{
      background: var(--success-light);
      color: var(--success);
      border-color: var(--success-border);
    }}

    .fc-btn-memorized:hover {{
      background: var(--success);
      color: white;
    }}

    .fc-btn-review {{
      background: var(--warning-light);
      color: var(--warning);
      border-color: var(--warning-border);
    }}

    .fc-btn-review:hover {{
      background: var(--warning);
      color: white;
    }}

    /* Flashcard Grid View (Toggleable) */
    .fc-grid-view {{
      display: none;
      grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
      gap: 1rem;
      margin-top: 1.5rem;
    }}

    .fc-grid-card {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      box-shadow: var(--shadow-sm);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      min-height: 220px;
      transition: var(--transition-smooth);
    }}

    .fc-grid-card:hover {{
      transform: translateY(-3px);
      box-shadow: var(--shadow-md);
      border-color: var(--primary);
    }}

    /* ==========================================================================
       TAB 3: COMPREHENSIVE SUMMARY (Chapters 5-11 + Comparison)
       ========================================================================== */
    .summary-layout {{
      display: grid;
      grid-template-columns: 260px 1fr;
      gap: 2rem;
      align-items: start;
    }}

    @media (max-width: 900px) {{
      .summary-layout {{
        grid-template-columns: 1fr;
      }}
    }}

    /* Summary TOC */
    .summary-toc {{
      position: sticky;
      top: 5rem;
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-md);
      padding: 1.25rem;
      box-shadow: var(--shadow-card);
    }}

    .toc-title {{
      font-family: var(--font-heading);
      font-size: 0.95rem;
      font-weight: 600;
      color: var(--text-main);
      margin-bottom: 0.85rem;
      padding-bottom: 0.5rem;
      border-bottom: 1px solid var(--border-color);
    }}

    .toc-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
    }}

    .toc-item a {{
      display: block;
      font-size: 0.85rem;
      color: var(--text-secondary);
      padding: 0.35rem 0.65rem;
      border-radius: var(--radius-sm);
      transition: var(--transition-smooth);
      text-decoration: none;
    }}

    .toc-item a:hover, .toc-item a.active {{
      background: var(--primary-light);
      color: var(--primary);
      font-weight: 500;
    }}

    /* Summary Content Cards */
    .summary-content {{
      display: flex;
      flex-direction: column;
      gap: 2rem;
    }}

    .chapter-section {{
      background: var(--bg-card);
      border: 1px solid var(--border-color);
      border-radius: var(--radius-lg);
      padding: 2rem;
      box-shadow: var(--shadow-card);
      scroll-margin-top: 6rem;
    }}

    .chapter-header {{
      display: flex;
      align-items: flex-start;
      gap: 1rem;
      margin-bottom: 1.5rem;
      padding-bottom: 1.25rem;
      border-bottom: 1px solid var(--border-color);
    }}

    .ch-icon {{
      width: 48px;
      height: 48px;
      border-radius: var(--radius-md);
      background: var(--primary-light);
      color: var(--primary);
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.5rem;
      flex-shrink: 0;
    }}

    .chapter-title {{
      font-size: 1.4rem;
      margin-bottom: 0.25rem;
    }}

    .chapter-subtitle {{
      color: var(--text-secondary);
      font-size: 0.95rem;
    }}

    /* Callout & Table styling in summary */
    .callout-box {{
      background: var(--bg-card-subtle);
      border: 1px solid var(--border-color);
      border-left: 4px solid var(--primary);
      border-radius: var(--radius-md);
      padding: 1.15rem 1.35rem;
      margin: 1.25rem 0;
      font-size: 0.95rem;
    }}

    .callout-box.tip {{
      border-left-color: var(--accent);
      background: var(--accent-light);
    }}

    .callout-box.warning {{
      border-left-color: var(--warning);
      background: var(--warning-light);
    }}

    .data-table-wrap {{
      overflow-x: auto;
      margin: 1.25rem 0;
      border-radius: var(--radius-md);
      border: 1px solid var(--border-color);
    }}

    .data-table {{
      width: 100%;
      border-collapse: collapse;
      font-size: 0.92rem;
      text-align: left;
    }}

    .data-table th {{
      background: var(--bg-pill);
      color: var(--text-main);
      padding: 0.85rem 1rem;
      font-family: var(--font-heading);
      font-weight: 600;
      border-bottom: 1px solid var(--border-color);
    }}

    .data-table td {{
      padding: 0.85rem 1rem;
      border-bottom: 1px solid var(--border-subtle);
      color: var(--text-secondary);
      line-height: 1.6;
    }}

    .data-table tr:last-child td {{
      border-bottom: none;
    }}

    .data-table tr:hover td {{
      background: var(--bg-card-subtle);
    }}

    /* Key points bullet list */
    .key-points-list {{
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      margin: 1rem 0;
    }}

    .key-points-list li {{
      position: relative;
      padding-left: 1.65rem;
      font-size: 0.95rem;
      color: var(--text-main);
    }}

    .key-points-list li::before {{
      content: '✓';
      position: absolute;
      left: 0;
      top: 0;
      color: var(--primary);
      font-weight: bold;
    }}

    /* ==========================================================================
       Footer & Floating Actions
       ========================================================================== */
    .site-footer {{
      background: var(--bg-card);
      border-top: 1px solid var(--border-color);
      padding: 2rem 1.25rem;
      text-align: center;
      margin-top: auto;
      font-size: 0.88rem;
      color: var(--text-muted);
    }}

    .floating-back-top {{
      position: fixed;
      bottom: 1.5rem;
      right: 1.5rem;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: var(--primary);
      color: white;
      border: none;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.1rem;
      box-shadow: var(--shadow-md);
      cursor: pointer;
      opacity: 0;
      pointer-events: none;
      transition: var(--transition-smooth);
      z-index: 999;
    }}

    .floating-back-top.show {{
      opacity: 1;
      pointer-events: auto;
    }}
  </style>
</head>
<body>

  <!-- ==========================================
       SITE HEADER
       ========================================== -->
  <header class="site-header">
    <div class="header-container">
      <a href="#" class="brand-area" onclick="switchTab('quiz'); return false;">
        <div class="brand-logo-icon">🌿</div>
        <div class="brand-titles">
          <span class="brand-course">EDP3502 • คณะศึกษาศาสตร์</span>
          <span class="brand-main">การช่วยเหลือและให้คำปรึกษาผู้เรียน</span>
        </div>
      </a>

      <!-- 3 Master Navigation Tabs -->
      <nav class="nav-tabs" role="tablist">
        <button class="nav-tab-btn active" id="tabBtn-quiz" onclick="switchTab('quiz')">
          <span>📝 คลังข้อสอบ</span>
          <span class="badge-count" id="headerQuizCount">60 ข้อ</span>
        </button>
        <button class="nav-tab-btn" id="tabBtn-flashcards" onclick="switchTab('flashcards')">
          <span>🗂️ แฟลชการ์ด</span>
          <span class="badge-count">40 ใบ</span>
        </button>
        <button class="nav-tab-btn" id="tabBtn-summary" onclick="switchTab('summary')">
          <span>📖 สรุปภาพรวม</span>
          <span class="badge-count">บทที่ 5-11</span>
        </button>
      </nav>

      <!-- Utilities: Theme & Font size -->
      <div class="header-actions">
        <select class="theme-select" id="themeSelect" onchange="changeTheme(this.value)" title="เลือกโทนสีถนอมสายตา">
          <option value="sage">🌿 เซจธรรมชาติ (สบายตา)</option>
          <option value="warm">🌾 เอิร์ธโทนอบอุ่น</option>
          <option value="night">🌙 ป่ารัตติกาล (ถนอมสายตา)</option>
        </select>
        <button class="font-size-btn" onclick="adjustFontSize(-1)" title="ลดขนาดตัวอักษร">A-</button>
        <button class="font-size-btn" onclick="adjustFontSize(1)" title="เพิ่มขนาดตัวอักษร">A+</button>
      </div>
    </div>
  </header>

  <!-- ==========================================
       MAIN APP CONTAINER
       ========================================== -->
  <main class="main-container">

    <!-- ========================================================
         VIEW 1: คลังข้อสอบ 60 ข้อ (QUIZ TAB)
         ======================================================== -->
    <section id="view-quiz" class="view-panel active">
      <!-- Hero -->
      <div class="hero-banner">
        <div class="hero-content">
          <h1>คลังข้อสอบจำลอง EDP3502 (60 ข้อ)</h1>
          <p>ครอบคลุมเนื้อหาบทที่ 5 - 11 แบ่งเป็น <strong>ประเด็นหลักและทฤษฎี 30 ข้อ</strong> และ <strong>ข้อสอบเชิงสถานการณ์และการประยุกต์ใช้ 30 ข้อ</strong> พร้อมเฉลยละเอียดและหลักคิดทางจิตวิทยา</p>
          <div class="hero-badges">
            <span class="chip-badge">✨ ครบ 60 ข้อ</span>
            <span class="chip-badge">⚡ โหมดฝึกฝน & โหมดสอบจริง</span>
            <span class="chip-badge accent">🎯 เน้นวิเคราะห์สถานการณ์จริง</span>
          </div>
        </div>
      </div>

      <!-- Controls & Filter Toolbar -->
      <div class="controls-card">
        <div class="control-row">
          <!-- Mode Switcher -->
          <div class="mode-switch-group">
            <button class="mode-btn active" id="modeBtn-practice" onclick="setQuizMode('practice')">
              <span>⚡ โหมดฝึกฝนทันที (เฉลยพร้อมอธิบาย)</span>
            </button>
            <button class="mode-btn" id="modeBtn-exam" onclick="setQuizMode('exam')">
              <span>🎯 โหมดสอบจริง (ตรวจตอนส่ง)</span>
            </button>
          </div>

          <!-- Question Type Filter -->
          <div class="filters-cluster">
            <select class="filter-select" id="chapterFilter" onchange="applyQuizFilters()">
              <option value="all">📚 ทุกบท (บทที่ 5 - 11)</option>
              <option value="5">บทที่ 5: กระบวนการให้คำปรึกษา 4 ขั้น</option>
              <option value="6">บทที่ 6: ตัวอย่างกระบวนการปรึกษา</option>
              <option value="7">บทที่ 7: ทักษะการให้คำปรึกษา</option>
              <option value="8">บทที่ 8: ทฤษฎีจิตวิเคราะห์ (Freud)</option>
              <option value="9">บทที่ 9: ทฤษฎีแอดเลอร์ (Adler)</option>
              <option value="10">บทที่ 10: บุคคลเป็นศูนย์กลาง (Rogers)</option>
              <option value="11">บทที่ 11: ทฤษฎีเกสตอลต์ (Perls)</option>
            </select>

            <select class="filter-select" id="typeFilter" onchange="applyQuizFilters()">
              <option value="all">🔍 ทุกประเภท (60 ข้อ)</option>
              <option value="concept">ตอนที่ 1: ประเด็นหลักและทฤษฎี (30 ข้อ)</option>
              <option value="situation">ตอนที่ 2: ข้อสอบเชิงสถานการณ์ (30 ข้อ)</option>
              <option value="flagged">🚩 ข้อที่ปักหมุดไว้</option>
              <option value="wrong">❌ ข้อที่ตอบผิด</option>
            </select>
          </div>

          <!-- Search box -->
          <div class="search-box-wrap">
            <span class="search-icon">🔍</span>
            <input type="text" class="search-input" id="quizSearchInput" placeholder="พิมพ์ค้นหาคีย์เวิร์ดในข้อสอบ..." oninput="applyQuizFilters()">
          </div>
        </div>

        <!-- Live Quiz Stats -->
        <div class="quiz-stats-summary">
          <div class="stat-pill">📋 แสดงอยู่: <strong id="statShownCount">60</strong>/60 ข้อ</div>
          <div class="stat-pill">✏️ ตอบแล้ว: <strong id="statAnsweredCount">0</strong>/60 ข้อ</div>
          <div class="stat-pill">🚩 ปักหมุด: <strong id="statFlaggedCount">0</strong> ข้อ</div>
          <div class="stat-pill" id="scoreDisplayPill" style="display: none;">🏆 คะแนน: <strong id="statScore">0</strong>/60</div>
        </div>
      </div>

      <!-- Quiz Main Layout (Questions List + Sticky Sidebar) -->
      <div class="quiz-layout">
        <!-- Left: Questions Container -->
        <div id="questionsContainer">
          <!-- Dynamically Rendered Questions -->
        </div>

        <!-- Right: Sticky Navigator Sidebar -->
        <aside class="quiz-sidebar">
          <div class="sidebar-header">
            <span class="sidebar-title">แผนที่ข้อสอบ</span>
            <span id="sidebarProgressText" style="font-size: 0.85rem; color: var(--text-muted); font-family: var(--font-heading);">0%</span>
          </div>

          <div class="progress-bar-wrap">
            <div class="progress-bar-fill" id="sidebarProgressBar"></div>
          </div>

          <!-- Question Jump Buttons (1 to 60) -->
          <div class="q-nav-grid" id="qNavGrid">
            <!-- Rendered via JS -->
          </div>

          <!-- Sidebar Actions -->
          <div class="sidebar-actions">
            <button class="btn-submit-exam" id="btnSubmitExam" onclick="submitExam()">
              <span>📊 ส่งข้อสอบ & ตรวจคะแนน</span>
            </button>
            <button class="btn-reset-quiz" onclick="resetQuiz()">
              <span>🔄 ล้างคำตอบทั้งหมด / ทำใหม่</span>
            </button>
          </div>
        </aside>
      </div>
    </section>

    <!-- ========================================================
         VIEW 2: แฟลชการ์ดความรู้ (FLASHCARDS TAB)
         ======================================================== -->
    <section id="view-flashcards" class="view-panel">
      <!-- Hero -->
      <div class="hero-banner">
        <div class="hero-content">
          <h1>แฟลชการ์ดความรู้ความจำ (40 คอนเซปต์หลัก)</h1>
          <p>ทบทวนนิยาม แก่นคิด คำสำคัญ และจุดที่มักออกข้อสอบ คลิกหรือกด <kbd>Spacebar</kbd> เพื่อพลิกดูคำอธิบาย พร้อมระบบติดตามความจำ</p>
          <div class="hero-badges">
            <span class="chip-badge">🗂️ 40 แฟลชการ์ด</span>
            <span class="chip-badge accent">🔄 พลิกแบบ 3D</span>
            <span class="chip-badge">✅ ระบบเช็คความจำ</span>
          </div>
        </div>
      </div>

      <div class="flashcards-container">
        <!-- Flashcard Controls -->
        <div class="fc-controls">
          <div class="filters-cluster">
            <select class="filter-select" id="fcChapterFilter" onchange="filterFlashcards()">
              <option value="all">📚 ทุกหมวดหมู่ (40 ใบ)</option>
              <option value="5">บทที่ 5: กระบวนการให้คำปรึกษา</option>
              <option value="6">บทที่ 6: ตัวอย่างกระบวนการปรึกษา</option>
              <option value="7">บทที่ 7: ทักษะการให้คำปรึกษา</option>
              <option value="8">บทที่ 8: จิตวิเคราะห์ (Freud)</option>
              <option value="9">บทที่ 9: แอดเลอร์ (Adler)</option>
              <option value="10">บทที่ 10: บุคคลเป็นศูนย์กลาง (Rogers)</option>
              <option value="11">บทที่ 11: เกสตอลต์ (Perls)</option>
            </select>

            <button class="fc-btn" onclick="shuffleFlashcards()" title="สลับลำดับการ์ดแบบสุ่ม">
              <span>🔀 สุ่มลำดับ</span>
            </button>
          </div>

          <div style="display: flex; gap: 0.5rem; align-items: center;">
            <button class="fc-btn" id="fcViewToggleBtn" onclick="toggleFlashcardView()">
              <span>📋 สลับดูการ์ดทั้งหมด</span>
            </button>
          </div>
        </div>

        <!-- Single Card Slider Scene -->
        <div id="fcSliderSceneWrap">
          <div class="fc-scene" onclick="flipCurrentCard()">
            <div class="fc-card" id="activeFlashcard">
              <!-- Front Side -->
              <div class="fc-face fc-front">
                <div class="fc-top-meta">
                  <span class="fc-ch-badge" id="fcFrontBadge">บทที่ 5</span>
                  <span class="fc-progress-num" id="fcProgressNum">1 / 40</span>
                </div>
                <div class="fc-center-content">
                  <div class="chip-badge accent" id="fcFrontTag" style="margin-bottom: 0.75rem;">คีย์เวิร์ด</div>
                  <h2 class="fc-term" id="fcFrontTerm">4 ขั้นตอนของกระบวนการให้คำปรึกษา</h2>
                  <p class="fc-hint" id="fcFrontHint">คลิกเพื่อดูคำอธิบายและจุดออกสอบ</p>
                </div>
                <div class="fc-bottom-tap">
                  <span>↺ คลิกที่การ์ด หรือกด Spacebar เพื่อพลิกดูคำอธิบาย</span>
                </div>
              </div>

              <!-- Back Side -->
              <div class="fc-face fc-back">
                <div class="fc-top-meta">
                  <span class="fc-ch-badge" id="fcBackBadge">เฉลยสาระสำคัญ</span>
                  <span class="fc-progress-num" id="fcBackProgressNum">1 / 40</span>
                </div>
                <div>
                  <h3 class="fc-back-title" id="fcBackTitle">หัวข้อสาระสำคัญ</h3>
                  <div class="fc-definition" id="fcBackDef">คำอธิบาย</div>
                  <div class="fc-takeaway-box" id="fcBackTakeaway">แก่นคิดสำคัญ</div>
                  <div class="fc-exam-box" id="fcBackExam">จุดเน้นออกสอบ</div>
                </div>
                <div class="fc-bottom-tap" style="margin-top: 1rem;">
                  <span>↺ คลิกอีกครั้งเพื่อพลิกกลับด้านหน้า</span>
                </div>
              </div>
            </div>
          </div>

          <!-- Bottom Navigation Bar for Slider -->
          <div class="fc-nav-bar">
            <button class="fc-btn" onclick="prevFlashcard()">
              <span>◀ ก่อนหน้า</span>
            </button>

            <!-- Memory Status Buttons -->
            <div class="fc-status-group">
              <button class="fc-btn fc-btn-review" onclick="markCardStatus('review')">
                <span>⏳ ยังไม่แม่น</span>
              </button>
              <button class="fc-btn fc-btn-memorized" onclick="markCardStatus('memorized')">
                <span>✅ จำได้แล้ว</span>
              </button>
            </div>

            <button class="fc-btn" onclick="nextFlashcard()">
              <span>ถัดไป ▶</span>
            </button>
          </div>

          <!-- Memorization Counter -->
          <div style="text-align: center; margin-top: 1rem; font-size: 0.88rem; color: var(--text-muted);">
            จำได้แล้ว: <strong id="fcMemorizedCount" style="color: var(--success);">0</strong> / 
            ต้องทบทวน: <strong id="fcReviewCount" style="color: var(--warning);">0</strong> / 
            ทั้งหมด: <strong id="fcTotalActive">40</strong> ใบ
          </div>
        </div>

        <!-- Grid View of All Cards (Initially Hidden) -->
        <div class="fc-grid-view" id="fcGridView">
          <!-- Rendered via JS -->
        </div>

      </div>
    </section>

    <!-- ========================================================
         VIEW 3: สรุปภาพรวมเนื้อหา (SUMMARY TAB)
         ======================================================== -->
    <section id="view-summary" class="view-panel">
      <!-- Hero -->
      <div class="hero-banner">
        <div class="hero-content">
          <h1>สรุปภาพรวมเนื้อหา EDP3502 (บทที่ 5 - 11)</h1>
          <p>เจาะลึก 4 ขั้นตอนกระบวนการ ทักษะการให้คำปรึกษา และ 4 ทฤษฎีหลัก (Freud, Adler, Rogers, Perls) พร้อมตารางสังเคราะห์เปรียบเทียบหมัดต่อหมัด</p>
          <div class="hero-badges">
            <span class="chip-badge">📖 เนื้อหาฉบับสมบูรณ์</span>
            <span class="chip-badge">📊 ตารางเปรียบเทียบ 4 ทฤษฎี</span>
            <span class="chip-badge accent">🎯 สรุปจุดออกสอบประจำบท</span>
          </div>
        </div>
      </div>

      <div class="summary-layout">
        <!-- Sticky Table of Contents -->
        <aside class="summary-toc">
          <div class="toc-title">📑 สารบัญเนื้อหา</div>
          <ul class="toc-list">
            <li class="toc-item"><a href="#ch-compare">🏆 ตารางเปรียบเทียบ 4 ทฤษฎี</a></li>
            <li class="toc-item"><a href="#ch5-summary">📌 บทที่ 5: กระบวนการ 4 ขั้น</a></li>
            <li class="toc-item"><a href="#ch6-summary">📌 บทที่ 6: ตัวอย่างเคส & การส่งต่อ</a></li>
            <li class="toc-item"><a href="#ch7-summary">📌 บทที่ 7: คลังทักษะการปรึกษา</a></li>
            <li class="toc-item"><a href="#ch8-summary">📌 บทที่ 8: จิตวิเคราะห์ (Freud)</a></li>
            <li class="toc-item"><a href="#ch9-summary">📌 บทที่ 9: แอดเลอร์ (Adler)</a></li>
            <li class="toc-item"><a href="#ch10-summary">📌 บทที่ 10: บุคคลเป็นศูนย์กลาง</a></li>
            <li class="toc-item"><a href="#ch11-summary">📌 บทที่ 11: เกสตอลต์ (Perls)</a></li>
          </ul>
        </aside>

        <!-- Main Summary Articles -->
        <div class="summary-content">

          <!-- 1. COMPARISON TABLE -->
          <article class="chapter-section" id="ch-compare">
            <div class="chapter-header">
              <div class="ch-icon">🏆</div>
              <div>
                <h2 class="chapter-title">ตารางเปรียบเทียบหมัดต่อหมัด 4 ทฤษฎีหลัก</h2>
                <div class="chapter-subtitle">Freud vs Adler vs Rogers vs Perls</div>
              </div>
            </div>

            <p>การเข้าใจความแตกต่างเชิงปรัชญาและจุดเน้นของแต่ละสำนักจะช่วยให้วิเคราะห์สถานการณ์และเลือกเทคนิคช่วยเหลือผู้เรียนได้อย่างถูกต้องแม่นยำ:</p>

            <div class="data-table-wrap">
              <table class="data-table">
                <thead>
                  <tr>
                    <th>ประเด็นเปรียบเทียบ</th>
                    <th>จิตวิเคราะห์ (Freud)</th>
                    <th>จิตวิทยาบุคคล (Adler)</th>
                    <th>บุคคลเป็นศูนย์กลาง (Rogers)</th>
                    <th>เกสตอลต์ (Perls)</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>ผู้ก่อตั้ง</strong></td>
                    <td>Sigmund Freud</td>
                    <td>Alfred Adler</td>
                    <td>Carl Rogers</td>
                    <td>Fritz Perls</td>
                  </tr>
                  <tr>
                    <td><strong>ทัศนะต่อมนุษย์</strong></td>
                    <td>มองแง่ลบ (Pessimistic) ขับเคลื่อนด้วยแรงดิบ สัญชาตญาณไร้เหตุผล</td>
                    <td>มองแง่บวก มีเป้าหมายสู่อนาคต (Teleology) มุ่งสู่ความสมบูรณ์</td>
                    <td>มองแง่บวกอย่างยิ่ง มีพลังมุ่งสู่ความงอกงามสูงสุด (Self-actualizing)</td>
                    <td>มองเป็นองค์รวม (Holism) ร่างกายและจิตประสานกันอย่างแนบแน่น</td>
                  </tr>
                  <tr>
                    <td><strong>สาเหตุของปัญหา</strong></td>
                    <td>ความขัดแย้งของ Id-Ego-Superego และปมบาดแผลในวัยเด็กที่ถูกเก็บกด</td>
                    <td>การเป็น "คนหมดกำลังใจ" (Discouraged) และปมด้อยที่ไม่ได้รับการชดเชยที่ถูกทาง</td>
                    <td>ภาวะไม่สอดคล้อง (Incongruence) ระหว่าง Self-concept กับ ประสบการณ์จริง</td>
                    <td>ไม่อยู่กับปัจจุบัน (Here & Now) ขาดการตระหนักรู้ มีเรื่องคั่งค้าง (Unfinished Business)</td>
                  </tr>
                  <tr>
                    <td><strong>มิติเวลาที่เน้น</strong></td>
                    <td>อดีต (วัยเด็ก 0-6 ขวบ)</td>
                    <td>อนาคต (เป้าหมายชีวิตและวิถีชีวิต)</td>
                    <td>ปัจจุบันขณะ (Here and Now)</td>
                    <td>ปัจจุบัน ที่นี่และเดี๋ยวนี้ (Here & Now)</td>
                  </tr>
                  <tr>
                    <td><strong>บทบาทผู้ให้คำปรึกษา</strong></td>
                    <td>ผู้เชี่ยวชาญ/นักสืบ ตีความจิตไร้สำนึก วางตัวเป็นกลาง</td>
                    <td>ผู้สร้างสัมพันธภาพ เป็นตัวแบบ ประเมินวิถีชีวิต และให้กำลังใจ</td>
                    <td>ผู้เอื้ออำนวย (Facilitator) เป็นกระจกสะท้อน ไม่สั่งสอน ไม่ชี้นำ</td>
                    <td>ผู้กระตุ้นการรู้ตัว (Mirror) สร้าง Creative Frustration ให้พึ่งตนเอง</td>
                  </tr>
                  <tr>
                    <td><strong>เทคนิคสำคัญ</strong></td>
                    <td>Free Association, Transference, Dream Analysis, แปลความ</td>
                    <td>The Question, Push-Button, Encouragement, Catching Oneself</td>
                    <td>Empathy, Genuineness, Unconditional Positive Regard, สะท้อนความรู้สึก</td>
                    <td>Empty Chair, Gestalt Dream Work, Top Dog vs Underdog, สัมผัสผัสสะ</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </article>

          <!-- 2. CHAPTER 5 -->
          <article class="chapter-section" id="ch5-summary">
            <div class="chapter-header">
              <div class="ch-icon">🌱</div>
              <div>
                <h2 class="chapter-title">บทที่ 5: กระบวนการและทักษะการให้คำปรึกษา 4 ขั้นตอน</h2>
                <div class="chapter-subtitle">โครงสร้างทางวิทยาศาสตร์และศิลปะในการช่วยเหลือผู้เรียน</div>
              </div>
            </div>

            <p>การให้คำปรึกษาเป็นกระบวนการที่เป็นทั้ง <strong>วิทยาศาสตร์</strong> (มีขั้นตอนที่เป็นระบบ ตรวจสอบได้) และ <strong>ศิลปะ</strong> (การรับฟังด้วยความอาทร เข้าถึงโลกภายในของผู้เรียน) โดยดำเนินไปตาม 4 ขั้นตอนหลัก:</p>

            <div class="callout-box">
              <strong>1. ขั้นเริ่มต้นและสร้างสัมพันธภาพ (Initial Stage & Rapport Building)</strong>
              <p style="margin-top: 0.35rem;">เป้าหมายคือสร้างบรรยากาศที่ปลอดภัย ไว้วางใจ และอบอุ่นให้เร็วที่สุด เพื่อให้ผู้เรียนกล้าเปิดเผยเรื่องราว มีการจัดโครงสร้าง (Structuring) ตกลงเรื่องบทบาท เวลา และ <em>หลักการรักษาความลับ (Confidentiality)</em></p>
            </div>

            <div class="callout-box">
              <strong>2. ขั้นสำรวจตนเพื่อทำความเข้าใจกับปัญหา (Exploration & Understanding)</strong>
              <p style="margin-top: 0.35rem;">กระตุ้นให้ผู้เรียนประเมินตนเอง สำรวจภาพลักษณ์ และเปิดเผยความรู้สึกอย่างแท้จริง มักเกิด <strong>การระบายความรู้สึก (Catharsis)</strong> ซึ่งช่วยคลายความตึงเครียด แต่มีข้อพึงระวังคือ <em>ผู้รับบริการอาจเข้าใจผิดว่าปัญหาจบแล้ว</em> ทำให้หมดไฟในการลงมือแก้ปัญหาจริง</p>
            </div>

            <div class="callout-box">
              <strong>3. ขั้นจัดการ (ดำเนินการ) กับปัญหา (Working Through / Action)</strong>
              <p style="margin-top: 0.35rem;">ขั้นที่ผู้ให้คำปรึกษาใช้ทักษะการฟัง การสะท้อน การเผชิญหน้า และการแปลความ เพื่อช่วยให้ผู้เรียนเกิดทางเลือกใหม่ และ <em>ลงมือแสดงพฤติกรรมใหม่ (New Behaviors)</em> โดยรับผิดชอบต่อชีวิตตนเอง</p>
            </div>

            <div class="callout-box">
              <strong>4. ขั้นการยุติการปรึกษา (Termination)</strong>
              <p style="margin-top: 0.35rem;">มี 3 เป้าหมายหลัก: (1) ประเมินความพร้อมในการใช้ชีวิตด้วยตนเอง (2) ทบทวนความก้าวหน้าและการเรียนรู้ (3) วางแผนรับมืออุปสรรคและเตรียมการส่งต่อหากจำเป็น ในขั้นนี้ไม่ควรรื้อฟื้นปมปัญหาใหม่ขึ้นมา</p>
            </div>
          </article>

          <!-- 3. CHAPTER 6 -->
          <article class="chapter-section" id="ch6-summary">
            <div class="chapter-header">
              <div class="ch-icon">🏫</div>
              <div>
                <h2 class="chapter-title">บทที่ 6: ตัวอย่างกระบวนการปรึกษา & การส่งต่อ</h2>
                <div class="chapter-subtitle">การนำ 4 ขั้นตอนไปประยุกต์ใช้จริงในโรงเรียน</div>
              </div>
            </div>

            <div class="callout-box tip">
              <strong>กรณีศึกษา 'ทะนง' (อายุ 15 ปี นักเรียนมัธยม):</strong>
              <ul class="key-points-list" style="margin-top: 0.5rem;">
                <li><strong>ปัญหา:</strong> ขาดเรียนบ่อย ระเบิดอารมณ์โกรธใส่ครูและเพื่อน แฟนสาวขู่เลิกหากคุมอารมณ์ไม่ได้</li>
                <li><strong>ขั้นที่ 1:</strong> ครูรับฟังอย่างอบอุ่น ไม่ด่วนตำหนิเรื่องขาดเรียน ทำให้ทะนงรู้สึกปลอดภัยและยอมเปิดใจ</li>
                <li><strong>ขั้นที่ 2:</strong> สำรวจพบว่าความโกรธเกิดจากความรู้สึกด้อยและคิดว่าตนไม่มีคุณค่าในสายตาผู้อื่น</li>
                <li><strong>ขั้นที่ 3:</strong> ฝึกพฤติกรรมใหม่ในการนับ 1-10 กำหนดลมหายใจ และฝึกสื่อสารความต้องการอย่างสร้างสรรค์</li>
                <li><strong>ขั้นที่ 4:</strong> ทบทวนความสำเร็จ ทะนงคุมอารมณ์ได้ดีขึ้น เพื่อนๆ ยอมรับมากขึ้น จึงยุติการปรึกษาด้วยความภาคภูมิใจ</li>
              </ul>
            </div>

            <div class="callout-box warning">
              <strong>หลักการส่งต่อ (Referral) ที่ต้องจำแม่น:</strong>
              <p style="margin-top: 0.35rem;">ผู้ให้คำปรึกษาต้องส่งต่อเมื่อปัญหาเกินขอบเขตความสามารถ จริยธรรม หรือมีภาวะอันตรายร้ายแรง (เช่น ซึมเศร้ารุนแรง สารเสพติด พฤติกรรมทำร้ายตนเอง) โดยต้องชี้แจงเหตุผลและ <em>ได้รับความยินยอมจากผู้รับบริการเสมอ</em></p>
            </div>
          </article>

          <!-- 4. CHAPTER 7 -->
          <article class="chapter-section" id="ch7-summary">
            <div class="chapter-header">
              <div class="ch-icon">💬</div>
              <div>
                <h2 class="chapter-title">บทที่ 7: คลังทักษะการให้คำปรึกษาที่จำเป็นสำหรับครู</h2>
                <div class="chapter-subtitle">เครื่องมือสื่อสารเชิงลึกเพื่อสร้างสัมพันธภาพและการหยั่งรู้</div>
              </div>
            </div>

            <div class="data-table-wrap">
              <table class="data-table">
                <thead>
                  <tr>
                    <th>ทักษะ</th>
                    <th>สาระสำคัญและหลักการปฏิบัติ</th>
                    <th>ข้อควรระวัง / ตัวอย่าง</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>การฟัง (Listening)</strong></td>
                    <td>ฟังทั้งภาษาพูด (Verbal) และภาษาท่าทาง (Non-verbal) สังเกตสายตา น้ำเสียง และเนื้อหาที่จงใจข้ามไป</td>
                    <td>อย่าด่วนคิดหาทางออกในใจขณะที่ผู้เรียนกำลังเล่าเรื่อง</td>
                  </tr>
                  <tr>
                    <td><strong>การใช้ความเงียบ (Silence)</strong></td>
                    <td>เปิดพื้นที่ให้ผู้เรียนได้จมอยู่ในภวังค์ความคิดและสัมผัสความรู้สึก สื่อสารว่าเราไม่เร่งรัดหรือควบคุม</td>
                    <td>ห้ามรีบพูดแทรกหรือเปลี่ยนเรื่องเพียงเพราะรู้สึกอึดอัด</td>
                  </tr>
                  <tr>
                    <td><strong>การสะท้อนข้อความ (Paraphrasing)</strong></td>
                    <td>เรียบเรียงถ้อยคำใหม่เพื่อจับสาระสำคัญของเนื้อหาในระดับผิวเผิน</td>
                    <td>ผู้เรียนยังอาจติดอยู่ในบทบาทของ "เหยื่อผู้ถูกกระทำ"</td>
                  </tr>
                  <tr>
                    <td><strong>การสะท้อนความรู้สึก (Reflecting)</strong></td>
                    <td>ระบุอารมณ์ความรู้สึกและดึง <em>ความคาดหวังในตนเอง</em> ขึ้นมาให้ตระหนักรู้ มีพลังลึกซึ้งกว่า</td>
                    <td>ช่วยให้ผู้เรียนเห็นว่าตนเองสามารถควบคุมและรับผิดชอบชีวิตตนเองได้</td>
                  </tr>
                  <tr>
                    <td><strong>การตั้งคำถาม (Questioning)</strong></td>
                    <td>เน้นคำถามปลายเปิด (Open-ended) เพื่อส่งเสริมการสำรวจตนเอง</td>
                    <td><strong>หลีกเลี่ยงคำว่า 'ทำไม' (Why)</strong> เพราะทำให้รู้สึกถูกไต่สวนและตั้งการป้องกันตัว</td>
                  </tr>
                  <tr>
                    <td><strong>การท้าทาย / เผชิญหน้า (Confrontation)</strong></td>
                    <td>สะท้อนความไม่สอดคล้อง (Discrepancy) ระหว่างคำพูดกับการกระทำ หรือความคิดกับความรู้สึก</td>
                    <td>ต้องทำเมื่อมีความไว้วางใจแน่นแฟ้นแล้ว และสื่อสารด้วยความห่วงใย ไม่ก้าวร้าว</td>
                  </tr>
                  <tr>
                    <td><strong>การให้ข้อมูล (Giving Info)</strong></td>
                    <td>ให้ข้อเท็จจริง แหล่งข้อมูล หรือทางเลือกที่จำเป็นต่อการตัดสินใจ</td>
                    <td>ต้องไม่เป็นการสั่งสอน หรือยัดเยียดค่านิยมของผู้ให้คำปรึกษา</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </article>

          <!-- 5. CHAPTER 8 -->
          <article class="chapter-section" id="ch8-summary">
            <div class="chapter-header">
              <div class="ch-icon">🧠</div>
              <div>
                <h2 class="chapter-title">บทที่ 8: ทฤษฎีจิตวิเคราะห์ (Sigmund Freud)</h2>
                <div class="chapter-subtitle">เครื่องจักรกลพลังงานจิต จิตไร้สำนึก และ 7 กลไกป้องกันตนเอง</div>
              </div>
            </div>

            <p>ฟรอยด์มองมนุษย์เหมือนระบบพลังงานกลศาสตร์ พลังงานจิต (Libido) มีปริมาณคงที่ สัญชาตญาณมี 2 ขั้วคือ <strong>Eros (สัญชาตญาณชีวิต/เพศ)</strong> และ <strong>Thanatos (สัญชาตญาณความตาย/ทำลายล้าง)</strong></p>

            <div class="callout-box">
              <strong>โครงสร้างจิต 3 องค์ประกอบ:</strong>
              <ul class="key-points-list">
                <li><strong>Id (อิด):</strong> ติดตัวมาแต่กำเนิด แหล่งสัญชาตญาณดิบ ยึด <em>Pleasure Principle</em> (สุขสำราญทันที ไม่สนใจเหตุผล)</li>
                <li><strong>Ego (อีโก้):</strong> พัฒนาทีหลัง ทำหน้าที่เป็น "คนกลาง/ผู้จัดการ" ไกล่เกลี่ย Id กับ Superego ยึด <em>Reality Principle</em></li>
                <li><strong>Superego (ซูเปอร์อีโก้):</strong> มโนธรรม สำนึกผิดชอบชั่วดี กฎเกณฑ์สังคม ยึด <em>Perfection Principle</em></li>
              </ul>
            </div>

            <h3 style="margin: 1.5rem 0 0.75rem;">7 กลไกการปกป้องตนเองของอีโก้ (Ego Defense Mechanisms)</h3>
            <div class="data-table-wrap">
              <table class="data-table">
                <thead>
                  <tr>
                    <th>กลไกป้องกันตนเอง</th>
                    <th>ความหมายเชิงจิตวิทยา</th>
                    <th>ตัวอย่างพฤติกรรมในโรงเรียน</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>1. การเก็บกด (Repression)</strong></td>
                    <td>กดเรื่องเจ็บปวดลงสู่จิตไร้สำนึก ลืมไปเลยเหมือนไม่เคยเกิดขึ้น</td>
                    <td>จำเหตุการณ์ถูกทำร้ายในวัยเด็กไม่ได้เลย</td>
                  </tr>
                  <tr>
                    <td><strong>2. การฉายภาพ (Projection)</strong></td>
                    <td>ตัวเองเป็น/คิดลบ แต่โยนความผิดนั้นไปให้คนอื่น</td>
                    <td>ตนเองแอบโกงข้อสอบ แต่เที่ยวไปบอกว่าเพื่อนทุกคนขี้โกง</td>
                  </tr>
                  <tr>
                    <td><strong>3. การกระทำตรงกันข้าม (Reaction Formation)</strong></td>
                    <td>ซ่อนความรู้สึกแท้จริง แล้วแสดงออกตรงข้ามอย่างโอเวอร์แอ็กติ้ง</td>
                    <td>เกลียดเพื่อนมาก แต่เจอหน้าวิ่งไปกอดและชมหวานเจี๊ยบ</td>
                  </tr>
                  <tr>
                    <td><strong>4. การติดตรึง (Fixation)</strong></td>
                    <td>หยุดชะงัก ไม่ยอมก้าวไปสู่วัยถัดไปเพราะกลัวล้มเหลว</td>
                    <td>ไม่ยอมรับงานใหม่ที่ท้าทาย ยึดติดกับตำแหน่งเดิมที่ปลอดภัย</td>
                  </tr>
                  <tr>
                    <td><strong>5. การถดถอย (Regression)</strong></td>
                    <td>ถอยหลังกลับไปทำตัวเป็นเด็กเมื่อเผชิญความเครียดรุนแรง</td>
                    <td>นักศึกษาปี 1 ปรับตัวไม่ได้ ร้องไห้งอแง ปัสสาวะรดที่นอน หนีกลับบ้าน</td>
                  </tr>
                  <tr>
                    <td><strong>6. การเลียนแบบ (Identification)</strong></td>
                    <td>รับเอาค่านิยมคนอื่นมาใส่ตัว (4 ชนิด: หลงตัวเอง, เป้าหมาย, สูญเสีย, <strong>เชิงอำนาจ</strong>)</td>
                    <td><strong>การเลียนแบบเชิงอำนาจ (Authority)</strong> จากพ่อแม่ คือตัวสร้าง Superego</td>
                  </tr>
                  <tr>
                    <td><strong>7. การย้ายที่ (Displacement)</strong></td>
                    <td>เปลี่ยนที่ระบายพลังงานความก้าวร้าว ไปลงกับเป้าหมายที่ปลอดภัยกว่า</td>
                    <td>ถูกพ่อตีที่บ้าน มาโรงเรียนเตะเก้าอี้และตวาดใส่เพื่อน</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div class="callout-box tip">
              <strong>เทคนิคสำคัญของจิตวิเคราะห์:</strong> Free Association (เชื่อมโยงอิสระ), Dream Analysis (Manifest content จำได้ vs Latent content ซ่อนเร้น), Transference (การถ่ายโยงความรู้สึกมาใส่ครู ➔ ครูต้องสำรวจตนเองก่อนเสมอ), และกฎเหล็ก 4 ข้อในการแปลความ
            </div>
          </article>

          <!-- 6. CHAPTER 9 -->
          <article class="chapter-section" id="ch9-summary">
            <div class="chapter-header">
              <div class="ch-icon">🤝</div>
              <div>
                <h2 class="chapter-title">บทที่ 9: ทฤษฎีจิตวิทยาบุคคลของแอดเลอร์ (Alfred Adler)</h2>
                <div class="chapter-subtitle">Teleology ความสนใจทางสังคม เด็กหมดกำลังใจ และ 8 เทคนิคการบำบัด</div>
              </div>
            </div>

            <p>แอดเลอร์เชื่อว่ามนุษย์มีเป้าหมายสู่อนาคต (Teleology) มุ่งชดเชยความรู้สึกด้อยเพื่อไปสู่ความสมบูรณ์ มนุษย์มีธรรมชาติที่ต้องการเป็นส่วนหนึ่งของสังคม (Social Interest) และเด็กที่มีปัญหาคือ <strong>"คนหมดกำลังใจ ไม่ใช่ผู้ป่วย" (Discouraged, not sick)</strong></p>

            <h3 style="margin: 1.5rem 0 0.75rem;">4 เป้าหมายพฤติกรรมปัญหาของเด็ก & ปฏิกิริยาของครู</h3>
            <div class="data-table-wrap">
              <table class="data-table">
                <thead>
                  <tr>
                    <th>เป้าหมายของเด็ก</th>
                    <th>พฤติกรรมที่เด็กแสดงออก</th>
                    <th>ความรู้สึกของครู</th>
                    <th>แนวทางช่วยเหลือของครู</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>1. เรียกร้องความสนใจ (Attention Seeking)</strong></td>
                    <td>ก่อกวน ทำตัวตลก พูดแทรก ทำตัวอ่อนแอ</td>
                    <td><strong>รำคาญใจ เหนื่อยหน่าย (Annoyed)</strong></td>
                    <td>ให้ความสนใจเชิงบวกเมื่อเด็กทำดี และเพิกเฉยต่อการเรียกร้องความสนใจที่ไม่เหมาะสม</td>
                  </tr>
                  <tr>
                    <td><strong>2. แสวงหาอำนาจ (Power Seeking)</strong></td>
                    <td>ดื้อรั้น ท้าทายกฎเกณฑ์ เถียงหัวชนฝา</td>
                    <td><strong>โกรธ ถูกคุกคาม (Threatened)</strong></td>
                    <td>ไม่ประจันหน้า เลี่ยงการต่อสู้เชิงอำนาจ ให้มีส่วนร่วมวางกฎและมอบบทบาทสำคัญ</td>
                  </tr>
                  <tr>
                    <td><strong>3. เพื่อแก้แค้น (Revenge)</strong></td>
                    <td>ทำร้ายจิตใจ ก้าวร้าว ทำลายข้าวของ ประชดรุนแรง</td>
                    <td><strong>เจ็บปวด เสียใจ ถูกทำร้าย (Hurt)</strong></td>
                    <td>สร้างสัมพันธภาพที่อบอุ่น ไม่ตอบโต้ด้วยความรุนแรง ให้เขารู้ว่ายังคงได้รับความรัก</td>
                  </tr>
                  <tr>
                    <td><strong>4. ประกาศความพ่ายแพ้ (Inadequacy)</strong></td>
                    <td>ยอมจำนน ไม่พยายามทำอะไร แกล้งทำเป็นโง่</td>
                    <td><strong>หมดหวัง ท้อแท้ สิ้นปัญญา (Despair)</strong></td>
                    <td>ไม่ยอมแพ้ไปกับเด็ก ซอยงานเป็นขั้นเล็กๆ ให้สัมผัสความสำเร็จ และให้กำลังใจสม่ำเสมอ</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div class="callout-box">
              <strong>ลีลาชีวิต 4 แบบ (Life Styles):</strong>
              <p style="margin-top: 0.35rem;">1) <em>ลีลาปกครอง (Ruling):</em> ชอบคุมคนอื่น ก้าวร้าว สนใจสังคมต่ำ 2) <em>ลีลาได้รับ (Getting):</em> คอยพึ่งพาคนอื่น เป็นผู้รับ สนใจสังคมต่ำ 3) <em>ลีลาหลีกหนี (Avoiding):</em> กลัวแพ้ หนีปัญหา สนใจสังคมต่ำที่สุด 4) <strong>ลีลาทำประโยชน์แก่สังคม (Socially Useful):</strong> สุขภาพจิตสมบูรณ์ สนใจสังคมสูง มุ่งมั่นแก้ปัญหาด้วยความกล้าหาญ</p>
            </div>

            <div class="callout-box tip">
              <strong>คลัง 8 เทคนิคของแอดเลอร์:</strong>
              1) Modeling (เป็นตัวแบบ) 2) Paradoxical Intention (จงใจทำให้ฉงน ท้าให้ทำอาการนั้นเพิ่ม) 3) Creating Images (สร้างภาพจินตนาการ) 4) <strong>The Question (คำถามวิเศษแยกกาย vs จิต)</strong> 5) Catching Oneself (การเตือนสติรู้ทันตนเอง) 6) <strong>Push-Button (กดปุ่มเลือกอารมณ์ ชี้ว่าเราสร้างอารมณ์เอง)</strong> 7) <strong>Encouragement (การให้กำลังใจ - หัวใจสำคัญที่สุด)</strong> 8) Doing for Others (การทำประโยชน์แก่ผู้อื่น)
            </div>
          </article>

          <!-- 7. CHAPTER 10 -->
          <article class="chapter-section" id="ch10-summary">
            <div class="chapter-header">
              <div class="ch-icon">🌿</div>
              <div>
                <h2 class="chapter-title">บทที่ 10: การให้คำปรึกษาแบบบุคคลเป็นศูนย์กลาง (Carl Rogers)</h2>
                <div class="chapter-subtitle">พลังความงอกงาม Incongruence และ 3 เงื่อนไขจำเป็น (Core Conditions)</div>
              </div>
            </div>

            <p>โรเจอรส์มองมนุษย์มี <strong>Self-Actualizing Tendency</strong> (พลังมุ่งสู่ความงอกงามสูงสุดตามธรรมชาติ) ผู้รับบริการไม่ใช่คนป่วย แต่มีทรัพยากรภายในครบถ้วน หน้าที่ของครูคือสร้างบรรยากาศที่ปราศจากการประเมินตัดสิน (Non-evaluative climate)</p>

            <div class="callout-box">
              <strong>มโนทัศน์เรื่อง Incongruence (ความไม่สอดคล้อง):</strong>
              <p style="margin-top: 0.35rem;">ความขัดแย้งระหว่าง <strong>ภาพลักษณ์ของตน (Self-concept)</strong> กับ <strong>ประสบการณ์จริง (Organismic Experience)</strong> ก่อให้เกิดสัญญาณเตือน 3 ด้าน: <em>ทางสรีระ</em> (ใจสั่น เหงื่อออก มือสั่น ปวดหัว), <em>ทางอารมณ์</em> (กระวนกระวาย หงุดหงิด วิตกกังวล), และ <em>ทางความคิด</em> (สับสน ขัดแย้งในตนเอง)</p>
            </div>

            <div class="callout-box tip">
              <strong>การปรับภาพลักษณ์ตนใหม่ (Reorganizing Self):</strong>
              <p style="margin-top: 0.35rem;">เกณฑ์ความสำเร็จคือการยอมรับความจริงว่า ตนเองมีทั้งด้านบวกและด้านลบ <strong>เป็นทั้ง 'เทวดาและปีศาจ'</strong> มีทั้งความโกรธ อิจฉา ควบคู่กับความอบอุ่น เมตตา เมื่อยอมรับได้โดยไม่ต้องสวมหน้ากาก อาการตึงเครียดทางกายจะยุติลง</p>
            </div>

            <h3 style="margin: 1.5rem 0 0.75rem;">3 เงื่อนไขจำเป็นของผู้ให้การปรึกษา (Core Conditions)</h3>
            <div class="data-table-wrap">
              <table class="data-table">
                <thead>
                  <tr>
                    <th>เงื่อนไขจำเป็น</th>
                    <th>ความหมายเชิงลึก</th>
                    <th>องค์ประกอบ / คุณลักษณะสำคัญ</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>1. Empathy (ความเข้าใจลึกซึ้ง)</strong></td>
                    <td>ก้าวเข้าสู่โลกภายในของผู้เรียน มองเห็นและรู้สึกเสมือนเป็นตัวเขา โดยไม่สูญเสียตัวตนตนเอง</td>
                    <td>ใช้น้ำเสียงอบอุ่น ตั้งใจจดจ่อ (Attending) สังเกตอวัจนภาษา และสะท้อนความรู้สึก</td>
                  </tr>
                  <tr>
                    <td><strong>2. Genuineness / Congruence (ความจริงแท้)</strong></td>
                    <td>ซื่อตรง ไม่เสแสร้ง ภายในกับภายนอกตรงกัน ไม่สวมหน้ากากผู้เชี่ยวชาญ</td>
                    <td><strong>5 คุณลักษณะ:</strong> Role-free (ไร้บทบาท), Spontaneous (เป็นธรรมชาติ), Non-defensive (ไม่แก้ตัว/ไม่ปกป้องตน), Consistent (คงเส้นคงวา), Self-disclosure (แบ่งปันตนอย่างเหมาะสม)</td>
                  </tr>
                  <tr>
                    <td><strong>3. Unconditional Positive Regard (ยอมรับทางบวกไม่มีเงื่อนไข)</strong></td>
                    <td>ยอมรับนับถือคุณค่าและศักดิ์ศรีความเป็นมนุษย์อย่างบริสุทธิ์ใจ ปราศจากการประเมินตัดสิน (Non-judgmental)</td>
                    <td>แยกคุณค่าของบุคคลออกจากค่านิยมส่วนตัว (เช่น เรื่องเพศสภาพ ความเชื่อ ความผิดพลาด)</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <p style="font-size: 0.88rem; color: var(--text-muted); margin-top: 0.5rem;"><em>วิวัฒนาการชื่อทฤษฎี:</em> การให้คำปรึกษาแบบไม่นำทาง (Non-directive) ➔ แบบผู้รับบริการเป็นศูนย์กลาง (Client-centered) ➔ แบบบุคคลเป็นศูนย์กลาง (Person-centered)</p>
          </article>

          <!-- 8. CHAPTER 11 -->
          <article class="chapter-section" id="ch11-summary">
            <div class="chapter-header">
              <div class="ch-icon">🎨</div>
              <div>
                <h2 class="chapter-title">บทที่ 11: ทฤษฎีการให้คำปรึกษาแบบเกสตอลต์ (Fritz Perls)</h2>
                <div class="chapter-subtitle">ส่วนรวมทั้งหมดที่มีความหมาย Here & Now ภาพและพื้น และ 5 ชั้นอาการประสาท</div>
              </div>
            </div>

            <p>เกสตอลต์ (Gestalt) แปลว่า <strong>"ส่วนรวมทั้งหมดที่มีความหมาย" (A meaningful whole)</strong> กายและจิตเป็นองค์รวมแยกกันไม่ได้ เน้นอยู่กับ <strong>"ที่นี่และเดี๋ยวนี้" (Here and Now)</strong> ไม่ถาม "ทำไม" แต่ถาม "อะไรและอย่างไร" เชื่อว่า <em>การมีสติตระหนักรู้ (Awareness) มีพลังบำบัดในตนเอง</em></p>

            <div class="callout-box">
              <strong>มโนทัศน์ ภาพ (Figure) และ พื้น (Ground) กับ สุขภาพจิต:</strong>
              <ul class="key-points-list">
                <li><strong>ผู้มีสุขภาพจิตดี:</strong> ภาพเด่นชัด แตกต่างจากพื้น และสลับสับเปลี่ยนกลับไปเป็นพื้นได้อย่างยืดหยุ่นเมื่อได้รับการตอบสนอง</li>
                <li><strong>ย้ำคิดย้ำทำ (OCD):</strong> ภาพติดแน่น ไม่ยอมถอยกลับไปเป็นพื้น ขาดช่องว่างให้ความต้องการใหม่เข้ามา</li>
                <li><strong>บุคลิกภาพแปรปรวน/ฮิสทีเรีย:</strong> ภาพสลับไปมาเร็วเกินไป พรั่งพรูจนจิตใจว้าวุ่น</li>
                <li><strong>ไม่รู้ว่าต้องการอะไร:</strong> ภาพไม่ปรากฏ จมหายอยู่ในพื้นพร่ามัว</li>
              </ul>
            </div>

            <h3 style="margin: 1.5rem 0 0.75rem;">5 ระดับของอาการประสาท (5 Layers of Neurosis)</h3>
            <p>1. <strong>ระดับเสแสร้ง (Phony):</strong> สวมบทบาท เล่นละครตามสังคม ➔ 2. <strong>ระดับกลัว (Phobic):</strong> กลัวความเปราะบาง กลัวถูกปฏิเสธ ➔ 3. <strong>ระดับทางตัน (Impasse):</strong> จุดวิกฤต รู้สึกว่างเปล่า เรียกร้องให้คนอื่นมาอุ้มชูแทน ➔ 4. <strong>ระดับระเบิดทางตัน (Implosive):</strong> เริ่มรู้ตัว เผชิญความจริง ปลดล็อกปมคั่งค้าง ➔ 5. <strong>ระดับระเบิดสู่ภายนอก (Explosive):</strong> ปลดปล่อยพลังงาน มีชีวิตชีวา เป็นองค์รวม (Wholeness)</p>

            <h3 style="margin: 1.5rem 0 0.75rem;">4 กลไกขัดขวางการติดต่อสัมพันธ์ (Boundary Disturbances)</h3>
            <div class="data-table-wrap">
              <table class="data-table">
                <thead>
                  <tr>
                    <th>กลไกทางจิต</th>
                    <th>ลักษณะนิยาม</th>
                    <th>ตัวอย่างพฤติกรรม</th>
                  </tr>
                </thead>
                <tbody>
                  <tr>
                    <td><strong>1. การกลืนค่านิยม (Introjection)</strong></td>
                    <td>กลืนความคิดคนอื่นโดยไม่เคี้ยวไตร่ตรอง</td>
                    <td>เป็นคนว่าง่าย รับทุกอย่างที่อาจารย์บอก แต่ข้างในไม่รู้ว่าตัวเองเชื่ออะไรแท้จริง</td>
                  </tr>
                  <tr>
                    <td><strong>2. การฉายภาพ (Projection)</strong></td>
                    <td>ปฏิเสธความรู้สึกตนเอง แล้วโยนบาปไปให้ผู้อื่น</td>
                    <td>ตนเองมีความต้องการทางเพศ แต่ไปต่อว่าและประณามว่าคนอื่นแต่งตัวยั่วยวน</td>
                  </tr>
                  <tr>
                    <td><strong>3. การย้อนกลับสู่ตน (Retroflection)</strong></td>
                    <td>กระทำต่อตนเองในสิ่งที่อยากกระทำต่อผู้อื่นภายนอก</td>
                    <td>โกรธคนอื่นแต่หันมาทำร้ายตัวเอง กัดเล็บ กัดปาก ทุบตีตนเอง กรีดแขน</td>
                  </tr>
                  <tr>
                    <td><strong>4. ความหละหลวม (Confluence)</strong></td>
                    <td>ไม่มีเส้นแบ่งอาณาเขต กลืนเป็นเนื้อเดียวกับคนอื่น</td>
                    <td>เพื่อนในกลุ่มต้องคิดเหมือนกัน ไปไหนไปด้วยกัน ถ้าใครแยกตัวจะโกรธจัด</td>
                  </tr>
                </tbody>
              </table>
            </div>

            <div class="callout-box tip">
              <strong>คลังเทคนิคเด่นของเกสตอลต์:</strong>
              1) <strong>Empty Chair (เก้าอี้ว่าง 3 ขั้น):</strong> สื่อความรู้สึกดี ➔ ปลดปล่อยความแค้น ➔ กล่าวคำอำลาปล่อยวาง 2) <strong>Gestalt Dream Work:</strong> สวมบทบาทเป็นทุกสิ่งในฝันเพื่อดึงกลับมาเป็นตนเอง 3) <strong>Top Dog vs Underdog:</strong> สงครามระหว่างจอมบงการ vs จอมตลบแตลง/ดื้อเงียบ (Underdog คือฝ่ายควบคุมพฤติกรรมจริง) นั่งสลับเก้าอี้เจรจากัน 4) การสังเกตสัมผัสผัสสะทางกาย และการให้อยู่กับความรู้สึก (Staying with the feeling)
            </div>
          </article>

        </div>
      </div>
    </section>

  </main>

  <!-- ==========================================
       SCORE REPORT MODAL
       ========================================== -->
  <div class="score-modal-backdrop" id="scoreModalBackdrop" onclick="closeScoreModal(event)">
    <div class="score-modal" onclick="event.stopPropagation()">
      <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 1rem;">
        <h2 style="font-size: 1.4rem; color: var(--text-main);">📊 ผลการสอบจำลอง EDP3502</h2>
        <button onclick="closeScoreModal()" style="background: none; border: none; font-size: 1.5rem; cursor: pointer; color: var(--text-muted);">&times;</button>
      </div>

      <div class="score-summary-grid">
        <div class="score-card-item">
          <div class="score-val" id="modalFinalScore">0</div>
          <div class="score-lbl">คะแนนที่ได้ (เต็ม 60)</div>
        </div>
        <div class="score-card-item">
          <div class="score-val" id="modalPercentage" style="color: var(--accent);">0%</div>
          <div class="score-lbl">คิดเป็นร้อยละ</div>
        </div>
        <div class="score-card-item">
          <div class="score-val" id="modalGrade" style="color: var(--success);">-</div>
          <div class="score-lbl">การประเมินผล</div>
        </div>
      </div>

      <h4 style="font-size: 1rem; margin: 1.25rem 0 0.65rem;">คะแนนจำแนกตามรายบท</h4>
      <div id="modalChapterBreakdown" style="display: flex; flex-direction: column; gap: 0.5rem;">
        <!-- Filled by JS -->
      </div>

      <div style="display: flex; gap: 0.75rem; margin-top: 1.5rem;">
        <button class="btn-submit-exam" style="flex: 1;" onclick="reviewWrongQuestions()">
          <span>🔍 ดูเฉพาะข้อที่ตอบผิด</span>
        </button>
        <button class="fc-btn" style="flex: 1; justify-content: center;" onclick="closeScoreModal()">
          <span>ทบทวนข้อสอบต่อ</span>
        </button>
      </div>
    </div>
  </div>

  <!-- Floating Back to Top Button -->
  <button class="floating-back-top" id="backToTopBtn" onclick="window.scrollTo({{ top: 0, behavior: 'smooth' }})" title="กลับขึ้นด้านบน">
    ▲
  </button>

  <!-- ==========================================
       SITE FOOTER
       ========================================== -->
  <footer class="site-footer">
    <p><strong>EDP3502 การช่วยเหลือและให้คำปรึกษาผู้เรียน</strong> • คลังข้อสอบ 60 ข้อ • แฟลชการ์ด 40 ใบ • สรุปภาพรวมบทที่ 5 - 11</p>
    <p style="margin-top: 0.35rem; font-size: 0.8rem; color: var(--text-light);">ออกแบบด้วยโทนสีถนอมสายตาสำหรับนักศึกษาครู เพื่อการทบทวนและเตรียมสอบอย่างมีประสิทธิภาพ</p>
  </footer>

  <!-- ==========================================
       JAVASCRIPT APPLICATION LOGIC
       ========================================== -->
  <script>
    // Load Question & Flashcard Datasets
    const questionsData = {questions_json_str};
    const flashcardsData = {flashcards_json_str};

    // State Variables
    let userAnswers = {{}}; // qid -> choiceKey
    let flaggedQuestions = new Set();
    let quizMode = 'practice'; // 'practice' or 'exam'
    let currentQuizFilter = {{ chapter: 'all', type: 'all', search: '' }};
    let examSubmitted = false;

    // Flashcard State
    let activeFcIndex = 0;
    let filteredFlashcards = [...flashcardsData];
    let fcMemoryState = {{}}; // fcId -> 'memorized' | 'review'
    let isFcFlipped = false;
    let isFcGridView = false;

    // Font size state
    let currentFontSizeOffset = 0;

    // Initialize application on load
    document.addEventListener('DOMContentLoaded', () => {{
      loadSavedState();
      renderQuestions();
      renderQNavGrid();
      updateQuizStats();
      renderCurrentFlashcard();
      renderFlashcardsGrid();
      setupScrollSpy();
    }});

    // LocalStorage helper
    function loadSavedState() {{
      try {{
        const savedTheme = localStorage.getItem('edp3502_theme');
        if (savedTheme) {{
          document.documentElement.setAttribute('data-theme', savedTheme);
          document.getElementById('themeSelect').value = savedTheme;
        }}
        const savedAnswers = localStorage.getItem('edp3502_answers');
        if (savedAnswers) userAnswers = JSON.parse(savedAnswers);

        const savedFlags = localStorage.getItem('edp3502_flags');
        if (savedFlags) flaggedQuestions = new Set(JSON.parse(savedFlags));

        const savedMemory = localStorage.getItem('edp3502_fc_memory');
        if (savedMemory) fcMemoryState = JSON.parse(savedMemory);
      }} catch (e) {{
        console.warn('Storage read error', e);
      }}
    }}

    function saveState() {{
      try {{
        localStorage.setItem('edp3502_answers', JSON.stringify(userAnswers));
        localStorage.setItem('edp3502_flags', JSON.stringify([...flaggedQuestions]));
        localStorage.setItem('edp3502_fc_memory', JSON.stringify(fcMemoryState));
      }} catch (e) {{}}
    }}

    // ==========================================
    // THEME & VIEW MANAGEMENT
    // ==========================================
    function changeTheme(themeName) {{
      document.documentElement.setAttribute('data-theme', themeName);
      localStorage.setItem('edp3502_theme', themeName);
    }}

    function adjustFontSize(delta) {{
      currentFontSizeOffset = Math.max(-2, Math.min(4, currentFontSizeOffset + delta));
      const baseSize = 16 + currentFontSizeOffset;
      document.documentElement.style.fontSize = baseSize + 'px';
    }}

    function switchTab(tabId) {{
      document.querySelectorAll('.view-panel').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.nav-tab-btn').forEach(el => el.classList.remove('active'));

      const activeView = document.getElementById('view-' + tabId);
      const activeBtn = document.getElementById('tabBtn-' + tabId);
      if (activeView) activeView.classList.add('active');
      if (activeBtn) activeBtn.classList.add('active');

      window.scrollTo({{ top: 0, behavior: 'smooth' }});
    }}

    // ==========================================
    // QUIZ LOGIC (60 Questions)
    // ==========================================
    function setQuizMode(mode) {{
      quizMode = mode;
      document.getElementById('modeBtn-practice').classList.toggle('active', mode === 'practice');
      document.getElementById('modeBtn-exam').classList.toggle('active', mode === 'exam');

      // If switching to practice, show explanations for answered questions
      // If switching to exam (before submit), hide explanations
      renderQuestions();
      renderQNavGrid();
    }}

    function applyQuizFilters() {{
      currentQuizFilter.chapter = document.getElementById('chapterFilter').value;
      currentQuizFilter.type = document.getElementById('typeFilter').value;
      currentQuizFilter.search = document.getElementById('quizSearchInput').value.trim().toLowerCase();
      renderQuestions();
    }}

    function getFilteredQuestions() {{
      return questionsData.filter(q => {{
        // Chapter filter
        if (currentQuizFilter.chapter !== 'all' && q.chapter.toString() !== currentQuizFilter.chapter) {{
          return false;
        }}
        // Type filter
        if (currentQuizFilter.type === 'concept' && q.type !== 'concept') return false;
        if (currentQuizFilter.type === 'situation' && q.type !== 'situation') return false;
        if (currentQuizFilter.type === 'flagged' && !flaggedQuestions.has(q.id)) return false;
        if (currentQuizFilter.type === 'wrong') {{
          if (!userAnswers[q.id] || userAnswers[q.id] === q.answer) return false;
        }}
        // Keyword Search
        if (currentQuizFilter.search) {{
          const fullText = (q.question + ' ' + Object.values(q.choices).join(' ') + ' ' + q.explanation).toLowerCase();
          if (!fullText.includes(currentQuizFilter.search)) return false;
        }}
        return true;
      }});
    }}

    function renderQuestions() {{
      const container = document.getElementById('questionsContainer');
      const filtered = getFilteredQuestions();

      document.getElementById('statShownCount').innerText = filtered.length;

      if (filtered.length === 0) {{
        container.innerHTML = `
          <div class="question-card" style="text-align: center; padding: 3rem 1.5rem;">
            <div style="font-size: 2.5rem; margin-bottom: 0.75rem;">🔍</div>
            <h3 style="margin-bottom: 0.5rem;">ไม่พบข้อสอบตามเงื่อนไขที่เลือก</h3>
            <p style="color: var(--text-muted); font-size: 0.95rem;">ลองเปลี่ยนการเลือกบท หรือล้างคำค้นหาดูอีกครั้ง</p>
            <button class="fc-btn" style="margin: 1rem auto 0;" onclick="resetFilters()">ล้างตัวกรองทั้งหมด</button>
          </div>
        `;
        return;
      }}

      let html = '';
      filtered.forEach(q => {{
        const qid = q.id;
        const selectedChoice = userAnswers[qid];
        const isFlagged = flaggedQuestions.has(qid);
        const isShowExpl = (quizMode === 'practice' && selectedChoice) || examSubmitted;

        html += `
          <div class="question-card ${{isFlagged ? 'flagged' : ''}}" id="q-card-${{qid}}">
            <div class="q-header">
              <div class="q-meta">
                <span class="q-number-badge">ข้อ ${{qid}}</span>
                <span class="q-chapter-tag">${{q.chapter_name}}</span>
                <span class="q-type-tag ${{q.type}}">${{q.type === 'situation' ? '🎯 สถานการณ์' : '💡 ทฤษฎี'}}</span>
              </div>
              <button class="flag-btn ${{isFlagged ? 'active' : ''}}" onclick="toggleFlag(${{qid}})" title="ปักหมุดข้อนี้เพื่อทบทวน">
                ${{isFlagged ? '🚩' : '🏳️'}}
              </button>
            </div>

            <div class="q-text">${{q.question}}</div>

            <div class="choices-list">
              ${{Object.entries(q.choices).map(([key, text]) => {{
                let choiceClass = 'choice-item';
                if (selectedChoice === key) choiceClass += ' selected';

                if (isShowExpl) {{
                  if (key === q.answer) {{
                    choiceClass += ' correct';
                  }} else if (selectedChoice === key && key !== q.answer) {{
                    choiceClass += ' wrong';
                  }}
                }}

                return `
                  <div class="${{choiceClass}}" onclick="selectChoice(${{qid}}, '${{key}}')">
                    <span class="choice-key">${{key}}</span>
                    <span>${{text}}</span>
                  </div>
                `;
              }}).join('')}}
            </div>

            <div class="explanation-box ${{isShowExpl ? 'show' : ''}}" id="expl-${{qid}}">
              <div class="explanation-title">
                <span>💡 คำอธิบายและเฉลยละเอียด (เฉลยข้อ ${{q.answer}}):</span>
              </div>
              <div>${{q.explanation}}</div>
            </div>
          </div>
        `;
      }});

      container.innerHTML = html;
      updateQuizStats();
    }}

    function selectChoice(qid, choiceKey) {{
      userAnswers[qid] = choiceKey;
      saveState();

      // In practice mode, reveal immediately on card
      if (quizMode === 'practice') {{
        renderQuestions();
      }} else {{
        // Exam mode: update selection styling without revealing correct answer
        const card = document.getElementById(`q-card-${{qid}}`);
        if (card) {{
          card.querySelectorAll('.choice-item').forEach(el => {{
            el.classList.remove('selected');
            if (el.querySelector('.choice-key').innerText.trim() === choiceKey) {{
              el.classList.add('selected');
            }}
          }});
        }}
      }}

      renderQNavGrid();
      updateQuizStats();
    }}

    function toggleFlag(qid) {{
      if (flaggedQuestions.has(qid)) {{
        flaggedQuestions.delete(qid);
      }} else {{
        flaggedQuestions.add(qid);
      }}
      saveState();
      renderQuestions();
      renderQNavGrid();
      updateQuizStats();
    }}

    function renderQNavGrid() {{
      const grid = document.getElementById('qNavGrid');
      let html = '';

      for (let i = 1; i <= 60; i++) {{
        const isAnswered = !!userAnswers[i];
        const isFlagged = flaggedQuestions.has(i);
        const q = questionsData.find(item => item.id === i);

        let statusClass = '';
        if (examSubmitted || (quizMode === 'practice' && isAnswered)) {{
          if (userAnswers[i] === q.answer) statusClass = 'correct';
          else if (isAnswered) statusClass = 'wrong';
        }} else if (isAnswered) {{
          statusClass = 'answered';
        }}

        if (isFlagged) statusClass += ' flagged';

        html += `
          <button class="q-nav-btn ${{statusClass}}" onclick="jumpToQuestion(${{i}})">
            ${{i}}
          </button>
        `;
      }}

      grid.innerHTML = html;
    }}

    function jumpToQuestion(qid) {{
      // Ensure the chapter/filter is set so the question is visible
      const q = questionsData.find(item => item.id === qid);
      if (q) {{
        let needRerender = false;
        if (currentQuizFilter.chapter !== 'all' && currentQuizFilter.chapter !== q.chapter.toString()) {{
          document.getElementById('chapterFilter').value = 'all';
          currentQuizFilter.chapter = 'all';
          needRerender = true;
        }}
        if (currentQuizFilter.type !== 'all') {{
          document.getElementById('typeFilter').value = 'all';
          currentQuizFilter.type = 'all';
          needRerender = true;
        }}
        if (currentQuizFilter.search) {{
          document.getElementById('quizSearchInput').value = '';
          currentQuizFilter.search = '';
          needRerender = true;
        }}
        if (needRerender) renderQuestions();

        setTimeout(() => {{
          const el = document.getElementById(`q-card-${{qid}}`);
          if (el) {{
            el.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
            el.style.boxShadow = '0 0 0 3px var(--primary)';
            setTimeout(() => el.style.boxShadow = '', 1500);
          }}
        }}, 50);
      }}
    }}

    function updateQuizStats() {{
      const answeredCount = Object.keys(userAnswers).length;
      document.getElementById('statAnsweredCount').innerText = answeredCount;
      document.getElementById('statFlaggedCount').innerText = flaggedQuestions.size;

      const progressPct = Math.round((answeredCount / 60) * 100);
      document.getElementById('sidebarProgressBar').style.width = progressPct + '%';
      document.getElementById('sidebarProgressText').innerText = progressPct + '%';

      if (quizMode === 'practice' || examSubmitted) {{
        let score = 0;
        questionsData.forEach(q => {{
          if (userAnswers[q.id] === q.answer) score++;
        }});
        document.getElementById('scoreDisplayPill').style.display = 'flex';
        document.getElementById('statScore').innerText = score;
      }} else {{
        document.getElementById('scoreDisplayPill').style.display = 'none';
      }}
    }}

    function submitExam() {{
      const answeredCount = Object.keys(userAnswers).length;
      if (answeredCount < 60) {{
        if (!confirm(`คุณตอบไปแล้ว ${{answeredCount}} จาก 60 ข้อ ต้องการส่งตรวจคะแนนเลยหรือไม่?`)) {{
          return;
        }}
      }}

      examSubmitted = true;
      let totalScore = 0;
      let chStats = {{}};

      questionsData.forEach(q => {{
        const ch = q.chapter;
        if (!chStats[ch]) chStats[ch] = {{ name: q.chapter_name, total: 0, score: 0 }};
        chStats[ch].total++;

        if (userAnswers[q.id] === q.answer) {{
          totalScore++;
          chStats[ch].score++;
        }}
      }});

      // Populate Modal
      document.getElementById('modalFinalScore').innerText = totalScore;
      const pct = Math.round((totalScore / 60) * 100);
      document.getElementById('modalPercentage').innerText = pct + '%';

      let grade = 'ผ่านเกณฑ์ดีเยี่ยม 🌟';
      if (pct < 50) grade = 'ต้องทบทวนเพิ่มเติม 📚';
      else if (pct < 70) grade = 'ผ่านเกณฑ์มาตรฐาน 👍';
      else if (pct < 85) grade = 'ดีมาก เก่งมาก 👏';
      document.getElementById('modalGrade').innerText = grade;

      // Breakdown by Chapter
      let bdHtml = '';
      for (const [ch, info] of Object.entries(chStats)) {{
        const chPct = Math.round((info.score / info.total) * 100);
        bdHtml += `
          <div style="background: var(--bg-card-subtle); padding: 0.6rem 0.85rem; border-radius: var(--radius-sm); border: 1px solid var(--border-color); font-size: 0.88rem;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.25rem;">
              <span><strong>${{info.name}}</strong></span>
              <span>${{info.score}} / ${{info.total}} ข้อ (${{chPct}}%)</span>
            </div>
            <div style="width: 100%; height: 6px; background: var(--bg-pill); border-radius: var(--radius-full); overflow: hidden;">
              <div style="height: 100%; width: ${{chPct}}%; background: ${{chPct >= 70 ? 'var(--success)' : (chPct >= 50 ? 'var(--warning)' : 'var(--danger)')}};"></div>
            </div>
          </div>
        `;
      }}
      document.getElementById('modalChapterBreakdown').innerHTML = bdHtml;

      document.getElementById('scoreModalBackdrop').classList.add('show');
      renderQuestions();
      renderQNavGrid();
      updateQuizStats();
    }}

    function closeScoreModal() {{
      document.getElementById('scoreModalBackdrop').classList.remove('show');
    }}

    function reviewWrongQuestions() {{
      closeScoreModal();
      document.getElementById('typeFilter').value = 'wrong';
      applyQuizFilters();
    }}

    function resetQuiz() {{
      if (confirm('ต้องการล้างคำตอบและการปักหมุดทั้งหมดเพื่อเริ่มทำใหม่หรือไม่?')) {{
        userAnswers = {{}};
        flaggedQuestions.clear();
        examSubmitted = false;
        saveState();
        renderQuestions();
        renderQNavGrid();
        updateQuizStats();
      }}
    }}

    function resetFilters() {{
      document.getElementById('chapterFilter').value = 'all';
      document.getElementById('typeFilter').value = 'all';
      document.getElementById('quizSearchInput').value = '';
      applyQuizFilters();
    }}

    // ==========================================
    // FLASHCARD LOGIC (40 Cards)
    // ==========================================
    function filterFlashcards() {{
      const chVal = document.getElementById('fcChapterFilter').value;
      if (chVal === 'all') {{
        filteredFlashcards = [...flashcardsData];
      }} else {{
        filteredFlashcards = flashcardsData.filter(fc => fc.chapter.toString() === chVal);
      }}
      activeFcIndex = 0;
      isFcFlipped = false;
      document.getElementById('activeFlashcard').classList.remove('flipped');
      renderCurrentFlashcard();
      if (isFcGridView) renderFlashcardsGrid();
    }}

    function shuffleFlashcards() {{
      filteredFlashcards.sort(() => Math.random() - 0.5);
      activeFcIndex = 0;
      isFcFlipped = false;
      document.getElementById('activeFlashcard').classList.remove('flipped');
      renderCurrentFlashcard();
      if (isFcGridView) renderFlashcardsGrid();
    }}

    function renderCurrentFlashcard() {{
      if (filteredFlashcards.length === 0) return;
      const fc = filteredFlashcards[activeFcIndex];

      // Front
      document.getElementById('fcFrontBadge').innerText = fc.chapter_name;
      document.getElementById('fcProgressNum').innerText = `${{activeFcIndex + 1}} / ${{filteredFlashcards.length}}`;
      document.getElementById('fcFrontTag').innerText = fc.tag;
      document.getElementById('fcFrontTerm').innerText = fc.term;
      document.getElementById('fcFrontHint').innerText = fc.front_hint;

      // Back
      document.getElementById('fcBackBadge').innerText = fc.chapter_name;
      document.getElementById('fcBackProgressNum').innerText = `${{activeFcIndex + 1}} / ${{filteredFlashcards.length}}`;
      document.getElementById('fcBackTitle').innerText = fc.back_title;
      document.getElementById('fcBackDef').innerHTML = fc.definition;
      document.getElementById('fcBackTakeaway').innerHTML = '💡 ' + fc.key_takeaway;
      document.getElementById('fcBackExam').innerHTML = '🎯 จุดเน้นข้อสอบ: ' + fc.exam_point;

      updateFcStats();
    }}

    function flipCurrentCard() {{
      isFcFlipped = !isFcFlipped;
      document.getElementById('activeFlashcard').classList.toggle('flipped', isFcFlipped);
    }}

    function nextFlashcard() {{
      if (activeFcIndex < filteredFlashcards.length - 1) {{
        activeFcIndex++;
      }} else {{
        activeFcIndex = 0; // loop
      }}
      isFcFlipped = false;
      document.getElementById('activeFlashcard').classList.remove('flipped');
      renderCurrentFlashcard();
    }}

    function prevFlashcard() {{
      if (activeFcIndex > 0) {{
        activeFcIndex--;
      }} else {{
        activeFcIndex = filteredFlashcards.length - 1; // loop
      }}
      isFcFlipped = false;
      document.getElementById('activeFlashcard').classList.remove('flipped');
      renderCurrentFlashcard();
    }}

    function markCardStatus(status) {{
      const fc = filteredFlashcards[activeFcIndex];
      if (fc) {{
        fcMemoryState[fc.id] = status;
        saveState();
        updateFcStats();
        nextFlashcard();
      }}
    }}

    function updateFcStats() {{
      let memCount = 0;
      let revCount = 0;
      filteredFlashcards.forEach(fc => {{
        if (fcMemoryState[fc.id] === 'memorized') memCount++;
        if (fcMemoryState[fc.id] === 'review') revCount++;
      }});
      document.getElementById('fcMemorizedCount').innerText = memCount;
      document.getElementById('fcReviewCount').innerText = revCount;
      document.getElementById('fcTotalActive').innerText = filteredFlashcards.length;
    }}

    function toggleFlashcardView() {{
      isFcGridView = !isFcGridView;
      document.getElementById('fcSliderSceneWrap').style.display = isFcGridView ? 'none' : 'block';
      document.getElementById('fcGridView').style.display = isFcGridView ? 'grid' : 'none';
      document.getElementById('fcViewToggleBtn').innerHTML = isFcGridView ? '<span>🗂️ สลับโหมดการ์ดเดี่ยว</span>' : '<span>📋 สลับดูการ์ดทั้งหมด</span>';
      if (isFcGridView) renderFlashcardsGrid();
    }}

    function renderFlashcardsGrid() {{
      const grid = document.getElementById('fcGridView');
      let html = '';
      filteredFlashcards.forEach((fc, idx) => {{
        const status = fcMemoryState[fc.id];
        let statusBadge = '';
        if (status === 'memorized') statusBadge = '<span style="color: var(--success); font-size: 0.8rem;">✅ จำได้</span>';
        if (status === 'review') statusBadge = '<span style="color: var(--warning); font-size: 0.8rem;">⏳ ทบทวน</span>';

        html += `
          <div class="fc-grid-card" onclick="openFlashcardFromGrid(${{idx}})">
            <div>
              <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
                <span class="chip-badge" style="font-size: 0.72rem;">${{fc.chapter_name}}</span>
                ${{statusBadge}}
              </div>
              <h4 style="font-size: 1.1rem; margin-bottom: 0.4rem;">${{fc.term}}</h4>
              <p style="font-size: 0.88rem; color: var(--text-secondary); line-height: 1.5;">${{fc.front_hint}}</p>
            </div>
            <div style="font-size: 0.8rem; color: var(--primary); font-weight: 600; margin-top: 0.75rem;">
              คลิกเพื่อเปิดอ่านรายละเอียด ➔
            </div>
          </div>
        `;
      }});
      grid.innerHTML = html;
    }}

    function openFlashcardFromGrid(idx) {{
      activeFcIndex = idx;
      toggleFlashcardView();
      renderCurrentFlashcard();
      window.scrollTo({{ top: 200, behavior: 'smooth' }});
    }}

    // Keyboard Shortcuts for Flashcards
    document.addEventListener('keydown', (e) => {{
      const flashcardsTab = document.getElementById('view-flashcards');
      if (flashcardsTab && flashcardsTab.classList.contains('active')) {{
        if (e.code === 'Space') {{
          e.preventDefault();
          flipCurrentCard();
        }} else if (e.code === 'ArrowRight') {{
          nextFlashcard();
        }} else if (e.code === 'ArrowLeft') {{
          prevFlashcard();
        }}
      }}
    }});

    // ==========================================
    // SUMMARY SCROLL SPY & BACK TO TOP
    // ==========================================
    function setupScrollSpy() {{
      const backBtn = document.getElementById('backToTopBtn');
      window.addEventListener('scroll', () => {{
        if (window.scrollY > 300) {{
          backBtn.classList.add('show');
        }} else {{
          backBtn.classList.remove('show');
        }}
      }});
    }}
  </script>
</body>
</html>
'''

# Write to index.html and update แบบทดสอบ_EDP3502_บทที่5-11.html
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)
print("Successfully wrote index.html!")

with open("แบบทดสอบ_EDP3502_บทที่5-11.html", "w", encoding="utf-8") as f:
    f.write(html_content)
print("Successfully updated แบบทดสอบ_EDP3502_บทที่5-11.html!")
