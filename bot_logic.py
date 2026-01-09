import pandas as pd

df = pd.read_csv("library_books_1000.csv")

library_rules = {
    "timing": "The library is open from 9:00 AM to 3:00 PM on working days.",
    "fine": "The fine is ₹2 per day after the due date.",
    "issue": "Students can issue 2 books for 14 days."
}

helpdesk = {
    "admission": "Please contact the school office for admission details.",
    "exam": "Exam schedules are shared via the school notice board.",
    "fees": "Fee details are available on the school website."
}

def librarian_bot(query):
    q = query.lower()

    for key in helpdesk:
        if key in q:
            return helpdesk[key]

    if "timing" in q:
        return library_rules["timing"]
    if "fine" in q:
        return library_rules["fine"]
    if "issue" in q or "borrow" in q:
        return library_rules["issue"]

    results = df[
        df['title'].str.lower().str.contains(q, na=False) |
        df['author'].str.lower().str.contains(q, na=False) |
        df['subject'].str.lower().str.contains(q, na=False)
    ]

    if results.empty:
        return "No matching books found."

    reply = ""
    for _, row in results.head(5).iterrows():
        reply += f"📘 {row['title']} | {row['subject']} | Class {row['class']} | Available: {row['available']}\n"
    return reply
