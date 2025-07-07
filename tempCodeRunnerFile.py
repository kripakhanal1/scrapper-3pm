with open("books.csv", "w", encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=books.keys())
        writer.writeheader()
        writer.writerows(all_books)
        print("Data written to books.csv")
all_books = scrape_books(url,)   