import sqlite3

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]

conn = sqlite3.connect('books.db')
c = conn.cursor()

c.execute("CREATE TABLE 'books'( 'id' INTEGER , 'title' TEXT, 'author' TEXT, 'first_sentence' TEXT,'published' INTEGER)")

for b in books:
    id = b['id']
    title = b['title']
    author = b['author']
    first_sentence = b['first_sentence']
    published = b['published']
    c.execute("INSERT INTO books VALUES (?,?,?,?,?)",
     [id ,title,author,first_sentence,published])
     conn.commit()

res = c.execute("SELECT * from books")
conn.close()
print(res.fetchall())