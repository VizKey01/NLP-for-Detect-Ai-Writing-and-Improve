import re

# The input string
input_string = 'Cansado de tener tantas pestañas abiertas para acceder a diferentes herramientas de escritura e investigación? , [ { "Vocabulary": "Sick", "Part of Speech": "Adjective", "Translation": "Enfermo/a", "Example": "I feel sick today. (Hoy me siento enfermo/a)" }, { "Vocabulary": "Tabs", "Part of Speech": "Noun", "Translation": "Pestañas", "Example": "I have many tabs open in my browser. (Tengo muchas pestañas abiertas en mi navegador)" }, ... ]'

# Define the regular expression pattern
pattern = r'^(.+)\s*,\s*(\[\s*\{.+\}\s*\]\s*)$'

# Use re.match to extract the parts of the string
# match = re.match(pattern, input_string)

match = re.sub(pattern,'', input_string)
match = match.strip()

print(match)

# If there's a match, extract the groups
# if match:
#     output_list = [match.group(1), match.group(2)]
#     print(output_list)
# else:
#     print("No match found.")
