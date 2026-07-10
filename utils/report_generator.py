from fpdf import FPDF
import io

def generate_pdf_report(compatibility, verdict, matches, gaps, improvements):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    
    # Title
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 15, "ATS Compliance Optimization Report", ln=True, align="C")
    pdf.ln(5)
    
    # Score Section
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(0, 10, f"ATS Compatibility Score: {compatibility}%", ln=True)
    pdf.cell(0, 10, f"Recruitment Verdict: {verdict}", ln=True)
    pdf.ln(5)
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(5)
    
    # Matches
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 10, "Detected Technical Matches:", ln=True)
    pdf.set_font("Helvetica", "", 11)
    if matches and len(matches) > 0:
        for match in matches:
            pdf.cell(0, 7, f"- {match}", ln=True)
    else:
        pdf.cell(0, 7, "No matching structural keywords isolated.", ln=True)
    pdf.ln(5)
    
    # Gaps
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 10, "Critical Skills Gaps:", ln=True)
    pdf.set_font("Helvetica", "", 11)
    if gaps and len(gaps) > 0:
        for gap in gaps:
            # Replaces any markdown asterisks or bullet formatting to print cleanly
            clean_gap = str(gap).replace("• ", "").replace("* ", "")
            pdf.multi_cell(0, 7, f"x {clean_gap}")
    else:
        pdf.cell(0, 7, "No explicit skills omissions flagged.", ln=True)
    pdf.ln(5)
    
    # Improvements
    pdf.set_font("Helvetica", "B", 12)
    pdf.cell(0, 10, "Granular Bullet Point Improvements:", ln=True)
    pdf.set_font("Helvetica", "", 11)
    if improvements and len(improvements) > 0:
        for imp in improvements:
            clean_imp = str(imp).replace("• ", "").replace("* ", "")
            pdf.multi_cell(0, 7, f"* {clean_imp}")
    else:
        pdf.cell(0, 7, "No structural improvements suggested.", ln=True)
        
    # Get raw output bytes directly and convert cleanly to stream
    pdf_bytes = pdf.output()
    return io.BytesIO(pdf_bytes)