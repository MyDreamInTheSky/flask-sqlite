from indexes.index import db, bcrypt


# Sản phẩm
class Product(db.Model):
  pd_id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), unique=True, nullable=False)
  img_id = db.Column(db.Integer)
  descript = db.Column(db.String(240), nullable=False)
  price = db.Column(db.Integer, nullable=False)

  def __str__(self):
    return f'{self.pd_id} , {self.name}'
  def __init__(self, name, descript, price):
        self.name = name
        self.descript = descript
        self.img_id= 1
        self.price = price

# Khách hàng
class User(db.Model):
    ur_id = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __init__(self, email, password):
        self.email = email
       # self.active = True
        self.password = User.hashed_password(password)

    @staticmethod
    def hashed_password(password):
        return bcrypt.generate_password_hash(password).decode("utf-8")

    @staticmethod
    def get_user_with_email_and_password(email, password):
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            return user
        else:
            return None

# Hình ảnh
class Image(db.Model):
    img_id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), unique=True, nullable=False)

    def __init__(self, url):
        self.url = url

# Giỏ hàng
class Cart(db.Model):
    cart_id = db.Column(db.Integer)
    pd_id = db.Column(db.Integer, db.ForeignKey('product.pd_id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    __table_args__ = (
    db.PrimaryKeyConstraint(
        cart_id, pd_id,
        ),
    )
    def __init__(self, pd_id,quantity):
        self.pd_id = pd_id
        self.quantity = quantity

class Order(db.Model):
    order_id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.cart_id'), nullable=False)
    ur_id = db.Column(db.Integer,db.ForeignKey('user.ur_id'),nullable=False)
    sum = db.Column(db.Integer, nullable=False)
    def __init__(self, ur_id,cart_id,sum):
        self.cart_id = cart_id
        self.ur_id = ur_id
        self.sum = sum
