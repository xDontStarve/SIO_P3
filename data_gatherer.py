import mysql.connector as db
import json

def connect_db():
    """Establishes a database connection."""
    return db.connect(user="root", password="root", host="127.0.0.1", database="project01_fixed")

def fetch_data(query):
    """Executes a given SQL query and returns the fetched results."""
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    cursor.close()
    conn.close()
    return results

def save_to_json(data, filename):
    """Saves fetched data to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

def query_titles_per_country():
    """Queries and saves the total number of titles per country to a JSON file."""
    query = """
    SELECT c.Country_name, COUNT(*) AS Title_Count
    FROM country_titles ct
    JOIN countries c ON ct.Country_ID = c.ID
    GROUP BY c.Country_name
    ORDER BY Title_Count DESC;
    """
    data = fetch_data(query)
    json_data = [{'country': country, 'count': count} for country, count in data]
    save_to_json(json_data, 'titles_per_country.json')

def query_movies_per_country():
    """Queries and saves the number of movies per country to a JSON file."""
    query = """
    SELECT c.Country_name, 
           SUM(CASE WHEN m.movie_TYPE = 'movie' THEN 1 ELSE 0 END) AS Movie_Count
    FROM country_titles ct
    JOIN countries c ON ct.Country_ID = c.ID
    JOIN movies m ON ct.Title_ID = m.ID
    GROUP BY c.Country_name
    ORDER BY Movie_Count DESC;
    """
    data = fetch_data(query)
    json_data = [{'country': country, 'count': count} for country, count in data]
    save_to_json(json_data, 'movies_per_country.json')

def query_shows_per_country():
    """Queries and saves the number of shows per country to a JSON file."""
    query = """
    SELECT c.Country_name, 
           SUM(CASE WHEN m.movie_TYPE = 'show' THEN 1 ELSE 0 END) AS Show_Count
    FROM country_titles ct
    JOIN countries c ON ct.Country_ID = c.ID
    JOIN movies m ON ct.Title_ID = m.ID
    GROUP BY c.Country_name
    ORDER BY Show_Count DESC;
    """
    data = fetch_data(query)
    json_data = [{'country': country, 'count': count} for country, count in data]
    save_to_json(json_data, 'shows_per_country.json')

# Execute the functions
query_titles_per_country()
query_movies_per_country()
query_shows_per_country()
