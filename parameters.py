class parameters(object):

	def __init__(self):

		#SCRAPER PARAMETERS
		#global variables
		self.root_filepath = "/media/darg1/Data/Projects/erhan_tez/WikimediaCommons-scraper/data"
		self.vocab_filename = "word_vocab.txt"
		self.output_filename = "wikimediacommons_photo_links.txt"
		self.limit = 1000 #number of urls to download for each keyword in dictionary
		self.urls = {}

		#supported image extensions of wikimedia commons
		self.image_extensions = ["jpg","jpeg","jpe","png","apng","gif","tiff","tif","xcf","webp"]

		#wikimedia urls
		self.url_prefix = "https://commons.wikimedia.org"
		self.page2parse = "https://commons.wikimedia.org/w/index.php?sort=relevance&title=Special:Search&profile=advanced&fulltext=1&advancedSearch-current=%7B%7D&ns0=1&ns6=1&ns12=1&ns14=1&ns100=1&ns106=1"#url of advance search page




PARAM = parameters()
