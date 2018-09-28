import asyncio
import os
import re

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

import Toloka

TOKEN = os.environ.get('token')

if not TOKEN:
    raise AttributeError('Please declare the token environment variable or modify this code')

loop = asyncio.get_event_loop()

bot = Bot(TOKEN, loop=loop)
dp = Dispatcher(bot, loop=loop)

search_regexp = re.compile(r'/search\s(\w+)', flags=re.IGNORECASE)


def stringify_toloka_search_result(result: Toloka.TolokaSearchResult) -> str:
    return f'ID: {result.id}' \
           f'\nLink: {result.link}' \
           f'\nTitle: {result.title}' \
           f'\nForum name: {result.forum_name}' \
           f'\nForum parent: {result.forum_parent}' \
           f'\nComments: {result.comments}' \
           f'\nSize: {result.size}' \
           f'\nSeeders: {result.seeders}' \
           f'\nLeechers: {result.leechers}' \
           f'\nComplete: {result.complete}'


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(m: types.Message):
    await m.reply('Hello! I can search Toloka.to and show you results with links'
                  '\nExample search:'
                  '\n`/search Batman`',
                  parse_mode=types.ParseMode.MARKDOWN, disable_web_page_preview=True)


@dp.message_handler(commands=['search'], regexp=search_regexp.pattern)
async def search_toloka(m: types.Message):
    query = search_regexp.match(m.text).group(1)
    results = await Toloka.search(query)

    if results:
        await m.reply(f'Results for {query}:', reply=False)

        for result in results:
            await m.reply(stringify_toloka_search_result(result), reply=False)

        await m.reply('End of list', reply=False)

    else:
        await m.reply(f'No results for {query}')


@dp.inline_handler(func=lambda query: bool(query.query))
async def inline_search_toloka(q: types.InlineQuery):
    results = await Toloka.search(q.query)

    if results:
        inline_results = []

        for n, result in enumerate(results):
            result: Toloka.TolokaSearchResult

            input_content = types.InputTextMessageContent(stringify_toloka_search_result(result))
            inline_result = types.InlineQueryResultArticle(id=str(n),
                                                           title=result.title,
                                                           input_message_content=input_content,
                                                           description=f'{result.size}, {result.seeders} S | {result.leechers} L | {result.complete} C')
            inline_results.append(inline_result)
            if n >= 50:
                break

        try:
            await bot.answer_inline_query(q.id, inline_results, cache_time=300, is_personal=False)
        except:
            pass


if __name__ == '__main__':
    executor.start_polling(dp, loop=loop, skip_updates=True, reset_webhook=True)
