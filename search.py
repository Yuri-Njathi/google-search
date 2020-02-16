from googlesearch import search
#Based on this article => "https://towardsdatascience.com/current-google-search-packages-using-python-3-7-a-simple-tutorial-3606e459e0d4"

queries = ["Blue Githeri","Matoke"]
my_results_list = []

#for i in search()
for query in queries:
	print(query,"\n")
	for i in search(query,        # The query you want to run
	                tld = 'com',  # The top level domain
	                lang = 'en',  # The language
	                num = 10,     # Number of results per page
	                start = 0,    # First result to retrieve
	                stop = 20,  # Last result to retrieve
	                pause = 2.0,  # Lapse between HTTP requests
	               ):
	    my_results_list.append(i)
	    print("\t",i)