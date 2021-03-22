"""
As a crazy politician, I would like to know, how many times is mentioned my name into this post. My name is Adolf.

POST:
----
Adolf not was the only one in this politic, there was other tree adolf's aDolf Junior, adolF, middle and the big ADOLF.
"""
post = """
Adolf not was the only one in this politic, there was other tree adolf's aDolf Junior, adolF, middle and 
the big ADOLF.
"""

print("Number of times that Adolf is mentioned: {}".format(post.lower().count("adolf")))
