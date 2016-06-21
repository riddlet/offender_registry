# offender_registry

This is code to extract data from the Maryland Sex Offender registry found [here](http://www.dpscs.state.md.us/sorSearch/)

The code is not yet tested, and as such, may still contain bugs. Nor has it been modified to run through the entire registry. At the moment, it scrapes 10 registrants at a time, specified by line 9 in `offender_spider.py`.

To run the code, download the entire directory, navigate to the directory using the command line and run `scrapy crawl maryland -o items.json`.

The output is a json file with the the details of each offender, and properties of the picture. The pictures are downloaded into `images/full`.

This spider was built using the [scrapy](http://doc.scrapy.org/en/1.1/index.html) framework.
