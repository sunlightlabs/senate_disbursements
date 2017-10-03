# Senate Disbursements

This is half-done code to parse the senate clerk's report on spending, which are available [here](http://www.senate.gov/legislative/common/generic/report_secsen.htm). 

For more about this project see the introductory blog post [here](https://sunlightfoundation.com/blog/2014/08/05/now-its-easier-to-account-for-how-the-senate-spends-your-money/). 

There's no `requirements.txt` file, but you'll need [pdftotext](http://macappstore.org/pdftotext/) installed on your system. 

## How to process new files

1. Grab a new file from [here](http://www.senate.gov/legislative/common/generic/report_secsen.htm). You'll want to download the "full report". 
2. Create a new directory to put it in. By convention I've been using  the document number as the dir name, i.e. 114_sdoc4.
3. In the new directory, copy over `rip_pages.py`, `read_pages.py`, `run.py`, and `format_csv.py` from the `114_sdoc7`. Also you need to create a "pages" subdirectory, where each of the pages will go.
4. Open the "full report" disbursement file and figure out where the "regular" itemizations begin and end. In [this file](http://www.gpo.gov/fdsys/pkg/GPO-CDOC-114sdoc4/pdf/GPO-CDOC-114sdoc4.pdf) the itemizations start on page 17 and end on page 2073. Edit `run.py` to reference the right `file_name`, `start_page`, `end_page`. The `start_page` and `end_page` should reflect those numbers (they are inclusive). 
5. Then run `run.py` (i.e. `$ python run.py`). 


## Notes:

- Sometimes read_pages.py will freak out and die because there are empty pages between sections in the report. You can just edit the script to exclude these pages. 
- Running read_pages.py will produce output about problems reading individual lines (it's also dumped to missing_data.txt). These lines are not included in the csv output because they couldn't be properly parsed. Most are "continuations" of lines that are included, so the result is that the description that appears in the csv file is truncated. Others are more complex problems, which may need manual fixes. 
