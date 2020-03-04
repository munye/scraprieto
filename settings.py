iDOWNLOADER_MIDDLEWARES.update({
    'scrapy.downloadermiddlewares.cookies.CookiesMiddleware': None,
    'scrapy_cookies.downloadermiddlewares.cookies.CookiesMiddleware': 700,
})

COOKIES_ENABLED = True

COOKIES_PERSISTENCE = True
COOKIES_PERSISTENCE_DIR = 'cookies'

# ------------------------------------------------------------------------------
# IN MEMORY STORAGE
# ------------------------------------------------------------------------------

COOKIES_STORAGE = 'scrapy_cookies.storage.in_memory.InMemoryStorage'
