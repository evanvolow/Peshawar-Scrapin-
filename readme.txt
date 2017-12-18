Hi, it looks like you found the GitHub page for my project, Peshawar Scrapin’.

The objective here was to expand on and improve the metadata for a set of CIA documents on the Afghan-Soviet War, sourced from the CIA FOIA Electronic Reading Room. The expanded metadata are in the file expanded_metadata.json

***Take everything in my metadata as a guess! This is intended as a tool to aid exploration of the documents, not 100% solid cataloging***

This task was accomplished mainly using Python. To run some of these scripts, you'll need the BeautifulSoup webscraping module installed. 

-------------------------

The Python scripts here, in order of application to achieve the final result, are:

—URLGrab.py - scrapes URLs for PDFs from CIA website. Produces the file urllist.json

—PDFGrab.py - actually downloads the PDFs.

—MetadataGrab.py - scrapes the (mostly useless) metadata for each document from the CIA website, and saves them in provided_metadata.json.

-exportText.py - exports OCR'd text from the PDFs into .txt files that share the same name as the PDF. I used Adobe Acrobat Pro for OCR. It took six days. I might upload the resulting text files somewhere eventually.

—WikiGrab.py - generates human-curated lists of people, organizations, et cetera by scraping links from input Wiki URLs and asking the user if/where to put each one. This script generated people.json, orgs.json, relevance.json, other.json, and checked.json. These json files required a lot of manual work after being created. 

-tagPeople.py - tags the people ingested from wikipedia to the appropriate articles
-tagOrgs.py - same, but with organizations
-tagOther.py - same, but with other stuff

-geoConvert.py - I got my file of geographic names in Afghanistan from the National Geospatial-Intelligence Agency (over here: http://geonames.nga.mil/gns/html/namefiles.html). They came as a tab-separated text file, which I saved as .csv and stripped down to the bare necessities in Excel. I originally used the really huge "af.txt" name file with EVERYTHING in it, but it was too slow and contained too many duplicated or ubiquitous names. Turns out there are a lot of places in Afghanistan with names like "China", or "Asia", or "Bag". I switched over to the just-administrative af_administrative_a.txt file, which took care of those problems. It basically tags provinces and major cities, but I think that's all most users will want, anyway.

-tagGeo.py - tags geographic features mentioned above

-relAnalysis.py - estimates relevance of document to subject of Soviet-Afghan war based on number of relevant terms versus total word count, on a 0 to 100 scale. Anything over 100 gets changed to 100.

-metaCSV.py - converts the expanded metadata JSON file to CSV for a broader audience. 


A prettier version of the CSV metadata may be found on Google Drive at: https://goo.gl/SrG8qL