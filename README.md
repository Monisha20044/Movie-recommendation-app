# Movie Recommendation App

This is a basic movie recommendation app built with Flask. It recommends movies to users based on a simple collaborative filtering approach using a mock dataset.

## Prerequisites

- Python 3.x
- Flask (install via pip)

## Installation

1. Clone this repository or download the source code.

2. Navigate to the project directory.

3. Install Flask if you haven't already:

    ```sh
    pip install flask
    ```

## Running the App

1. In the project directory, create a file named `app.py` and add the following code:

    ```python
    from flask import Flask, request, jsonify

    app = Flask(__name__)

    # Mock dataset: A dictionary of movies with movie IDs as keys
    movies = {
        "1": {"title": "The Shawshank Redemption", "genre": "Drama"},
        "2": {"title": "The Godfather", "genre": "Crime"},
        "3": {"title": "The Dark Knight", "genre": "Action"},
        "4": {"title": "12 Angry Men", "genre": "Drama"},
        "5": {"title": "Schindler's List", "genre": "Biography"},
    }

    # Mock user ratings: A dictionary of user ratings with user IDs as keys
    user_ratings = {
        "user1": {"1": 5, "2": 4, "3": 4},
        "user2": {"2": 5, "3": 5, "4": 3},
        "user3": {"1": 4, "4": 5, "5": 4},
    }

    # Function to get recommendations for a given user ID
    def get_recommendations(user_id):
        # Get the movies rated by the user
        rated_movies = user_ratings.get(user_id, {})
        recommendations = []

        # Loop through all movies
        for movie_id, movie in movies.items():
            # If the movie is not rated by the user, add it to the recommendations
            if movie_id not in rated_movies:
                recommendations.append(movie)

        return recommendations

    # Route to get recommendations
    @app.route('/recommendations', methods=['GET'])
    def recommendations():
        # Get the user_id from the request arguments
        user_id = request.args.get('user_id')
        if not user_id:
            return jsonify({"error": "User ID is required"}), 400

        # Get recommendations for the user
        recommendations = get_recommendations(user_id)
        return jsonify(recommendations)

    if __name__ == '__main__':
        app.run(debug=True)
    ```

2. Run the Flask app:

    ```sh
    python app.py
    ```

3. Open your browser and navigate to `http://127.0.0.1:5000/recommendations?user_id=user1` to see recommendations for `user1`.

## How It Works

- The app uses a mock dataset of movies and user ratings.
- The `get_recommendations` function recommends movies that the user hasn't rated yet.
- The `/recommendations` endpoint takes a `user_id` parameter and returns the recommended movies for that user.

## Future Enhancements

- Use a real dataset for movies and user ratings.
- Implement a more sophisticated recommendation algorithm.
- Store data in a database instead of in-memory dictionaries.
- Add user authentication and profiles.
- Create a frontend interface for a better user experience.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
