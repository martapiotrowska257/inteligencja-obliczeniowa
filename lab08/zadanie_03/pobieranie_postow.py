import praw
import pandas as pd
from datetime import datetime
from openpyxl.utils import get_column_letter

# konfiguracja Reddit API

reddit = praw.Reddit(
    client_id="0Xyav0k_Dw_1cC_MEXw-CQ",
    client_secret="WYoQhs20LJxa0C0yXvg2UGo2l7VBTQ",
    user_agent="script:game-posts:v1.0 (by /ActionVast9655)"
)

def pobierz_posty(subreddit_name, search_term, limit=100):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []

    for post in subreddit.search(query=search_term, sort="new", limit=limit):
        posts.append([
            datetime.fromtimestamp(post.created_utc).strftime('%Y-%m-%d %H:%M:%S'),
            post.author.name if post.author else "[usunięty]",
            post.title,
            post.selftext[:1000] + "..." if len(post.selftext) > 1000 else post.selftext,  # ograniczenie długości
            post.score,
            post.num_comments,
            f"https://www.reddit.com{post.permalink}"
        ])
    return posts

# parametry
subreddit_name = "gaming"
search_term = "minecraft"
limit = 100

print(f"Szukam {limit} najnowszych postów o '{search_term}' w r/{subreddit_name}...")
posts = pobierz_posty(subreddit_name, search_term, limit)

if posts:
    df = pd.DataFrame(posts, columns=["Data", "Użytkownik", "Tytuł", "Treść", "Punkty", "Komentarze", "Link"])

    # zapis do CSV
    csv_filename = "reddit_minecraft.csv"
    df.to_csv(csv_filename, index=False, encoding='utf-8')

    # zapis do Excela
    excel_filename = "reddit_minecraft.xlsx"
    writer = pd.ExcelWriter(excel_filename, engine='openpyxl')
    df.to_excel(writer, index=False, sheet_name='Posty')

    # formatowanie kolumn
    sheet = writer.sheets['Posty']
    for i, col in enumerate(df.columns):
        col_letter = get_column_letter(i + 1)
        if col == "Treść":
            sheet.column_dimensions[col_letter].width = 70
        elif col == "Tytuł":
            sheet.column_dimensions[col_letter].width = 40
        elif col == "Link":
            sheet.column_dimensions[col_letter].width = 45
        else:
            sheet.column_dimensions[col_letter].width = 15

    writer._save()

    print(f"Zapisano {len(posts)} postów do plików:")
    print(f"- CSV: {csv_filename}")
    print(f"- Excel: {excel_filename}")
else:
    print("Nie znaleziono żadnych postów.")
