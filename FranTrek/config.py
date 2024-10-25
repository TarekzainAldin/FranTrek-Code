import os 

class Config:
    
  SECRET_KEY= '16c749724f0c2920edea51b1b4e7af80f9a10f2ed97981830c0c9109f2370862'
  SQLALCHEMY_DATABASE_URI = 'sqlite:///FranTrek.db'
  SQLALCHEMY_TRACK_MODIFICATIONS = True
  CKEDITOR_ENABLE_CODESNIPPET = True
  CKEDITOR_FILE_UPLOADER = 'main.upload'
  MAIL_SERVER = "smtp.googlemail.com"
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = 'frantrekcode@gmail.com'
  MAIL_PASSWORD = 'bfjg bwzs ujco ebzj' 