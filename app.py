from flask import Flask

app = (__name__)

@app.rout('/home')
def home ():
    return "welcom in the first main"
if __name__ == '__main__':
    app.run(debuge=True)
    