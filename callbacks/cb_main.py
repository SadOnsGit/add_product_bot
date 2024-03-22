from aiogram.types import CallbackQuery, Message
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import Router, F

addproduct_router = Router()

class Addproduct(StatesGroup):
    name = State()
    description = State()
    price = State()
    product_url = State()
    
@addproduct_router.callback_query(F.data == 'add.course')
async def add_name(call: CallbackQuery, state: FSMContext):
    await call.message.answer('<b>Вы начали добавление нового курса' \
        '\nДля начала введите Имя вашего курса</b>', parse_mode='html')
    await state.set_state(Addproduct.name)
    
@addproduct_router.message(Addproduct.name)
async def add_description(msg: Message, state: FSMContext):
    await state.update_data(name = msg.text)
    await msg.answer('<b>Отлично, теперь введите описание товара</b>', 
                     parse_mode='html')
    await state.set_state(Addproduct.description)
    
@addproduct_router.message(Addproduct.description)
async def add_price(msg: Message, state: FSMContext):
    await state.update_data(description = msg.text)
    await msg.answer('<b>Отлично, теперь цену товара</b>', parse_mode='html')
    await state.set_state(Addproduct.price)

@addproduct_router.message(Addproduct.price)
async def add_product_url(msg: Message, state: FSMContext):
    await state.update_data(price=msg.text)
    await msg.answer('<b>Отлично, теперь введите ссылку на товар</b>', 
                     parse_mode='html')
    await state.set_state(Addproduct.product_url)
    
@addproduct_router.message(Addproduct.product_url)
async def add_course_to_db(msg: Message, state: FSMContext):
    await state.update_data(product_url = msg.text)
    data = await state.get_data()
    name = data['name']
    description = data['description']
    price = data['price']
    product_url = data['product_url']
    # await add_course_to_db(name, description, price, product_url)
    await msg.answer(f'name: {name}\ndescription: {description}\nprice: {price}' \
        f'\nproduct_url: {product_url}')
    await state.clear()