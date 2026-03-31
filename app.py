from flask import Flask, render_template, jsonify, request
import csv
from datetime import datetime

app = Flask(__name__)

def read_co2_data():
    """Nolasa CO2 datus no CSV faila"""
    data = []
    try:
        with open('CO2.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)
            for row in csv_reader:
                if len(row) >= 3:
                    item = {
                        'id': int(row[0]),
                        'co2': float(row[1]),
                        'day': int(row[2])
                    }
                    if len(row) >= 4:
                        item['device'] = row[3]
                    if len(row) >= 5:
                        item['location'] = row[4]
                    if len(row) >= 6:
                        item['temperature'] = float(row[5]) if row[5] else None
                    if len(row) >= 7:
                        item['humidity'] = int(row[6]) if row[6] else None
                    data.append(item)
    except FileNotFoundError:
        print(f"Kļūda: CO2.csv fails nav atrasts!")
    except Exception as e:
        print(f"Kļūda: {e}")
    return data

def get_statistics(data):
    """Aprēķina statistiku no CO2 datiem"""
    if not data:
        return {}
    
    co2_values = [d['co2'] for d in data]
    return {
        'count': len(co2_values),
        'min': min(co2_values),
        'max': max(co2_values),
        'avg': sum(co2_values) / len(co2_values),
        'first_day': min([d['day'] for d in data]),
        'last_day': max([d['day'] for d in data])
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chart')
def chart():
    return render_template('chart.html')

@app.route('/data')
def data():
    all_data = read_co2_data()
    return render_template('data.html', all_data=all_data)

@app.route('/api/data')
def api_data():
    return jsonify(read_co2_data())

@app.route('/api/data/<int:day>')
def api_data_by_day(day):
    data = read_co2_data()
    result = [d for d in data if d['day'] == day]
    if result:
        return jsonify(result)
    return jsonify({'error': 'Diena nav atrasta'}), 404

@app.route('/api/statistics')
def api_statistics():
    return jsonify(get_statistics(read_co2_data()))

if __name__ == '__main__':
    app.run(debug=True)