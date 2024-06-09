from flask import jsonify
from . import app_views  # Assuming this file is in views folder

@app_views.route('/status', methods=['GET'])
def get_status():
    """
    Returns the API status as a JSON response.
    ---
    responses:
        200:
            description: The API is up and running.
            content:
                application/json:
                    schema:
                        type: object
                        properties:
                            status:
                                type: string
                                description: The API status.
    """
    return jsonify({'status': 'OK'})

