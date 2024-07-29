from flask import Flask
from models import Cartoon, db
import json
import requests
from PIL import Image
from io import BytesIO

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cartoons.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def optimize_image(image_url):
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content))
    # Оптимизация изображения здесь, например, изменение размера, компрессия и т.д.
    # После оптимизации можно сохранить изображение на сервере или использовать его напрямую
    # В данном примере просто возвращаем URL изображения
    return image_url

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

        with open('cartoons.json', encoding='utf-8') as f:
            cartoons_data = json.load(f)

        for cartoon_data in cartoons_data:
            # Оптимизация изображения перед добавлением в базу данных
            optimized_image_url = optimize_image(cartoon_data['фотография'])
            cartoon = Cartoon(title=cartoon_data['название'],
                        author=cartoon_data['автор'],
                        year=cartoon_data['год публикации'],
                        description=cartoon_data['описание'],
                        image_url=optimized_image_url,
                        video=cartoon_data['видео'])
            db.session.add(cartoon)

        db.session.commit()