import phonenumbers
from phonenumbers import carrier, geocoder
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/phonenumber/<phone_number>', methods=['GET'])
def get_phone_info(phone_number):
    try:
        # Parse the phone number
        parsed_number = phonenumbers.parse(phone_number)
        
        # Get the service provider
        provider = carrier.name_for_number(parsed_number, 'en')
        
        # Get the location
        location = geocoder.description_for_number(parsed_number, 'en')
        
        # Return the results in JSON format
        return jsonify({
            'phone_number': phone_number,
            'provider': provider,
            'location': location
        })

    except phonenumbers.NumberParseException:
        return jsonify({'error': 'Invalid phone number format'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
