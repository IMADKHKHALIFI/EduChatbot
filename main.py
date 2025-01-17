import streamlit as st
from streamlit_option_menu import option_menu
import google.generativeai as gen_ai
import base64
import os

# API Key for Gemini AI
api_key1 = "your API key "

# Set up the Streamlit app with custom theme
st.set_page_config(page_title="AI Mentor - Your Professional Guide", page_icon="🤖", layout="wide")

# Function to add custom background image
def add_bg_from_local(image_file):
    if os.path.exists(image_file):
        with open(image_file, "rb") as f:
            encoded_string = base64.b64encode(f.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url(data:image/jpg;base64,{encoded_string});
                background-size: cover;
                background-position: center;
            }}
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <style>
            .stApp {
                background: linear-gradient(135deg, #1f4037, #99f2c8);
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

# Add custom background image or fallback to gradient
add_bg_from_local("background.jpg")

# Custom CSS for Glassmorphism and other styling
st.markdown(
    """
    <style>
    /* Glassmorphism Styling */
    .main {
        background: rgba(255, 255, 255, 0.1) !important;
        backdrop-filter: blur(10px) !important;
        border-radius: 15px !important;
        border: 1px solid rgba(255, 255, 255, 0.2) !important;
        padding: 2rem !important;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5) !important;
        color: white !important;
    }
    /* Header Logo */
    .header-logo {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 2rem;
    }
    .header-logo img {
        width: 150px;
        height: auto;
        margin-right: 15px;
    }
    .header-title {
        font-size: 2.5rem;
        font-weight: bold;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    /* Navigation Menu */
    .stButton button, .roadmap-item, .course-section {
        background-color: rgba(45, 106, 79, 0.8) !important;
        color: white !important;
        border-radius: 8px !important;
        margin: 0.5rem 0 !important;
        box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    .stButton button:hover, .roadmap-item:hover, .course-section:hover {
        background-color: rgba(64, 145, 108, 0.8) !important;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5) !important;
        transform: translateY(-2px) !important;
    }
    /* Expandable Sections */
    .st-expander {
        background: rgba(52, 78, 65, 0.8) !important;
        color: white !important;
        border-radius: 8px !important;
    }
    .st-expander:hover {
        background: rgba(45, 106, 79, 0.8) !important;
    }
    /* Inputs Styling */
    div.stTextInput > div > div > input {
        background-color: rgba(31, 31, 31, 0.8) !important;
        color: white !important;
        padding: 0.5rem 1rem !important;
        border-radius: 25px !important;
        border: 2px solid #2196F3 !important; /* Blue border */
    }
    /* Tool Card Styling */
    .tool-card {
        background: rgba(45, 106, 79, 0.8);
        border-radius: 10px;
        padding: 1rem;
        margin: 1rem 0;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    }
    .tool-card h4 {
        margin-top: 0;
    }
    .tool-card a {
        text-decoration: none;
    }
    .tool-card button {
        background-color: #2196F3; /* Blue color */
        color: white;
        padding: 0.5rem 1rem;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 1rem;
        margin: 0.2rem;
    }
    .tool-card button:hover {
        background-color: #1e88e5; /* Darker blue on hover */
    }
    /* Footer Styling */
    .footer {
        text-align: center;
        padding: 1rem;
        margin-top: 2rem;
        font-size: 0.9rem;
        color: #ddd;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Navigation using option_menu
with st.sidebar:
    st.header("Navigation")
    selected = option_menu(
        "Main Menu",
        ["Home", "Roadmap", "Chat"],
        icons=['house', 'map', 'chat'],
        menu_icon="cast",
        default_index=0,
    )

if selected == "Home":
    # Header with University Logo

# Encode the image to Base64
    def get_base64_of_image(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    # Get the Base64 string of the logo
    logo_base64 = get_base64_of_image("un.png")

    # Display the logo using Base64
    st.markdown(
        f"""
        <div class="header-logo">
            <img src="data:image/png;base64,{logo_base64}" alt="University Logo" style="width: 150px; height: auto;">
            <span class="header-title">AI Mentor</span>
        </div>
        <div style="text-align: center;">
            <p>Your Personalized Data Science and AI Guide</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Course Information Section
    st.markdown("## 📚 Course Information")
    semesters = {
        "Semestre 1": [
            "📘 REPRESENTATION DES CONNAISSANCES",
            "🐍 PYTHON AVANCE POUR LA DATA SCIENCE",
            "🤖 ROBOTIQUE",
            "🎲 VARIABLES ALEATOIRES",
            "📊 STATISTIQUES",
            "🧠 COMPETENCES GENERALES",
            "🌍 LANGUES ETRANGERES (ANGLAIS/FRANÇAIS)"
        ],
        "Semestre 2": [
            "⛏️ DATA MINING",
            "🖥️ SYSTEMES INFORMATIQUES DISTRIBUES ET MIDDLEWARES",
            "📈 APPRENTISSAGE AUTOMATIQUE",
            "🎨 PROGRAMMATION D'INTERFACES GRAPHIQUES",
            "🖼️ PROJET 1: INTELLIGENCE ARTIFICIELLE ET IMAGERIE",
            "💻 CULTURE DIGITALE",
            "🌍 LANGUES ETRANGERES (ANGLAIS/FRANÇAIS)"
        ],
        "Semestre 3": [
            "💬 NLP ET WEB MINING",
            "🗄️ ARCHITECTURES POUR BIG DATA",
            "🧠 L'APPRENTISSAGE EN PROFONDEUR",
            "📊 PROJET 2: INTELLIGENCE ARTIFICIELLE ET DONNEES NUMERIQUES",
            "🕶️ IA, REALITE VIRTUELLE ET AUGMENTEE",
            "🎨 CULTURE AND ART SKILLS",
            "🌍 LANGUES ETRANGERES (ANGLAIS/FRANÇAIS)"
        ],
        "Semestre 4": [
            "💼 EMPLOYMENT SKILLS",
            "📜 PROJET DE FIN D'ETUDES (PFE)"
        ],
    }

    for semester, modules in semesters.items():
        with st.expander(f"🎓 {semester}", expanded=False):
            for module in modules:
                st.markdown(f"""
                    <div class="course-section">
                        <h4>{module}</h4>
                    </div>
                """, unsafe_allow_html=True)

    # Study Requirements and Tools Section
    with st.expander("📖 Study Requirements and Tools", expanded=False):
        st.markdown("### 🛠️ Required Tools and Libraries")
        tools = [
            {"Name": "🐍 Python", "Command": "Download from [python.org](https://www.python.org/)", "Docs": "https://docs.python.org/3/"},
            {"Name": "🖥️ VSCode", "Command": "Download from [code.visualstudio.com](https://code.visualstudio.com/)", "Docs": "https://code.visualstudio.com/docs"},
            {"Name": "🐍 Anaconda", "Command": "Download from [anaconda.com](https://www.anaconda.com/)", "Docs": "https://docs.anaconda.com/"},
            {"Name": "📓 Jupyter Notebook", "Command": "Install via Anaconda or `pip install notebook`", "Docs": "https://jupyter.org/documentation"},
            {"Name": "🐼 Pandas", "Command": "`pip install pandas`", "Docs": "https://pandas.pydata.org/docs/"},
            {"Name": "🔢 NumPy", "Command": "`pip install numpy`", "Docs": "https://numpy.org/doc/"},
            {"Name": "📊 Matplotlib", "Command": "`pip install matplotlib`", "Docs": "https://matplotlib.org/stable/contents.html"},
            {"Name": "🤖 Scikit-learn", "Command": "`pip install scikit-learn`", "Docs": "https://scikit-learn.org/stable/"},
            {"Name": "🧠 TensorFlow", "Command": "`pip install tensorflow`", "Docs": "https://www.tensorflow.org/api_docs"},
            {"Name": "🔥 PyTorch", "Command": "`pip install torch`", "Docs": "https://pytorch.org/docs/stable/index.html"},
            {"Name": "🐙 Git", "Command": "Download from [git-scm.com](https://git-scm.com/)", "Docs": "https://git-scm.com/doc"},
            {"Name": "🐳 Docker", "Command": "Download from [docker.com](https://www.docker.com/)", "Docs": "https://docs.docker.com/"},
            {"Name": "📦 SQLAlchemy", "Command": "`pip install sqlalchemy`", "Docs": "https://docs.sqlalchemy.org/"},
            {"Name": "🌐 Flask", "Command": "`pip install flask`", "Docs": "https://flask.palletsprojects.com/"},
            {"Name": "📈 Seaborn", "Command": "`pip install seaborn`", "Docs": "https://seaborn.pydata.org/"},
            {"Name": "📉 Plotly", "Command": "`pip install plotly`", "Docs": "https://plotly.com/python/"},
            {"Name": "📚 NLTK", "Command": "`pip install nltk`", "Docs": "https://www.nltk.org/"},
            {"Name": "📖 SpaCy", "Command": "`pip install spacy`", "Docs": "https://spacy.io/"},
            {"Name": "📊 OpenCV", "Command": "`pip install opencv-python`", "Docs": "https://docs.opencv.org/"},
            {"Name": "📦 PySpark", "Command": "`pip install pyspark`", "Docs": "https://spark.apache.org/docs/latest/api/python/"},
        ]
        
        for tool in tools:
            st.markdown(f"""
                <div class="tool-card">
                    <h4>{tool['Name']}</h4>
                    <p><strong>Install Command:</strong> {tool['Command']}</p>
                    <a href="{tool['Docs']}" target="_blank">
                        <button>📚 Documentation</button>
                    </a>
                    {"<a href='" + tool['Command'].split('[')[1].split(']')[0] + "' target='_blank'><button>⬇️ Install</button></a>" if "Download from" in tool['Command'] else ""}
                </div>
            """, unsafe_allow_html=True)

    # Resource Hub Section
    with st.expander("📂 Resource Hub", expanded=False):
        drive_url = "https://drive.google.com/drive/folders/10D1tFIyslQPaLr9RH2urxDSA81MTjtGM"
        st.markdown(
            f"""
            <div style="text-align: center; padding: 2rem;">
                <a href="{drive_url}" target="_blank" style="text-decoration:none;">
                    <button style="background-color:#2196F3; color:white; padding:1rem 2rem; 
                            border:none; border-radius:5px; cursor:pointer; font-size: 1.1rem;">
                        🌐 Access All Resources (Cours, TP, TD)
                    </button>
                </a>
            </div>
            """,
            unsafe_allow_html=True,
        )

elif selected == "Roadmap":
    st.title("📍 Learning Roadmap")

    # Add custom CSS for animations and effects
    st.markdown(
        """
        <style>
        /* Button hover and click effects */
        .topic-button {
            background-color: rgba(45, 106, 79, 0.8);
            color: white;
            border-radius: 8px;
            padding: 1rem;
            margin: 0.5rem 0;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease;
            cursor: pointer;
            text-align: center;
            font-size: 1.2rem;
            font-weight: bold;
            display: block;
            width: 100%;
        }
        .topic-button:hover {
            background-color: rgba(64, 145, 108, 0.8);
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.5);
            transform: translateY(-2px);
        }
        .topic-button:active {
            transform: translateY(0);
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.3);
        }

        /* Subtopic animation */
        .subtopic-container {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
            animation: fadeIn 0.5s ease-in-out;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        /* Resource buttons */
        .resource-button {
            background-color: #2196F3;
            color: white;
            padding: 0.5rem 1rem;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            font-size: 1rem;
            margin: 0.2rem;
            transition: all 0.3s ease;
        }
        .resource-button:hover {
            background-color: #1e88e5;
            transform: scale(1.05);
        }
        .resource-button.youtube {
            background-color: #FF0000;
        }
        .resource-button.youtube:hover {
            background-color: #cc0000;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    roadmap_topics = {
        "Python Fundamentals": {
            "Basic Concepts": {
                "Docs": "https://docs.python.org/3/tutorial/index.html",
                "YouTube": "https://www.youtube.com/watch?v=kqtD5dpn9C8",
                "Description": "Learn the basics of Python programming, including variables, data types, and control flow."
            },
            "OOP": {
                "Docs": "https://docs.python.org/3/tutorial/classes.html",
                "YouTube": "https://www.youtube.com/watch?v=JeznW_7DlB0",
                "Description": "Understand Object-Oriented Programming (OOP) concepts like classes, objects, inheritance, and polymorphism."
            },
            "Advanced Topics": {
                "Docs": "https://docs.python.org/3/tutorial/index.html",
                "YouTube": "https://www.youtube.com/watch?v=HGOBQPFzWKo",
                "Description": "Explore advanced Python topics such as decorators, generators, and context managers."
            }
        },
        "Data Science Basics": {
            "Data Manipulation": {
                "Docs": "https://pandas.pydata.org/docs/",
                "YouTube": "https://www.youtube.com/watch?v=vmEHCJofslg",
                "Description": "Master data manipulation techniques using Pandas, including data cleaning and transformation."
            },
            "Data Visualization": {
                "Docs": "https://matplotlib.org/stable/contents.html",
                "YouTube": "https://www.youtube.com/watch?v=UO98lJQ3QGI",
                "Description": "Learn to create visualizations using Matplotlib, Seaborn, and Plotly."
            },
            "Statistics": {
                "Docs": "https://docs.scipy.org/doc/scipy/reference/stats.html",
                "YouTube": "https://www.youtube.com/watch?v=xxpc-HPKN28",
                "Description": "Understand statistical concepts like descriptive stats, inferential stats, and probability."
            }
        },
        "Machine Learning": {
            "Supervised Learning": {
                "Docs": "https://scikit-learn.org/stable/supervised_learning.html",
                "YouTube": "https://www.youtube.com/watch?v=7eh4d6sabA0",
                "Description": "Learn supervised learning techniques such as regression, classification, and model evaluation."
            },
            "Unsupervised Learning": {
                "Docs": "https://scikit-learn.org/stable/unsupervised_learning.html",
                "YouTube": "https://www.youtube.com/watch?v=8oYISfMy3kQ",
                "Description": "Explore unsupervised learning methods like clustering and dimensionality reduction."
            },
            "Deep Learning": {
                "Docs": "https://www.tensorflow.org/tutorials",
                "YouTube": "https://www.youtube.com/watch?v=6_2hzRopPbQ",
                "Description": "Dive into deep learning with neural networks, CNNs, and RNNs using TensorFlow and PyTorch."
            }
        }
    }

    # Initialize session state for selected topic
    if "selected_topic" not in st.session_state:
        st.session_state.selected_topic = None

    # Display topics as interactive buttons
    for topic in roadmap_topics.keys():
        if st.button(f"🎯 {topic}", key=f"button_{topic}"):
            st.session_state.selected_topic = topic

    # Display subtopics if a topic is selected
    if st.session_state.selected_topic:
        st.markdown(f"### 🎯 {st.session_state.selected_topic}")
        st.markdown("---")  # Divider

        subtopics = roadmap_topics[st.session_state.selected_topic]
        for category, resources in subtopics.items():
            st.markdown(
                f"""
                <div class="subtopic-container">
                    <h4>{category}</h4>
                    <p style='color: #ddd;'>{resources['Description']}</p>
                    <a href="{resources['Docs']}" target="_blank">
                        <button class="resource-button">📚 Documentation</button>
                    </a>
                    <a href="{resources['YouTube']}" target="_blank">
                        <button class="resource-button youtube">▶️ YouTube Tutorial</button>
                    </a>
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.markdown("---")  # Divider

elif selected == "Chat":
    # Function to encode image to base64
    def get_base64_of_image(image_path):
        with open(image_path, "rb") as img_file:
            return base64.b64encode(img_file.read()).decode()

    # Add custom CSS for chat interface
    st.markdown(
        """
        <style>
        /* Chat container styling */
        .chat-container {
            background: rgba(255, 255, 255, 0.1);
            backdrop-filter: blur(10px);
            border-radius: 15px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 1.5rem;
            margin: 1rem 0;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.5);
        }
        /* User message styling */
        .user-message {
            background-color: rgba(45, 106, 79, 0.8);
            color: white;
            border-radius: 10px;
            padding: 0.75rem 1rem;
            margin: 0.5rem 0;
            max-width: 70%;
            align-self: flex-end;
            animation: slideInRight 0.3s ease-in-out;
        }
        /* Assistant message styling */
        .assistant-message {
            background-color: rgba(31, 31, 31, 0.8);
            color: white;
            border-radius: 10px;
            padding: 0.75rem 1rem;
            margin: 0.5rem 0;
            max-width: 70%;
            align-self: flex-start;
            animation: slideInLeft 0.3s ease-in-out;
        }
        /* Animations */
        @keyframes slideInRight {
            from { transform: translateX(20px); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        @keyframes slideInLeft {
            from { transform: translateX(-20px); opacity: 0; }
            to { transform: translateX(0); opacity: 1; }
        }
        /* Chat input styling */
        .stTextInput > div > div > input {
            background-color: rgba(31, 31, 31, 0.8) !important;
            color: white !important;
            padding: 0.75rem 1rem !important;
            border-radius: 25px !important;
            border: 2px solid #2196F3 !important;
        }
        /* Footer styling */
        .footer {
            text-align: center;
            padding: 1rem;
            margin-top: 2rem;
            font-size: 0.9rem;
            color: #ddd;
        }
        /* Header logo styling */
        .header-logo {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 2rem;
        }
        .header-logo img {
            width: 150px;
            height: auto;
            margin-right: 15px;
        }
        .header-title {
            font-size: 2.5rem;
            font-weight: bold;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
        }
        /* Creative symbol styling */
        .creative-symbol {
            font-size: 3rem;
            text-align: center;
            margin-bottom: 1rem;
            animation: float 3s ease-in-out infinite;
        }
        @keyframes float {
            0%, 100% { transform: translateY(0); }
            50% { transform: translateY(-10px); }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Display the logo and creative symbol at the top
    st.markdown(
        f"""
        <div class="header-logo">
            <img src="data:image/png;base64,{get_base64_of_image("un.png")}" alt="University Logo">
            <span class="header-title">AI Mentor</span>
        </div>
        <div class="creative-symbol">
            🤖✨
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("Ask me anything about your courses, study roadmap, or tools!")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(
                f"""
                <div class="{'user-message' if message['role'] == 'user' else 'assistant-message'}">
                    {message['content']}
                </div>
                """,
                unsafe_allow_html=True,
            )

    if api_key := api_key1:
        gen_ai.configure(api_key=api_key)
        model = gen_ai.GenerativeModel("gemini-pro")

        if prompt := st.chat_input("Ask a question..."):
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(
                    f"""
                    <div class="user-message">
                        {prompt}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

            with st.chat_message("assistant"):
                response_placeholder = st.empty()
                full_response = ""
                response = model.generate_content(prompt, stream=True)

                for chunk in response:
                    full_response += chunk.text
                    response_placeholder.markdown(
                        f"""
                        <div class="assistant-message">
                            {full_response + "▌"}
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                response_placeholder.markdown(
                    f"""
                    <div class="assistant-message">
                        {full_response}
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            st.session_state.messages.append({"role": "assistant", "content": full_response})

    # Footer
    st.markdown(
        """
        <div class="footer">
            <p>Made by <strong>IMAD EL KHELYFY</strong>, a passionate SDIA student at FS Meknes 🚀</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
