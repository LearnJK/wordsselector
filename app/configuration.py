class Config(object):
	DEBUG = False
	TESTING = False
	SECRET_KEY = "wordselector"

class ProductionConfig(Config):
	pass

class DevelopmentConfig(Config):
	DEBUG = True