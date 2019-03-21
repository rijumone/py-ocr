# forms.py

from flask_wtf import FlaskForm
from wtforms import SubmitField
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_uploads import UploadSet, IMAGES

photos = UploadSet('photos', IMAGES)

class UploadForm(FlaskForm):
    photo = FileField(
    	'Image',
    	# validators=[FileAllowed(photos, u'Image only!'), FileRequired(u'File was empty!')]
    	)
    submit = SubmitField(u'Upload')
