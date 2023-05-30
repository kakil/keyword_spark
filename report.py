from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import textwrap

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import textwrap

import re

def generate_pdf_report(topic, summaries, content_ideas, tweets,cost,token_count):
    # Create a new PDF document with the given filename
    pdf_filename = 'report.pdf'
    c = canvas.Canvas(pdf_filename, pagesize=letter)

    # Function to create a new page
    def new_page():
        nonlocal y
        c.showPage()
        y = 750

    # Set the font and font size for the report
    c.setFont("Helvetica", 12)

    # Write the report title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, 750, "Report for Topic: {}".format(topic))

    # Write section headings and corresponding text
    y = 700
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Summaries:")
    c.setFont("Helvetica", 12)
    y -= 20
    for summary in summaries:
        lines = summary.splitlines()  # split the summary into lines
        for i, line in enumerate(lines):
            wrapped_lines = textwrap.wrap(line, width=70)  # wrap each line to the desired width
            for j, wrapped_line in enumerate(wrapped_lines):
                # Only add a dash if it's the start of a new summary and the first character is not a dash
                if j == 0 and not line.startswith('-'):
                    c.drawString(50, y, "- " + wrapped_line)
                else:
                    c.drawString(50, y, wrapped_line)
                y -= 15
                if y < 30:
                    new_page()


    # Add a space between sections
    y -= 20
    if y < 30:
        new_page()

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Content Ideas:")
    c.setFont("Helvetica", 12)
    y -= 20
    for idea in content_ideas:
    # Split the idea into sections based on occurrences of a number followed by a period
        sections = re.split(r'(\d+[\.\)]\s)', idea)
        for section in sections:
            # If the section is a number followed by a period and a space, start a new line
            if re.match(r"\d+[\.\)]\s", section):
                y -= 15
                if y < 30:
                    new_page()
                # Wrap the section and print each line
                lines_to_print = textwrap.wrap(section.strip(), width=70)
                for line_to_print in lines_to_print:
                    c.drawString(50, y, line_to_print)
                    # y -= 15
                    if y < 30:
                        new_page()
            else:
                # Wrap the section and print each line
                lines = textwrap.wrap(section, width=70)
                for line in lines:
                    # Print the line as is, without any "-"
                    c.drawString(50, y, "      " + line)
                    y -= 15
                    if y < 30:
                        new_page()
                    



    # Add a space between sections
    y -= 20
    if y < 30:
        new_page()

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Twitter Tweets:")
    c.setFont("Helvetica", 12)
    y -= 20
    for tweet in tweets:
        # split the tweets into sections based on occurrences of a number followed by a period
        sections = re.split(r'(\d+[\.\)]\s)', tweet)
        for section in sections:
            # If the section is a number followed by a period and a space, start a new line
            if re.match(r"\d+[\.\)]\s", section):
                y -= 15
                if y < 30:
                    new_page()
                
                # Wrapt the section and print each line
                lines_to_print = textwrap.wrap(section, width=70)
                for line_to_print in lines_to_print:
                    c.drawString(50, y, line_to_print)
                    # y -= 15
                    if y < 30:
                        new_page()      
            else:
                # Wrap the section and print each line
                lines = textwrap.wrap(section, width=70)
                for line in lines:
                    #Print the line as is 
                    c.drawString(50, y, "     " + line)
                    y -= 15
                    if y < 30:
                        new_page()
                
            

    # Add a space between sections
    y -= 20
    if y < 30:
        new_page()

   
    
    c.setFont("Helvetica", 14)
    c.drawString(50, y, "Estimated Cost: $ {} for {} tokens".format(cost,token_count))

    # Save the PDF document
    c.save()


  


