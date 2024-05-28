from aiogram import Router, types
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import any_state
from aiogram.utils.i18n import gettext as _

from keyboards.inline.aternos.server import get_kb_server_list

start_router = Router(name=__name__)


@start_router.message(CommandStart(), any_state)
async def command_start_handler(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(_("Welcome, <b>{first_name} {last_name}(@{username})</b>").format(first_name=message.from_user.first_name, last_name=message.from_user.last_name, username=message.from_user.username),
                         reply_markup=get_kb_server_list())
