
// Search functionality
const searchInput = document.getElementById('searchInput');
const searchResults = document.getElementById('searchResults');

const searchableContent = {
    'about eh': '#about-eh',
    'emergency hamburg': '#about-eh',
    'wiki': 'https://wiki.emergency-hamburg.com/en/home',
    'report player': 'https://emergency-hamburg.com/player-report',
    'unban': 'https://emergency-hamburg.com/unban-request',
    'map': '#map-title',
    'eh map': '#map-title',
    'hamburg map': '#map-title',
    'play': '#play-button',
    'play game': '#play-button'
};

searchInput.addEventListener('input', function() {
    const query = this.value.toLowerCase();
    const results = document.getElementById('search-results');
    
    if (query.length < 2) {
        results.style.display = 'none';
        return;
    }

    let matches = Object.entries(searchableContent).filter(([key]) => 
        key.includes(query)
    );

    if (matches.length > 0) {
        results.innerHTML = matches.map(([key, url]) => 
            `<div class="search-result-item" onclick="handleSearchResult('${url}')">${key}</div>`
        ).join('');
        results.style.display = 'block';
    } else {
        results.style.display = 'none';
    }
});

function handleSearchResult(target) {
    if (target.startsWith('#')) {
        const element = document.querySelector(target);
        if (element) {
            element.scrollIntoView({ behavior: 'smooth' });
        }
    } else {
        window.location.href = target;
    }
    document.getElementById('search-results').style.display = 'none';
    searchInput.value = '';
}

document.addEventListener('click', function(e) {
    if (!e.target.closest('.search-container')) {
        document.getElementById('search-results').style.display = 'none';
    }
});

window.addEventListener('load', function() {
    const loader = document.getElementById('loader');
    setTimeout(() => {
        loader.style.opacity = '0';
        setTimeout(() => {
            loader.style.display = 'none';
        }, 500);
    }, 1500);
});
