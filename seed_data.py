from main import db  # Replace 'your_app_name' with the actual name of your Flask app module
from main.models import Category, Author, Genre, Book  # Replace 'your_app_name' with your app's name
from datetime import datetime

# Define the categories
categories = [
    Category(name="Latest Release"),
    Category(name="Limited Editions"),
    Category(name="Top Picks for Today")
]

# Define some authors
authors = [
    Author(name="George Orwell", bio="English novelist, essayist, and critic."),
    Author(name="Harper Lee", bio="American novelist known for her Pulitzer Prize-winning novel 'To Kill a Mockingbird'."),
    Author(name="J.K. Rowling", bio="British author, best known for writing the Harry Potter fantasy series."),
    Author(name="Margaret Atwood", bio="Canadian poet, novelist, literary critic, and essayist, known for 'The Handmaid's Tale' and its sequel 'The Testaments'."),
    Author(name="Colson Whitehead", bio="American novelist, known for works like 'The Underground Railroad' and 'The Nickel Boys'."),
    Author(name="Tara Westover", bio="American memoirist, essayist, and historian, known for her memoir 'Educated'."),
    Author(name="Kazuo Ishiguro", bio="British novelist, known for his works exploring memory, time, and self-delusion, including 'The Remains of the Day' and 'Klara and the Sun'."),
    Author(name="Sally Rooney", bio="Irish author known for her novels 'Normal People' and 'Conversations with Friends'."),
    Author(name="Madeline Miller", bio="American author known for her novels 'The Song of Achilles' and 'Circe', both based on Greek mythology."),
    Author(name="Brit Bennett", bio="American author known for her novel 'The Vanishing Half'."),
    Author(name="Donna Tartt", bio="American author, known for 'The Secret History' and 'The Goldfinch'."),
    Author(name="George Saunders", bio="American writer of short stories, essays, and novels, known for 'Lincoln in the Bardo'."),
    Author(name="Hanya Yanagihara", bio="American novelist, editor, and travel writer, known for her novel 'A Little Life'."),
    Author(name="Erin Morgenstern", bio="American author, known for 'The Night Circus'."),
    Author(name="Jeff VanderMeer", bio="American author known for his Southern Reach Trilogy, including 'Annihilation'."),
    Author(name="Chimamanda Ngozi Adichie", bio="Nigerian writer known for 'Half of a Yellow Sun' and 'Americanah'."),
    Author(name="Cormac McCarthy", bio="American novelist, playwright, and screenwriter, known for 'The Road'."),
    Author(name="Paula Hawkins", bio="British author, known for her psychological thriller 'The Girl on the Train'."),
    Author(name="Gillian Flynn", bio="American author, known for her psychological thrillers including 'Gone Girl'."),
    Author(name="John Green", bio="American author, known for his young adult novels including 'The Fault in Our Stars'."),
    Author(name="Delia Owens", bio="American author, known for her novel 'Where the Crawdads Sing'."),
    Author(name="Liane Moriarty", bio="Australian author, known for her novels 'Big Little Lies' and 'Nine Perfect Strangers'."),
    Author(name="Celeste Ng", bio="American novelist and short story writer, known for 'Little Fires Everywhere'.")
]


# Define some genres
genres = [
    Genre(name="Dystopian", description="Books set in an imagined future, often under totalitarian regimes."),
    Genre(name="Historical Fiction", description="Fictional stories set against historical backdrops."),
    Genre(name="Fantasy", description="Books featuring magical elements and fantastical worlds."),
    Genre(name="Science Fiction", description="Books based on speculative scientific concepts."),
    Genre(name="Memoir", description="Personal recounting of the author's experiences."),
    Genre(name="Literary Fiction", description="Fictional works focused on style, character, and theme."),
    Genre(name="Thriller", description="Books that create excitement and suspense, often featuring crime."),
    Genre(name="Young Adult", description="Books primarily targeted at young adults."),
    Genre(name="Psychological Fiction", description="Fiction that explores the complexities of the human mind and behavior."),
    Genre(name="Mythology", description="Stories rooted in mythological traditions."),
    Genre(name="Post-Apocalyptic", description="Books set in a world after a catastrophic event."),
    Genre(name="Magical Realism", description="Books where magical elements blend seamlessly with the real world."),
    Genre(name="Contemporary Fiction", description="Fictional works set in the modern-day world.")
]


# Define some books
books = [
    # Latest Releases
    Book(
        title="1984",
        author_id=1,  # George Orwell
        genre_id=1,   # Dystopian
        description="In a chilling vision of a dystopian future, George Orwell presents a totalitarian regime led by the omnipresent Big Brother, where surveillance, propaganda, and the repression of individuality dominate every aspect of life.",
        published_date=datetime(1949, 6, 8),
        category_id=1  # Latest Release
    ),
    Book(
        title="The Testaments",
        author_id=4,  # Margaret Atwood
        genre_id=1,   # Dystopian
        description="Margaret Atwood's gripping sequel to 'The Handmaid's Tale' continues the story of Gilead, revealing new perspectives and deeper insights into the dystopian world as characters navigate the oppressive regime's shifting dynamics.",
        published_date=datetime(2019, 9, 10),
        category_id=1  # Latest Release
    ),
    Book(
        title="The Nickel Boys",
        author_id=5,  # Colson Whitehead
        genre_id=6,   # Literary Fiction
        description="Colson Whitehead's powerful novel unearths the harrowing truth behind a reform school in Florida, shedding light on systemic abuse and the resilience of those who endured its horrors.",
        published_date=datetime(2019, 7, 16),
        category_id=1  # Latest Release
    ),
    Book(
        title="Educated",
        author_id=6,  # Tara Westover
        genre_id=5,   # Memoir
        description="Tara Westover's memoir chronicles her extraordinary journey from growing up in a strict, survivalist family in rural Idaho to earning a PhD from Cambridge University, revealing a powerful story of self-discovery and resilience.",
        published_date=datetime(2018, 2, 18),
        category_id=1  # Latest Release
    ),
    Book(
        title="Normal People",
        author_id=8,  # Sally Rooney
        genre_id=6,   # Literary Fiction
        description="Sally Rooney's novel delves into the intricate relationship between Connell and Marianne, two individuals from different backgrounds who navigate the complexities of love, friendship, and social dynamics throughout their lives.",
        published_date=datetime(2018, 8, 28),
        category_id=1  # Latest Release
    ),
    Book(
        title="Klara and the Sun",
        author_id=7,  # Kazuo Ishiguro
        genre_id=4,   # Science Fiction
        description="Kazuo Ishiguro's thought-provoking narrative follows Klara, an artificial friend, as she observes human behavior and explores the boundaries between humanity and artificial intelligence in a future marked by technological advancements.",
        published_date=datetime(2021, 3, 2),
        category_id=1  # Latest Release
    ),
    Book(
        title="Circe",
        author_id=9,  # Madeline Miller
        genre_id=10,  # Mythology
        description="Madeline Miller's enchanting retelling of the myth of Circe, a powerful enchantress from Greek mythology, offers a fresh perspective on her life and trials, weaving a tale of transformation, power, and resilience.",
        published_date=datetime(2018, 4, 10),
        category_id=1  # Latest Release
    ),
    Book(
        title="The Vanishing Half",
        author_id=10,  # Brit Bennett
        genre_id=6,   # Literary Fiction
        description="Brit Bennett's compelling novel follows the divergent paths of twin sisters who separate in their youth, exploring themes of identity, family, and the enduring impact of their choices on their lives and the lives of those around them.",
        published_date=datetime(2020, 6, 2),
        category_id=1  # Latest Release
    ),

    # Limited Editions
    Book(
        title="Harry Potter and the Philosopher's Stone",
        author_id=3,  # J.K. Rowling
        genre_id=3,   # Fantasy
        description="J.K. Rowling's enchanting tale introduces readers to the magical world of Hogwarts, where young wizard Harry Potter begins his journey, discovering friendship, bravery, and the battle against dark forces.",
        published_date=datetime(1997, 6, 26),
        category_id=2  # Limited Editions
    ),
    Book(
        title="The Underground Railroad",
        author_id=5,  # Colson Whitehead
        genre_id=2,   # Historical Fiction
        description="Colson Whitehead's novel reimagines the Underground Railroad as a literal network of railways, following the harrowing escape of Cora, a young enslaved woman, as she seeks freedom in the antebellum South.",
        published_date=datetime(2016, 8, 2),
        category_id=2  # Limited Editions
    ),
    Book(
        title="The Goldfinch",
        author_id=11,  # Donna Tartt
        genre_id=6,    # Literary Fiction
        description="Donna Tartt's intricate novel follows Theo Decker, a boy whose life is forever changed after surviving a museum explosion, as he grapples with loss, art, and the impact of a stolen masterpiece.",
        published_date=datetime(2013, 10, 22),
        category_id=2  # Limited Editions
    ),
    Book(
        title="Lincoln in the Bardo",
        author_id=12,  # George Saunders
        genre_id=11,   # Post-Apocalyptic
        description="George Saunders' imaginative novel explores the afterlife as it depicts President Lincoln's grief over the death of his young son, Willie, set in a graveyard where the dead are caught between life and death.",
        published_date=datetime(2017, 2, 14),
        category_id=2  # Limited Editions
    ),
    Book(
        title="A Little Life",
        author_id=13,  # Hanya Yanagihara
        genre_id=6,    # Literary Fiction
        description="Hanya Yanagihara's poignant novel traces the lives of four friends in New York City, delving into their troubled pasts and exploring the deep bonds of friendship and the scars of trauma.",
        published_date=datetime(2015, 3, 10),
        category_id=2  # Limited Editions
    ),
    Book(
        title="The Night Circus",
        author_id=14,  # Erin Morgenstern
        genre_id=12,   # Magical Realism
        description="Erin Morgenstern's mesmerizing tale centers on a magical competition between two young illusionists set in a fantastical circus that only opens at night, blending romance, mystery, and enchantment.",
        published_date=datetime(2011, 9, 13),
        category_id=2  # Limited Editions
    ),
    Book(
        title="Annihilation",
        author_id=15,  # Jeff VanderMeer
        genre_id=4,    # Science Fiction
        description="Jeff VanderMeer's eerie novel follows a team of scientists exploring the mysterious Area X, a region where bizarre and unsettling phenomena defy explanation and challenge their understanding of reality.",
        published_date=datetime(2014, 2, 4),
        category_id=2  # Limited Editions
    ),
    Book(
        title="Half of a Yellow Sun",
        author_id=16,  # Chimamanda Ngozi Adichie
        genre_id=2,    # Historical Fiction
        description="Chimamanda Ngozi Adichie's powerful novel examines the Nigerian Civil War through the eyes of various characters, exploring themes of love, loss, and the complexities of identity amidst conflict.",
        published_date=datetime(2006, 9, 12),
        category_id=2  # Limited Editions
    ),

    # Top Picks for Today
    Book(
        title="The Road",
        author_id=17,  # Cormac McCarthy
        genre_id=11,   # Post-Apocalyptic
        description="Cormac McCarthy's hauntingly beautiful novel follows a father and his young son as they traverse a desolate, post-apocalyptic landscape, facing both the physical and moral challenges of survival.",
        published_date=datetime(2006, 9, 26),
        category_id=3  # Top Picks for Today
    ),
    Book(
        title="The Girl on the Train",
        author_id=18,  # Paula Hawkins
        genre_id=7,    # Thriller
        description="Paula Hawkins' gripping thriller unfolds the story of a woman who becomes entangled in a missing person's case after witnessing a troubling event during her daily train commute, leading to shocking revelations.",
        published_date=datetime(2015, 1, 13),
        category_id=3  # Top Picks for Today
    ),
    Book(
        title="Gone Girl",
        author_id=19,  # Gillian Flynn
        genre_id=9,    # Psychological Fiction
        description="Gillian Flynn's suspenseful novel explores the disappearance of Amy Dunne on her fifth wedding anniversary, unraveling a web of deceit, manipulation, and dark secrets in a tale full of twists and turns.",
        published_date=datetime(2012, 6, 5),
        category_id=3  # Top Picks for Today
    ),
    Book(
        title="The Fault in Our Stars",
        author_id=20,  # John Green
        genre_id=8,    # Young Adult
        description="John Green's heartwarming novel follows the romance between two teenagers with cancer, capturing their journey through love, loss, and the search for meaning in the face of terminal illness.",
        published_date=datetime(2012, 1, 10),
        category_id=3  # Top Picks for Today
    ),
    Book(
        title="Where the Crawdads Sing",
        author_id=21,  # Delia Owens
        genre_id=6,    # Literary Fiction
        description="Delia Owens' evocative novel tells the story of Kya Clark, a young girl raised in isolation in the marshlands of North Carolina, who becomes entangled in a murder investigation and confronts the mysteries of her own past.",
        published_date=datetime(2018, 8, 14),
        category_id=3  # Top Picks for Today
    ),
    Book(
        title="Big Little Lies",
        author_id=22,  # Liane Moriarty
        genre_id=6,    # Literary Fiction
        description="Liane Moriarty's intriguing novel revolves around three women whose seemingly perfect lives in Sydney unravel as they become entangled in a murder investigation, exposing buried secrets and personal conflicts.",
        published_date=datetime(2014, 7, 29),
        category_id=3  # Top Picks for Today
    ),
    Book(
        title="Little Fires Everywhere",
        author_id=23,  # Celeste Ng
        genre_id=6,    # Literary Fiction
        description="Celeste Ng's compelling narrative explores the lives of two families in a suburban community, revealing the impact of secrets, tensions, and differing values that ignite conflicts and lead to unexpected consequences.",
        published_date=datetime(2017, 9, 12),
        category_id=3  # Top Picks for Today
    ),
    Book(
        title="To Kill a Mockingbird",
        author_id=2,   # Harper Lee
        genre_id=2,    # Historical Fiction
        description="Harper Lee's timeless classic delves into the issues of racial injustice and moral growth in the American South during the 1930s, as seen through the eyes of Scout Finch, a young girl grappling with the complexities of her world.",
        published_date=datetime(1960, 7, 11),
        category_id=3  # Top Picks for Today
    )
]


# Add the data to the database
def populate_db():
    # Add the categories
    for category in categories:
        db.session.add(category)

    # Add the authors
    for author in authors:
        db.session.add(author)

    # Add the genres
    for genre in genres:
        db.session.add(genre)

    # Add the books
    for book in books:
        db.session.add(book)

    # Commit the transaction
    db.session.commit()
    print("Database has been populated with seed data!")

if __name__ == "__main__":
    populate_db()
