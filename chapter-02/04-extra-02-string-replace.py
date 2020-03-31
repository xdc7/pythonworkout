"""
In academia, it’s common to remove the authors' names from a paper submitted for peer review. Given a string containing an article and a separate list of strings containing authors' names, replace all names in the article with _ characters.

"""

def redactAuthorNames(articleString, authorsList):
	for author in authorsList:
		articleString = articleString.replace(author, '_')
	return articleString
	
	

print (redactAuthorNames('What a fine article by authors John Smith, Helen Mattingly, and Matthew Stevens',['John Smith', 'Helen Mattingly', 'Matthew Stevens']))

print (redactAuthorNames('great synopsis by  by authors John A. Smith, Helen Jane Mattingly, and W. Matthew Stevens',['John A. Smith', 'Helen Jane Mattingly', 'W. Matthew Stevens']))


