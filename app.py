import streamlit as st
import pandas as pd

# Set layout constraints
st.set_page_config(
    page_title="Incredible India: Ultimate Cyber Almanac",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ----------------------------------------------------------------------------------
# MAXIMUM OVERKILL CSS INJECTION (Chrome Tabs & Neon Cyber Color Theme)
# ----------------------------------------------------------------------------------
st.markdown("""
<style>
    /* Absolute page reset to a dark slate-carbon aesthetic */
    .stApp {
        background: linear-gradient(135deg, #0d0e15 0%, #161925 100%) !important;
        color: #e2e8f0 !important;
    }
    
    /* Chrome-Style Horizontal Tab Bar Styling Override */
    div[data-testid="stTabs"] {
        background-color: #1a1d2e !important;
        padding: 10px 10px 0px 10px !important;
        border-radius: 12px 12px 0 0 !important;
        border: 1px solid #2d3250 !important;
        border-bottom: none !important;
        box-shadow: 0px -4px 20px rgba(0, 242, 254, 0.05) !important;
    }
    
    /* Individual Chrome Tabs */
    div[data-testid="stTabs"] button {
        background: #121424 !important;
        color: #8fa0dd !important;
        border: 1px solid #252945 !important;
        border-bottom: none !important;
        margin-right: 4px !important;
        padding: 12px 30px !important;
        font-weight: 600 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        font-size: 15px !important;
        /* Sleek trapezoid angled tab shape similar to premium browsers */
        border-radius: 10px 10px 0px 0px !important;
        transition: all 0.25s ease-in-out !important;
        position: relative !important;
    }
    
    /* Chrome Tab Hover State */
    div[data-testid="stTabs"] button:hover {
        background: #22263f !important;
        color: #00f2fe !important;
        border-color: #3b4270 !important;
        transform: translateY(-2px) !important;
    }
    
    /* Chrome Active Selected Tab State */
    div[data-testid="stTabs"] button[aria-selected="true"] {
        background: linear-gradient(180deg, #1e2238 0%, #0d0e15 100%) !important;
        color: #00f2fe !important;
        border-color: #00f2fe !important;
        border-bottom: 2px solid #0d0e15 !important;
        font-weight: 700 !important;
        box-shadow: 0px -3px 10px rgba(0, 242, 254, 0.2) !important;
    }
    
    /* Active underline laser indicator */
    div[data-testid="stTabs"] button[aria-selected="true"]::after {
        content: '';
        position: absolute;
        bottom: 0;
        left: 0;
        right: 0;
        height: 3px;
        background: linear-gradient(90deg, #00f2fe, #4facfe) !important;
        border-radius: 3px 3px 0 0;
    }

    /* Sidebar Custom Dark Dressing */
    section[data-testid="stSidebar"] {
        background-color: #08090e !important;
        border-right: 1px solid #1e2238 !important;
    }

    /* Metric cards styling optimization */
    div[data-testid="stMetricValue"] {
        color: #00f2fe !important;
        font-family: monospace !important;
        font-weight: 700 !important;
    }
</style>
""", unsafe_allow_html=True)

# ----------------------------------------------------------------------------------
# APP CORE ROUTING ARCHITECTURE
# ----------------------------------------------------------------------------------
st.sidebar.title("⚡ Cyber Index v9.0")
st.sidebar.caption("Extreme Visual Overkill Matrix Enabled")

state_selection = st.sidebar.radio(
    "Select Target Grid Array:",
    [
        "0. Comprehensive Tourism Abstract",
        "1. Rajasthan: Land of Kings",
        "2. Kerala: God's Own Country",
        "3. Maharashtra: The Gateway of India",
        "4. Punjab: The Granary of India",
        "5. West Bengal: The Cultural Capital"
    ]
)

if state_selection == "0. Comprehensive Tourism Abstract":
    st.title("🇮🇳 Incredible India: State & Cuisine Almanac")
    st.info("🔥 STATUS: MAXIMUM VISUAL OVERKILL MODE STYLED VIA CUSTOM CHROMIUM HOOKS")
    
    t1, t2 = st.tabs(["🏛️ Overview Hub", "📊 System Analytics"])
    
    t1.markdown("### The Culinary and Geographical Landscape")
    t1.write("India's cultural layout is incredibly diverse, shaped by distinct climates, historical trajectories, and deep local traditions across its regions. This encyclopedia isolates five major Indian states, exploring their unique geography, historical markers, architectural wonders, and signature multi-course cuisines.")
    t1.image("https://unsplash.com", caption="Figure 0.1: Iconic Monuments of India Heritage", use_container_width=True)

    t2.markdown("### Core Regional Specifications Matrix")
    metrics_table = {
        "State Region": ["Rajasthan", "Kerala", "Maharashtra", "Punjab", "West Bengal"],
        "Primary Language": ["Hindi / Marwari", "Malayalam", "Marathi", "Punjabi", "Bengali"],
        "Signature Spice Base": ["Mathania Chili", "Black Pepper", "Godha Masala", "Kasoori Methi", "Panch Phoron"],
        "Harvest Staple": ["Bajra / Wheat", "Monsoon Rice", "Jowar / Millets", "Premium Wheat", "Freshwater Paddy"]
    }
    t2.table(pd.DataFrame(metrics_table))

elif state_selection == "1. Rajasthan: Land of Kings":
    st.title("👑 Chapter 1: Rajasthan — The Land of Kings")
    t1, t2 = st.tabs(["🏛️ History & Architecture", "🍲 Culinary Heritage & Images"])
    
    t1.markdown("### 1.1 Architectural and Historical Legacies")
    t1.write("Rajasthan, located in northwestern India, is defined by the vast Thar Desert and the ancient Aravalli mountain range. It features massive sandstone citadels, ornate royal palaces, and beautifully decorated stepwells.")
    t1.image("https://unsplash.com", caption="Figure 1.1: Majestic Sandstone Palaces of Rajasthan", use_container_width=True)

    t2.markdown("### 1.2 Signature Desert Cuisine Profiles")
    t2.write("Because the hot, dry desert climate severely limits fresh water and green vegetables, traditional Rajasthani cooking relies heavily on milk, clarified butter (ghee), buttermilk, lentils, and unique wild desert beans.")
    t2.write("**Iconic Dish — Dal Baati Churma:** Dense wheat balls cooked over open fire pits (*baati*), dipped in rich ghee, served with a spiced multi-lentil stew (*dal*), and paired with a sweet wheat dessert (*churma*).")
    t2.image("https://unsplash.com", caption="Figure 1.2: Traditional Rich Rajasthani Culinary Service", use_container_width=True)

elif state_selection == "2. Kerala: God's Own Country":
    st.title("🌴 Chapter 2: Kerala — God's Own Country")
    t1, t2 = st.tabs(["🌴 Geography & Environment", "🍛 Coastal Cuisine & Images"])
    
    t1.markdown("### 2.1 Tropical Geographies & Coastal Ecosystems")
    t1.write("Kerala rests along the southwestern Malabar Coast of India. It features a stunning tropical landscape of winding interconnected backwaters, lush high-altitude tea plantations, and dense palm trees.")
    t1.image("https://unsplash.com", caption="Figure 2.1: Serene Coastal Ecosystems and Backwaters of Kerala", use_container_width=True)

    t2.markdown("### 2.2 Coastal Culinary Frameworks")
    t2.write("Kerala's cooking style is driven by its massive natural harvests of fresh coconut and aromatic spices like black pepper, cardamom, and cinnamon. Rice serves as the main food staple across the region.")
    t2.write("**Iconic Feast — The Kerala Sadya:** A magnificent, all-vegetarian banquet served traditionally on a large, fresh green banana leaf with up to 28 distinct small dishes.")
    t2.image("https://unsplash.com", caption="Figure 2.2: Authentic Southern Spice and Rice Formations", use_container_width=True)

elif state_selection == "3. Maharashtra: The Gateway of India":
    st.title("🦁 Chapter 3: Maharashtra — The Gateway of India")
    t1, t2 = st.tabs(["🌆 Regional Topography", "🌶️ Dynamic Cuisine & Images"])
    
    t1.markdown("### 3.1 Industrial Valleys & High-Plateau History")
    t1.write("Maharashtra stretches across a massive part of central-western India, spanning from the bustling coastline of Mumbai up through the vast Deccan plateau.")
    t1.image("https://unsplash.com", caption="Figure 3.1: Mumbai Coastline Infrastructure and Gateway Structures", use_container_width=True)

    t2.markdown("### 3.2 Dynamic Street Food and Spiced Curries")
    t2.write("The Konkan coast features fiery coconut-seafood curries, while the interior plateau uses intense, slow-simmered peanut and chili spice mixes.")
    t2.write("**Iconic Staple — Misal Pav:** A widely popular, high-spice breakfast dish made of a rich curry of sprouted moth beans (*misal*) topped with crispy farsan noodles.")
    t2.image("https://unsplash.com", caption="Figure 3.2: Popular Savory Delicacies of Mumbai Markets", use_container_width=True)

elif state_selection == "4. Punjab: The Granary of India":
    st.title("🌾 Chapter 4: Punjab — The Granary of India")
    t1, t2 = st.tabs(["🚜 Agriculture & Fields", "🧈 Heavy Dairy Cuisine & Images"])
    
    t1.markdown("### 4.1 Alluvial River Basins & Agricultural Hubs")
    t1.write("Punjab sits in northwestern India and is famously known as the land of five rivers. Its plains make it the primary agricultural heartland of the country.")
