from pdf2image import convert_from_path
import os

# Create static/images directory if it doesn't exist
os.makedirs('static/images', exist_ok=True)

# Convert each PDF to PNG
pdf_files = {
    'figs/2b_pretrained.pdf': 'static/images/fig2.png',
    'figs/gemma_forgetting.pdf': 'static/images/fig3.png',
    'figs/runtime.pdf': 'static/images/fig4.png'
}

for pdf_path, png_path in pdf_files.items():
    # Convert PDF to image
    images = convert_from_path(pdf_path)
    # Save first page as PNG
    images[0].save(png_path, 'PNG')
    print(f'Converted {pdf_path} to {png_path}') 