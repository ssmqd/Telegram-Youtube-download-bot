from aiogram import types, Dispatcher
from aiogram.types.chat import Chat
from create_bot import bot, dp, ID
from aiogram.types import ReplyKeyboardRemove
from aiogram.dispatcher.filters import Text
from keyboards import kb_client
from pytube import YouTube
import os
from pathlib import Path
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


async def start_com(message: types.Message):
    await bot.send_message(message.from_user.id, "Дароу мій господин!", reply_markup=kb_client)
    await message.delete()


async def close_kb(message: types.Message):
    await message.answer('To open keyboard print /start', reply_markup=ReplyKeyboardRemove())


async def load_url(message: types.Message):
    if message.from_user.id == ID:
        video = YouTube(message.text).streams.filter(only_audio=True).first()
        pas = f'/poggg/audio/AYFF/audiof/{video.title}.mp3'
        try:
            out_file = video.download(output_path='/poggg/audio/AYFF/audiof')
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            await bot.send_audio(message.from_user.id, audio=open(pas, 'rb'))
        except:
            await message.reply('you already downloaded this video')
            await bot.send_audio(message.from_user.id, audio=open(pas, 'rb'))
    else:
        await message.answer(f'You dont have permission {message.from_user.first_name}')


async def element(message: types.Message):
    await message.answer('_______________Audio_Files_______________')
    for path in Path('audiof').rglob('*.mp3'):
        await bot.send_message(message.from_user.id, f'{path.name}')
        await bot.send_message(message.from_user.id, 'Menage the audio file:', reply_markup=InlineKeyboardMarkup().\
                               add(InlineKeyboardButton('Upload', callback_data=f'load {path.name}')).\
                               insert(InlineKeyboardButton('Load to group', callback_data=f'group {path.name}')).\
                               add(InlineKeyboardButton('Delete', callback_data=f'del {path.name}')))
    await message.delete()


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
async def delete_element(callback_query: types.CallbackQuery):
    if callback_query.from_user.id == ID:
        os.remove(f"/poggg/audio/AYFF/audiof/{callback_query.data.replace('del ', '')}")
        await callback_query.answer(text=f'{callback_query.data.replace("del ", "")} deleted.', show_alert=True)
    else:
        await callback_query.message.answer(f'You dont have permission {callback_query.from_user.first_name}')


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('group '))
async def load_group(callback_query: types.CallbackQuery):
    pas = f'/poggg/audio/AYFF/audiof/{callback_query.data.replace("group ", "")}'
    await bot.send_audio('-802746227', audio=open(pas, 'rb'))
    await callback_query.answer(text=f'{callback_query.data.replace("group ", "")} uploaded.', show_alert=True)


@dp.callback_query_handler(lambda x: x.data and x.data.startswith('load '))
async def load_element(callback_query: types.CallbackQuery):
    pas = f'/poggg/audio/AYFF/audiof/{callback_query.data.replace("load ", "")}'
    await bot.send_audio(callback_query.from_user.id, audio=open(pas, 'rb'))
    await callback_query.answer(text=f'{callback_query.data.replace("load ", "")} uploaded.', show_alert=True)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(start_com, commands='start')
    dp.register_message_handler(close_kb, Text(equals='close', ignore_case=True))
    dp.register_message_handler(load_url, Text(startswith='https:'))
    dp.register_message_handler(element, Text(equals='elements', ignore_case=True))