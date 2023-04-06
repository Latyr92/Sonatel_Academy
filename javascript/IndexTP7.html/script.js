const APIURL =
  "https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=04c35731a5ee918f014970082a0088b1&page=1";
const IMGPATH = "https://image.tmdb.org/t/p/w1280";
const SEARCHAPI =
  "https://api.themoviedb.org/3/search/movie?&api_key=04c35731a5ee918f014970082a0088b1&query=";
  const searchInput = document.getElementById("search-bar");
  const searchBtn = document.getElementById("searchBtn");

const moviesContainer = document.querySelector(".movies-container");
const searchForm = document.querySelector(".search-container");
const searchBar = document.querySelector("#search-bar");
const movieOverlay = document.querySelector(".movie-overlay");
const movieOverlayTitle = document.querySelector(".movie-overlay-title");
const movieOverlayDescription = document.querySelector(".movie-overlay-description");

getMovies(APIURL);

async function getMovies(url) {
  const response = await fetch(url);
  const data = await response.json();
  showMovies(data.results);
}

function showMovies(movies) {
  moviesContainer.innerHTML = "";
  movies.forEach((movie) => {
    const { poster_path, title, overview,vote_average } = movie;
    const movieElement = document.createElement("div");
    movieElement.classList.add("movie");
   
    movieElement.innerHTML = `
      <img src="${IMGPATH + poster_path}" alt="${title}">
      <h2 class="movie-title">${title}</h2>
      <p class="description">${overview}</p>
      <str class="vote">${vote_average}

    `;

    // movieElement.addEventListener("mouseover", () => {
    //   showMovieDescription(overview);
    // });

    // movieElement.addEventListener("mouseout", () => {
    //   hideMovieDescription();
    // });

    moviesContainer.appendChild(movieElement);
  });
}

function showMovieDescription(description) {
  const descriptionElement = document.createElement("div");
  descriptionElement.classList.add("movie-description");
  descriptionElement.textContent = description;

  document.body.appendChild(descriptionElement);
}

function hideMovieDescription() {
  const descriptionElement = document.querySelector(".movie-description");
  if (descriptionElement) {
    descriptionElement.remove();
  }
}
searchInput.addEventListener("input", () => {
  const searchText = searchInput.value.toLowerCase();
  const searchUrl = SEARCHAPI + searchText;
  getMovies(searchUrl);
});





  
