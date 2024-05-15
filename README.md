# Wikipedia Pathfinder

Wikipedia Pathfinder is a **Project** web application which a user can find the shortest path between two wikipedia articles.

It uses [Flask](https://flask.palletsprojects.com/en/3.0.x/) to serve a web page style with [TailwindCSS](https://tailwindcss.com/) in which the user can input article URLs.

In addition to the front end, the pathfinder can be access via CLI using arguments.

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) is used to scrape the the articles live.


### Installing and running

* Clone this respository
    * HTTPS: `git clone https://github.com/AlexTuTruong/wikipedia-pathfinder.git`
    * SSH: `git clone git@github.com:AlexTuTruong/wikipedia-pathfinder.git`
    * Github CLI: `gh repo clone AlexTuTruong/wikipedia-pathfinder`
* Navigate to the root folder in this repository
    * `cd /path/to/folder/wikipedia-pathfinder`
* Install the dependencies
    * `pip install -r requirements.txt`
* Run the application
    * `python3 run.py` within the root directory
        * This should run a web server in which you can access from `http://localhost:5000/` or `http://127.0.0.1:5000/`

Optionally, Use CLI pathfinder:

* Run `python3 pathfinder_cli.py [--max-depth MAX_DEPTH] start_url target_url`
    * For help, run `python3 pathfinder_cli.py -h`


## Notes

There are definitely faster methods to find the shortest path between two wikipedia articles, most of these solutions require a database containing article ID's, links and redirects. I wanted to learn and experiment with web scraping, hence the use of Beautiful Soup. There are rate limits other delays associated with HTTP requests which make the BFS slow.

Wikipedia logo credit: [Wikipedia](https://en.wikipedia.org/wiki/Wikipedia_logo)

Pathfinder image credit: [Opallolo](https://www.redbubble.com/people/opallolo/shop)


## Image
![WikiPathfinder](https://github.com/AlexTuTruong/wikipedia-pathfinder/assets/53573114/99422ce8-2f96-4f52-8f98-51e377e55959)

Input field on the left will take the start url, input field on the right will take the target URL.

A list of encountered paths will be placed on the bottom portion of the page

## License

This project is licensed under the MIT License - see the LICENSE.md file for details
