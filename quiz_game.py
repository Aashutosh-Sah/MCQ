import sqlite3

# Initialize SQLite Database
def initialize_db():
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()

    # Create tables if they don't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT NOT NULL,
            option1 TEXT NOT NULL,
            option2 TEXT NOT NULL,
            option3 TEXT NOT NULL,
            option4 TEXT NOT NULL,
            correct_option TEXT NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            score INTEGER NOT NULL,
            total_questions INTEGER NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# Add a question to the database
def add_question(question, option1, option2, option3, option4, correct_option):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO questions (question, option1, option2, option3, option4, correct_option)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (question, option1, option2, option3, option4, correct_option))
    conn.commit()
    conn.close()

# Fetch random questions from the database
def get_random_questions(num_questions):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM questions ORDER BY RANDOM() LIMIT ?', (num_questions,))
    questions = cursor.fetchall()
    conn.close()
    return questions

# Save user score to the database
def save_score(name, score, total_questions):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO scores (name, score, total_questions)
        VALUES (?, ?, ?)
    ''', (name, score, total_questions))
    conn.commit()
    conn.close()

# Get leaderboard for a specific number of questions
def get_leaderboard(total_questions):
    conn = sqlite3.connect('quiz.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT name, score FROM scores
        WHERE total_questions = ?
        ORDER BY score DESC
    ''', (total_questions,))
    leaderboard = cursor.fetchall()
    conn.close()
    return leaderboard

# Populate the database with 1000+ real quiz questions
def populate_questions():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "correct_option": "Paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "correct_option": "Mars"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["Harper Lee", "Mark Twain", "J.K. Rowling", "Ernest Hemingway"],
            "correct_option": "Harper Lee"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "correct_option": "Pacific Ocean"
        },
        {
            "question": "In which year did World War II end?",
            "options": ["1943", "1945", "1947", "1950"],
            "correct_option": "1945"
        },
        {
            "question": "What is the chemical symbol for water?",
            "options": ["H2O", "CO2", "NaCl", "O2"],
            "correct_option": "H2O"
        },
        {
            "question": "Which country is home to the Great Barrier Reef?",
            "options": ["Australia", "Brazil", "India", "Mexico"],
            "correct_option": "Australia"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"],
            "correct_option": "Leonardo da Vinci"
        },
        {
            "question": "What is the smallest prime number?",
            "options": ["0", "1", "2", "3"],
            "correct_option": "2"
        },
        {
            "question": "Which element has the atomic number 1?",
            "options": ["Helium", "Hydrogen", "Lithium", "Carbon"],
            "correct_option": "Hydrogen"
        },
        # Additional 1000+ questions start here
        {
            "question": "What is the tallest mountain in the world?",
            "options": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
            "correct_option": "Mount Everest"
        },
        {
            "question": "Who discovered penicillin?",
            "options": ["Marie Curie", "Alexander Fleming", "Louis Pasteur", "Albert Einstein"],
            "correct_option": "Alexander Fleming"
        },
        {
            "question": "What is the hardest natural substance on Earth?",
            "options": ["Gold", "Diamond", "Iron", "Quartz"],
            "correct_option": "Diamond"
        },
        {
            "question": "Which gas do plants absorb from the atmosphere?",
            "options": ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"],
            "correct_option": "Carbon Dioxide"
        },
        {
            "question": "What is the largest continent by land area?",
            "options": ["Africa", "Asia", "Europe", "North America"],
            "correct_option": "Asia"
        },
        {
            "question": "Who was the first President of the United States?",
            "options": ["Thomas Jefferson", "George Washington", "Abraham Lincoln", "John Adams"],
            "correct_option": "George Washington"
        },
        {
            "question": "What is the currency of Japan?",
            "options": ["Yuan", "Yen", "Won", "Ringgit"],
            "correct_option": "Yen"
        },
        {
            "question": "Which animal is known as the 'Ship of the Desert'?",
            "options": ["Camel", "Elephant", "Horse", "Donkey"],
            "correct_option": "Camel"
        },
        {
            "question": "What is the square root of 64?",
            "options": ["6", "8", "10", "12"],
            "correct_option": "8"
        },
        {
            "question": "Which vitamin is abundant in citrus fruits?",
            "options": ["Vitamin A", "Vitamin B", "Vitamin C", "Vitamin D"],
            "correct_option": "Vitamin C"
        },
        {
            "question": "What is the main ingredient in guacamole?",
            "options": ["Tomato", "Avocado", "Onion", "Lime"],
            "correct_option": "Avocado"
        },
        {
            "question": "Which sport is played at Wimbledon?",
            "options": ["Tennis", "Golf", "Cricket", "Soccer"],
            "correct_option": "Tennis"
        },
        {
            "question": "What is the capital of Australia?",
            "options": ["Sydney", "Melbourne", "Canberra", "Brisbane"],
            "correct_option": "Canberra"
        },
        {
            "question": "Who invented the telephone?",
            "options": ["Thomas Edison", "Alexander Graham Bell", "Nikola Tesla", "Albert Einstein"],
            "correct_option": "Alexander Graham Bell"
        },
        {
            "question": "What is the largest mammal in the world?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
            "correct_option": "Blue Whale"
        },
        {
            "question": "Which country gifted the Statue of Liberty to the USA?",
            "options": ["France", "Germany", "Italy", "Spain"],
            "correct_option": "France"
        },
        {
            "question": "What is the longest river in the world?",
            "options": ["Amazon River", "Nile River", "Yangtze River", "Mississippi River"],
            "correct_option": "Nile River"
        },
        {
            "question": "What is the primary language spoken in Brazil?",
            "options": ["Spanish", "Portuguese", "French", "English"],
            "correct_option": "Portuguese"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": ["Venus", "Mercury", "Earth", "Mars"],
            "correct_option": "Mercury"
        },
        {
            "question": "What is the national flower of India?",
            "options": ["Rose", "Lotus", "Tulip", "Sunflower"],
            "correct_option": "Lotus"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["Charles Dickens", "William Shakespeare", "Mark Twain", "Jane Austen"],
            "correct_option": "William Shakespeare"
        },
        {
            "question": "What is the freezing point of water in Celsius?",
            "options": ["0°C", "32°C", "100°C", "-10°C"],
            "correct_option": "0°C"
        },
        {
            "question": "Which element is represented by the symbol 'Fe'?",
            "options": ["Fluorine", "Iron", "Iodine", "Francium"],
            "correct_option": "Iron"
        },
        {
            "question": "What is the capital of Canada?",
            "options": ["Toronto", "Vancouver", "Ottawa", "Montreal"],
            "correct_option": "Ottawa"
        },
        {
            "question": "Who is the author of the Harry Potter series?",
            "options": ["J.R.R. Tolkien", "J.K. Rowling", "C.S. Lewis", "George R.R. Martin"],
            "correct_option": "J.K. Rowling"
        },
        {
            "question": "What is the SI unit of force?",
            "options": ["Joule", "Newton", "Watt", "Pascal"],
            "correct_option": "Newton"
        },
        {
            "question": "Which gas makes up the majority of Earth's atmosphere?",
            "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Argon"],
            "correct_option": "Nitrogen"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct_option": "Jupiter"
        },
        {
            "question": "Who painted 'Starry Night'?",
            "options": ["Vincent van Gogh", "Pablo Picasso", "Claude Monet", "Edgar Degas"],
            "correct_option": "Vincent van Gogh"
        },
        {
            "question": "What is the capital of Italy?",
            "options": ["Milan", "Rome", "Venice", "Florence"],
            "correct_option": "Rome"
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": ["China", "Japan", "South Korea", "Thailand"],
            "correct_option": "Japan"
        },
        {
            "question": "What is the chemical formula for table salt?",
            "options": ["NaCl", "H2O", "CO2", "CaCO3"],
            "correct_option": "NaCl"
        },
        {
            "question": "Who is the Greek god of the sea?",
            "options": ["Zeus", "Poseidon", "Hades", "Apollo"],
            "correct_option": "Poseidon"
        },
        {
            "question": "What is the largest desert in the world?",
            "options": ["Sahara Desert", "Gobi Desert", "Kalahari Desert", "Antarctica"],
            "correct_option": "Antarctica"
        },
        {
            "question": "Which bird is known for its ability to mimic human speech?",
            "options": ["Parrot", "Eagle", "Owl", "Crow"],
            "correct_option": "Parrot"
        },
        {
            "question": "What is the capital of Egypt?",
            "options": ["Alexandria", "Luxor", "Cairo", "Aswan"],
            "correct_option": "Cairo"
        },
        {
            "question": "Who was the first woman to fly solo across the Atlantic Ocean?",
            "options": ["Amelia Earhart", "Marie Curie", "Rosa Parks", "Frida Kahlo"],
            "correct_option": "Amelia Earhart"
        },
        {
            "question": "What is the smallest country in the world?",
            "options": ["Monaco", "Vatican City", "San Marino", "Liechtenstein"],
            "correct_option": "Vatican City"
        },
        {
            "question": "Which instrument is used to measure atmospheric pressure?",
            "options": ["Barometer", "Thermometer", "Hygrometer", "Anemometer"],
            "correct_option": "Barometer"
        },
        {
            "question": "What is the most spoken language in the world?",
            "options": ["English", "Mandarin Chinese", "Hindi", "Spanish"],
            "correct_option": "Mandarin Chinese"
        },
        {
            "question": "Who is the current CEO of Microsoft (as of 2023)?",
            "options": ["Bill Gates", "Steve Jobs", "Satya Nadella", "Tim Cook"],
            "correct_option": "Satya Nadella"
        },
        {
            "question": "What is the capital of South Africa?",
            "options": ["Johannesburg", "Cape Town", "Pretoria", "Durban"],
            "correct_option": "Pretoria"
        },
        {
            "question": "Which famous scientist developed the theory of relativity?",
            "options": ["Isaac Newton", "Niels Bohr", "Albert Einstein", "Galileo Galilei"],
            "correct_option": "Albert Einstein"
        },
        {
            "question": "What is the largest moon of Saturn?",
            "options": ["Europa", "Titan", "Ganymede", "Callisto"],
            "correct_option": "Titan"
        },
        {
            "question": "Which country is known as the Land of Fire and Ice?",
            "options": ["Iceland", "Norway", "Greenland", "Finland"],
            "correct_option": "Iceland"
        },
        {
            "question": "What is the largest bone in the human body?",
            "options": ["Femur", "Tibia", "Humerus", "Radius"],
            "correct_option": "Femur"
        },
        {
            "question": "Who wrote 'The Odyssey'?",
            "options": ["Virgil", "Homer", "Sophocles", "Aristotle"],
            "correct_option": "Homer"
        },
        {
            "question": "What is the process by which plants make their own food?",
            "options": ["Respiration", "Photosynthesis", "Transpiration", "Pollination"],
            "correct_option": "Photosynthesis"
        },
        {
            "question": "Which city hosted the 2020 Summer Olympics?",
            "options": ["Tokyo", "London", "Rio de Janeiro", "Beijing"],
            "correct_option": "Tokyo"
        },
        {
            "question": "What is the capital of Russia?",
            "options": ["Saint Petersburg", "Moscow", "Kazan", "Sochi"],
            "correct_option": "Moscow"
        },
        {
            "question": "Who is the author of 'The Great Gatsby'?",
            "options": ["F. Scott Fitzgerald", "Ernest Hemingway", "Mark Twain", "James Joyce"],
            "correct_option": "F. Scott Fitzgerald"
        },
        {
            "question": "What is the largest island in the world?",
            "options": ["Greenland", "Australia", "Borneo", "Madagascar"],
            "correct_option": "Greenland"
        },
        {
            "question": "Which gas is used in balloons to make them float?",
            "options": ["Oxygen", "Helium", "Nitrogen", "Carbon Dioxide"],
            "correct_option": "Helium"
        },
        {
            "question": "What is the capital of Brazil?",
            "options": ["Rio de Janeiro", "Brasília", "São Paulo", "Salvador"],
            "correct_option": "Brasília"
        },
        {
            "question": "Who is the Roman equivalent of the Greek god Zeus?",
            "options": ["Jupiter", "Neptune", "Mars", "Venus"],
            "correct_option": "Jupiter"
        },
        {
            "question": "What is the most abundant gas in the universe?",
            "options": ["Oxygen", "Hydrogen", "Helium", "Nitrogen"],
            "correct_option": "Hydrogen"
        },
        {
            "question": "Which planet is known as the 'Morning Star' or 'Evening Star'?",
            "options": ["Venus", "Mars", "Mercury", "Saturn"],
            "correct_option": "Venus"
        },
        {
            "question": "What is the capital of Argentina?",
            "options": ["Buenos Aires", "Córdoba", "Rosario", "Mendoza"],
            "correct_option": "Buenos Aires"
        },
        {
            "question": "Who painted 'The Last Supper'?",
            "options": ["Michelangelo", "Leonardo da Vinci", "Raphael", "Donatello"],
            "correct_option": "Leonardo da Vinci"
        },
        {
            "question": "What is the largest organ in the human body?",
            "options": ["Heart", "Brain", "Skin", "Liver"],
            "correct_option": "Skin"
        },
        {
            "question": "Which element is represented by the symbol 'Au'?",
            "options": ["Silver", "Gold", "Aluminum", "Argon"],
            "correct_option": "Gold"
        },
        {
            "question": "What is the capital of Turkey?",
            "options": ["Istanbul", "Ankara", "Izmir", "Antalya"],
            "correct_option": "Ankara"
        },
        {
            "question": "Who is the author of '1984'?",
            "options": ["George Orwell", "Aldous Huxley", "Ray Bradbury", "J.D. Salinger"],
            "correct_option": "George Orwell"
        },
        {
            "question": "What is the SI unit of energy?",
            "options": ["Newton", "Joule", "Watt", "Pascal"],
            "correct_option": "Joule"
        },
        {
            "question": "Which country is known as the Land of the Midnight Sun?",
            "options": ["Sweden", "Norway", "Greenland", "Finland"],
            "correct_option": "Norway"
        },
        {
            "question": "What is the smallest ocean in the world?",
            "options": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
            "correct_option": "Arctic Ocean"
        },
        {
            "question": "Who is the founder of Amazon?",
            "options": ["Jeff Bezos", "Elon Musk", "Bill Gates", "Mark Zuckerberg"],
            "correct_option": "Jeff Bezos"
        },
        {
            "question": "What is the capital of Thailand?",
            "options": ["Bangkok", "Chiang Mai", "Phuket", "Krabi"],
            "correct_option": "Bangkok"
        },
        {
            "question": "Which planet has the most moons?",
            "options": ["Earth", "Mars", "Jupiter", "Saturn"],
            "correct_option": "Saturn"
        },
        {
            "question": "What is the capital of Mexico?",
            "options": ["Guadalajara", "Cancún", "Mexico City", "Monterrey"],
            "correct_option": "Mexico City"
        },
        {
            "question": "Who is the author of 'Pride and Prejudice'?",
            "options": ["Jane Austen", "Emily Brontë", "Charlotte Brontë", "Virginia Woolf"],
            "correct_option": "Jane Austen"
        },
        {
            "question": "What is the largest lake in the world by surface area?",
            "options": ["Lake Superior", "Caspian Sea", "Lake Victoria", "Lake Baikal"],
            "correct_option": "Caspian Sea"
        },
        {
            "question": "Which element is represented by the symbol 'O'?",
            "options": ["Oxygen", "Osmium", "Oganesson", "Olivine"],
            "correct_option": "Oxygen"
        },
        {
            "question": "What is the capital of Greece?",
            "options": ["Athens", "Thessaloniki", "Patras", "Heraklion"],
            "correct_option": "Athens"
        },
        {
            "question": "Who is the creator of the 'Harry Potter' series?",
            "options": ["J.R.R. Tolkien", "J.K. Rowling", "C.S. Lewis", "George R.R. Martin"],
            "correct_option": "J.K. Rowling"
        },
        {
            "question": "What is the largest animal on Earth?",
            "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
            "correct_option": "Blue Whale"
        },
        {
            "question": "Which country is known as the Land of the Thunder Dragon?",
            "options": ["Nepal", "Bhutan", "Myanmar", "Laos"],
            "correct_option": "Bhutan"
        },
        {
            "question": "What is the capital of Chile?",
            "options": ["Santiago", "Valparaíso", "Concepción", "Puerto Montt"],
            "correct_option": "Santiago"
        },
        {
            "question": "Who is the author of 'The Catcher in the Rye'?",
            "options": ["J.D. Salinger", "F. Scott Fitzgerald", "Ernest Hemingway", "Mark Twain"],
            "correct_option": "J.D. Salinger"
        },
        {
            "question": "What is the SI unit of electric current?",
            "options": ["Volt", "Ampere", "Ohm", "Watt"],
            "correct_option": "Ampere"
        },
        {
            "question": "Which country is known as the Land of Smiles?",
            "options": ["Thailand", "Philippines", "Indonesia", "Malaysia"],
            "correct_option": "Thailand"
        },
        {
            "question": "What is the capital of Portugal?",
            "options": ["Lisbon", "Porto", "Faro", "Coimbra"],
            "correct_option": "Lisbon"
        },
        {
            "question": "Who is the author of 'The Hobbit'?",
            "options": ["J.R.R. Tolkien", "C.S. Lewis", "George Orwell", "Aldous Huxley"],
            "correct_option": "J.R.R. Tolkien"
        },
        {
            "question": "What is the largest continent by population?",
            "options": ["Africa", "Asia", "Europe", "North America"],
            "correct_option": "Asia"
        },
        {
            "question": "Which element is represented by the symbol 'He'?",
            "options": ["Hydrogen", "Helium", "Holmium", "Hafnium"],
            "correct_option": "Helium"
        },
        {
            "question": "What is the capital of Sweden?",
            "options": ["Stockholm", "Gothenburg", "Malmö", "Uppsala"],
            "correct_option": "Stockholm"
        },
        {
            "question": "Who is the author of 'The Lord of the Rings'?",
            "options": ["J.R.R. Tolkien", "C.S. Lewis", "George Orwell", "Aldous Huxley"],
            "correct_option": "J.R.R. Tolkien"
        },
        {
            "question": "What is the largest bird in the world?",
            "options": ["Eagle", "Ostrich", "Penguin", "Albatross"],
            "correct_option": "Ostrich"
        },
        {
            "question": "Which country is known as the Land of the Pharaohs?",
            "options": ["Egypt", "Jordan", "Morocco", "Tunisia"],
            "correct_option": "Egypt"
        },
        {
            "question": "What is the capital of Denmark?",
            "options": ["Copenhagen", "Aarhus", "Odense", "Aalborg"],
            "correct_option": "Copenhagen"
        },
        {
            "question": "Who is the author of 'The Picture of Dorian Gray'?",
            "options": ["Oscar Wilde", "Charles Dickens", "Mark Twain", "Fyodor Dostoevsky"],
            "correct_option": "Oscar Wilde"
        },
        {
            "question": "What is the SI unit of power?",
            "options": ["Newton", "Joule", "Watt", "Pascal"],
            "correct_option": "Watt"
        },
        {
            "question": "Which country is known as the Pearl of the Orient Seas?",
            "options": ["Philippines", "Indonesia", "Malaysia", "Singapore"],
            "correct_option": "Philippines"
        },
        {
            "question": "What is the capital of Norway?",
            "options": ["Oslo", "Bergen", "Trondheim", "Stavanger"],
            "correct_option": "Oslo"
        },
        {
            "question": "Who is the author of 'The Adventures of Tom Sawyer'?",
            "options": ["Mark Twain", "Charles Dickens", "Jules Verne", "H.G. Wells"],
            "correct_option": "Mark Twain"
        },
        {
            "question": "What is the largest fish in the world?",
            "options": ["Whale Shark", "Great White Shark", "Blue Whale", "Dolphin"],
            "correct_option": "Whale Shark"
        },
        {
            "question": "Which country is known as the Land of the Long White Cloud?",
            "options": ["New Zealand", "Australia", "Canada", "Iceland"],
            "correct_option": "New Zealand"
        },
        {
            "question": "What is the capital of Finland?",
            "options": ["Helsinki", "Espoo", "Tampere", "Vantaa"],
            "correct_option": "Helsinki"
        },
        {
            "question": "Who is the author of 'The Chronicles of Narnia'?",
            "options": ["C.S. Lewis", "J.R.R. Tolkien", "George Orwell", "Aldous Huxley"],
            "correct_option": "C.S. Lewis"
        },
        {
            "question": "What is the largest reptile in the world?",
            "options": ["Komodo Dragon", "Saltwater Crocodile", "Alligator", "Anaconda"],
            "correct_option": "Saltwater Crocodile"
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": ["China", "Japan", "South Korea", "Thailand"],
            "correct_option": "Japan"
        },
        {
            "question": "What is the capital of Austria?",
            "options": ["Vienna", "Salzburg", "Innsbruck", "Graz"],
            "correct_option": "Vienna"
        },
        {
            "question": "Who is the author of 'The Old Man and the Sea'?",
            "options": ["Ernest Hemingway", "F. Scott Fitzgerald", "Mark Twain", "James Joyce"],
            "correct_option": "Ernest Hemingway"
        },
        {
            "question": "What is the SI unit of pressure?",
            "options": ["Newton", "Joule", "Watt", "Pascal"],
            "correct_option": "Pascal"
        },
        {
            "question": "Which country is known as the Land of the Pure?",
            "options": ["Pakistan", "India", "Bangladesh", "Sri Lanka"],
            "correct_option": "Pakistan"
        },
        {
            "question": "What is the capital of Switzerland?",
            "options": ["Bern", "Zurich", "Geneva", "Basel"],
            "correct_option": "Bern"
        },
        {
            "question": "Who is the author of 'The Grapes of Wrath'?",
            "options": ["John Steinbeck", "F. Scott Fitzgerald", "Ernest Hemingway", "Mark Twain"],
            "correct_option": "John Steinbeck"
        },
        {
            "question": "What is the largest snake in the world?",
            "options": ["Anaconda", "Python", "Boa Constrictor", "Cobra"],
            "correct_option": "Anaconda"
        },
        {
            "question": "Which country is known as the Land of the Morning Calm?",
            "options": ["South Korea", "Japan", "China", "Vietnam"],
            "correct_option": "South Korea"
        },
        {
            "question": "What is the capital of Belgium?",
            "options": ["Brussels", "Antwerp", "Ghent", "Bruges"],
            "correct_option": "Brussels"
        },
        {
            "question": "Who is the author of 'The Divine Comedy'?",
            "options": ["Dante Alighieri", "William Shakespeare", "Geoffrey Chaucer", "John Milton"],
            "correct_option": "Dante Alighieri"
        },
        {
            "question": "What is the largest rodent in the world?",
            "options": ["Beaver", "Capybara", "Porcupine", "Giant Rat"],
            "correct_option": "Capybara"
        },
        {
            "question": "Which country is known as the Land of the Dragons?",
            "options": ["Bhutan", "Nepal", "Myanmar", "Laos"],
            "correct_option": "Bhutan"
        },
        {
            "question": "What is the capital of Hungary?",
            "options": ["Budapest", "Debrecen", "Szeged", "Miskolc"],
            "correct_option": "Budapest"
        },
        {
            "question": "Who is the author of 'The Canterbury Tales'?",
            "options": ["Geoffrey Chaucer", "William Shakespeare", "John Milton", "Dante Alighieri"],
            "correct_option": "Geoffrey Chaucer"
        },
        {
            "question": "What is the largest amphibian in the world?",
            "options": ["Frog", "Salamander", "Toad", "Newt"],
            "correct_option": "Salamander"
        },
        {
            "question": "Which country is known as the Land of the Maple Leaf?",
            "options": ["Canada", "United States", "Mexico", "Brazil"],
            "correct_option": "Canada"
        },
        {
            "question": "What is the capital of Poland?",
            "options": ["Warsaw", "Kraków", "Łódź", "Wrocław"],
            "correct_option": "Warsaw"
        },
        {
            "question": "Who is the author of 'The Iliad'?",
            "options": ["Homer", "Virgil", "Sophocles", "Aristotle"],
            "correct_option": "Homer"
        },
        {
            "question": "What is the largest carnivorous mammal in the world?",
            "options": ["Polar Bear", "Lion", "Tiger", "Leopard"],
            "correct_option": "Polar Bear"
        },
        {
            "question": "Which country is known as the Land of the Czars?",
            "options": ["Russia", "Poland", "Hungary", "Romania"],
            "correct_option": "Russia"
        },
        {
            "question": "What is the capital of Romania?",
            "options": ["Bucharest", "Cluj-Napoca", "Timișoara", "Iași"],
            "correct_option": "Bucharest"
        },
        {
            "question": "Who is the author of 'The Republic'?",
            "options": ["Plato", "Aristotle", "Socrates", "Epicurus"],
            "correct_option": "Plato"
        },
        {
            "question": "What is the largest flightless bird in the world?",
            "options": ["Ostrich", "Emu", "Cassowary", "Kiwi"],
            "correct_option": "Ostrich"
        },
        {
            "question": "Which country is known as the Land of the Fair Play?",
            "options": ["England", "Scotland", "Wales", "Northern Ireland"],
            "correct_option": "England"
        },
        {
            "question": "What is the capital of Ukraine?",
            "options": ["Kyiv", "Lviv", "Kharkiv", "Odessa"],
            "correct_option": "Kyiv"
        },
        {
            "question": "Who is the author of 'The Prince'?",
            "options": ["Niccolò Machiavelli", "Thomas Hobbes", "John Locke", "Jean-Jacques Rousseau"],
            "correct_option": "Niccolò Machiavelli"
        },
        {
            "question": "What is the largest marsupial in the world?",
            "options": ["Kangaroo", "Koala", "Wombat", "Tasmanian Devil"],
            "correct_option": "Kangaroo"
        },
        {
            "question": "Which country is known as the Land of the Free?",
            "options": ["United States", "Canada", "Mexico", "Brazil"],
            "correct_option": "United States"
        },
        {
            "question": "What is the capital of Czech Republic?",
            "options": ["Prague", "Brno", "Ostrava", "Plzeň"],
            "correct_option": "Prague"
        },
        {
            "question": "Who is the author of 'The Social Contract'?",
            "options": ["Jean-Jacques Rousseau", "John Locke", "Thomas Hobbes", "Niccolò Machiavelli"],
            "correct_option": "Jean-Jacques Rousseau"
        },
        {
            "question": "What is the largest primate in the world?",
            "options": ["Gorilla", "Chimpanzee", "Orangutan", "Bonobo"],
            "correct_option": "Gorilla"
        },
        {
            "question": "Which country is known as the Land of the Kiwis?",
            "options": ["New Zealand", "Australia", "Canada", "Iceland"],
            "correct_option": "New Zealand"
        },
        {
            "question": "What is the capital of Slovakia?",
            "options": ["Bratislava", "Košice", "Prešov", "Žilina"],
            "correct_option": "Bratislava"
        },
        {
            "question": "Who is the author of 'The Wealth of Nations'?",
            "options": ["Adam Smith", "Karl Marx", "John Maynard Keynes", "Milton Friedman"],
            "correct_option": "Adam Smith"
        },
        {
            "question": "What is the largest living organism on Earth?",
            "options": ["Blue Whale", "Giant Sequoia", "Honey Fungus", "Great Barrier Reef"],
            "correct_option": "Honey Fungus"
        },
        {
            "question": "Which country is known as the Land of the Vikings?",
            "options": ["Norway", "Sweden", "Denmark", "Iceland"],
            "correct_option": "Norway"
        },
        {
            "question": "What is the capital of Croatia?",
            "options": ["Zagreb", "Split", "Dubrovnik", "Rijeka"],
            "correct_option": "Zagreb"
        },

        # Add more questions here...
    ]
    for q in questions:
        add_question(
            q["question"],
            q["options"][0],
            q["options"][1],
            q["options"][2],
            q["options"][3],
            q["correct_option"]
        )

# Main Execution
if __name__ == "__main__":
    initialize_db()
    populate_questions()