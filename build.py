from glob import glob
import os.path
from collections import defaultdict


def main():
    with open('./README_template.md', 'r', encoding='utf-8') as fp:
        template = fp.read().strip() + '\n\n'

    articles = defaultdict(lambda: defaultdict(list))

    for file_path in glob('./news/**/*.md', recursive=True):
        temp = os.path.split(file_path)
        date_str = os.path.split(temp[0])[1]
        assert date_str.isdigit() and len(date_str) == 8

        year = date_str[:4]
        day = f"{date_str[4:6]}-{date_str[6:]}"

        articles[year][day].append(file_path)

    for year in sorted(articles.keys(), reverse=True):
        template += f"# {year}\n\n"

        for day in sorted(articles[year].keys(), reverse=True):
            template += f"## {day}\n\n"

            for file_path in articles[year][day]:
                with open(file_path, 'r', encoding='utf-8') as fp:
                    first_line = fp.readline()

                assert first_line.startswith('#')

                title = first_line.strip('#').strip()

                template += f"[{title}]({file_path})\n\n"

    with open('./README.md', 'w', encoding='utf-8') as fp:
        fp.write(template)


if __name__ == '__main__':
    main()
