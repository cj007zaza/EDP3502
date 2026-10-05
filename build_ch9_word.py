import os
import shutil
import docx
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import parse_xml, OxmlElement
from docx.oxml.ns import nsdecls, qn

def create_document():
    doc = docx.Document()

    # Set page margins to 1 inch (72pt)
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1.0)
        section.bottom_margin = Inches(1.0)
        section.left_margin = Inches(1.0)
        section.right_margin = Inches(1.0)
        section.page_width = Inches(8.27)  # A4
        section.page_height = Inches(11.69)

    # Palette
    C_NAVY = RGBColor(30, 58, 138)      # #1E3A8A Primary Title / Heading 1
    C_BLUE = RGBColor(37, 99, 235)      # #2563EB Subheading / Heading 2
    C_TEAL = RGBColor(13, 148, 136)     # #0D9488 Accent
    C_BODY = RGBColor(30, 41, 59)       # #1E293B Body text
    C_MUTED = RGBColor(100, 116, 139)   # #64748B Secondary / dates
    C_AMBER = RGBColor(217, 119, 6)     # #D97706 Highlights
    
    HEX_PRIMARY = "1E3A8A"
    HEX_LIGHT_BLUE = "EFF6FF"
    HEX_BORDER_BLUE = "3B82F6"
    HEX_LIGHT_GREEN = "F0FDF4"
    HEX_BORDER_GREEN = "22C55E"
    HEX_LIGHT_AMBER = "FEF3C7"
    HEX_BORDER_AMBER = "F59E0B"
    HEX_GRAY_ROW = "F8FAFC"
    HEX_HEADER_GRAY = "E2E8F0"

    FONT_FAMILY = "TH Sarabun New"

    def apply_font(run, size_pt=16, bold=False, italic=False, color=C_BODY, font_name=FONT_FAMILY):
        run.font.name = font_name
        run.font.size = Pt(size_pt)
        run.bold = bold
        run.italic = italic
        if color:
            run.font.color.rgb = color
        rPr = run._r.get_or_add_rPr()
        rFonts = parse_xml(f'<w:rFonts {nsdecls("w")} w:ascii="{font_name}" w:hAnsi="{font_name}" w:cs="{font_name}"/>')
        rPr.append(rFonts)

    def set_cell_shading(cell, color_hex):
        tcPr = cell._tc.get_or_add_tcPr()
        shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{color_hex}"/>')
        tcPr.append(shd)

    def set_cell_margins(cell, top=140, bottom=140, left=180, right=180):
        tcPr = cell._tc.get_or_add_tcPr()
        tcMar = parse_xml(f'<w:tcMar {nsdecls("w")}><w:top w:w="{top}" w:type="dxa"/><w:bottom w:w="{bottom}" w:type="dxa"/><w:left w:w="{left}" w:type="dxa"/><w:right w:w="{right}" w:type="dxa"/></w:tcMar>')
        tcPr.append(tcMar)

    def set_table_borders(table, border_color="CBD5E1"):
        tblPr = table._tbl.tblPr
        borders = parse_xml(f'''
            <w:tblBorders {nsdecls("w")}>
                <w:top w:val="single" w:sz="6" w:space="0" w:color="{border_color}"/>
                <w:left w:val="none"/>
                <w:bottom w:val="single" w:sz="8" w:space="0" w:color="{border_color}"/>
                <w:right w:val="none"/>
                <w:insideH w:val="single" w:sz="4" w:space="0" w:color="{border_color}"/>
                <w:insideV w:val="none"/>
            </w:tblBorders>
        ''')
        tblPr.append(borders)

    def add_callout(text_list, title="💡 สาระสำคัญ", bg_color=HEX_LIGHT_BLUE, border_color=HEX_BORDER_BLUE):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        cell = table.cell(0, 0)
        cell.width = Inches(6.27)
        set_cell_shading(cell, bg_color)
        set_cell_margins(cell, top=160, bottom=160, left=220, right=200)

        tcPr = cell._tc.get_or_add_tcPr()
        borders = parse_xml(f'''
            <w:tcBorders {nsdecls("w")}>
                <w:top w:val="none"/>
                <w:left w:val="single" w:sz="36" w:space="0" w:color="{border_color}"/>
                <w:bottom w:val="none"/>
                <w:right w:val="none"/>
            </w:tcBorders>
        ''')
        tcPr.append(borders)

        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.15
        r_title = p.add_run(title)
        apply_font(r_title, size_pt=16, bold=True, color=C_NAVY)

        for item in text_list:
            p_item = cell.add_paragraph()
            p_item.paragraph_format.space_before = Pt(2)
            p_item.paragraph_format.space_after = Pt(2)
            p_item.paragraph_format.line_spacing = 1.15
            if isinstance(item, tuple):
                # (bold_prefix, text)
                r_pre = p_item.add_run(item[0])
                apply_font(r_pre, size_pt=15, bold=True, color=C_BODY)
                r_txt = p_item.add_run(item[1])
                apply_font(r_txt, size_pt=15, bold=False, color=C_BODY)
            else:
                r_txt = p_item.add_run(str(item))
                apply_font(r_txt, size_pt=15, bold=False, color=C_BODY)

        # Empty spacer paragraph after table
        p_sp = doc.add_paragraph()
        p_sp.paragraph_format.space_before = Pt(0)
        p_sp.paragraph_format.space_after = Pt(4)

    def add_dialogue_box(dialogues, title="💬 ตัวอย่างบทสนทนาการให้การปรึกษา"):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        cell = table.cell(0, 0)
        cell.width = Inches(6.27)
        set_cell_shading(cell, "F8FAFC")
        set_cell_margins(cell, top=140, bottom=140, left=200, right=180)

        tcPr = cell._tc.get_or_add_tcPr()
        borders = parse_xml(f'''
            <w:tcBorders {nsdecls("w")}>
                <w:top w:val="single" w:sz="6" w:space="0" w:color="CBD5E1"/>
                <w:left w:val="single" w:sz="24" w:space="0" w:color="64748B"/>
                <w:bottom w:val="single" w:sz="6" w:space="0" w:color="CBD5E1"/>
                <w:right w:val="single" w:sz="6" w:space="0" w:color="CBD5E1"/>
            </w:tcBorders>
        ''')
        tcPr.append(borders)

        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        r_head = p.add_run(title)
        apply_font(r_head, size_pt=15, bold=True, color=C_NAVY)

        for speaker, speech, note in dialogues:
            p_d = cell.add_paragraph()
            p_d.paragraph_format.space_before = Pt(2)
            p_d.paragraph_format.space_after = Pt(2)
            p_d.paragraph_format.line_spacing = 1.15
            
            r_spk = p_d.add_run(f"• {speaker}: ")
            apply_font(r_spk, size_pt=15, bold=True, color=C_BLUE if "ผู้ให้" in speaker else C_AMBER)
            
            r_spe = p_d.add_run(f'"{speech}" ')
            apply_font(r_spe, size_pt=15, bold=False, italic=True, color=C_BODY)
            
            if note:
                r_nt = p_d.add_run(f"({note})")
                apply_font(r_nt, size_pt=14, bold=False, italic=False, color=C_MUTED)

        p_sp = doc.add_paragraph()
        p_sp.paragraph_format.space_before = Pt(0)
        p_sp.paragraph_format.space_after = Pt(4)

    def add_h1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(14)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        apply_font(r, size_pt=20, bold=True, color=C_NAVY)
        return p

    def add_h2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        r = p.add_run(text)
        apply_font(r, size_pt=17, bold=True, color=C_BLUE)
        return p

    def add_body_p(text, bold_prefix="", bullet=False):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.line_spacing = 1.15
        if bullet:
            p.paragraph_format.left_indent = Inches(0.25)
            r_b = p.add_run("• ")
            apply_font(r_b, size_pt=16, bold=True, color=C_BLUE)
        if bold_prefix:
            r_pre = p.add_run(bold_prefix)
            apply_font(r_pre, size_pt=16, bold=True, color=C_BODY)
        r_txt = p.add_run(text)
        apply_font(r_txt, size_pt=16, bold=False, color=C_BODY)
        return p

    # ==========================
    # DOCUMENT COVER / HEADER
    # ==========================
    p_pre = doc.add_paragraph()
    p_pre.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_pre.paragraph_format.space_before = Pt(0)
    p_pre.paragraph_format.space_after = Pt(2)
    r_sub0 = p_pre.add_run("รายวิชา EDP3502 การช่วยเหลือและให้คำปรึกษาผู้เรียน")
    apply_font(r_sub0, size_pt=15, bold=True, color=C_MUTED)

    p_title = doc.add_paragraph()
    p_title.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_title.paragraph_format.space_before = Pt(4)
    p_title.paragraph_format.space_after = Pt(4)
    r_title = p_title.add_run("สรุปเนื้อหาบทที่ 9\nทฤษฎีการให้การปรึกษาแบบแอดเลอร์\n(Adlerian Counseling / Individual Psychology)")
    apply_font(r_title, size_pt=24, bold=True, color=C_NAVY)

    p_sub = doc.add_paragraph()
    p_sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_sub.paragraph_format.space_before = Pt(2)
    p_sub.paragraph_format.space_after = Pt(12)
    r_sub = p_sub.add_run("ฉบับสรุปสมบูรณ์ • เจาะลึกแนวคิด ทัศนะมนุษย์ วิถีชีวิต การประเมิน และ 8 เทคนิคการบำบัด")
    apply_font(r_sub, size_pt=15, bold=False, italic=True, color=C_MUTED)

    # Executive Overview Callout Box
    add_callout([
        ("ผู้ริเริ่มทฤษฎี: ", "อัลเฟรด แอดเลอร์ (Alfred Adler) จิตแพทย์ชาวออสเตรีย บิดาแห่งจิตวิทยาบุคคล (Individual Psychology)"),
        ("แก่นคิดสำคัญที่สุด (Core Mindset): ", "มนุษย์ไม่ได้ป่วยเพราะแรงขับใต้สำนึก แต่พฤติกรรมทุกอย่างมี 'เป้าหมายสู่อนาคต' คนที่มีปัญหาคือ 'คนหมดกำลังใจ' ไม่ใช่คนป่วย การบำบัดคือการฟื้นฟูกำลังใจและพัฒนา 'ความสนใจทางสังคม' (Social Interest)"),
        ("โครงสร้างเนื้อหาบทที่ 9: ", "ครอบคลุม 7 ส่วนหลัก: 1) ปรัชญามนุษย์ 2) งานชีวิต 3 ด้าน 3) ครอบครัวและพฤติกรรมปัญหา 4 ขั้น 4) คลังความเชื่อและปมด้อย 5) ลีลาชีวิต 4 แบบ 6) บทบาทการประเมิน 7) 8 เทคนิคการให้คำปรึกษา")
    ], title="📌 แถบสรุปภาพรวมบทเรียน (Executive Summary)", bg_color="EFF6FF", border_color="1E3A8A")

    # ==========================================
    # SECTION 1: มุมมองต่อธรรมชาติมนุษย์
    # ==========================================
    add_h1("ส่วนที่ 1: ปรัชญาและมุมมองต่อธรรมชาติมนุษย์ (View of Human Nature)")
    add_body_p("แอดเลอร์มีมุมมองต่อธรรมชาติของมนุษย์ที่เป็นเอกลักษณ์และแตกต่างจากจิตวิเคราะห์ดั้งเดิมของฟรอยด์อย่างสิ้นเชิง โดยมีหลักการสำคัญดังนี้:")

    add_body_p(" มนุษย์ขับเคลื่อนไปข้างหน้า ไม่หยุดนิ่งอยู่กับที่ มีเป้าหมายชีวิตส่วนตัวเพื่อพัฒนาตนเองให้ก้าวข้ามความไม่สมบูรณ์ไปสู่ความสมบูรณ์แบบ (Striving for Perfection / Superiority)", bold_prefix="1. มองมนุษย์ในแง่บวกและมีพลังสร้างสรรค์ (Positive & Creative Power):", bullet=True)
    add_body_p(" มนุษย์ไม่ได้ตกเป็นทาสของสิ่งแวดล้อมหรืออดีตที่ผ่านไปแล้ว แม้สิ่งแวดล้อมจะมีอิทธิพล แต่มนุษย์มีเจตจำนงและพลังสร้างสรรค์ที่จะเลือกตอบสนองและกำหนดวิถีทางของตนเอง", bold_prefix="2. มีอิสระและเสรีภาพในการเลือก (Freedom & Agency):", bullet=True)
    add_body_p(" มนุษย์เป็นส่วนหนึ่งของระบบตั้งแต่ครอบครัว โรงเรียน ไปจนถึงชุมชนใหญ่ การเข้าใจบุคคลต้องเข้าใจสัมพันธภาพที่เขามีต่อระบบสังคมรอบตัว", bold_prefix="3. มนุษย์เป็นองค์รวมและเป็นส่วนหนึ่งของระบบ (Systemic & Holistic View):", bullet=True)
    add_body_p(" เป็นคุณลักษณะที่ติดตัวมาแต่กำเนิด มนุษย์มีธรรมชาติที่ต้องการเป็นส่วนหนึ่ง มีพฤติกรรมเพื่อการแลกเปลี่ยนและเกื้อกูลต่อสังคม", bold_prefix="4. ความสนใจทางสังคม (Social Interest / Gemeinschaftsgefühl):", bullet=True)
    add_body_p(" มนุษย์มีแนวโน้มแสดงพฤติกรรมตามการรับรู้และความเชื่อส่วนบุคคล (Private Logic) ไม่ว่าความเชื่อนั้นจะมีเหตุผลหรือบิดเบือนก็ตาม", bold_prefix="5. พฤติกรรมเป็นไปตามการรับรู้และความเชื่อ (Subjective Perception):", bullet=True)

    # ==========================================
    # SECTION 2: งานหลักของชีวิต 3 ด้าน
    # ==========================================
    add_h1("ส่วนที่ 2: งานหลักของชีวิต 3 ด้าน (The Three Life Tasks)")
    add_body_p("แอดเลอร์ชี้ว่า สิ่งชี้นำที่แสดงว่าบุคคลสามารถเผชิญกับชีวิตได้ดีเพียงใด คือ 'ความเต็มใจที่จะเสี่ยงเพื่อหาความหมายของชีวิตที่ตอบสนองสังคม' บุคลิกภาพที่พัฒนาเต็มที่จะรู้จักร่วมมือกับผู้อื่นเพื่อให้รู้สึกว่าตน 'มีส่วนร่วมหรือมีความเป็นเจ้าของ' (Belonging) ผ่านงานหลัก 3 ด้าน:")

    # Table for 3 Life Tasks
    tbl_tasks = doc.add_table(rows=4, cols=3)
    tbl_tasks.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_tasks.autofit = False
    set_table_borders(tbl_tasks)

    task_headers = ["งานหลักของชีวิต (Life Tasks)", "ความหมายและสาระสำคัญ", "ผลกระทบเมื่อเผชิญปัญหา"]
    col_widths_tasks = [Inches(1.8), Inches(2.6), Inches(1.87)]

    # Header Row
    for idx, name in enumerate(task_headers):
        cell = tbl_tasks.cell(0, idx)
        cell.width = col_widths_tasks[idx]
        set_cell_shading(cell, HEX_PRIMARY)
        set_cell_margins(cell, top=140, bottom=140, left=140, right=140)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(name)
        apply_font(r, size_pt=15, bold=True, color=RGBColor(255, 255, 255))

    task_data = [
        ("1. งานด้านมิตรภาพ\n(Friendship / Social Task)", 
         "เป็นตัวชี้นำความสนใจทางสังคมที่ชัดเจนที่สุด คือการสร้างสัมพันธภาพ การรู้จักอยู่ร่วม และการมีปฏิสัมพันธ์กับผู้อื่นในสังคมอย่างเกื้อกูล", 
         "หากล้มเหลว บุคคลจะแยกตัว โดดเดี่ยว หรือปฏิเสธสัมพันธภาพ ทำให้น้ำหนักความกดดันไหลไปเพิ่มที่ด้านอื่น"),
        ("2. งานด้านอาชีพ\n(Work / Occupation Task)", 
         "การทำงาน เลี้ยงชีพ สร้างคุณค่า มีบทบาทหน้าที่ และทำประโยชน์ตอบแทนแก่ชุมชนและสังคม", 
         "หากล้มเหลว จะรู้สึกว่าชีวิตตนเองว่างเปล่า ไม่เติมเต็ม ไร้คุณค่า และอาจไม่ยอมรับผิดชอบงานตั้งแต่วัยเด็กจนโต"),
        ("3. งานด้านความรัก\n(Love / Intimacy Task)", 
         "บทบาทความสัมพันธ์คู่ครอง ความใกล้ชิด การให้เกียรติ และความเข้าใจซึ่งกันและกัน ไม่ได้เกิดจากเพียงแรงขับทางเพศ", 
         "หากบกพร่อง จะส่งผลให้เกิดความขัดแย้งในชีวิตสมรสและความล้มเหลวในการสร้างครอบครัวที่อบอุ่น")
    ]

    for row_idx, data in enumerate(task_data, start=1):
        for col_idx in range(3):
            cell = tbl_tasks.cell(row_idx, col_idx)
            cell.width = col_widths_tasks[col_idx]
            if row_idx % 2 == 1:
                set_cell_shading(cell, HEX_GRAY_ROW)
            set_cell_margins(cell, top=120, bottom=120, left=140, right=140)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(data[col_idx])
            apply_font(r, size_pt=14, bold=(col_idx == 0), color=C_BODY)

    doc.add_paragraph() # spacing

    # ==========================================
    # SECTION 3: สังคมครอบครัวและพฤติกรรมปัญหาของเด็ก
    # ==========================================
    add_h1("ส่วนที่ 3: ครอบครัวและเป้าหมายพฤติกรรมที่เป็นปัญหาของเด็ก (Family & 4 Goals of Misbehavior)")
    add_body_p("ครอบครัวคือ 'สังคมเบื้องต้น' ที่เด็กเรียนรู้การมีปฏิสัมพันธ์ เด็กทุกคนแสวงหาความสำคัญและการมีส่วนร่วมในครอบครัว หากเด็กเผชิญกับการแข่งขันแล้วรู้สึกว่าตนสู้ไม่ได้ หรือเป็นเด็กพิการ/มีปมด้อย เด็กจะยิ่งเรียกร้องการมีส่วนร่วมสูงขึ้น และแสดงออกด้วย 'พฤติกรรมที่เป็นปัญหา'")
    
    add_callout([
        ("หลักคิดหัวใจของแอดเลอร์: ", "แอดเลอร์มองว่าเด็กที่แสดงพฤติกรรมก้าวร้าว เกเร หรือมีปัญหานั้น 'ต้องการกำลังใจ ไม่ใช่ผู้ป่วย' (Discouraged, not sick) พฤติกรรมแย่ๆ คือความพยายามอย่างผิดวิธีเพื่อให้ตนเองมีที่ยืนและมีความสำคัญ"),
        ("ลักษณะของเป้าหมาย: ", "เป้าหมายเหล่านี้เป็นเพียง 'เป้าหมายระยะสั้น' ของเด็กที่มีปัญหา")
    ], title="💡 มุมมองต่อเด็กที่มีปัญหาตามทฤษฎีแอดเลอร์", bg_color=HEX_LIGHT_AMBER, border_color=HEX_BORDER_AMBER)

    add_h2("เจาะลึก: เป้าหมายระยะสั้นของพฤติกรรมที่เป็นปัญหา 4 ประการ (Four Goals of Misbehavior)")

    tbl_goals = doc.add_table(rows=5, cols=4)
    tbl_goals.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_goals.autofit = False
    set_table_borders(tbl_goals)

    goals_headers = ["เป้าหมายของเด็ก", "พฤติกรรมที่เด็กแสดงออก", "ความรู้สึกของครู/ผู้ปกครอง", "แนวทางการช่วยเหลือของครู"]
    goals_widths = [Inches(1.5), Inches(1.8), Inches(1.4), Inches(1.57)]

    for idx, name in enumerate(goals_headers):
        cell = tbl_goals.cell(0, idx)
        cell.width = goals_widths[idx]
        set_cell_shading(cell, HEX_PRIMARY)
        set_cell_margins(cell, top=140, bottom=140, left=120, right=120)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(name)
        apply_font(r, size_pt=14, bold=True, color=RGBColor(255, 255, 255))

    goals_data = [
        ("1. เพื่อได้รับความสนใจ\n(Attention Seeking)",
         "ก่อกวน ทำตัวตลก พูดแทรก หรือทำตัวอ่อนแอ เพื่อให้ทุกคนจับจ้อง",
         "รำคาญใจ เหนื่อยหน่าย (Annoyed)",
         "ให้ความสนใจในเชิงบวกเมื่อเด็กทำดี เพิกเฉยต่อการเรียกร้องความสนใจที่ไม่เหมาะสม"),
        ("2. เพื่อได้รับอำนาจ\n(Power Seeking)",
         "ดื้อรั้น ท้าทาย ไม่ยอมทำตามคำสั่ง โต้วาที เถียงหัวชนฝา",
         "ถูกคุกคาม โกรธ รู้สึกสูญเสียการควบคุม (Threatened / Angry)",
         "ไม่ประจันหน้า ไม่ต่อสู้เชิงอำนาจ ให้เด็กมีส่วนร่วมในการตัดสินใจและมอบหมายหน้าที่สำคัญ"),
        ("3. เพื่อได้แก้แค้น\n(Revenge)",
         "ทำร้ายจิตใจ ก้าวร้าว ทำลายข้าวของ ประชดประชันรุนแรง",
         "เจ็บปวด เสียใจ รู้สึกถูกทำร้าย (Hurt)",
         "สร้างสัมพันธภาพที่อบอุ่น ไม่ตอบโต้ด้วยความรุนแรง ให้เด็กรู้ว่าเขายังคงได้รับความรักและการยอมรับ"),
        ("4. เพื่อประกาศความพ่ายแพ้\n(Display of Inadequacy)",
         "ยอมจำนน ถอดใจ ไม่พยายามทำอะไร แกล้งทำเป็นโง่หรือไม่สามารถทำได้",
         "หมดหวัง ท้อแท้ สงสาร สิ้นปัญญา (Despair / Helpless)",
         "ไม่ยอมแพ้ไปกับเด็ก ซอยงานเป็นขั้นตอนเล็กๆ ให้เด็กประสบความสำเร็จทีละก้าว เสริมกำลังใจอย่างสม่ำเสมอ")
    ]

    for row_idx, data in enumerate(goals_data, start=1):
        for col_idx in range(4):
            cell = tbl_goals.cell(row_idx, col_idx)
            cell.width = goals_widths[col_idx]
            if row_idx % 2 == 1:
                set_cell_shading(cell, HEX_GRAY_ROW)
            set_cell_margins(cell, top=120, bottom=120, left=120, right=120)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(data[col_idx])
            apply_font(r, size_pt=13, bold=(col_idx == 0), color=C_BODY)

    doc.add_paragraph()

    # ==========================================
    # SECTION 4: คลังสะสมความเชื่อและการเกิดปมด้อย
    # ==========================================
    add_h1("ส่วนที่ 4: คลังสะสมความเชื่อ (Belief System) และการเกิดปมด้อย")
    add_body_p("เด็กที่เติบโตขึ้นจะมีการรับรู้ประสบการณ์ในชีวิตที่บิดเบือนไม่มากก็น้อย ทำให้เกิดคลังสะสมความเชื่อส่วนตัว (Private Logic) 4 ด้าน:")

    add_body_p(" เป็นความเชื่อว่าตัวเราเองเป็นคนอย่างไร เก่ง อ่อนแอ ดี เลว มีความสามารถหรือไม่", bold_prefix="1. ความเชื่อเกี่ยวกับตนเอง (Self-concept):", bullet=True)
    add_body_p(" เป็นความเชื่อว่าเรา 'ควรจะเป็นคนอย่างไร' จึงจะสมบูรณ์และเป็นที่ยอมรับ", bold_prefix="2. ความเชื่อเกี่ยวกับตนในอุดมคติ (Self-ideal):", bullet=True)
    add_body_p(" เป็นความเชื่อเกี่ยวกับมนุษย์ ธรรมชาติ สังคม และสิ่งรอบตัว เช่น โลกนี้ปลอดภัยหรือโลกนี้อันตราย", bold_prefix="3. ความเชื่อเกี่ยวกับโลก (Concept of the World):", bullet=True)
    add_body_p(" ความปักใจเชื่อส่วนบุคคลถึงสิ่งที่ถูก-ผิด ดี-ชั่ว ทางศีลธรรม", bold_prefix="4. ความเชื่อทางจริยธรรม (Ethical Convictions):", bullet=True)

    add_h2("กลไกความไม่สอดคล้อง (Incongruence) นำไปสู่ความรู้สึกด้อย")
    add_body_p("ความรู้สึกด้อย (Inferiority Feelings) จะปะทุขึ้นเมื่อเกิดความไม่สอดคล้องกันระหว่างคลังความเชื่อเหล่านี้:")
    add_body_p(" เกิดความรู้สึกด้อยเมื่อตนเองในความเป็นจริงไม่ถึงเกณฑ์อุดมคติ เช่น หญิงรู้สึกด้อยเพราะอยากเท่าเทียมชาย หรือชายรู้สึกว่าความเป็นชายของตนยังไม่สมบูรณ์", bold_prefix="• ตนเอง (1) ขัดแย้งกับ ตนในอุดมคติ (2): ")
    add_body_p(" เช่น เชื่อว่า 'โลกนี้น่ากลัว อันตราย ไม่น่าไว้วางใจ' ขณะเดียวกันมองว่า 'ตนเองเป็นคนอ่อนแอ' จึงเกิดความรู้สึกด้อยและหวาดระแวง", bold_prefix="• ตนเอง (1) ขัดแย้งกับ โลก (3): ")
    add_body_p(" เช่น ปักใจเชื่อว่า 'การพูดปดผิดศีลร้ายแรง' แต่ตนเองเผลอพูดโกหกไป 2 ครั้ง ทำให้รู้สึกด้อยและผิดบาปอย่างรุนแรง", bold_prefix="• ตนเอง (1) ขัดแย้งกับ จริยธรรม (4): ")

    add_callout([
        ("ปริมาณความรู้สึกด้อย: ", "แอดเลอร์เชื่อว่า ความรู้สึกด้อยเป็นเรื่องของ 'ปริมาณความมากน้อย' ทุกคนมีติดตัวมาแต่เกิดเพื่อเป็นแรงกระตุ้นให้พัฒนา"),
        ("จากความรู้สึกด้อยสู่ปมด้อย: ", "ตราบใดที่บุคคลปรับตัวได้ จะไม่เกิดอาการผิดปกติ แต่หากไม่สามารถรับมือได้ จะกลายเป็นการ 'หมดกำลังใจ' หรือ 'ปมด้อย' (Inferiority Complex) ซึ่งวงการแพทย์เรียกว่าพยาธิสภาพ")
    ], title="📌 ข้อสรุปเรื่องปมด้อยตามแนวคิดแอดเลอร์", bg_color=HEX_LIGHT_BLUE, border_color=HEX_BORDER_BLUE)

    # ==========================================
    # SECTION 5: ลีลาหรือวิถีชีวิต 4 รูปแบบ
    # ==========================================
    add_h1("ส่วนที่ 5: ลีลาหรือวิถีชีวิต 4 รูปแบบ (Styles of Life)")
    add_body_p("ลีลาชีวิต (Life Style) คือแบบแผนพฤติกรรม ทัศนคติ และวิธีที่บุคคลใช้ในการดำเนินชีวิตและแก้ปัญหา แอดเลอร์จำแนกไว้เป็น 4 รูปแบบหลัก:")

    tbl_styles = doc.add_table(rows=5, cols=4)
    tbl_styles.alignment = WD_TABLE_ALIGNMENT.CENTER
    tbl_styles.autofit = False
    set_table_borders(tbl_styles)

    style_headers = ["ลีลาชีวิต (Life Style)", "ลักษณะพฤติกรรมและการดำเนินชีวิต", "ความสนใจสังคม", "ระดับกิจกรรม/การกระทำ"]
    style_widths = [Inches(1.6), Inches(2.57), Inches(1.1), Inches(1.0)]

    for idx, name in enumerate(style_headers):
        cell = tbl_styles.cell(0, idx)
        cell.width = style_widths[idx]
        set_cell_shading(cell, HEX_PRIMARY)
        set_cell_margins(cell, top=140, bottom=140, left=120, right=120)
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(0)
        r = p.add_run(name)
        apply_font(r, size_pt=14, bold=True, color=RGBColor(255, 255, 255))

    styles_data = [
        ("1. ลีลาปกครอง\n(Ruling Style)",
         "ต้องการอยู่เหนือผู้อื่น เป็นผู้ควบคุมสัมพันธภาพ มองโลกในแง่เป็นศัตรู ไม่สนใจประโยชน์ส่วนรวมอย่างแท้จริง มักก้าวร้าวหรือข่มเหงผู้อื่น",
         "ต่ำมาก\n(Low)", "สูง\n(High)"),
        ("2. ลีลาได้รับ\n(Getting Style)",
         "สัมพันธ์กับโลกเพื่อเป็นฝ่าย 'ได้รับ' เท่านั้น คอยพึ่งพาผู้อื่นให้จัดการสิ่งต่างๆ ให้ ขาดความกระตือรือร้นในการลงมือทำประโยชน์ แต่ไม่ค่อยข่มเหงใคร",
         "ต่ำ\n(Low)", "ปานกลาง/ต่ำ\n(Med-Low)"),
        ("3. ลีลาหลีกหนี\n(Avoiding Style)",
         "หลีกหนีปัญหาชีวิต ไม่ทำประโยชน์แก่สังคม เพราะกลัวความล้มเหลว คิดว่าตนเองล้มเหลวมากกว่าประสบความสำเร็จ ระดับการแก้ปัญหาต่ำมาก",
         "ต่ำที่สุด\n(Lowest)", "ต่ำมาก\n(Low)"),
        ("4. ลีลาทำประโยชน์แก่สังคม\n(Socially Useful Style)",
         "คำนึงถึงเพื่อนมนุษย์ มุ่งมั่นเพื่อส่วนรวม ผูกพันกับสังคม แก้ปัญหาด้วยความกล้าหาญ เต็มใจปฏิบัติงานหลักชีวิตทั้ง 3 ด้านโดยไม่มีข้อแก้ตัว",
         "สูงมาก\n(High)", "สูงและสร้างสรรค์\n(High & Creative)")
    ]

    for row_idx, data in enumerate(styles_data, start=1):
        for col_idx in range(4):
            cell = tbl_styles.cell(row_idx, col_idx)
            cell.width = style_widths[col_idx]
            if row_idx % 2 == 1:
                set_cell_shading(cell, HEX_GRAY_ROW)
            set_cell_margins(cell, top=120, bottom=120, left=120, right=120)
            p = cell.paragraphs[0]
            p.paragraph_format.space_before = Pt(0)
            p.paragraph_format.space_after = Pt(0)
            p.paragraph_format.line_spacing = 1.15
            r = p.add_run(data[col_idx])
            apply_font(r, size_pt=13, bold=(col_idx == 0), color=C_BODY)

    doc.add_paragraph()

    # ==========================================
    # SECTION 6: เป้าหมายและบทบาทหน้าที่ของผู้ให้การปรึกษา
    # ==========================================
    add_h1("ส่วนที่ 6: เป้าหมายและบทบาทหน้าที่ของผู้ให้การปรึกษา")
    add_h2("เป้าหมายของการให้การปรึกษา 6 ประการ")
    add_body_p(" ส่งเสริมและฟื้นฟูความสนใจทางสังคม (Promote Social Interest)", bullet=True)
    add_body_p(" ลดความรู้สึกด้อย และเรียกคืนกำลังใจที่สูญเสียไป (Overcome Discouragement)", bullet=True)
    add_body_p(" ปรับเปลี่ยนลีลาหรือวิถีชีวิตเดิมที่ไม่เหมาะสม (Modify Style of Life)", bullet=True)
    add_body_p(" ปรับปรุงแรงจูงใจและค่านิยมที่ผิดพลาด (Change Faulty Motivations)", bullet=True)
    add_body_p(" ส่งเสริมให้บุคคลตระหนักในความเท่าเทียมเสมอภาคกับผู้อื่น (Equality)", bullet=True)
    add_body_p(" ช่วยให้บุคคลรู้จักทำตนให้เป็นประโยชน์ต่อสังคมส่วนรวม (Be of Use to Others)", bullet=True)

    add_h2("บทบาทหน้าที่และการประเมินของผู้ให้การปรึกษา (Counselor Roles & Assessment)")
    add_body_p("ผู้ให้การปรึกษาต้องทำตัวเสมือนเป็นผู้รับการปรึกษา เพื่อเข้าใจระบบความเชื่อและการดำเนินชีวิต โดยมีภารกิจหลักดังนี้:")

    add_body_p(" ครอบครัวคือสถานการณ์ที่เปลี่ยนแปลงเสมอ ไม่มีลูกคนไหนเกิดในสถานการณ์เดียวกัน (อายุพ่อแม่เปลี่ยน ฐานะเปลี่ยน ความฉลาดเปลี่ยน) ต้องสำรวจลำดับการเกิด พี่น้องที่คล้ายหรือต่างกันที่สุด และการมีสัมพันธภาพกับพ่อแม่", bold_prefix="1. ทำความเข้าใจลำดับการเกิดในครอบครัว (Birth Order / Family Constellation): ", bullet=True)
    add_body_p(" ความทรงจำในวัยเด็กเป็น 'ดัชนีชี้วัดความสนใจสังคม' และสะท้อนเป้าหมายชีวิตปัจจุบัน ผู้ให้การปรึกษาจะรวบรวมเรื่องราวที่จำได้ประมาณ 3–6 เรื่อง เพื่อแปลความหมายของวิถีชีวิต", bold_prefix="2. ทำความเข้าใจความทรงจำในตอนต้นของชีวิต (Early Recollections): ", bullet=True)
    add_body_p(" นำข้อมูลวัยเด็กมาวิเคราะห์ร่วมกับงาน 3 ด้านในปัจจุบัน (มิตรภาพ การงาน ความรัก) เพื่อดูว่าผู้รับการปรึกษาเผชิญชีวิตได้ดีเพียงใด", bold_prefix="3. ทำความเข้าใจงานหลักของชีวิตในปัจจุบัน (Current Life Tasks): ", bullet=True)
    add_body_p(" สัมภาษณ์เพื่อจัดลำดับว่าผู้รับการปรึกษาให้ความสำคัญกับลีลาใดเป็นหลัก:", bold_prefix="4. จัดลำดับความสำคัญของลีลาชีวิต (Life Style Priorities): ", bullet=True)

    # 4 Priorities details
    add_body_p(" มุ่งประสิทธิภาพ ถูกต้อง มีประโยชน์ แต่ผลเสียคือเหนื่อยล้า เครียด กังวล ขาดความมั่นใจในสัมพันธภาพ", bold_prefix="    • การเป็นผู้เหนือผู้อื่น (Superiority): ")
    add_body_p(" ควบคุมตนเองหรือผู้อื่น ผลเสียคือการเหินห่างจากผู้คน ความเป็นธรรมชาติและความสร้างสรรค์ลดลง", bold_prefix="    • การควบคุม (Control): ")
    add_body_p(" มีความสุขเมื่อได้ช่วยเหลือผู้อื่น แต่ระยะยาวกลายเป็นการทำร้ายตนเองและผู้อื่น สัมพันธภาพบวกจะลดลง", bold_prefix="    • การปลอบโยน (Comfort): ")
    add_body_p(" ได้ผลดีในระยะสั้น แต่ระยะยาวจะถูกปฏิเสธ คับข้องใจ โกรธเคือง และหยุดชะงักการเติบโต", bold_prefix="    • การเอาอกเอาใจ (Pleasing): ")

    add_body_p(" แปลความจากบทสนทนา ความฝัน จินตนาการ เพื่อให้ผู้รับการปรึกษาเกิดการหยั่งรู้ว่าลีลาชีวิตเดิมสร้างปัญหาอย่างไร การแปลความอาจถูกต่อต้าน ซึ่งการต่อต้านนั้นมักเป็นรูปแบบเดียวกับที่ผู้รับการปรึกษาใช้กับบุคคลสำคัญที่เขารู้สึกไม่ปลอดภัย", bold_prefix="5. ทำหน้าที่แปลความและช่วยให้เกิดการหยั่งรู้ (Interpretation & Insight): ", bullet=True)
    add_body_p(" เสนอความคิดและความเชื่อใหม่ ท้าทายความคิดเดิม เป็นการปรับปรุงแรงจูงใจมากกว่าแค่ปรับพฤติกรรมภายนอก เช่น ตั้งคำถามว่า 'อะไรคือสิ่งเลวร้ายที่สุดที่จะเกิดขึ้น หากเปลี่ยนจากวิถีชีวิตเดิม?'", bold_prefix="6. กำหนดทิศทางใหม่ (Reorientation): ", bullet=True)

    doc.add_paragraph()

    # ==========================================
    # SECTION 7: 8 เทคนิคและวิธีการให้การปรึกษา
    # ==========================================
    add_h1("ส่วนที่ 7: เทคนิคและวิธีการให้การปรึกษาแบบแอดเลอร์ (8 Core Techniques)")
    add_body_p("แอดเลอร์และนักจิตวิทยารุ่นหลังได้พัฒนาเทคนิคการบำบัดที่ใช้งานได้จริงในชีวิตประจำวันไว้ 8 เทคนิคหลัก ดังนี้:")

    # Technique 1
    add_h2("เทคนิคที่ 1: การเป็นตัวแบบ (Modeling)")
    add_body_p("ผู้ให้การปรึกษาทำหน้าที่เป็นตัวแบบในเรื่อง 'ค่านิยม' โดยแสดงออกถึงการเป็นตัวของตัวเองที่แท้จริง กล้าที่จะยอมรับว่าความผิดพลาดเป็นเรื่องธรรมดา รู้จักหัวเราะให้กับตนเอง มีความเอื้ออาทรและมีความสนใจทางสังคม เพื่อให้ผู้รับการปรึกษาซึมซับและยึดถือเป็นแบบอย่าง")

    # Technique 2
    add_h2("เทคนิคที่ 2: การจงใจทำให้ฉงน (Paradoxical Intention)")
    add_body_p("การสนับสนุนหรือท้าทายให้ผู้รับการปรึกษา 'แสดงพฤติกรรมหรืออาการที่เป็นปัญหาให้มากยิ่งขึ้น' ผู้รับคำปรึกษาจะรู้สึกประหลาดใจเพราะปกติคนเราต้องการลดอาการ เมื่อเขาลองทำตาม เขาจะเริ่มตระหนักว่าพฤติกรรมปัญหานั้นไม่คุ้มค่า และหากเขาต่อต้านไม่ยอมทำ พฤติกรรมปัญหานั้นก็จะถูกควบคุมไปโดยปริยาย (ใช้เฉพาะช่วงระยะเวลาหนึ่ง)")

    # Technique 3
    add_h2("เทคนิคที่ 3: การสร้างจินตภาพ (Creating Images)")
    add_body_p("การขอให้ผู้รับการปรึกษาสร้างภาพจินตนาการที่สอดคล้องกับเป้าหมายใหม่ เช่น ให้คนที่เอาอกเอาใจคนอื่นจินตนาการว่าตนเองเป็น 'นายกรัฐมนตรี' หรือในกรณีผู้มีปัญหาเรื่องสมรรถภาพทางเพศจากความวิตกกังวล ให้จินตนาการว่าตนเป็น 'สุนัข' เพราะสุนัขไม่เคยกังวลใจเวลาทำกิจกรรมทางเพศ จินตภาพช่วยให้จดจำเป้าหมายได้ดีกว่าเพียงแค่คำพูดตกลงกันตามสุภาษิต 'สิบปากว่าไม่เท่าตาเห็น'")

    # Technique 4
    add_h2("เทคนิคที่ 4: การสร้างคำถามสมมุติ (The Question)")
    add_body_p("ตั้งคำถามเพื่อตรวจสอบว่าปัญหาของผู้รับการปรึกษามีพื้นฐานมาจาก 'ทางกาย' หรือ 'ทางจิตใจ' รวมถึงเผยเป้าหมายซ่อนเร้นที่ใช้หลีกเลี่ยงภาระชีวิต:")
    add_dialogue_box([
        ("ผู้ให้การปรึกษา", "ถ้าครูมียาวิเศษในขณะนี้ที่สามารถช่วยให้อาการปวดศีรษะของหนูหายไปในทันที ชีวิตของหนูจะเปลี่ยนไปอย่างไร?", "คำถามสมมุติเพื่อแยกแยะ"),
        ("ผู้รับฯ (ฐานทางกาย)", "หนูจะรู้สึกดีขึ้น และจะได้ไม่ต้องกินยา เบื่อมากๆ ค่ะ", "แสดงว่าเป็นปัญหาทางสรีระ"),
        ("ผู้รับฯ (ฐานทางจิต)", "หนูจะรู้สึกดีขึ้น และจะได้เลิกไปหากิ๊กแล้วค่ะ", "เผยเป้าหมายซ่อนเร้นทางจิตใจ"),
        ("ผู้ให้การปรึกษา", "อืม... หนูไม่อยากจะปวดหัว และฟังดูเหมือนไม่อยากจะยุ่งเกี่ยวกับกิ๊กด้วย หนูคิดอย่างไรกับเรื่องนี้?", "ท้าทายความคิดเพื่อสะท้อนความจริง")
    ], title="💬 ตัวอย่างเทคนิค The Question (คำถามวิเศษ)")

    # Technique 5
    add_h2("เทคนิคที่ 5: การเตือนตัวเอง (Catching Oneself)")
    add_body_p("ฝึกให้ผู้รับการปรึกษา 'รู้เท่าทัน' ความคิด ความรู้สึก หรือพฤติกรรมเดิมๆ ของตนเอง แล้วฝึกหยุดความคิดนั้นด้วยการดึงสติและพูดเตือนตนเอง:")
    add_dialogue_box([
        ("ผู้รับการปรึกษา", "เมื่อดิฉันรู้สึกตื่นเต้นมาก หัวใจจะเต้นเร็วและแรง ทั้งที่เหตุการณ์ไม่มีอะไรแต่ก็ประหม่า ดิฉันรู้สึกโกรธตัวเองมากค่ะ", "เผชิญอาการเดิม"),
        ("ผู้ให้การปรึกษา", "ต่อไปถ้าคุณเริ่มสังเกตเห็นว่าหัวใจเริ่มเต้นแรง แทนที่จะบอกว่ากำลังประหม่า ให้หยุดคิด แล้วพูดกับตัวเองในใจว่า 'วิภาเปลี่ยนไปแล้ว วิภาเปลี่ยนไปแล้ว วิภาไม่เหมือนเดิม'", "ฝึกเตือนตนเองเพื่อเปลี่ยนปฏิกิริยา")
    ], title="💬 ตัวอย่างเทคนิค การเตือนตัวเอง (Catching Oneself)")

    # Technique 6
    add_h2("เทคนิคที่ 6: กดปุ่มเมื่อต้องการ (Push-Button Technique)")
    add_body_p("ฝึกให้ผู้รับการปรึกษาสร้างจินตภาพเหตุการณ์ที่มีความสุข ชัดเจน สังเกตอารมณ์ตนเอง จากนั้นให้สลับไปสร้างจินตภาพเหตุการณ์ในอดีตที่ปวดร้าว ล้มเหลว เสียหน้า แล้วสังเกตอารมณ์ทุกข์ที่เกิดขึ้น จากนั้นให้ 'กดปุ่มสลับ' กลับมาที่ภาพความสุขอีกครั้ง")
    add_callout([
        ("เป้าหมายของ Push-Button: ", "เพื่อให้ผู้รับการปรึกษาตระหนักรู้ด้วยตนเองว่า 'เขาสามารถควบคุมอารมณ์ความรู้สึกได้ เพียงแค่ฝึกควบคุมความคิด'"),
        ("Mindset สำคัญ: ", "มนุษย์เป็น 'ผู้สร้างอารมณ์' ของตนเอง ไม่ใช่ตกเป็น 'เหยื่อของอารมณ์'")
    ], title="💡 ข้อค้นพบสำคัญจากเทคนิคกดปุ่มเมื่อต้องการ", bg_color=HEX_LIGHT_GREEN, border_color=HEX_BORDER_GREEN)

    # Technique 7
    add_h2("เทคนิคที่ 7: การให้กำลังใจ (Encouragement)")
    add_body_p("เป็น **'หัวใจสำคัญที่สุด'** ตลอดกระบวนการช่วยเหลือของแอดเลอร์ เพราะแอดเลอร์เชื่อว่าผู้รับการปรึกษาคือ 'ผู้สูญเสียกำลังใจ' ผู้ให้การปรึกษาต้องยอมรับเขาตามสภาพที่เป็นจริงในฐานะมนุษย์ที่มีคุณค่า ไม่ใช่ตัดสินหรือบีบคั้นให้เขาเป็นคนที่ควรจะเป็น:")
    add_dialogue_box([
        ("ผู้รับการปรึกษา", "ผมทำแบบนั้นได้อย่างไรนะ... ผมซ้อมภรรยาตัวเอง ผมน่าจะควบคุมตนเองได้ (ร้องไห้เสียใจ)", "หมดกำลังใจและรู้สึกผิด"),
        ("ผู้ให้การปรึกษา", "คุณคงรู้สึกปวดร้าวมากกับเหตุการณ์ที่เกิดขึ้น และผมมองเห็นคนคนหนึ่งที่ปวดร้าว รู้สึกผิด ขณะเดียวกันคนคนนั้นก็กำลังพยายามอย่างมากที่จะคิดว่า ทำอย่างไรเหตุการณ์แบบนั้นจะไม่เกิดขึ้นอีก", "สะท้อนคุณค่าและให้กำลังใจเพื่อเริ่มต้นใหม่")
    ], title="💬 ตัวอย่างเทคนิค การให้กำลังใจ (Encouragement)")

    # Technique 8
    add_h2("เทคนิคที่ 8: การเอาใจคนอื่น / ทำประโยชน์ให้ผู้อื่น (Doing for Others)")
    add_body_p("สนับสนุนให้ผู้รับการปรึกษา 'ก้าวออกจากโลกที่จมอยู่กับตนเอง' แล้วฝึกสร้างสัมพันธภาพโดยการเป็นผู้ให้ ทำสิ่งดีๆ ให้แก่ผู้อื่น เพื่อปรับผู้รับการปรึกษาให้กลับคืนสู่ 'ความสนใจทางสังคม' (Social Interest):")
    add_dialogue_box([
        ("ผู้รับการปรึกษา", "ผมรู้สึกอยากอยู่คนเดียวตามลำพัง ไม่อยากคุยกับใคร แม้แต่เพื่อนสนิทที่ผมรักที่สุดตอนนี้ผมยังไม่อยากคุยด้วยเลยครับ", "แยกตัวออกจากสังคม"),
        ("ผู้ให้การปรึกษา", "ผมคิดว่าบางทีคุณน่าจะลองแวะไปหาเพื่อนรักของคุณ หรือโทรศัพท์ไปหา เล่าเรื่องราวให้เขาฟัง หรือแวะเอาขนม หนังสือไปให้ ชวนไปกินข้าวดูหนัง และบอกเขาว่าคุณดีใจที่มีเพื่อนอย่างเขา", "สนับสนุนให้ลงมือทำเพื่อผู้อื่น")
    ], title="💬 ตัวอย่างเทคนิค การเอาใจคนอื่น (Doing for Others)")

    doc.add_paragraph()

    # ==========================================
    # SECTION 8: สรุปหัวใจสำคัญเพื่อการนำไปใช้ / เตรียมสอบ
    # ==========================================
    add_h1("ส่วนที่ 8: สรุปหัวใจสำคัญเพื่อการนำไปใช้หน้างานและเตรียมสอบ (Key Takeaways)")

    add_callout([
        ("1. มองเด็กด้วยความเข้าใจ: ", "เด็กที่เกเร ดื้อ หรือยอมแพ้ ไม่ใช่คนเลวร้าย แต่คือเด็กที่ 'หมดกำลังใจ' และกำลังหาที่ยืนในครอบครัว/โรงเรียนผ่านเป้าหมายผิดๆ 4 ขั้น"),
        ("2. มนุษย์มีเป้าหมายเสมอ (Teleology): ", "พฤติกรรมไม่ได้ถูกกำหนดด้วยอดีตอย่างตายตัว แต่ถูกขับเคลื่อนด้วย 'เป้าหมายสู่อนาคต' เพื่อเอาชนะความรู้สึกด้อย"),
        ("3. ยาขนานแท้คือ 'กำลังใจ' (Encouragement): ", "การลงโทษมักยิ่งผลักให้เด็กไปสู่ขั้น 'แก้แค้น' หรือ 'ยอมจำนน' ครูต้องใช้การให้กำลังใจเพื่อดึงเด็กกลับสู่ 'ความสนใจทางสังคม'"),
        ("4. คำศัพท์ยอดฮิตที่กำเนิดจากแอดเลอร์: ", "ปมด้อย (Inferiority Complex), การชดเชยสู่ความเด่น (Striving for Superiority), ลำดับการเกิด (Birth Order), ความสนใจสังคม (Social Interest)"),
        ("5. คำถามวิเศษ (The Question): ", "จำประโยค 'ถ้ายาวิเศษทำให้อาการหายไปทันที จะทำอะไร' ไว้เสมอ ใช้แยกปัญหาทางกาย vs ทางจิตได้แม่นยำที่สุด")
    ], title="🎯 ตะลุยสอบ & สรุปสูตรจำ EDP3502 บทที่ 9", bg_color=HEX_LIGHT_AMBER, border_color=HEX_BORDER_AMBER)

    # Save to file
    out_filename = "สรุปบทที่9_ทฤษฎีการให้การปรึกษาแบบแอดเลอร์.docx"
    doc.save(out_filename)
    print(f"Successfully generated: {out_filename}")

    # Also save a copy in 'งาน' folder if exists
    work_dir = "งาน"
    if os.path.exists(work_dir):
        shutil.copy2(out_filename, os.path.join(work_dir, out_filename))
        print(f"Copied to: {os.path.join(work_dir, out_filename)}")

if __name__ == "__main__":
    create_document()
