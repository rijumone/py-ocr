import os
import glob
from flask import Flask, render_template
from flask_uploads import UploadSet, configure_uploads, IMAGES, patch_request_class
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import SubmitField

from PIL import Image
import pytesseract

import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('FLASK_PYOCR_SECRET_KEY')
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(os.getcwd(), 'uploads')

photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)
patch_request_class(app)  # set maximum file size, default is 16MB


class UploadForm(FlaskForm):
    photo = FileField(validators=[FileAllowed(photos, u'Image only!'), FileRequired(u'File was empty!')])
    submit = SubmitField(u'Upload')


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    # first clear upload dir
    for f in glob.glob(app.config['UPLOADED_PHOTOS_DEST'] + '/*'):
        os.remove(f)

    form = UploadForm()
    salvaged_text = None
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        file_url = photos.url(filename)
        just_the_filename = file_url.split('/')[-1]
        salvaged_text = pytesseract.image_to_string(Image.open(os.path.join(app.config['UPLOADED_PHOTOS_DEST'], just_the_filename)))
        logging.debug(salvaged_text)
    else:
        file_url = None
    return render_template(
        'index.html', 
        form=form, 
        file_url=file_url,
        salvaged_text=salvaged_text,
        )


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        debug=True,
        )