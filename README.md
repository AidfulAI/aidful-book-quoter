# Aidful Book Quoter

A Python script that creates shareable quote images from books, combining the book cover with a beautifully formatted quote.

## Description

Aidful Book Quoter takes a book quote and the book's cover image to generate a visually appealing image suitable for social media sharing. The output image features:
- The quote in a clean, readable format with a stylish blockquote bar
- The book title and author
- The book cover image
- A clean, modern design with consistent formatting

## Examples
![Ikigai quote](example-ikigai.jpg)
![Millon Dollar Weekend quote](example-million.jpg)
## Requirements

- Python 3.x
- Pillow (Python Imaging Library)

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/aidful-book-quoter.git
cd aidful-book-quoter
```

2. Install required dependencies:
```bash
pip install Pillow
```

## Usage

1. Name your book cover image following the format: `Book Title - Author.ext` (where .ext is .jpg, .png, etc.)
2. Create a text file containing your quote
3. Run the script (Note: Spaces in filenames need to be escaped with backslashes, but tab completion in your terminal will handle this automatically):

```bash
python aidful-book-quoter.py data/quote.txt data/Million\ Dollar\ Weekend\ -\ Noah\ Kagan.jpg
```

The script will generate an image named `Book Title - Quote.png` in the current directory.

## License

This project is licensed under the Apache License, Version 2.0. You may obtain a copy of the license at:

http://www.apache.org/licenses/LICENSE-2.0

### Font License

This project uses Open Sans, which is also licensed under the Apache License, Version 2.0:

```
Copyright 2020 The Open Sans Project Authors (https://github.com/googlefonts/opensans)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
