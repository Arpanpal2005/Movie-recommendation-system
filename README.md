
<h1 align="center">
  <a href="https://git.io/typing-svg">
    <img src="https://readme-typing-svg.herokuapp.com/?lines=Hello;This+Project+is+by+Arpan&center=true&size=25">
  </a>
</h1>

<h1 align="center">🎬 Movie Recommendation System</h1>

<p align="center">
A <b>content-based movie recommendation system</b> that suggests movies similar to a user’s selected movie using 
<b>TF-IDF vectorization</b> and <b>Cosine Similarity</b>.
<br>
Built as an <b>interactive Streamlit web application</b> with a modern UI and real-time movie posters fetched from the 
<b>TMDB API</b>.
</p>

<hr>

<h2>📌 Features</h2>
<ul>
  <li>🔍 Search and select a movie from the dataset</li>
  <li>🎯 Get top <b>5 similar movie recommendations</b></li>
  <li>🖼️ Movie posters and cinematic background fetched from TMDB API</li>
  <li>⚡ Fast recommendations using a precomputed similarity matrix</li>
  <li>🎨 Modern, dark-themed UI built with custom CSS</li>
  <li>🔄 Click any recommended movie to get new recommendations instantly</li>
</ul>

<hr>

<h2>🧠 How It Works</h2>
<ol>
  <li>Movie metadata is preprocessed in a <b>Jupyter Notebook</b></li>
  <li>Text features (overview, genres, tags, etc.) are vectorized using <b>TF-IDF</b></li>
  <li><b>Cosine Similarity</b> is computed between all movies</li>
  <li>The similarity matrix and movie metadata are saved as <code>.pkl</code> files</li>
  <li>Streamlit loads these files and serves recommendations in real time</li>
</ol>

<hr>

<h2>🧩 System Architecture</h2>

<pre>
User selects a movie
        ↓
TF-IDF Vector Space
        ↓
Cosine Similarity Calculation
        ↓
Top-N Similar Movies
        ↓
Displayed via Streamlit UI
</pre>

<hr>

<h2>🛠 Tech Stack</h2>

<h3>Programming & Machine Learning</h3>
<ul>
  <li>Python</li>
  <li>Pandas</li>
  <li>NumPy</li>
  <li>Scikit-learn</li>
</ul>

<h3>Web App & UI</h3>
<ul>
  <li>Streamlit</li>
  <li>HTML + CSS (custom styling)</li>
</ul>

<h3>Data & Models</h3>
<ul>
  <li>Pickle (<code>.pkl</code>) for serialized data</li>
  <li>Git LFS for large ML artifacts</li>
</ul>

<h3>API</h3>
<ul>
  <li>TMDB (The Movie Database) API</li>
</ul>

<hr>

<h2>📁 Project Structure</h2>

<pre>
movie-recommendation-system/
│
├── movierecom.py          # Streamlit application (UI + logic)
├── movies.pkl             # Movie metadata (Git LFS)
├── similarity.pkl         # Cosine similarity matrix (Git LFS)
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
└── .gitattributes         # Git LFS configuration
</pre>

<hr>

<h2>🧪 Model Development (Jupyter Notebook)</h2>

<p>
The model training and preprocessing were done separately in a <b>Jupyter Notebook</b>:
</p>

<ul>
  <li>Data cleaning and feature engineering</li>
  <li>TF-IDF vectorization of text features</li>
  <li>Cosine similarity computation</li>
  <li>Serialization of results using <code>pickle</code></li>
</ul>

<p>
<b>Only the final artifacts</b> (<code>movies.pkl</code>, <code>similarity.pkl</code>) are used in the Streamlit app.
</p>

<hr>

<h2>👤 Author</h2>
<p>
<b>Arpan Pal</b><br>
Machine Learning & Python Developer
</p>

<p>
⭐ If you like this project, consider giving it a star on GitHub!
</p>
