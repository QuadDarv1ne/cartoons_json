from flask import Flask, render_template
from models import Cartoon, db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cartoons.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# связываем приложение и экземпляр SQLAlchemy
db.init_app(app)

@app.route('/')
def index():
    cartoons = Cartoon.query.all()
    return render_template('cartoons.html', cartoons=cartoons)

@app.route('/cartoon/<int:cartoon_id>')
def cartoon_detail(cartoon_id):
    cartoon = Cartoon.query.get_or_404(cartoon_id)
    # Извлекаем идентификатор видео из ссылки
    video_url = cartoon.video
    video_id = video_url.split('/')[-1]
    return render_template('cartoon.html', cartoon=cartoon, video_id=video_id)

if __name__ == '__main__':
    app.run(debug=True)
