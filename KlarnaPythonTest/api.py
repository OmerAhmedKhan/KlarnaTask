import logging
from flask import Flask
from flask import abort
from flask_restful import Resource, Api
from module import get_fab, get_ack, get_fact
from flask_restful import request
from flask import jsonify
from flask import render_template





logging.basicConfig(filename='error.log',level=logging.ERROR)

app = Flask(__name__)
api = Api(app)


def basic_validations(args):
    """Basic validations for arguments"""

    for k, v in args.items():
        if not k:
            if not isinstance(v, int):
                error = 'Argument parameter should only be an integer'
                return error

        if k not in ['m', 'n']:
            error = 'Invalid Argument parameter'
            logging.error(error)
            return error

    try:
        int(args['m'])
    except KeyError:
        pass
    except:
        error = 'Invalid argument m'
        logging.error(error)
        return error

    try:
        int(args['n'])
    except KeyError:
        pass
    except:
        error = 'Invalid argument n'
        logging.error(error)
        return error

    if int(args.get('n', 0)) < 0 or int(args.get('m', 0)) < 0:
        error = 'Numbers can not be negative'
        logging.error(error)
        return error

    return ""


class Status(Resource):
    """ Get status of Webserver """
    def get(self):
        response = {'status': 'Active'}
        return jsonify(response)


class FabocciniNumber(Resource):
    """ API for Faboccini number """
    def get(self):
        args = request.args
        error = basic_validations(args)
        if error:
            return {'error':error}, 400

        number = int(args['n'])
        response = get_fab(number)

        return jsonify(response)


class AckermannNumbers(Resource):
    """ API for Ackermann number """
    def get(self):
        args = request.args
        error = basic_validations(args)
        if error:
            return {'error':error}, 400

        n = int(args['n'])
        m = int(args['m'])

        response = get_ack(m, n)

        return jsonify(response)


class Factorial(Resource):
    """ API for Factorial number """
    def get(self):
        args = request.args
        error = basic_validations(args)
        if error:
            return {'error':error}, 400

        number = int(args['n'])
        response = get_fact(number)

        return jsonify(response)


@app.errorhandler(404)
def http_error_handler(error):
    return render_template('404.html'), 404




api.add_resource(Status, '/status/')
api.add_resource(FabocciniNumber, '/fabocciniNumber/')
api.add_resource(AckermannNumbers, '/ackermannNumbers/')
api.add_resource(Factorial, '/factorial/')

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')