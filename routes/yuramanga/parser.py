from bs4 import Tag
from config.bs4 import create_soup
from .schemas import Chapter, Manga


async def parse_mangas_from_html_str(html: str) -> list[Manga]:
    soup = create_soup(html)
    items: list[Manga] = []
    if not (
        flexboxes := soup.select(
            "body > main > div > div.container > div.flexbox4 > div.flexbox4-item"
        )
    ):
        print("Container element did not have any children")
        return []
    for manga_item_el in flexboxes:
        manga_content_el = manga_item_el.div
        if manga_content_el is None:
            continue
        title = str((manga_content_el.select_one("a[title]") or Tag()).get("title", ""))
        series_url = str(
            (manga_content_el.select_one("a[title]") or Tag()).get("href", "")
        )
        type = (manga_content_el.select_one("a[title] span.type") or Tag()).get_text()
        cover_uri = str(
            (manga_content_el.select_one("a[title] img[data-src]") or Tag()).get(
                "data-src"
            )
        )
        latest_chapters: list[Chapter] = []
        latest_chapters_ul = manga_content_el.select("ul.chapter li")
        for chapter_li in latest_chapters_ul:
            latest_chapters.append(
                Chapter(
                    chapter_url=str(
                        (chapter_li.select_one("a") or Tag()).get("href", "")
                    ),
                    name=(chapter_li.select_one("a") or Tag()).get_text(),
                    updated_at=(chapter_li.select_one("span.date") or Tag()).get_text(),
                )
            )
        item = Manga(
            title=title,
            series_url=series_url,
            type=type,
            cover_uri=cover_uri,
            latest_chapters=latest_chapters,
        )
        items.append(item)
    return items


async def parse_manga_from_html_str(html: str) -> Manga:
    soup = create_soup(html)
    # with open("series.html", "w", encoding="utf-8") as html_file:
    #     if flexbox := soup.select_one("body > main > div > div > div.container > div"):
    #         print(flexbox.decode())
    #         html_file.write(str(flexbox))
    return Manga(
        title="",
        series_url="series_url",
        type="type",
        cover_uri="cover_uri",
    )
