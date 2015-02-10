from flask.views import View
from flask import render_template
from adm.views.forms.businessform import BusinessForm

class Index(View):
    def dispatch_request(self):
    	bf = BusinessForm()
        return render_template('index.html', form=bf)
