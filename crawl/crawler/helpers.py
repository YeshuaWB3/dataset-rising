from typing import Optional

from .crawler import Crawler
import urllib.parse

def get_e621_index_crawler(output_file: str):
    return Crawler(
        output_file=output_file,
        base_url='https://e621.net/posts.json?limit=320',
        page_type='index',
        page_field='page'
    )


def get_e621_search_crawler(output_file: str, search_query: str):
    return Crawler(
        output_file=output_file,
        base_url='https://e621.net/posts.json?limit=320&tags=' + urllib.parse.quote(search_query, ''),
        page_type='index',
        page_field='page'
    )

def get_e621_tag_crawler(output_file: str):
    return Crawler(
        output_file=output_file,
        base_url='https://e621.net/tags.json?limit=320&search[order]=count',
        page_type='index',
        page_field='page',
        json_field=None
    )

def get_e621_implications_crawler(output_file: str):
    return Crawler(
        output_file=output_file,
        base_url='https://e621.net/tag_implications.json?limit=320',
        page_type='index',
        page_field='page',
        json_field=None
    )


def get_gelbooru_search_crawler(output_file: str, search_query: str):
    return Crawler(
        output_file=output_file,
        base_url='https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&limit=100&tags=' + urllib.parse.quote(search_query),
        page_type='index',
        page_field='pid',
        json_field='post'
    )


def get_gelbooru_index_crawler(output_file: str):
    return Crawler(
        output_file=output_file,
        base_url='https://gelbooru.com/index.php?page=dapi&s=post&q=index&json=1&limit=100',
        page_type='index',
        page_field='pid',
        json_field='post'
    )

def get_gelbooru_tag_crawler(output_file: str):
    return Crawler(
        output_file=output_file,
        base_url='https://gelbooru.com/index.php?page=dapi&s=tag&q=index&json=1&limit=100',
        page_type='index',
        page_field='pid',
        json_field='tag'
    )

def get_danbooru_search_crawler(output_file: str, search_query: str):
    return Crawler(
        output_file=output_file,
        base_url='https://danbooru.donmai.us/posts.json?limit=200&tags=' + urllib.parse.quote(search_query),
        page_type='index',
        page_field='page',
        json_field=None
    )

def get_danbooru_index_crawler(output_file: str):
    return Crawler(
        output_file=output_file,
        base_url='https://danbooru.donmai.us/posts.json?limit=200',
        page_type='index',
        page_field='page',
        json_field=None
    )

def get_danbooru_tag_crawler(output_file: str):
    return Crawler(
        output_file=output_file,
        base_url='https://danbooru.donmai.us/tags.json?limit=200',
        page_type='index',
        page_field='page',
        json_field=None
    )

def get_crawler(source: str, type: str, output_file: str, search_query: Optional[str]) -> Crawler:
    if source == 'e621':
        if type == 'index':
            return get_e621_index_crawler(output_file)
        elif type == 'search':
            return get_e621_search_crawler(output_file, search_query)
        elif type == 'tags':
            return get_e621_tag_crawler(output_file)
        elif type == 'implications':
            return get_e621_implications_crawler(output_file)
    elif source == 'gelbooru':
        if type == 'index':
            return get_gelbooru_index_crawler(output_file)
        elif type == 'search':
            return get_gelbooru_search_crawler(output_file, search_query)
        elif type == 'tags':
            return get_gelbooru_tag_crawler(output_file)
    elif source == 'danbooru':
        if type == 'index':
            return get_danbooru_index_crawler(output_file)
        elif type == 'search':
            return get_danbooru_search_crawler(output_file, search_query)
        elif type == 'tags':
            return get_danbooru_tag_crawler(output_file)

    raise Exception(f'Unsupported source (\'{source}\') or type (\'{type}\')')
