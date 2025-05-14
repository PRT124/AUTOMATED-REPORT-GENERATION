from fpdf import FPDF

def analyze_data(file_path):
    """Simple analysis: count lines, words, characters"""
    with open(file_path, 'r') as f:
        text = f.read()
    lines = text.split('\n')
    words = text.split()
    return len(lines), len(words), len(text)

def generate_pdf(lines, words, characters, output_path):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="File Analysis Report", ln=True, align="C")
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Total Lines: {lines}", ln=True)
    pdf.cell(200, 10, txt=f"Total Words: {words}", ln=True)
    pdf.cell(200, 10, txt=f"Total Characters: {characters}", ln=True)

    pdf.output(output_path)

def main():
    file_path = input("Enter the path of the text file: ")
    lines, words, characters = analyze_data(file_path)
    generate_pdf(lines, words, characters, "report.pdf")
    print("Report generated: report.pdf")

if __name__ == "__main__":
    main()
