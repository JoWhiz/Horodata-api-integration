from flask import Flask, jsonify
import boto3
import json

application = Flask(__name__)


@application.route('/horoscope/weekly/<zodiac_sign>')
def get_weekly_horoscope(zodiac_sign):
    s3 = boto3.client('s3')
    s3_bucket_name = 'horodata1'
    object_key = f'horoscopes/pisces_weekly.json'

    try:
        response = s3.get_object(Bucket=s3_bucket_name, Key=object_key)
        horoscope_data = json.loads(response['Body'].read())

        # Assuming the structure of horoscope_data is like your provided JSON
        areas = horoscope_data.get('areas', [])

        # You can customize how you want to present the horoscope data
        horoscope_text = "\n".join(area['desc'] for area in areas)

        response_data = {
            'zodiac_sign': zodiac_sign,
            'horoscope': horoscope_text,
            'time_period': 'weekly'
        }

        return jsonify(response_data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    application.run(debug=True)
