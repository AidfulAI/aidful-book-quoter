from PIL import Image, ImageDraw, ImageFont
import sys
import os
import argparse

def parse_cover_filename(filename):
    base = os.path.splitext(filename)[0]
    parts = base.split(' - ')
    if len(parts) != 2:
        raise ValueError("Cover file must be named 'Book Title - Author.ext'")
    return parts[0], parts[1]

def read_quote(quote_file):
    try:
        with open(quote_file, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except IOError:
        print(f"Could not read quote file: {quote_file}")
        exit(1)

def create_quote_image(quote_file, cover_path):
    # Extract book title and author from filename
    book_title, author = parse_cover_filename(cover_path)

    # Read quote from file
    quote = read_quote(quote_file)

    # Font path (assuming it's in the same directory)
    font_path = 'OpenSans-Regular.ttf'

    # Load the book cover image
    try:
        book_cover = Image.open(cover_path)
    except IOError:
        print("Book cover image file not found.")
        exit(1)

    # Get the size of the cover image
    cover_width, cover_height = book_cover.size

    # Define the output image size
    output_width = 3 * cover_width
    output_height = cover_height

    # Create new image with white background
    img = Image.new('RGB', (output_width, output_height), color='white')

    # Fill the left two-thirds with a homogeneous color (e.g., light gray)
    from PIL import ImageColor
    left_background_color = ImageColor.getrgb("#f5f5f5")  # Light gray color
    left_background = Image.new('RGB', (2 * cover_width, cover_height), color=left_background_color)
    img.paste(left_background, (0, 0))

    # Paste book cover onto the right third of the main image
    book_cover_x = 2 * cover_width  # Start position for the book cover
    book_cover_y = 0
    img.paste(book_cover, (book_cover_x, book_cover_y))

    # Create drawing context
    draw = ImageDraw.Draw(img)

    # Font sizes (adjust as needed)
    quote_font_size = int(cover_height * 0.05)
    title_font_size = int(cover_height * 0.04)
    author_font_size = int(cover_height * 0.035)

    # Load fonts
    try:
        quote_font = ImageFont.truetype(font_path, quote_font_size)
        title_font = ImageFont.truetype(font_path, title_font_size)
        author_font = ImageFont.truetype(font_path, author_font_size)
    except IOError:
        print("Font file not found. Please ensure the font file is in the same directory.")
        quote_font = ImageFont.load_default()
        title_font = ImageFont.load_default()
        author_font = ImageFont.load_default()

    # Colors for text and block quote
    text_color = (50, 50, 50)  # Dark gray for text
    blockquote_color = (100, 100, 100)  # Gray for the vertical bar

    # Modify margins to account for block quote
    margin = int(cover_width * 0.05)
    vertical_spacing = int(cover_height * 0.02)

    # Function to get text size
    def get_text_size(text, font):
        bbox = font.getbbox(text)
        width = bbox[2] - bbox[0]
        height = bbox[3] - bbox[1]
        return width, height

    # Function to wrap text
    def wrap_text(text, font, max_width):
        lines = []
        words = text.split()
        current_line = ''
        for word in words:
            test_line = current_line + ' ' + word if current_line else word
            line_width, _ = get_text_size(test_line, font)
            if line_width <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line)
                current_line = word
        if current_line:
            lines.append(current_line)
        return lines

    # Margins
    margin = int(cover_width * 0.05)
    text_area_width = (2 * cover_width) - (2 * margin)

    # Calculate text block dimensions
    quote_lines = wrap_text(quote, quote_font, text_area_width - margin)  # Reduce width for bar
    title_lines = wrap_text(book_title, title_font, text_area_width)
    author_lines = wrap_text(author, author_font, text_area_width)

    # Calculate total height
    total_height = 0
    for line in quote_lines:
        _, height = get_text_size(line, quote_font)
        total_height += height + vertical_spacing
    total_height += vertical_spacing * 2  # Extra spacing before and after quote

    for line in title_lines:
        _, height = get_text_size(line, title_font)
        total_height += height + vertical_spacing

    for line in author_lines:
        _, height = get_text_size(line, author_font)
        total_height += height + vertical_spacing

    # Center the text block vertically
    current_y = (cover_height - total_height) // 2

    # Draw vertical bar for blockquote
    bar_width = int(cover_width * 0.01)
    bar_x = margin
    bar_start_y = current_y
    quote_height = sum([get_text_size(line, quote_font)[1] + vertical_spacing for line in quote_lines])
    bar_end_y = bar_start_y + quote_height
    draw.rectangle([(bar_x, bar_start_y), (bar_x + bar_width, bar_end_y)],
                fill=blockquote_color)

    # Draw quote text with indentation
    quote_x = margin + bar_width + int(margin * 0.5)
    for line in quote_lines:
        width, height = get_text_size(line, quote_font)
        draw.text((quote_x, current_y), line, font=quote_font, fill=text_color)
        current_y += height + vertical_spacing

    current_y += vertical_spacing  # Extra space after quote

    # Draw book title
    for line in title_lines:
        width, height = get_text_size(line, title_font)
        line = line.replace('data/', '')  # Remove data/ folder from title
        draw.text((margin, current_y), line, font=title_font, fill=text_color)
        current_y += height + vertical_spacing

    # Draw author
    for line in author_lines:
        width, height = get_text_size(line, author_font)
        draw.text((margin, current_y), line, font=author_font, fill=text_color)
        current_y += height + vertical_spacing

    # Save the image
    output_filename = f"{book_title} - Quote.jpg"
    img.save(output_filename)
    print(f"Image saved as {output_filename}")

def main():
    parser = argparse.ArgumentParser(description='Create a book quote image')
    parser.add_argument('quote_file', help='Path to text file containing the quote')
    parser.add_argument('cover', help='Path to book cover image (format: "book title - author.ext")')

    args = parser.parse_args()
    create_quote_image(args.quote_file, args.cover)

if __name__ == "__main__":
    main()
