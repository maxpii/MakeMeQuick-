from flask import Flask, render_template, request, jsonify
from Vertex import Vertex
from graph import Graph

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/p16", methods=["GET", "POST"])
def p16():

    graph = create16Graph()

    if request.method == "POST":

        data = request.get_json()

        for i in data:
            graph.changeVertexStrength(i, data[i])

    desire = Vertex("Desire",100)
    event = Vertex("1600m",100)

    djk = [str(v) for v in graph.djk(desire, event)]
    temp = graph.degree_centrality()
    centrality = [str(v) for v in temp]
    bfs = [str(v) for v in graph.bfs(desire)]

    if request.method == "POST":
        return jsonify({
            "djk": djk,
            "bfs": bfs,
            "centrality": centrality
        })

    return render_template(
        "performance.html",
        djk=djk,
        bfs=bfs,
        centrality=centrality,
        event_name="1600m",
        route="/p16"
    )

@app.route("/p8", methods=["GET", "POST"])
def p8():

    graph = create8Graph()

    if request.method == "POST":

        data = request.get_json()

        for i in data:
            graph.changeVertexStrength(i, data[i])

    desire = Vertex("Desire",100)
    event = Vertex("800m",100)

    djk = [str(v) for v in graph.djk(desire, event)]
    temp = graph.degree_centrality()
    centrality = [str(v) for v in temp]
    bfs = [str(v) for v in graph.bfs(desire)]

    if request.method == "POST":
        return jsonify({
            "djk": djk,
            "bfs": bfs,
            "centrality": centrality
        })

    return render_template(
        "performance.html",
        djk=djk,
        bfs=bfs,
        centrality=centrality,
        event_name="800m",
        route="/p8"
    )
@app.route("/p32", methods=["GET", "POST"])
def p32():

    graph = create32Graph()

    if request.method == "POST":

        data = request.get_json()

        for i in data:
            graph.changeVertexStrength(i, data[i])

    desire = Vertex("Desire",100)
    event = Vertex("3200m",100)

    djk = [str(v) for v in graph.djk(desire, event)]
    temp = graph.degree_centrality()
    centrality = [str(v) for v in temp]
    bfs = [str(v) for v in graph.bfs(desire)]

    if request.method == "POST":
        return jsonify({
            "djk": djk,
            "bfs": bfs,
            "centrality": centrality
        })

    return render_template(
        "performance.html",
        djk=djk,
        bfs=bfs,
        centrality=centrality,
        event_name="3200m",
        route="/p32"
    )



@app.route("/analyze")
def analyze():
    return render_template("analyze.html")


def create16Graph():
    desire = Vertex("Desire", 100)

    sleep = Vertex("Sleep", 100)
    nutrition = Vertex("Nutrition", 100)
    consistency = Vertex("Consistency", 100)

    strength = Vertex("Strength Training", 100)
    vo2_reps = Vertex("5K Pace Reps", 100)
    strides = Vertex("Strides", 100)
    threshold_intervals = Vertex("Threshold Intervals", 100)
    tempo_runs = Vertex("Tempo Runs", 100)
    zone2_running = Vertex("Zone 2 Running", 100)


    threshold = Vertex("Threshold", 100)
    vo2 = Vertex("VO2 Max", 100)
    economy = Vertex("Running Economy", 100)

    event = Vertex("1600m", 100)


    g = Graph()

    #keeping base factors the same, but modifying training methods/event stuff 
    
    g.add_edge(desire, sleep, 100)
    g.add_edge(desire, consistency, 100)
    g.add_edge(desire, nutrition, 100)

    g.add_edge(sleep, strength, 100)
    g.add_edge(sleep, vo2_reps, 100)
    g.add_edge(sleep, strides, 100)
    g.add_edge(sleep, threshold_intervals, 100)
    g.add_edge(sleep, tempo_runs, 100)
    g.add_edge(sleep, zone2_running, 100)

    g.add_edge(nutrition, strength, 100)
    g.add_edge(nutrition, vo2_reps, 100)
    g.add_edge(nutrition, strides, 100)
    g.add_edge(nutrition, threshold_intervals, 100)
    g.add_edge(nutrition, tempo_runs, 100)
    g.add_edge(nutrition, zone2_running, 100)

    g.add_edge(consistency, strength, 100)
    g.add_edge(consistency, vo2_reps, 100)
    g.add_edge(consistency, strides, 100)
    g.add_edge(consistency, threshold_intervals, 100)
    g.add_edge(consistency, tempo_runs, 100)
    g.add_edge(consistency, zone2_running, 100)

    g.add_edge(strength, threshold, 100-25)
    g.add_edge(strength, vo2, 100-30)
    g.add_edge(strength, economy, 100-80)

    g.add_edge(vo2_reps, threshold, 100-75)
    g.add_edge(vo2_reps, vo2, 100-95)
    g.add_edge(vo2_reps, economy, 100-60)

    g.add_edge(strides, threshold, 100-5)
    g.add_edge(strides, vo2, 100-10)
    g.add_edge(strides, economy, 100-70)

    g.add_edge(threshold_intervals, threshold, 100-90)
    g.add_edge(threshold_intervals, vo2, 100-70)
    g.add_edge(threshold_intervals, economy, 100-40)

    g.add_edge(tempo_runs, threshold, 100-80)
    g.add_edge(tempo_runs, vo2, 100-60)
    g.add_edge(tempo_runs, economy, 100-30)

    g.add_edge(zone2_running, threshold, 100-70)
    g.add_edge(zone2_running, vo2, 100-80)
    g.add_edge(zone2_running, economy, 100-50)

    g.add_edge(threshold, event, 100-30)
    g.add_edge(vo2, event, 100-35)
    g.add_edge(economy, event, 100-40)

    return g

def create8Graph():
    desire = Vertex("Desire", 100)

    sleep = Vertex("Sleep", 100)
    nutrition = Vertex("Nutrition", 100)
    consistency = Vertex("Consistency", 100)

    strength = Vertex("Strength Training", 100)
    vo2_reps = Vertex("5K Pace Reps", 100)
    strides = Vertex("Strides", 100)
    threshold_intervals = Vertex("Threshold Intervals", 100)
    tempo_runs = Vertex("Tempo Runs", 100)
    zone2_running = Vertex("Zone 2 Running", 100)


    threshold = Vertex("Threshold", 100)
    vo2 = Vertex("VO2 Max", 100)
    economy = Vertex("Running Economy", 100)

    event = Vertex("800m", 100)


    g = Graph()

    g.add_edge(desire, sleep, 100)
    g.add_edge(desire, consistency, 100)
    g.add_edge(desire, nutrition, 100)

    g.add_edge(sleep, strength, 100)
    g.add_edge(sleep, vo2_reps, 100)
    g.add_edge(sleep, strides, 100)
    g.add_edge(sleep, threshold_intervals, 100)
    g.add_edge(sleep, tempo_runs, 100)
    g.add_edge(sleep, zone2_running, 100)

    g.add_edge(nutrition, strength, 100)
    g.add_edge(nutrition, vo2_reps, 100)
    g.add_edge(nutrition, strides, 100)
    g.add_edge(nutrition, threshold_intervals, 100)
    g.add_edge(nutrition, tempo_runs, 100)
    g.add_edge(nutrition, zone2_running, 100)

    g.add_edge(consistency, strength, 100)
    g.add_edge(consistency, vo2_reps, 100)
    g.add_edge(consistency, strides, 100)
    g.add_edge(consistency, threshold_intervals, 100)
    g.add_edge(consistency, tempo_runs, 100)
    g.add_edge(consistency, zone2_running, 100)

    g.add_edge(strength, threshold, 100-25)
    g.add_edge(strength, vo2, 100-30)
    g.add_edge(strength, economy, 100-80)

    g.add_edge(vo2_reps, threshold, 100-75)
    g.add_edge(vo2_reps, vo2, 100-95)
    g.add_edge(vo2_reps, economy, 100-60)

    g.add_edge(strides, threshold, 100-5)
    g.add_edge(strides, vo2, 100-10)
    g.add_edge(strides, economy, 100-70)

    g.add_edge(threshold_intervals, threshold, 100-90)
    g.add_edge(threshold_intervals, vo2, 100-70)
    g.add_edge(threshold_intervals, economy, 100-40)

    g.add_edge(tempo_runs, threshold, 100-80)
    g.add_edge(tempo_runs, vo2, 100-60)
    g.add_edge(tempo_runs, economy, 100-30)

    g.add_edge(zone2_running, threshold, 100-70)
    g.add_edge(zone2_running, vo2, 100-80)
    g.add_edge(zone2_running, economy, 100-50)

    g.add_edge(threshold, event, 100-20)
    g.add_edge(vo2, event, 100-30)
    g.add_edge(economy, event, 100-50)

    return g

def create32Graph():
    desire = Vertex("Desire", 100)

    sleep = Vertex("Sleep", 100)
    nutrition = Vertex("Nutrition", 100)
    consistency = Vertex("Consistency", 100)

    strength = Vertex("Strength Training", 100)
    vo2_reps = Vertex("5K Pace Reps", 100)
    strides = Vertex("Strides", 100)
    threshold_intervals = Vertex("Threshold Intervals", 100)
    tempo_runs = Vertex("Tempo Runs", 100)
    zone2_running = Vertex("Zone 2 Running", 100)


    threshold = Vertex("Threshold", 100)
    vo2 = Vertex("VO2 Max", 100)
    economy = Vertex("Running Economy", 100)

    event = Vertex("3200m", 100)


    g = Graph()
    
    g.add_edge(desire, sleep, 100)
    g.add_edge(desire, consistency, 100)
    g.add_edge(desire, nutrition, 100)

    g.add_edge(sleep, strength, 100)
    g.add_edge(sleep, vo2_reps, 100)
    g.add_edge(sleep, strides, 100)
    g.add_edge(sleep, threshold_intervals, 100)
    g.add_edge(sleep, tempo_runs, 100)
    g.add_edge(sleep, zone2_running, 100)

    g.add_edge(nutrition, strength, 100)
    g.add_edge(nutrition, vo2_reps, 100)
    g.add_edge(nutrition, strides, 100)
    g.add_edge(nutrition, threshold_intervals, 100)
    g.add_edge(nutrition, tempo_runs, 100)
    g.add_edge(nutrition, zone2_running, 100)

    g.add_edge(consistency, strength, 100)
    g.add_edge(consistency, vo2_reps, 100)
    g.add_edge(consistency, strides, 100)
    g.add_edge(consistency, threshold_intervals, 100)
    g.add_edge(consistency, tempo_runs, 100)
    g.add_edge(consistency, zone2_running, 100)

    g.add_edge(strength, threshold, 100-25)
    g.add_edge(strength, vo2, 100-30)
    g.add_edge(strength, economy, 100-80)

    g.add_edge(vo2_reps, threshold, 100-75)
    g.add_edge(vo2_reps, vo2, 100-95)
    g.add_edge(vo2_reps, economy, 100-60)

    g.add_edge(strides, threshold, 100-5)
    g.add_edge(strides, vo2, 100-10)
    g.add_edge(strides, economy, 100-70)

    g.add_edge(threshold_intervals, threshold, 100-90)
    g.add_edge(threshold_intervals, vo2, 100-70)
    g.add_edge(threshold_intervals, economy, 100-40)

    g.add_edge(tempo_runs, threshold, 100-80)
    g.add_edge(tempo_runs, vo2, 100-60)
    g.add_edge(tempo_runs, economy, 100-30)

    g.add_edge(zone2_running, threshold, 100-70)
    g.add_edge(zone2_running, vo2, 100-80)
    g.add_edge(zone2_running, economy, 100-50)

    g.add_edge(threshold, event, 100-70)
    g.add_edge(vo2, event, 100-60)
    g.add_edge(economy, event, 100-30)

    return g

# graph = create16Graph()
# desire = Vertex("Desire",100)
# event = Vertex("1600m", 100)

# djk = graph.djk(desire, event)
# centrality = graph.degree_centrality()
# bfs = graph.bfs(desire)

# print(djk)
# print()
# print(centrality)
# print()
# print(bfs)


if __name__ == "__main__":
    pass
    app.run(debug=True)



