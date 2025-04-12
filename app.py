from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

# Load CSV data with pandas
df = pd.read_csv('employee_salaries.csv')

# Clean up whitespace
df.columns = df.columns.str.strip()
df['Full Name'] = df['Full Name'].astype(str).str.strip()

@app.route('/', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    if request.method == 'POST':
        query = request.form['name'].strip().lower()
        if query:
            keywords = query.split()
            def name_matches(name):
                name_lower = name.lower()
                return all(word in name_lower for word in keywords)
            
            matches = df[df['Full Name'].apply(name_matches)]
            results = matches.to_dict(orient='records')
    return render_template('index.html', results=results)



if __name__ == '__main__':
    app.run(debug=True)
