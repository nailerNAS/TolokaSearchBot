import typing
import urllib.parse

from aiohttp import ClientSession

from .TolokaSearchResult import TolokaSearchResult

API_URL = r'https://toloka.to/api.php?'


async def search(query: str) -> typing.List[TolokaSearchResult]:
    _query = encode_query(query)
    results = []

    async with ClientSession() as s:
        async with s.get(API_URL + _query) as resp:
            d = await resp.json()

            for json_result in d:
                toloka_result = TolokaSearchResult.from_json(json_result)
                results.append(toloka_result)

    return results


def encode_query(query: str) -> str:
    return urllib.parse.urlencode({'search': query})
