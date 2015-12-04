import os

def rip_pages(file_name, start_page, end_page):

    for page_number in range(start_page, end_page+1):
        output_filename = "pages/layout_%s.txt" % (page_number)
        layout_cmd = "pdftotext -f %s -l %s -layout %s %s" % (page_number, page_number, file_name, output_filename)
        print layout_cmd
        result = os.popen(layout_cmd).read()
        print result