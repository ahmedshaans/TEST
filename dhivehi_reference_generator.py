def generate_reference(author: str, year: int, month: str, day: int, title: str, url: str) -> str:
    """
    Generates a Dhivehi reference string.

    Args:
        author: The author's name.
        year: The publication year.
        month: The publication month (Dhivehi name).
        day: The publication day.
        title: The title of the work.
        url: The URL of the work.

    Returns:
        A string formatted as: Author. (Year، Month Day). Title. ނެގީ: URL ން.
    """
    return f"{author}. ({year}، {month} {day}). {title}. ނެގީ: {url} ން"

if __name__ == "__main__":
    author = "ޖުބޭޔާ އަހަމަދު"
    year = 2025
    month = "ޖޫން"
    day = 7
    title = "އިސްލާމް ފޯބިޑްސް އެކްސްޓްރާވެގެންސް، ވޭސްޓް"
    url = "https://www.daily-sun.com/printversion/details/634638"

    reference = generate_reference(author, year, month, day, title, url)
    print(reference)
