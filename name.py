from flask import Flask, jsonify, request
import csv
movies = []

with open("movies.csv") as f:
    reader = csv.reader(f)
    data = list(reader)
    movies = data[1:]

likedmovies = []
unlikedmovies = []
didnotwatch = []

app = Flask(__name__)
@app.route("/get-movie")

def getmovie():
    return jsonify({
        data: movies[0]
    })

@app.route("/liked-movie",methods = ["POST"])

def likedmovie():
    movie = movies[0]
    movies = movies[1:]
    likedmovies.append(movie)
    return jsonify({
        status: "success"
    })
    
@app.route("/unliked-movie",methods = ["POST"])

def unlikedmovie():
    movie = movies[0]
    movies = movies[1:]
    unlikedmovies.append(movie)
    return jsonify({
        status: "success"
    })

@app.route("/did-not-watch",methods = ["POST"])

def didnotwatch():
    movie = movies[0]
    movies = movies[1:]
    didnotwatch.append(movie)
    return jsonify({
        status: "success"
    })
    
if __name__ == "__main__":
    app.run()