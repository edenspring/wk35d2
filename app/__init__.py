from flask import Flask, render_template, redirect
from .config import Configuration
from app import dbfuncs
from app.forms import NewCarForm, ChangeOwner
from app.routes import app_routes


app = Flask(__name__)

app.config.from_object(Configuration)

try:
    cars = dbfuncs.get_all_cars()
except:
    dbfuncs.seed()

app.register_blueprint(app_routes, url_prefix="/")


# @app.route('/')
# def home():
#     info = {
#         "title": "CARS CARS CARS",
#         "header": "THIS IS THE CARS HOME PAGE!"
#     }
#     cars = dbfuncs.get_all_cars()
#     return render_template('page.html', info=info, cars=cars)


# @app.route('/test')
# def test():
#     info = {
#         "title": "Test page",
#         "header": "This is the test page"
#     }
#     return render_template('page.html', info=info)


# @app.route('/form', methods=('GET', 'POST'))
# def form():
#     form = NewCarForm()
#     if form.validate_on_submit():
#         print("+++++++MADE IT TO FORM!!!+++++++++")
#         dbfuncs.add_new_car(form.manu_year.data, form.make.data,
#                             form.model.data, form.owner_id.data)
#         return redirect("/")
#     info = {
#         "title": "NEW CAR FORM!",
#         "header": "ADD A NEW CAR 😎"
#     }
#     cars = dbfuncs.get_all_cars()  # RENDER CARS ON FORM!
#     owners = dbfuncs.get_all_owners()  # RENDER OWNERS SO THEY KNOW WHO CAN OWN A CAR
#     return render_template("page.html", info=info, form=form, cars=cars, owners=owners)

# @app.route("/change-owners",methods=('GET', 'POST'))
# def change():
#     form = ChangeOwner()
#     if form.validate_on_submit():
#         dbfuncs.change_car_owner(car_id=form.car_id.data, new_owner_id=form.owner_id.data)
#         return redirect("/")
#     cars = dbfuncs.get_all_cars()
#     owners = dbfuncs.get_all_owners()
#     info = {
#         "title": "CHANGE OWNER FORM!",
#         "header": "CHANGE A CAR'S OWNER 😎"
#     }
#     return render_template("page.html", info=info, forms=form, cars=cars, owners=owners)
