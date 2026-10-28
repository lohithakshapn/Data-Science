#!/usr/bin/env python3

"""Generate P. Lohithaksha's one-page resume PDF — dark quant-lab branded.

Run:
    python generate_resume.py

The generated PDF will be saved in the same folder as this script.
"""

import os

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    HRFlowable,
)


# ============================================================
# IDENTITY
# ============================================================

NAME = "P. LOHITHAKSHA"
TITLE = "DATA SCIENTIST"

EMAIL = "pnlohithaksha99@gmail.com"
PHONE = "+91 72078 09767"
LINKEDIN_URL = "https://www.linkedin.com/in/pn-0a5495360"
GITHUB_URL = "https://github.com/lohithaksha"
MEDIUM_URL = "https://medium.com/@lohit349" 
 
 
# ============================================================ 
# CONTENT 
# ============================================================ 
 
SUMMARY = ( 
    "Data Scientist with 3+ years of experience specializing in machine learning, " 
    "statistical modeling, and financial analytics. Experienced in building predictive " 
    "models for time-series forecasting and fraud detection using Python and SQL. Strong " 
    "focus on feature engineering, model evaluation, and delivering business impact " 
    "through data-driven insights." 
) 
 
 
EXPERIENCE = [ 
    { 
        "role": "Data Scientist", 
        "company": "Raymond James — Florida, USA", 
        "period": "Feb 2024 – Mar 2026", 
        "bullets": [ 
            "Designed and deployed financial time-series forecasting models (ARIMA, GARCH, Exponential Smoothing), improving portfolio return predictions by 18%.", 
            "Developed fraud detection models on imbalanced datasets using Logistic Regression, Random Forest, and XGBoost, reducing false positives by 15%.", 
            "Designed feature engineering pipelines and conducted model evaluation using ROC-AUC, PR curves, and cross-validation to improve model robustness.", 
            "Contributed to deployment and monitoring of ML models, ensuring stable performance and detecting drift across financial datasets.", 
            "Applied anomaly detection techniques to identify unusual financial transaction patterns.", 
        ], 
    }, 
    { 
        "role": "Data Analyst Intern", 
        "company": "Unical Systems — Hyderabad, IN", 
        "period": "Aug 2021 – Dec 2021", 
        "bullets": [ 
            "Partnered with business teams to define KPIs and deliver actionable insights to improve marketing decision-making.", 
            "Performed data cleaning, transformation, and analysis on structured and unstructured datasets using SQL and Python.", 
            "Designed and maintained interactive Tableau dashboards for executive reporting and customer behavior analysis.", 
            "Optimized SQL Server databases and supported efficient data querying for analytics and reporting needs.", 
            "Applied basic NLP techniques (tokenization, stop-word removal, lemmatization) to analyze customer feedback and reviews.", 
        ], 
    }, 
] 
 
 
SKILLS = [ 
    ("Languages", "Python, SQL, PySpark, Java"), 
    ( 
        "Databases & Big Data", 
        "Hive, Impala, Sqoop, Spark SQL, MySQL, Oracle, Azure Data Lake Gen2", 
    ), 
    ( 
        "ML & Analytics", 
        "Regression, Classification, Logistic Regression, Random Forest, " 
        "XGBoost, K-Means, DBSCAN, Time-Series (ARIMA, GARCH), " 
        "Scikit-learn, Pandas, NumPy, NLP", 
    ), 
    ( 
        "Visualization", 
        "Tableau, Power BI, Matplotlib, Seaborn, Plotly", 
    ), 
    ( 
        "Cloud & Deployment", 
        "Azure Cloud, AWS Cloud, Azure DevOps, GitHub, Anaconda Enterprise", 
    ), 
    ( 
        "Methodologies", 
        "Agile, Scrum, Waterfall, JIRA, Azure DevOps Boards", 
    ), 
    ( 
        "Statistics", 
        "Hypothesis Testing, A/B Testing, ROC-AUC", 
    ), 
] 
 
 
EDUCATION = [ 
    ( 
        "Postgraduate Program in Data Science and Analytics with GenAI", 
        "Imarticus Learning — Hyderabad, India", 
        "Dec 2025 – Aug 2026", 
    ), 
    ( 
        "Master of Science in Computer Science", 
        "Lamar University — Texas, USA", 
        "Aug 2022 – Dec 2023", 
    ), 
] 
 
 
CERTIFICATIONS = [ 
    "AWS AI Practitioner", 
    "AWS Cloud Practitioner", 
    "KPMG Data Science Pro-Degree", 
    "Microsoft Database Fundamentals", 
    "PGP in Data Science and Analytics with GenAI — Imarticus Learning", 
] 
 
 
# ============================================================ 
# OUTPUT 
# ============================================================ 
 
BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
 
OUT = os.path.join( 
    BASE_DIR, 
    "lohithaksha-resume.pdf", 
) 
 
 
# ============================================================ 
# COLORS 
# ============================================================ 
 
BG_DARK = HexColor("#0A0E17") 
CYAN = HexColor("#00B8CC") 
CYAN_BRIGHT = HexColor("#00F0FF") 
INK = HexColor("#1A2332") 
GRAY = HexColor("#5A6B80") 
LIGHT_LINE = HexColor("#D8E0EA") 
 
PAGE_W, PAGE_H = letter 
 
HEADER_H = 1.28 * inch 
MARGIN_X = 0.5 * inch 
 
 
# ============================================================ 
# STYLES 
# ============================================================ 
 
S = { 
    "section": ParagraphStyle( 
        "section", 
        fontName="Helvetica-Bold", 
        fontSize=9.5, 
        textColor=CYAN, 
        spaceAfter=3, 
        spaceBefore=10, 
        tracking=1.5, 
    ), 
 
    "body": ParagraphStyle( 
        "body", 
        fontName="Helvetica", 
        fontSize=8.1, 
        textColor=INK, 
        leading=10.6, 
        alignment=TA_LEFT, 
    ), 
 
    "bullet": ParagraphStyle( 
        "bullet", 
        fontName="Helvetica", 
        fontSize=8.1, 
        textColor=INK, 
        leading=10.6, 
        leftIndent=9, 
        bulletIndent=0, 
        spaceAfter=2.2, 
        bulletColor=CYAN, 
        bulletFontName="Helvetica-Bold", 
    ), 
 
    "role": ParagraphStyle( 
        "role", 
        fontName="Helvetica-Bold", 
        fontSize=9.6, 
        textColor=INK, 
        spaceAfter=0.5, 
    ), 
 
    "company": ParagraphStyle( 
        "company", 
        fontName="Helvetica-Oblique", 
        fontSize=8.2, 
        textColor=GRAY, 
        spaceAfter=2.5, 
    ), 
 
    "skill_label": ParagraphStyle( 
        "skill_label", 
        fontName="Helvetica-Bold", 
        fontSize=8.1, 
        textColor=INK, 
        leading=10.6, 
        spaceAfter=1, 
    ), 
 
    "skill_val": ParagraphStyle( 
        "skill_val", 
        fontName="Helvetica", 
        fontSize=7.8, 
        textColor=GRAY, 
        leading=10, 
        spaceAfter=4.5, 
    ), 
 
    "edu_deg": ParagraphStyle( 
        "edu_deg", 
        fontName="Helvetica-Bold", 
        fontSize=8.3, 
        textColor=INK, 
        leading=10.6, 
        spaceAfter=0.5, 
    ), 
 
    "edu_meta": ParagraphStyle( 
        "edu_meta", 
        fontName="Helvetica", 
        fontSize=7.8, 
        textColor=GRAY, 
        leading=9.8, 
        spaceAfter=5, 
    ), 
 
    "cert": ParagraphStyle( 
        "cert", 
        fontName="Helvetica", 
        fontSize=8.1, 
        textColor=INK, 
        leading=10.6, 
        leftIndent=9, 
        bulletIndent=0, 
        spaceAfter=2.2, 
        bulletColor=CYAN, 
        bulletFontName="Helvetica-Bold", 
    ), 
} 
 
 
# ============================================================ 
# CLICKABLE CONTACT LINKS 
# ============================================================ 
 
def draw_contact_links(canvas): 
    """ 
    Draw contact information in the header and make 
    email, phone, LinkedIn, GitHub, and Medium clickable. 
    """ 
 
    canvas.saveState() 
 
    x = MARGIN_X 
    y = PAGE_H - 1.04 * inch 
 
    font_name = "Helvetica" 
    font_size = 7.3 
 
    canvas.setFont( 
        font_name, 
        font_size, 
    ) 
 
    links = [ 
        ( 
            PHONE, 
            "tel:+917207809767", 
        ), 
        ( 
            EMAIL, 
            f"mailto:{EMAIL}", 
        ), 
        ( 
            "linkedin.com/in/pn-0a5495360", 
            LINKEDIN_URL, 
        ), 
        ( 
            "github.com/lohithaksha", 
            GITHUB_URL, 
        ), 
        ( 
            "medium.com/@lohit349", 
            MEDIUM_URL, 
        ), 
    ] 
 
    separator = "   |   " 
 
    for index, (text, url) in enumerate(links): 
 
        # Draw text 
        canvas.setFillColor( 
            HexColor("#94A3B8") 
        ) 
 
        canvas.drawString( 
            x, 
            y, 
            text, 
        ) 
 
        # Calculate text width 
        text_width = canvas.stringWidth( 
            text, 
            font_name, 
            font_size, 
        ) 
 
        # Make text clickable 
        canvas.linkURL( 
            url, 
            ( 
                x, 
                y - 2, 
                x + text_width, 
                y + font_size + 2, 
            ), 
            relative=0, 
        ) 
 
        # Move to next position 
        x += text_width 
 
        # Draw separator 
        if index < len(links) - 1: 
 
            canvas.setFillColor( 
                HexColor("#64748B") 
            ) 
 
            canvas.drawString( 
                x, 
                y, 
                separator, 
            ) 
 
            separator_width = canvas.stringWidth( 
                separator, 
                font_name, 
                font_size, 
            ) 
 
            x += separator_width 
 
    canvas.restoreState() 
 
# ============================================================ 
# HEADER 
# ============================================================ 
 
def draw_header(canvas, doc): 
 
    canvas.saveState() 
 
    # -------------------------------------------------------- 
    # Dark header 
    # -------------------------------------------------------- 
 
    canvas.setFillColor( 
        BG_DARK 
    ) 
 
    canvas.rect( 
        0, 
        PAGE_H - HEADER_H, 
        PAGE_W, 
        HEADER_H, 
        stroke=0, 
        fill=1, 
    ) 
 
    # -------------------------------------------------------- 
    # Cyan accent line 
    # -------------------------------------------------------- 
 
    canvas.setFillColor( 
        CYAN_BRIGHT 
    ) 
 
    canvas.rect( 
        0, 
        PAGE_H - HEADER_H - 3, 
        PAGE_W, 
        3, 
        stroke=0, 
        fill=1, 
    ) 
 
    # -------------------------------------------------------- 
    # Name 
    # -------------------------------------------------------- 
 
    canvas.setFillColor( 
        HexColor("#F8FAFC") 
    ) 
 
    canvas.setFont( 
        "Helvetica-Bold", 
        27, 
    ) 
 
    canvas.drawString( 
        MARGIN_X, 
        PAGE_H - 0.62 * inch, 
        NAME, 
    ) 
 
    # -------------------------------------------------------- 
    # Title 
    # -------------------------------------------------------- 
 
    canvas.setFillColor( 
        CYAN_BRIGHT 
    ) 
 
    canvas.setFont( 
        "Helvetica-Bold", 
        10.5, 
    ) 
 
    canvas.drawString( 
        MARGIN_X, 
        PAGE_H - 0.84 * inch, 
        TITLE, 
    ) 
 
    # -------------------------------------------------------- 
    # Clickable contact links 
    # -------------------------------------------------------- 
 
    draw_contact_links(canvas) 
 
    # -------------------------------------------------------- 
    # Decorative terminal prompt 
    # -------------------------------------------------------- 
 
    canvas.setFillColor( 
        HexColor("#1E293B") 
    ) 
 
    canvas.setFont( 
        "Courier-Bold", 
        22, 
    ) 
 
    canvas.drawRightString( 
        PAGE_W - MARGIN_X, 
        PAGE_H - 0.68 * inch, 
        "", 
    ) 
 
    # -------------------------------------------------------- 
    # Footer 
    # -------------------------------------------------------- 
 
    canvas.setFillColor( 
        GRAY 
    ) 
 
    canvas.setFont( 
        "Helvetica", 
        6.8, 
    ) 
 
    canvas.drawCentredString( 
        PAGE_W / 2, 
        0.32 * inch, 
        "Built with the same stack as the portfolio — HTML / CSS / JS / Bootstrap / GSAP", 
    ) 
 
    canvas.restoreState() 
 
 
# ============================================================ 
# SECTION HEADER 
# ============================================================ 
 
def section(title): 
 
    return [ 
        Paragraph( 
            title.upper(), 
            S["section"], 
        ), 
 
        HRFlowable( 
            width="100%", 
            thickness=0.7, 
            color=LIGHT_LINE, 
            spaceAfter=4, 
        ), 
    ] 
 
 
# ============================================================ 
# BUILD PDF 
# ============================================================ 
 
def build(): 
 
    doc = SimpleDocTemplate( 
        OUT, 
        pagesize=letter, 
 
        leftMargin=MARGIN_X, 
        rightMargin=MARGIN_X, 
 
        topMargin=HEADER_H + 0.28 * inch, 
        bottomMargin=0.5 * inch, 
 
        title=f"{NAME.title()} — Data Scientist Resume", 
        author=NAME.title(), 
    ) 
 
    left = [] 
    right = [] 
 
    # ======================================================== 
    # LEFT COLUMN 
    # ======================================================== 
 
    # Profile 
    left += section("Profile") 
 
    left.append( 
        Paragraph( 
            SUMMARY, 
            S["body"], 
        ) 
    ) 
 
    # Experience 
    left += section("Experience") 
 
    for job in EXPERIENCE: 
 
        left.append( 
            Paragraph( 
                f'{job["role"]} ' 
                f'<font color="#00B8CC">| {job["period"]}</font>', 
                S["role"], 
            ) 
        ) 
 
        left.append( 
            Paragraph( 
                job["company"], 
                S["company"], 
            ) 
        ) 
 
        for bullet in job["bullets"]: 
 
            left.append( 
                Paragraph( 
                    bullet, 
                    S["bullet"], 
                    bulletText="\u00bb", 
                ) 
            ) 
 
        left.append( 
            Spacer( 
                1, 
                5, 
            ) 
        ) 
 
    # ======================================================== 
    # RIGHT COLUMN 
    # ======================================================== 
 
    # Technical Skills 
    right += section("Technical Skills") 
 
    for label, value in SKILLS: 
 
        right.append( 
            Paragraph( 
                label.upper(), 
                S["skill_label"], 
            ) 
        ) 
 
        right.append( 
            Paragraph( 
                value, 
                S["skill_val"], 
            ) 
        ) 
 
    # Education 
    right += section("Education") 
 
    for degree, school, period in EDUCATION: 
 
        right.append( 
            Paragraph( 
                degree, 
                S["edu_deg"], 
            ) 
        ) 
 
        right.append( 
            Paragraph( 
                f"{school}<br/>{period}", 
                S["edu_meta"], 
            ) 
        ) 
 
    # Certifications 
    right += section("Certifications") 
 
    for certification in CERTIFICATIONS: 
 
        right.append( 
            Paragraph( 
                certification, 
                S["cert"], 
                bulletText="\u00bb", 
            ) 
        ) 
 
    # ======================================================== 
    # TWO COLUMN LAYOUT 
    # ======================================================== 
 
    col_w = ( 
        PAGE_W 
        - 2 * MARGIN_X 
        - 0.3 * inch 
    ) 
 
    grid = Table( 
        [[left, right]], 
        colWidths=[ 
            col_w * 0.585, 
            col_w * 0.415, 
        ], 
    ) 
 
    grid.setStyle( 
        TableStyle( 
            [ 
                ( 
                    "VALIGN", 
                    (0, 0), 
                    (-1, -1), 
                    "TOP", 
                ), 
 
                ( 
                    "LEFTPADDING", 
                    (0, 0), 
                    (-1, -1), 
                    0, 
                ), 
 
                ( 
                    "RIGHTPADDING", 
                    (0, 0), 
                    (0, 0), 
                    14, 
                ), 
 
                ( 
                    "RIGHTPADDING", 
                    (1, 0), 
                    (1, 0), 
                    0, 
                ), 
 
                ( 
                    "TOPPADDING", 
                    (0, 0), 
                    (-1, -1), 
                    0, 
                ), 
 
                ( 
                    "BOTTOMPADDING", 
                    (0, 0), 
                    (-1, -1), 
                    0, 
                ), 
 
                ( 
                    "LINEBEFORE", 
                    (1, 0), 
                    (1, 0), 
                    0.7, 
                    LIGHT_LINE, 
                ), 
 
                ( 
                    "LEFTPADDING", 
                    (1, 0), 
                    (1, 0), 
                    14, 
                ), 
            ] 
        ) 
    ) 
 
    # ======================================================== 
    # GENERATE PDF 
    # ======================================================== 
 
    doc.build( 
        [grid], 
        onFirstPage=draw_header, 
        onLaterPages=draw_header, 
    ) 
 
    print() 
    print("========================================") 
    print("Resume PDF generated successfully!") 
    print("========================================") 
    print(f"Output: {OUT}") 
    print() 
 
 
# ============================================================ 
# MAIN 
# ============================================================ 
 
if __name__ == "__main__": 
    build() 
 