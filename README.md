# Manga Downloader using Python

This project is a personal learning project aimed at building a web to download mangas into PDF. i'm still having an issue on production (Vercel) so if you want to try this project you can run on your local machine.

## Features

- Search manga
- List manga chapters
- Download manga into PDF

## Installation

To run this project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/ilhamnyto/manga-downloader-python.git`
2. Create a Virtual Environment: `virtualenv venv`
3. Activate virtualenv `source venv/Scripts/activate` (Windows) or `source venv/bin/activate` (Linux)
4. Install dependencies: `pip install -r requirements.txt`
5. Install npm dependencies: `npm install`
6. Copy the env files: `cp .env.example .env`.
7. Run the database migrations: `python manage.py runserver`
8. Open browser: `localhost:8000`

## License

This project is licensed under the [MIT License](./LICENSE).

## Acknowledgments

This project was made possible by the following open-source libraries:

- [Django](https://www.djangoproject.com/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [AIOHTTP](https://docs.aiohttp.org/en/stable/)
- [PyPDF2](https://pypdf2.readthedocs.io/en/latest/modules/PdfWriter.html)
- [reportlab](https://pypi.org/project/reportlab/)
- [TailwindCSS](https://tailwindcss.com/)

