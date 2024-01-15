web: gunicorn server.wsgi --log-file -
worker: python main.py
scraper: /bin/bash -c "python manage.py scrape_toldot && python manage.py scrape_arister"

