from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # This enables CORS for all routes

# Mock dataset that simulates the structure of the provided data analysis.
# This data is structured to provide a comprehensive view for the dashboard.
COVID_DATA = {
    "Global": {
        "name": "Global",
        "totalTrials": 5783,
        "trialStatusDistribution": {
            "Recruiting": 1968,
            "Completed": 1785,
            "Active, not recruiting": 782,
            "Other": 1248
        },
        "topCountries": [
            {"country": "United States", "count": 2500},
            {"country": "China", "count": 1020},
            {"country": "United Kingdom", "count": 850},
            {"country": "France", "count": 520},
            {"country": "Germany", "count": 480},
        ],
        "phaseStatusDistribution": [
            {"phase": "Phase 1", "Recruiting": 150, "Completed": 120, "Active": 80},
            {"phase": "Phase 2", "Recruiting": 350, "Completed": 300, "Active": 250},
            {"phase": "Phase 3", "Recruiting": 500, "Completed": 450, "Active": 320},
            {"phase": "Phase 4", "Recruiting": 200, "Completed": 250, "Active": 100},
            {"phase": "Other", "Recruiting": 100, "Completed": 80, "Active": 50}
        ],
        "trialsOverTime": [
            {"date": "Jan 2020", "count": 10},
            {"date": "Feb 2020", "count": 50},
            {"date": "Mar 2020", "count": 150},
            {"date": "Apr 2020", "count": 300},
            {"date": "May 2020", "count": 450},
            {"date": "Jun 2020", "count": 400},
            {"date": "Jul 2020", "count": 350},
            {"date": "Aug 2020", "count": 380},
            {"date": "Sep 2020", "count": 420},
            {"date": "Oct 2020", "count": 450},
            {"date": "Nov 2020", "count": 480},
            {"date": "Dec 2020", "count": 500},
        ],
        "countriesList": [
            "United States", "China", "United Kingdom", "France", "Germany", "India",
            "Canada", "Brazil", "Australia", "Japan", "Italy", "Spain"
        ]
    },
    "United States": {
        "name": "United States",
        "totalTrials": 2500,
        "trialStatusDistribution": {
            "Recruiting": 850,
            "Completed": 700,
            "Active, not recruiting": 400,
            "Other": 550
        },
        "phaseStatusDistribution": [
            {"phase": "Phase 1", "Recruiting": 80, "Completed": 70, "Active": 50},
            {"phase": "Phase 2", "Recruiting": 250, "Completed": 200, "Active": 150},
            {"phase": "Phase 3", "Recruiting": 350, "Completed": 300, "Active": 200},
            {"phase": "Phase 4", "Recruiting": 120, "Completed": 100, "Active": 50}
        ],
        "trialsOverTime": [
            {"date": "Jan 2020", "count": 5},
            {"date": "Feb 2020", "count": 25},
            {"date": "Mar 2020", "count": 75},
            {"date": "Apr 2020", "count": 150},
            {"date": "May 2020", "count": 200},
            {"date": "Jun 2020", "count": 180},
            {"date": "Jul 2020", "count": 150},
            {"date": "Aug 2020", "count": 170},
            {"date": "Sep 2020", "count": 190},
            {"date": "Oct 2020", "count": 210},
            {"date": "Nov 2020", "count": 230},
            {"date": "Dec 2020", "count": 250},
        ]
    },
    "China": {
        "name": "China",
        "totalTrials": 1020,
        "trialStatusDistribution": {
            "Recruiting": 400,
            "Completed": 350,
            "Active, not recruiting": 150,
            "Other": 120
        },
        "phaseStatusDistribution": [
            {"phase": "Phase 1", "Recruiting": 30, "Completed": 40, "Active": 20},
            {"phase": "Phase 2", "Recruiting": 80, "Completed": 70, "Active": 50},
            {"phase": "Phase 3", "Recruiting": 150, "Completed": 120, "Active": 80},
            {"phase": "Phase 4", "Recruiting": 50, "Completed": 60, "Active": 30}
        ],
        "trialsOverTime": [
            {"date": "Jan 2020", "count": 2},
            {"date": "Feb 2020", "count": 10},
            {"date": "Mar 2020", "count": 50},
            {"date": "Apr 2020", "count": 100},
            {"date": "May 2020", "count": 120},
            {"date": "Jun 2020", "count": 100},
            {"date": "Jul 2020", "count": 80},
            {"date": "Aug 2020", "count": 90},
            {"date": "Sep 2020", "count": 100},
            {"date": "Oct 2020", "count": 110},
            {"date": "Nov 2020", "count": 120},
            {"date": "Dec 2020", "count": 130},
        ]
    },
    "United Kingdom": {
        "name": "United Kingdom",
        "totalTrials": 850,
        "trialStatusDistribution": {
            "Recruiting": 250,
            "Completed": 200,
            "Active, not recruiting": 100,
            "Other": 300
        },
        "phaseStatusDistribution": [
            {"phase": "Phase 1", "Recruiting": 20, "Completed": 15, "Active": 10},
            {"phase": "Phase 2", "Recruiting": 50, "Completed": 40, "Active": 30},
            {"phase": "Phase 3", "Recruiting": 80, "Completed": 70, "Active": 50},
            {"phase": "Phase 4", "Recruiting": 30, "Completed": 35, "Active": 20}
        ],
        "trialsOverTime": [
            {"date": "Jan 2020", "count": 1},
            {"date": "Feb 2020", "count": 8},
            {"date": "Mar 2020", "count": 20},
            {"date": "Apr 2020", "count": 50},
            {"date": "May 2020", "count": 70},
            {"date": "Jun 2020", "count": 60},
            {"date": "Jul 2020", "count": 50},
            {"date": "Aug 2020", "count": 55},
            {"date": "Sep 2020", "count": 60},
            {"date": "Oct 2020", "count": 65},
            {"date": "Nov 2020", "count": 70},
            {"date": "Dec 2020", "count": 75},
        ]
    },
    "France": {
        "name": "France",
        "totalTrials": 520,
        "trialStatusDistribution": {
            "Recruiting": 150,
            "Completed": 120,
            "Active, not recruiting": 80,
            "Other": 170
        },
        "phaseStatusDistribution": [
            {"phase": "Phase 1", "Recruiting": 15, "Completed": 10, "Active": 8},
            {"phase": "Phase 2", "Recruiting": 40, "Completed": 35, "Active": 25},
            {"phase": "Phase 3", "Recruiting": 60, "Completed": 50, "Active": 40},
            {"phase": "Phase 4", "Recruiting": 20, "Completed": 25, "Active": 15}
        ],
        "trialsOverTime": [
            {"date": "Jan 2020", "count": 1},
            {"date": "Feb 2020", "count": 5},
            {"date": "Mar 2020", "count": 15},
            {"date": "Apr 2020", "count": 30},
            {"date": "May 2020", "count": 40},
            {"date": "Jun 2020", "count": 35},
            {"date": "Jul 2020", "count": 30},
            {"date": "Aug 2020", "count": 32},
            {"date": "Sep 2020", "count": 35},
            {"date": "Oct 2020", "count": 40},
            {"date": "Nov 2020", "count": 45},
            {"date": "Dec 2020", "count": 50},
        ]
    },
    "Germany": {
        "name": "Germany",
        "totalTrials": 480,
        "trialStatusDistribution": {
            "Recruiting": 120,
            "Completed": 110,
            "Active, not recruiting": 70,
            "Other": 180
        },
        "phaseStatusDistribution": [
            {"phase": "Phase 1", "Recruiting": 10, "Completed": 8, "Active": 5},
            {"phase": "Phase 2", "Recruiting": 30, "Completed": 25, "Active": 20},
            {"phase": "Phase 3", "Recruiting": 50, "Completed": 45, "Active": 30},
            {"phase": "Phase 4", "Recruiting": 15, "Completed": 18, "Active": 10}
        ],
        "trialsOverTime": [
            {"date": "Jan 2020", "count": 1},
            {"date": "Feb 2020", "count": 4},
            {"date": "Mar 2020", "count": 12},
            {"date": "Apr 2020", "count": 25},
            {"date": "May 2020", "count": 35},
            {"date": "Jun 2020", "count": 30},
            {"date": "Jul 2020", "count": 28},
            {"date": "Aug 2020", "count": 30},
            {"date": "Sep 2020", "count": 32},
            {"date": "Oct 2020", "count": 35},
            {"date": "Nov 2020", "count": 40},
            {"date": "Dec 2020", "count": 45},
        ]
    }
}


@app.route('/api/covid-data', methods=['GET'])
def get_covid_data():
    """
    Serves mock COVID-19 clinical trial data.
    """
    return jsonify(COVID_DATA)

if __name__ == '__main__':
    app.run(debug=True)
