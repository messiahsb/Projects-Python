
function MovieCard({ movie }) {
    
    function onHeartClick() {
        alert("clicked")
    }

    return <div className="movie-card">
        <div className="movie-poster">
            <div className="movie-poster">
                <img src={movie.url} alt={movie.tytle} />
                <div className="movie-overlay">
                    <button className="favorite-btn" onClick={onHeartClick}>
                        ❤️
                    </button>
                </div>
            </div>
        </div>
        <div className="movie-info">
            <h3>{movie.title}</h3>
            <p>{movie.release_date}</p>
        </div>
    </div>

}

export default MovieCard