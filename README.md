# offender_registry

This is code to extract data from the Maryland Sex Offender registry found [here](http://www.dpscs.state.md.us/sorSearch/)

The code is lightly tested and should not contain any major bugs. There are two errors on the website itself, necessitating a skip of a couple of pages. It's not clear whether there should be listings on those pages or not. Regardless, the crawler should obtain all listings from the website.

To run the code, download the entire directory, navigate to the directory using the command line and run `scrapy crawl maryland -o items.json`.

The output is a json file with the the details of each offender, and properties of the picture. The pictures are downloaded into `images/full`.

This spider was built using the [scrapy](http://doc.scrapy.org/en/1.1/index.html) framework.
