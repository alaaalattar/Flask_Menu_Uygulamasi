from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user,login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, EqualTo
from flask_uploads import UploadSet, configure_uploads, IMAGES


app = Flask(__name__)
app.config['SECRET_KEY'] = 'alaa'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['UPLOADED_PHOTOS_DEST'] = 'uploads'  # new: destination for uploaded photos
db = SQLAlchemy(app)

photos = UploadSet('photos', IMAGES)  # new: setup for flask_uploads
configure_uploads(app, photos)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

class MenuItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(200))
    image = db.Column(db.String(120))  # new: column for image filenames

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Thanks for registering! Now you can login.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')

def index():
    items = MenuItem.query.all()
    return render_template('index.html', items=items)


@app.route('/add', methods=['GET', 'POST'])
@login_required
def add_item():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')
        description = request.form.get('description')
        image = photos.save(request.files['photo'])  # new: save the uploaded photo
        new_item = MenuItem(name=name, price=price, description=description, image=image)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add_item.html')


@app.route('/edit/<int:item_id>', methods=['GET', 'POST'])
@login_required
def edit_item(item_id):
    item = MenuItem.query.get_or_404(item_id)
    if request.method == 'POST':
        item.name = request.form.get('name')
        item.price = request.form.get('price')
        item.description = request.form.get('description')
        file = request.files.get('image')
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            item.image = filename
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit_item.html', item=item)



@app.route('/delete/<int:item_id>', methods=['POST'])
@login_required
def delete_item(item_id):
    item = MenuItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/uploads/<filename>')  # new route for serving uploaded files
def send_uploaded_file(filename):
    return send_from_directory(app.config['UPLOADED_PHOTOS_DEST'], filename)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
