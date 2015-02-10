from flask_wtf import Form
from wtforms import TextField, TextAreaField, IntegerField

class BusinessForm(Form):
    lloji_biznesit = TextField('Lloji i biznesit:')
    numri_regjistrimit = IntegerField('Numri i regjistrimit:')
    numri_fiskal = IntegerField('Numri i regjistrimit:')
    kta_certificate_number = IntegerField('KTA Ccertificate number:')
    pronare = TextField('Pronare:')
    aktivitetet = TextAreaField('Aktivitet/et:')
    numri_puntoreve = IntegerField('Numri i puntoreve:')
    data_konstituimit = TextField('Data e konstituimit:')
    data_aplikimit = TextField('Data e aplikimit:')
    persona_fizik = TextField('Data e aplikimit:')
    adresa = TextField('Data e aplikimit:')
    telefoni = IntegerField('Telefoni:')
