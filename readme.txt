Hi, it looks like you found the GitHub page for my project, Peshawar Scrapin’.

The objective here was to expand on and improve the metadata for a set of CIA documents on the Afghan-Soviet War, sourced from the CIA FOIA Electronic Reading Room. The expanded metadata are in the file expanded_metadata.json

***Take everything in my metadata as a guess! This is intended as a tool to aid exploration of the documents, not 100% solid cataloging***

This task was accomplished mainly using Python. The Python scripts here, in order of application to achieve the final result, are:

—URLGrab.py - scrapes URLs for PDFs from CIA website. Produces the file urllist.json
—PDFGrab.py - actually downloads the PDFs.
—MetadataGrab.py - scrapes the (mostly useless) metadata for each document from the CIA website, and saves them in provided_metadata.json.
-exportText.py - exports OCR'd text from the PDFs into .txt files that share the same name as the PDF. I used Adobe Acrobat Pro for OCR. It took six days. I might upload the resulting text files somewhere eventually.
—WikiGrab.py - generates human-curated lists of people, organizations, et cetera by scraping links from input Wiki URLs and asking the user if/where to put each one. This script generated people.json, orgs.json, relevance.json, other.json, and checked.json. These json files required a lot of manual work after being created. 
-geoConvert.py - I got my file of geographic names in Afghanistan from the National Geospatial-Intelligence Agency (over here: http://geonames.nga.mil/gns/html/namefiles.html). They came as a tab-separated text file, which I saved as .csv and stripped down to the bare necessities in Excel. This script takes the CSV and converts it into a JSON, putting all variants of a place name under one heading to facilitate clean tagging. Apparently there are places in Afghanistan called "China", or "Asia", or "Bag", et cetera, plus a lot of places that share the same name. I ended up doing a lot of cleanup so the tagging wouldn't be bizarre, and there's still more to be done. For example, since "Afghan" appears as an alternate name for "Gurguri Tanah", that one got tagged an inordinate amount. Again, take everything with a grain of salt.
-tagPeople.py - tags the people from people.json in the documents. Adds them to expanded_metadata.json, along with counts of mentions in the document.
-tagOrgs.py - same, but with organizations.
-tagGeo.py - same, but with geographic features of Afghanistan. 
-degurgurizer.py - removes the aforementioned extraneous "Gurguri Tanah" and other offending tags from the geographic metadata.