
@ APP.route('/submit', methods=['GET'])
def submit(message=None):
    '''run throu a pickle model'''

    result = request.values['song']

    result = pickle_model(message)

    return render_template('index.html', result=result)