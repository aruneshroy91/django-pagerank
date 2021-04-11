from django.http.response import Http404, HttpResponse
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import urllib.parse as p

# Create your views here.

data = {}

# Request the home page

def home(request):
    return render(request, 'home.html',{'name':'Google page ranking by keywords'})

# Now the algorithm

def add(request):
    target_domain = request.GET['website']
    query = request.GET['keywords']
    # get the API KEY here: https://developers.google.com/custom-search/v1/overview
    API_KEY = "<Put_your_API_KEY_here>"
    # get your Search Engine ID on your CSE control panel
    SEARCH_ENGINE_ID = "<Put_your_Search_Engine_ID_here>"

    for page in range(1, 11):
        print("[*] Going for page:", page)
        start = (page - 1) * 10 + 1
        
        url = f"https://www.googleapis.com/customsearch/v1?key={API_KEY}&cx={SEARCH_ENGINE_ID}&q={query}&start={start}"
        data = requests.get(url).json()
        search_items = data.get("items")
        
        found = False
        for i, search_item in enumerate(search_items, start=1):
            
            title = search_item.get("title")
            
            snippet = search_item.get("snippet")
            
            html_snippet = search_item.get("htmlSnippet")
            
            link = search_item.get("link")
            
            domain_name = p.urlparse(link).netloc
            if domain_name.endswith(target_domain):
                
                rank = i + start - 1
                print(f"[+] {target_domain} is found on rank #{rank} for keyword: '{query}'")
                print("[+] Title:", title)
                print("[+] Snippet:", snippet)
                print("[+] URL:", link)
                # target domain is found, exit out of the program
                found = True
                break
        if found:
            break
    # rank+1 is due to counting starts from 
    # return render(request, "rank.html",{'result':rank+1})
    # ({"found":print(rank<=10)},{"rank":rank},{"page":link},{"domain":target_domain})
    return JsonResponse({"found" : found, "rank":rank+1, "page":link, "domain":target_domain})


