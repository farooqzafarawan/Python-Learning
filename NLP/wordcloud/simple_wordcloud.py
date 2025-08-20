from collections import Counter  # Count the frequency of distinct strings
from wordcloud import WordCloud, ImageColorGenerator  # Generate wordclouds
from PIL import Image  # Load images from files
from pathlib import Path  # Handle file paths

dataDir = Path(__file__).parent.parent.parent / "DATA"  # Directory containing resources
txtFile = dataDir / "adelaide.txt"  # Path to the text file

with open(txtFile, "r") as file:
    text = file.read()

text[:200]

# Split the text into a list of individual words
tokens = text.split(" ")

# Count the frequency of each word
word_counts = Counter(tokens)


# Display the count for a single word.
word_counts["love"]


our_wordcloud = WordCloud()  # Create a wordcloud generator 

our_wordcloud.generate(text)  # Generate the cloud using raw text

our_wordcloud.to_image().show()    # Save the generated image

our_wordcloud.to_image().save(dataDir / "adelaide_wordcloud.png")