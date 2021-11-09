from myapp import db,myobj
from sqlalchemy import asc
from myapp.forms import TopCitiesForm
from myapp.models import TopCities
from flask import render_template, escape, flash, redirect,request


@myobj.route("/", methods=['GET', 'POST'])
def home():
    form = TopCitiesForm()
    name = 'Lian'
    title = 'Top Cities'
    # if the user hit submit on the forms page
    if form.validate_on_submit(): 
        flash(f'City Name : {form.city_name.data} added')
    
    if request.method == 'POST':
        city = request.form['city_name']
        rank = request.form['city_rank']
        add_city = TopCities(city_name = city,city_rank =rank)
        db.session.add(add_city)
        db.session.commit()
        return redirect("/")
  
    else:
        topcities = TopCities.query.order_by(asc(TopCities.city_rank)).all()
        return render_template('home.html',form=form,name = name,topcities=topcities,title = title)



