from config import settings
from sqlalchemy import create_engine, text

engine = create_engine(
    url=settings.DATABASE_URL_mysql,
)

async def add_course_to_db(name: str, desc: str, price: int, prod_url: str):
    with engine.connect() as conn:
        conn.execute(text(
            f'INSERT INTO u2556815_products.item (title, price, text, prod_url) VALUES ({name}, {price}, {desc}, {prod_url})')
        )
        conn.commit()