from io import StringIO
from pdfminer.high_level import extract_text
from pdfminer.layout import LTTextBoxHorizontal

def replace_text_in_pdf(input_path, output_path, text_to_replace, replaced_text):
  """
  Replaces text in a PDF document using PDFMiner.six.

  Args:
      input_path (str): Path to the input PDF file.
      output_path (str): Path to save the modified PDF file.
      text_to_replace (str): The text to be replaced (case-sensitive).
      replaced_text (str): The text to replace with.
  """
  with open(input_path, 'rb') as f:
      pages = extract_text(f).split('\n\n')  # Split by page breaks

  modified_pages = []
  for page in pages:
      modified_text = ""
      for line in page.splitlines():
          if isinstance(line, LTTextBoxHorizontal):  # Check for horizontal text boxes
              modified_text += line.strip().replace(text_to_replace, replaced_text) + "\n"
          else:
              # Handle other elements (optional)
              modified_text += line + "\n"
      modified_pages.append(modified_text)

  with open(output_path, 'w', encoding='utf-8') as f:
      f.write(''.join(modified_pages))

  print(f"Text replacement completed. Output file: {output_path}")

# Example usage
input_path = "input.pdf"
output_path = "output.pdf"
text_to_replace = "summary"
replaced_text = "replaced-text"

replace_text_in_pdf(input_path, output_path, text_to_replace, replaced_text)
