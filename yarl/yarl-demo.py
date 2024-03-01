import yarl

# Create a URL
url = yarl.URL("https://www.example.com/path/to/resource?param1=value1&param2=value2")

# Accessing different components of the URL
print("Scheme:", url.scheme)
print("Host:", url.host)
print("Path:", url.path)
print("Query parameters:", url.query)

# Modifying the URL
url = url.with_path("/newpath")
url = url.with_query({"newparam": "newvalue"})

# Printing the modified URL
print("Modified URL:", url)

# Resolving relative URLs
relative_url = yarl.URL("/relative/path")
resolved_url = url.join(relative_url)
print("Resolved URL:", resolved_url)
