
import re
import sys

def main():
    html = input("HTML: ")
    print(parse(html))


def parse(html):

    pattern = r'src="(https?://(?:www\.)?youtube\.com/embed/[\w-]+)"'


    match = re.search(pattern, html)

    if match:

        url = match.group(1)
        video_id = url.split("/")[-1]
        short_url = f"https://youtu.be/{video_id}"
        return short_url

    return None


if __name__ == "__main__":
    main()
