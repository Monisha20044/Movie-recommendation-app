from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock dataset
movies = {
    "1": {"title": "The Shawshank Redemption", "genre": "Drama"},
    "2": {"title": "The Godfather", "genre": "Crime"},
    "3": {"title": "The Dark Knight", "genre": "Action"},
    "4": {"title": "12 Angry Men", "genre": "Drama"},
    "5": {"title": "Schindler's List", "genre": "Biography"},
}

# Mock user ratings
user_ratings = {
    "user1": {"1": 5, "2": 4, "3": 4},
    "user2": {"2": 5, "3": 5, "4": 3},
    "user3": {"1": 4, "4": 5, "5": 4},
}

def get_recommendations(user_id):
    rated_movies = user_ratings.get(user_id, {})
    recommendations = []

    for movie_id, movie in movies.items():
        if movie_id not in rated_movies:
            recommendations.append(movie)

    return recommendations

@app.route('/recommendations', methods=['GET'])
def recommendations():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    recommendations = get_recommendations(user_id)
    return jsonify(recommendations)

if __name__ == '__main__':
    app.run(debug=True)
