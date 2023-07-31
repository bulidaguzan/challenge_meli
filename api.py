from flask import Flask, jsonify, request
from zapv2 import ZAPv2

app = Flask(__name__)
zap = ZAPv2(apikey='your_api_key', proxies={
            'http': 'http://zap:8080', 'https': 'http://zap:8080'})


@app.route('/scan', methods=['POST'])
def initiate_scan():
    data = request.get_json()
    urls = data.get('urls', [])
    scan_id = zap.ascan.scan(urls=urls)
    return jsonify({'scan_id': scan_id})


@app.route('/scan/<scan_id>', methods=['GET'])
def get_scan_results(scan_id):
    scan_status = zap.ascan.status(scanid=scan_id)
    if scan_status == '100':
        alerts = zap.core.alerts(baseurl=scan_id)
        return jsonify({'scan_status': scan_status, 'alerts': alerts})
    else:
        return jsonify({'scan_status': scan_status})


if __name__ == '__main__':
    app.run(debug=True)
