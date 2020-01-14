import React, { useState, useEffect } from 'react';
import RecipeList from './components/RecipeList';
import './App.css'


function App() {
  // remeber to replace key
  const apiKey = `INSERT AN OMDB API KEY HERE`
  const movieSearchString = `t=${movieToSearch}`
  // LINK TO OMDB API DOCS: http://www.omdbapi.com/
  let movieUrl = `http://www.omdbapi.com/?apikey=${apiKey}`
  let imageUrl = `http://image.omdbapi.com/?apikey=${apiKey}`
  const [showHomeButton, setShowHomeButton] = useState(false)
  const [movie, setMovie] = useState([])
  const [loading, setLoading] = useState(true)
  const [search, setSearch] = useState('')
  const [error, setError] = useState('')

  const fetchRecipe = async () => {
    try {
      const recipeData = await fetch(movieUrl)
      const { movie } = await recipeData.json()
      setMovie(movie)
      setLoading(false)

    } catch (e) {
      if (e) {
        setError(e.message)
        console.log(error)
      }
    }
  }

  const handleSearch = async (e: any) => {
    e.preventDefault()
    try {
      setLoading(true)
      const searchUrl = `${movieUrl}&t=${movieSearchString}`
      const searchedRecipeData = await fetch(searchUrl)
      const { movie } = await searchedRecipeData.json()
      setMovie(movie)
      setLoading(false)
      setShowHomeButton(true)
    } catch (e) {
      console.log(e)
    }
  }

  const handleSearchChange = (e) => {
    setSearch(e.target.value)
  }

  const handleReturnHome = () => {
    fetchRecipe()
    setShowHomeButton(false)
  }

  useEffect(() => {
    fetchRecipe()

  }, [])

  return (
    <div>
      {loading ? <h1 className="text-center">...fetching {search} Recipe</h1> :
        <RecipeList
          search={search}
          handleSearch={handleSearch}
          handleSearchChange={handleSearchChange}
          movie={movie}
          showHomeButton={showHomeButton}
          handleReturnHome={handleReturnHome} />}
    </div>
  );
}

export default App;