def get_recommendations(user_id):
    rated_movies = user_ratings.get(user_id, {})
    recommendations = []

    for movie_id, movie in movies.items():
        if movie_id not in rated_movies:
            recommendations.append(movie)

    return recommendations
