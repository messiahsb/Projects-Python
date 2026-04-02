import './App.css'
import MovieCard from './components/MovieCard'

// componenet
function App() {
  return (
    // parent elements
   //fragment
    <>
    <MovieCard movie={{title:"Fake Film", release_date:"2024"}}/>
    <MovieCard movie={{title:"Fake Film P2", release_date:"2024"}}/>
  </>
  )
}


export default App
