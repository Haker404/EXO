from aiogram import Bot, Dispatcher, types, executor
from config import  TELEGRAM_TOKEN

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command= '/start', description= 'Команда для запуска бота'),
        types.BotCommand(command='/help', description='Команда для того, чтобы узнать с чем бот может помочь'),
        types.BotCommand(command='/info', description='Команда для того, чтобы узнать о чём этот бот'),
        types.BotCommand(command='/donate', description='Команда для доната'),
        types.BotCommand(command='/creators', description='Команда которая показывает создателей бота'),
    ]
    await bot.set_my_commands(commands)

@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Привет, я ЭХО бот')

@dp.message_handler(commands= 'help')
async def help(message: types.Message):
    await message.reply('Я могу помочь тебе...')

@dp.message_handler(commands= 'info')
async def info(message: types.Message):
    await message.reply('Я ЭХО бот, который дублирует твои сообщения!')

@dp.message_handler(commands= 'donate')
async def donate (message: types.Message):
    await message.reply('Поддержать можно здесь 835097835735902876235907 \nСпасибо за поддержку!!!' )

@dp.message_handler(commands= 'creators')
async def creators(message: types.Message):
    await message.reply('Создатели: @Rzrgz')

@dp.message_handler()
async def exo(message: types.Message):
    await message.answer(message.text)

async  def on_startup(dispatcher):
    await set_commands(dispatcher.bot)


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates= True, on_startup=on_startup)