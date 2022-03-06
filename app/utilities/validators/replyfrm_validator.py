
from wtforms import validators, Form, StringField

class ClsReplyFrm(Form):
    title = StringField('title',[validators.length(min=4, max=64)])
    description = StringField('description',[validators.length(min=40)])

