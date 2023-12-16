from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import text
from dotenv import load_dotenv
import os


load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

db = SQLAlchemy(app)

@app.route("/")
def home():
    return "Hello, World!"

@app.route("/flight/search")
def flightSearch():
    sql_cmd = "select * from airport;"
 
    query_data = db.session.execute(text(sql_cmd)).fetchall()
    return render_template('flight.html', data = query_data)

@app.route('/flight/search/submit', methods=['POST'])
def flightSubmit():
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    departure = request.form.get('departure')
    destination = request.form.get('destination')

    sql_cmd = f"""
                Select f.*, r.depart_airport, r.arrive_airport, s.ticket_sold
                From (Select *
                        From flight
                        Where DATE(depart_time) Between '{start_date}' And
                        '{end_date}') As f
                Join route As r on f.route_id = r.route_id
                Left Join (Select flight_id , Count(*) As ticket_sold
                            From ticket
                            Group by flight_id) As s on f.flight_id = s.flight_id
                Where r.depart_airport = {departure} And r.arrive_airport = {destination}
                Order By f.depart_time;
                """
 
    query_data = db.session.execute(text(sql_cmd))
    keys = query_data.keys()
    query_data = query_data.fetchall()
    return render_template('flightsubmit.html', data = query_data, keys = keys \
            , start_date = start_date, end_date = end_date, departure = departure, destination = destination)

@app.route("/flight/insert")
def flightIns():
    sql1 = "select * from airport;"
    sql2 = "select * from airplane;"
 
    airports = db.session.execute(text(sql1)).fetchall()
    planes = db.session.execute(text(sql2)).fetchall()
    return render_template('flightinsert.html', airports = airports, planes = planes)

@app.route('/flight/insert/submit', methods=['POST'])
def flightInsSubmit():
    start_date = request.form.get('start_date')
    end_date = request.form.get('end_date')
    departure = request.form.get('departure')
    destination = request.form.get('destination')

    sql_cmd = f"""
                Select f.*, r.depart_airport, r.arrive_airport, s.ticket_sold
                From (Select *
                        From flight
                        Where DATE(depart_time) Between '{start_date}' And
                        '{end_date}') As f
                Join route As r on f.route_id = r.route_id
                Left Join (Select flight_id , Count(*) As ticket_sold
                            From ticket
                            Group by flight_id) As s on f.flight_id = s.flight_id
                Where r.depart_airport = {departure} And r.arrive_airport = {destination}
                Order By f.depart_time;
                """
 
    query_data = db.session.execute(text(sql_cmd))
    keys = query_data.keys()
    query_data = query_data.fetchall()
    return 'Success'

@app.route("/flight/delete")
def flightDel():
    return "Hello, World!"

@app.route("/flight/delete/submit")
def flightDelSubmit():
    return "Hello, World!"

@app.route("/employee/position")
def empPosition():
    sql_cmd = f"""
                select employee_position, count(*) as employee_count
                from employee
                group by employee_position;
                """
 
    query_data = db.session.execute(text(sql_cmd)).fetchall()
    return render_template('empposition.html', employees = query_data)

@app.route('/employee/position/submit', methods=['POST'])
def empPositionSubmit():
    position = request.form.get('selectedemployee')

    sql_cmd = f"""
                select *
                from employee
                where employee_position = '{position}';
                """
 
    query_data = db.session.execute(text(sql_cmd))
    keys = query_data.keys()
    query_data = query_data.fetchall()
    return render_template('empsubmit.html', employees = query_data, keys = keys)

@app.route("/employee/id")
def empId():
    return render_template('empid.html')

@app.route('/employee/id/submit', methods=['POST'])
def empIdSubmit():
    id = request.form.get('emp_id')

    sql_cmd = f"""
                select *
                from employee
                where employee_id = {id};
                """
 
    query_data = db.session.execute(text(sql_cmd))
    keys = query_data.keys()
    query_data = query_data.fetchall()
    return render_template('empsubmit.html', employees = query_data, keys = keys)

@app.route("/partschedule")
def partSchedule():
    return "Hello, World!"

@app.route("/maintainrecord")
def maintainRecord():
    return "Hello, World!"

@app.route("/maintainrecord/submit")
def maintainRecordSubmit():
    return "Success"

if __name__ == '__main__':
    app.run()