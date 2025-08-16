import json
import os

def create_html(config_path, output_path):
    """
    Generates an HTML file from a JSON config file.

    Args:
        config_path (str): The path to the JSON config file.
        output_path (str): The path to the output HTML file.
    """
    with open(config_path, 'r') as f:
        config = json.load(f)

    movies = []
    tv_shows = []

    for item in config.values():
        if item.get('match_type') == 'movie':
            movies.append(item)
        elif item.get('match_type') == 'episode':
            tv_shows.append(item)

    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Media Library</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #141414;
            color: #fff;
            margin: 0;
            padding: 0;
        }}
        .container {{
            padding: 20px;
        }}
        .header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 20px;
        }}
        .logo {{
            font-size: 24px;
            font-weight: bold;
            color: #e50914;
        }}
        .filter {{
            margin-bottom: 20px;
        }}
        .filter input {{
            padding: 10px;
            border-radius: 5px;
            border: none;
            width: 300px;
        }}
        .category {{
            margin-bottom: 30px;
        }}
        .category-title {{
            font-size: 20px;
            margin-bottom: 10px;
        }}
        .cards {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap: 20px;
        }}
        .card {{
            background-color: #222;
            border-radius: 5px;
            overflow: hidden;
            cursor: pointer;
            transition: transform 0.2s;
        }}
        .card:hover {{
            transform: scale(1.05);
        }}
        .card img {{
            width: 100%;
            height: auto;
        }}
        .card-body {{
            padding: 10px;
        }}
        .card-title {{
            font-size: 16px;
            font-weight: bold;
            margin-bottom: 5px;
        }}
        .card-text {{
            font-size: 14px;
            color: #aaa;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <div class="logo">MEDIA LIBRARY</div>
        </div>
        <div class="filter">
            <input type="text" id="filterInput" onkeyup="filterMedia()" placeholder="Filter by title...">
        </div>

        <div class="category" id="movies">
            <h2 class="category-title">Movies</h2>
            <div class="cards">
                {''.join([create_card(item) for item in movies])}
            </div>
        </div>

        <div class="category" id="tv-shows">
            <h2 class="category-title">TV Shows</h2>
            <div class="cards">
                {''.join([create_card(item) for item in tv_shows])}
            </div>
        </div>
    </div>

    <script>
        function filterMedia() {{
            const filter = document.getElementById('filterInput').value.toUpperCase();
            const cards = document.querySelectorAll('.card');
            cards.forEach(card => {{
                const title = card.querySelector('.card-title').textContent.toUpperCase();
                if (title.indexOf(filter) > -1) {{
                    card.style.display = "";
                }} else {{
                    card.style.display = "none";
                }}
            }});
        }}
    </script>
</body>
</html>
    """

    with open(output_path, 'w') as f:
        f.write(html_content)

def create_card(item):
    """
    Creates an HTML card for a media item.
    """
    if item.get('match_type') == 'movie':
        title = item.get('title')
        year = item.get('year')
        poster_path = item.get('poster_path')
        return f"""
        <div class="card" data-title="{title}">
            <img src="https://image.tmdb.org/t/p/w500{poster_path}" alt="{title}">
            <div class="card-body">
                <div class="card-title">{title}</div>
                <div class="card-text">{year}</div>
            </div>
        </div>
        """
    elif item.get('match_type') == 'episode':
        series_name = item.get('series_name')
        season = item.get('season')
        episode = item.get('episode')
        episode_name = item.get('episode_name')
        poster_path = item.get('poster_path')
        return f"""
        <div class="card" data-title="{series_name} {episode_name}">
            <img src="https://image.tmdb.org/t/p/w500{poster_path}" alt="{series_name}">
            <div class="card-body">
                <div class="card-title">{series_name}</div>
                <div class="card-text">S{season:02d}E{episode:02d}: {episode_name}</div>
            </div>
        </div>
        """
    return ''

if __name__ == '__main__':
    if not os.path.exists('output'):
        os.makedirs('output')
    create_html('config.json', 'output/index.html')
