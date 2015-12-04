from rip_pages import rip_pages
from read_pages import read_pages
from format_csv import format_csv

# STEP 1: CONFIG VARIABLES
SOURCE_DOC = '114sdoc7'
FILE_NAME = "GPO-CDOC-" + SOURCE_DOC + ".pdf"
OUT_FILE = 'senate_data.csv'
MISSING_FILE = 'missing_data.json'
START_PAGE = 17
END_PAGE = 2259

# STEP 2: Rip text, read pages, format output
rip_pages(FILE_NAME, START_PAGE, END_PAGE)
read_pages(START_PAGE, END_PAGE, OUT_FILE, MISSING_FILE)
format_csv(SOURCE_DOC, OUT_FILE)

# STEP 3: Reconcile data in MISSING_FILE



