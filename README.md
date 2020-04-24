# Scraping PCG to CSV files

## Custom variables

1) Set list of URL to scrape.

    - Rename ***urls_to_scrape_EMTPY.json*** file to ***urls_to_scrape.json*** or the name you want.
    - Edit ***urls_to_scrape.json*** file and add list of urls and output CSV files JSON format.

        ```JSON
        [
            {
                "url": "https://www.url-1.com",
                "file": "output-file-1.csv"
            },
            {
                "url": "https://www.url-2.com",
                "file": "output-file-2.csv"
            }
        ]
        ```

1) Configure params on *main.py* file.

    - **INPUT_FILE**: Input file (i.e: "urls_to_scrape_TEST.json")
    - **OUTPUT_DIRECTORY**: Output directory (i.e: "c:/tmp/")
    - **CSV_HEADER**: First row of CSV file (i.e:  "Prefix-1\tPrefix-2\tId\tDescription\tLink\tDate update")