import os
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
os.sys.path.insert(0,parentdir)
from include import rake


def extract(text):
    rake_object = rake.Rake("data/stopwords.txt")
    """
    Each word has at least 5 characters
    Each phrase has at most 3 words
    Each keyword appears in the text at least 1 time
    """
    # text = "Give me a restaurant that is cheap. The restaurant should be within city limits."
    return rake_object.run(text)

extract('')