from domainstackr.app import app
from domainstackr.scraping.ScraperFactory import ScraperFactory


if __name__ == '__main__':
    factory = ScraperFactory()
    factory.start()
    app.run(debug=True)
