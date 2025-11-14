from bs4 import BeautifulSoup
SAMPLE_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Sample Web Page</title>
</head>
<body>

    <h1>Welcome to My Page</h1>
    <p class="substitue">This is a paragraph of text on my sample web page. It contains some important inf
    ormation.</p>

    <h2>Things to Remember</h2>
    <ul>
        <li>Item 1: This is the first point.</li>
        <li>Item 2: This is the second point, which can be emphasized.</li>
        <li>Item 3: And here is the third item in the list.</li>
    </ul>

</body>
"""
simple_soup = BeautifulSoup(SAMPLE_HTML, 'html.parser')
print(simple_soup.find('h1').string)

def find_list_item():
    list_items = simple_soup.find_all('li')
    for item in list_items:
        print(item.string)
def find_subtitle():
    paragraph = simple_soup.find('p', {'class': 'substitue'})  
    print(paragraph.string)  
        
find_list_item()  
find_subtitle()  