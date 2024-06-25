document.addEventListener("DOMContentLoaded", function() {
  const searchButton = document.getElementById('search-button');
  const searchResults = document.getElementById('search-results');

  searchButton.addEventListener('click', () => {
    if (searchResults.style.display === "block") {
      searchResults.style.display = "none";
    } else {
      searchResults.style.display = "block";
      new PagefindUI({ element: "#search-results" });
    }
  });
});

