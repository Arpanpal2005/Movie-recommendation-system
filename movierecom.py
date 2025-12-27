import requests
import streamlit as st
import pickle

# =====================================================
# PAGE CONFIG
# =====================================================
st.set_page_config(
    page_title="Movie Recommendation System",
    page_icon="🎬",
    layout="wide"
)

# =====================================================
# SESSION STATE
# =====================================================
if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

# =====================================================
# CUSTOM CSS
# =====================================================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75));
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

section.main > div {
    background-color: rgba(0,0,0,0.55);
    padding: 2rem;
    border-radius: 20px;
    backdrop-filter: blur(8px);
}

h1 {
    text-align: center;
    font-weight: 800;
}

.section-title {
    font-size: 24px;
    font-weight: 700;
    margin: 30px 0 15px;
    color: #f5c518;
    border-left: 5px solid #f5c518;
    padding-left: 12px;
}

label {
    color: #f5c518 !important;
    font-size: 16px !important;
    font-weight: 600 !important;
}

div[data-baseweb="select"] > div {
    background-color: rgba(0,0,0,0.75) !important;
    border-radius: 14px !important;
    border: 2px solid #f5c518 !important;
}

div[data-baseweb="select"] span {
    color: white !important;
}

div[data-baseweb="option"]:hover {
    background-color: #f5c518 !important;
    color: black !important;
}

.stButton button {
    background: linear-gradient(135deg, #f5c518, #ffb703);
    color: black;
    font-weight: 700;
    border-radius: 14px;
    padding: 0.7rem 1.4rem;
    border: none;
    transition: 0.3s ease;
}

.stButton button:hover {
    transform: scale(1.05);
    box-shadow: 0 0 25px rgba(245,197,24,0.6);
}

.movie-card {
    background: rgba(255,255,255,0.08);
    border-radius: 16px;
    padding: 12px;
    text-align: center;
    transition: 0.3s ease;
}

.movie-card:hover {
    transform: translateY(-8px);
    box-shadow: 0 15px 40px rgba(245,197,24,0.4);
}

.movie-title {
    margin-top: 10px;
    font-size: 15px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD DATA
# =====================================================
movies = pickle.load(open("movies.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

# =====================================================
# TMDB API
# =====================================================
API_KEY = "5c48a1a198a6da57f7c081e2a9f30a06"

@st.cache_data(show_spinner=False)
def fetch_movie(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    return requests.get(url).json()

def get_poster(movie_id):
    data = fetch_movie(movie_id)
    return (
        "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
        if data.get("poster_path")
        else "https://via.placeholder.com/500x750?text=No+Poster"
    )

def get_backdrop(movie_id):
    data = fetch_movie(movie_id)
    return (
        "https://image.tmdb.org/t/p/original/" + data["backdrop_path"]
        if data.get("backdrop_path")
        else None
    )

def set_background(img):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background:
            linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)),
            url("{img}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# =====================================================
# RECOMMENDATION FUNCTION
# =====================================================
def recommend(movie_title):
    index = movies[movies["title"] == movie_title].index[0]
    distances = similarity[index]

    movie_indices = sorted(
        list(enumerate(distances)),
        key=lambda x: x[1],
        reverse=True
    )[1:6]

    names, posters = [], []
    for i in movie_indices:
        movie_id = movies.iloc[i[0]]["id"]
        names.append(movies.iloc[i[0]]["title"])
        posters.append(get_poster(movie_id))

    return names, posters

# =====================================================
# UI HELPERS
# =====================================================
def section(title):
    st.markdown(f'<div class="section-title">{title}</div>', unsafe_allow_html=True)

def movie_card(img, title=None):
    st.markdown(
        f"""
        <div class="movie-card">
            <img src="{img}" style="width:100%; border-radius:12px;">
            {f"<div class='movie-title'>{title}</div>" if title else ""}
        </div>
        """,
        unsafe_allow_html=True
    )

# =====================================================
# MAIN UI
# =====================================================
st.title("🎬 Movie Recommendation System")
st.markdown(
    "<p style='text-align:center; font-size:18px;'>Find movies similar to your favorite one 🍿</p>",
    unsafe_allow_html=True
)

movie_list = movies["title"].tolist()
default_index = (
    movie_list.index(st.session_state.selected_movie)
    if st.session_state.selected_movie in movie_list
    else 0
)

# SEARCH + BUTTON ROW
col_search, col_btn = st.columns([4, 1])

with col_search:
    selected = st.selectbox(
        "🎥 Select a movie",
        movie_list,
        index=default_index
    )

with col_btn:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("✨ Recommend", use_container_width=True):
        st.session_state.selected_movie = selected


# =====================================================
# RESULTS
# =====================================================
if st.session_state.selected_movie:

    movie_id = movies[movies["title"] == st.session_state.selected_movie].iloc[0]["id"]
    bg = get_backdrop(movie_id)
    if bg:
        set_background(bg)

    section("Selected Movie")

    col1, col2 = st.columns([1, 4])

    with col1:
        movie_card(get_poster(movie_id))

    with col2:
        st.markdown(f"<h3 style='margin-top:40px;'>{st.session_state.selected_movie}</h3>", unsafe_allow_html=True)

    section("Recommended Movies")

    rec_movies, rec_posters = recommend(st.session_state.selected_movie)
    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            if st.button(rec_movies[i], key=f"rec_{i}", use_container_width=True):
                st.session_state.selected_movie = rec_movies[i]
                st.rerun()
            movie_card(rec_posters[i])

# =====================================================
# FOOTER
# =====================================================
st.markdown(
    "<hr><p style='text-align:center; color:gray;'>🎬 Built by Arpan Pal</p>",
    unsafe_allow_html=True
)
