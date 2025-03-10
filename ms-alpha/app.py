from main import create_app

app = create_app()

@app.route('/healthcheck')
def healthcheck():
    return 'App working correctly!', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)