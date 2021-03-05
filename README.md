# django-Google-pagerank
A simple Django app to find page ranking in google by keywords.

1. First problem encountered is how to fetch the google search data. To solve this Requests
package along with custom search engine and a generated API key is used to obtain the google
search data.
2. A code for making the query and ranking :
◦ A loop over all 10 pages fetched by Google search
◦ API request is made to fetch search data for particular page with desired keyword
◦ Another loop inside the first loop investigates the page data to obtain the desired keyword
and parent domain.
◦ If the domain name ends with target domain we get the page rank and other features printed.
Django integration
1. In home.html we ask for the input, target domain and the keyword(s).
2. Send the input data in the add function of views.py
3. The logic of the code is integrated within the views.py
4. Returns JSON response.
