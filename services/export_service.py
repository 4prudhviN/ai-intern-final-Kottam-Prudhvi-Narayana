from fpdf import FPDF
import os
from datetime import datetime

EXPORT_DIR = "exports"
os.makedirs(EXPORT_DIR, exist_ok=True)

LEFT_MARGIN = 20
RIGHT_MARGIN = 20
TOP_MARGIN = 20


def export_txt(content: str):
    txt_path = os.path.join(EXPORT_DIR, "research_output.txt")
    with open(txt_path, "w", encoding="utf-8") as file:
        file.write(content)
    return txt_path


def clean_line(text: str) -> str:
    """Sanitize a single line: strip non-latin-1 chars and break long tokens."""
    safe = text.encode("latin-1", errors="replace").decode("latin-1")
    words = safe.split(" ")
    broken = []
    for word in words:
        # Break tokens longer than 60 chars with a space every 60 chars
        if len(word) > 60:
            chunks = [word[i:i+60] for i in range(0, len(word), 60)]
            broken.append(" ".join(chunks))
        else:
            broken.append(word)
    return " ".join(broken)


class PDF(FPDF):
    def __init__(self):
        super().__init__()
        self.set_margins(LEFT_MARGIN, TOP_MARGIN, RIGHT_MARGIN)

    @property
    def usable_width(self):
        return self.w - self.l_margin - self.r_margin

    def header(self):
        self.image("assets/logo.png", x=10, y=8, w=25)
        self.set_font("Arial", "B", 14)
        self.set_text_color(30, 30, 30)
        self.cell(self.usable_width, 10, "AI Research Intelligence Platform", ln=True, align="C")
        self.set_font("Arial", "I", 9)
        self.set_text_color(120, 120, 120)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.cell(self.usable_width, 6, f"Generated: {timestamp}", ln=True, align="C")
        self.ln(3)
        self.set_draw_color(99, 102, 241)
        self.set_line_width(0.4)
        self.line(self.l_margin, self.get_y(), self.w - self.r_margin, self.get_y())
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(self.usable_width, 10, f"Page {self.page_no()} | AI Research Intelligence Platform", align="C")

    def write_line(self, text: str, font_style: str, font_size: int, color: tuple, line_height: int):
        self.set_font("Arial", font_style, font_size)
        self.set_text_color(*color)
        safe = clean_line(text)
        self.multi_cell(self.usable_width, line_height, safe)


def export_pdf(content: str):
    pdf_path = os.path.join(EXPORT_DIR, "research_output.pdf")

    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=20)
    pdf.add_page()

    for raw_line in content.split("\n"):
        stripped = raw_line.strip()

        if stripped.startswith("# ") and not stripped.startswith("## "):
            pdf.write_line(stripped[2:], "B", 15, (20, 20, 20), 10)
            pdf.ln(2)

        elif stripped.startswith("## "):
            pdf.write_line(stripped[3:], "B", 12, (40, 40, 40), 8)
            pdf.ln(1)

        elif stripped.startswith("- ") or stripped.startswith("* "):
            pdf.write_line("  \u2022 " + stripped[2:], "", 10, (60, 60, 60), 7)

        elif stripped.startswith("*") and stripped.endswith("*") and len(stripped) > 2:
            pdf.write_line(stripped.strip("*"), "I", 9, (120, 120, 120), 6)

        elif stripped == "---":
            pdf.set_draw_color(200, 200, 200)
            pdf.set_line_width(0.3)
            pdf.line(pdf.l_margin, pdf.get_y(), pdf.w - pdf.r_margin, pdf.get_y())
            pdf.ln(4)

        elif stripped == "":
            pdf.ln(3)

        else:
            pdf.write_line(stripped, "", 10, (50, 50, 50), 7)

    pdf.output(pdf_path)
    return pdf_path
