import streamlit as st
import pandas as pd

# Set layout constraints with sidebar completely hidden by default
st.set_page_config(
    page_title="Incredible India: State & Cuisine Almanac",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ----------------------------------------------------------------------------------
# CHROMIUM STYLE CSS OVERRIDES (Chrome Tabs Styled for Global Navigation)
# ----------------------------------------------------------------------------------
st.markdown("""
<style>
    /* Absolute page reset to a dark slate-carbon aesthetic */
    .stApp {
        background: linear-gradient(135deg, #0d0e15 0%, #161925 100%) !important;
        color: #e2e8f0 !important;
    }
    
    /* Completely hide the sidebar navigation element if it tries to render */
    section[data-testid="stSidebar"] {
        display: none !important;
    }
    
    /* Chrome-Style Horizontal Tab Bar Styling Override */
    div[data-testid="stTabs"] {
        background-color: #1a1d2e !important;
        padding: 10px 10px 0px 10px !important;
        border-radius: 12px 12px 0 0 !important;
        border: 1px solid #2d3250 !important;
        border-bottom: none !important;
        box-shadow: 0px -4px 20px rgba(0, 242, 254, 0.05) !important;
        margin-bottom: 20px !important;
    }
    
    /* Individual Chrome Tabs */
    div[data-testid="stTabs"] button {
        background: #121424 !important;
        color: #8fa0dd !important;
        border: 1px solid #252945 !important;
        border-bottom: none !important;
        margin-right: 4px !important;
        padding: 12px 24px !important;
        font-weight: 600 !important;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
        font-size: 14px !important;
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
</style>
""", unsafe_allow_html=True)

st.title("🇮🇳 Incredible India: State & Cuisine Almanac")
st.caption("Global Navigation Array v11.0")

# Primary Top Navigation Tabs replacing the sidebar completely
state_tabs = st.tabs([
    "📂 0. Overview Abstract",
    "👑 1. Rajasthan",
    "🌴 2. Kerala",
    "🦁 3. Maharashtra",
    "🌾 4. Punjab",
    "🎨 5. West Bengal"
])

# ----------------------------------------------------------------------------------
# MAIN ROUTING BLOCKS INSIDE TOP TABS
# ----------------------------------------------------------------------------------

# 0. ABSTRACT REGION
with state_tabs[0]:
    st.subheader("An Informative Cultural Compendium covering Diverse Geographies")
    st.info("📊 Digital Archive Notice: This digital guide contains deeply detailed documentation structured entirely through clean top-level horizontal dashboard tabs.")
    
    sub_t1, sub_t2 = st.tabs(["🏛️ Overview Hub", "📊 Regional Analytics"])
    sub_t1.markdown("### The Culinary and Geographical Landscape")
    sub_t1.write("India's cultural layout is incredibly diverse, shaped by distinct climates, historical trajectories, and deep local traditions across its regions. This encyclopedia isolates five major Indian states, exploring their unique geography, historical markers, architectural wonders, and signature multi-course cuisines.")
    sub_t1.image("https://unsplash.com", caption="Figure 0.1: Iconic Monuments of India Heritage", use_container_width=True)

    sub_t2.markdown("### Core Regional Specifications Matrix")
    metrics_table = {
        "State Region": ["Rajasthan", "Kerala", "Maharashtra", "Punjab", "West Bengal"],
        "Primary Language": ["Hindi / Marwari", "Malayalam", "Marathi", "Punjabi", "Bengali"],
        "Signature Spice Base": ["Mathania Chili", "Black Pepper", "Godha Masala", "Kasoori Methi", "Panch Phoron"],
        "Harvest Staple": ["Bajra / Wheat", "Monsoon Rice", "Jowar / Millets", "Premium Wheat", "Freshwater Paddy"]
    }
    sub_t2.table(pd.DataFrame(metrics_table))

# 1. RAJASTHAN REGION
with state_tabs[1]:
    st.subheader("Chapter 1: Rajasthan — The Land of Kings")
    sub_t1, sub_t2 = st.tabs(["🏛️ History & Architecture", "🍲 Culinary Heritage & Images"])
    
    sub_t1.markdown("### 1.1 Architectural and Historical Legacies")
    sub_t1.write("Rajasthan, located in northwestern India, is defined by the vast Thar Desert and the ancient Aravalli mountain range. It features massive sandstone citadels, ornate royal palaces, and beautifully decorated stepwells.")
    sub_t1.image("https://unsplash.com", caption="Figure 1.1: Majestic Sandstone Palaces of Rajasthan", use_container_width=True)

    sub_t2.markdown("### 1.2 Signature Desert Cuisine Profiles")
    sub_t2.write("Because the hot, dry desert climate severely limits fresh water and green vegetables, traditional Rajasthani cooking relies heavily on milk, clarified butter (ghee), buttermilk, lentils, and unique wild desert beans.")
    sub_t2.write("**Iconic Dish — Dal Baati Churma:** Dense wheat balls cooked over open fire pits (*baati*), dipped in rich ghee, served with a spiced multi-lentil stew (*dal*), and paired with a sweet wheat dessert (*churma*).")
    sub_t2.image("https://unsplash.com", caption="Figure 1.2: Traditional Rich Rajasthani Culinary Service", use_container_width=True)

# 2. KERALA REGION
with state_tabs[2]:
    st.subheader("Chapter 2: Kerala — God's Own Country")
    sub_t1, sub_t2 = st.tabs(["🌴 Geography & Environment", "🍛 Coastal Cuisine & Images"])
    
    sub_t1.markdown("### 2.1 Tropical Geographies & Coastal Ecosystems")
    sub_t1.write("Kerala rests along the southwestern Malabar Coast of India. It features a stunning tropical landscape of winding interconnected backwaters, lush high-altitude tea plantations, and dense palm trees.")
    sub_t1.image("https://unsplash.com", caption="Figure 2.1: Serene Coastal Ecosystems and Backwaters of Kerala", use_container_width=True)

    sub_t2.markdown("### 2.2 Coastal Culinary Frameworks")
    sub_t2.write("Kerala's cooking style is driven by its massive natural harvests of fresh coconut and aromatic spices like black pepper, cardamom, and cinnamon. Rice serves as the main food staple across the region.")
    sub_t2.write("**Iconic Feast — The Kerala Sadya:** A magnificent, all-vegetarian banquet served traditionally on a large, fresh green banana leaf with up to 28 distinct small dishes.")
    sub_t2.image("https://unsplash.com", caption="Figure 2.2: Authentic Southern Spice and Rice Formations", use_container_width=True)

# 3. MAHARASHTRA REGION
with state_tabs[3]:
    st.subheader("Chapter 3: Maharashtra — The Gateway of India")
    sub_t1, sub_t2 = st.tabs(["🌆 Regional Topography", "🌶️ Dynamic Cuisine & Images"])
    
    sub_t1.markdown("### 3.1 Industrial Valleys & High-Plateau History")
    sub_t1.write("Maharashtra stretches across a massive part of central-western India, spanning from the bustling coastline of Mumbai up through the vast Deccan plateau.")
    sub_t1.image("https://unsplash.com", caption="Figure 3.1: Mumbai Coastline Infrastructure and Gateway Structures", use_container_width=True)

    sub_t2.markdown("### 3.2 Dynamic Street Food and Spiced Curries")
    sub_t2.write("The Konkan coast features fiery coconut-seafood curries, while the interior plateau uses intense, slow-simmered peanut and chili spice mixes.")
    sub_t2.write("**Iconic Staple — Misal Pav:** A widely popular, high-spice breakfast dish made of a rich curry of sprouted moth beans (*misal*) topped with crispy farsan noodles.")
    sub_t2.image("https://unsplash.com", caption="Figure 3.2: Popular Savory Delicacies of Mumbai Markets", use_container_width=True)

# 4. PUNJAB REGION
with state_tabs[4]:
    st.subheader("Chapter 4: Punjab — The Granary of India")
    sub_t1, sub_t2 = st.tabs(["🚜 Agriculture & Fields", "🧈 Heavy Dairy Cuisine & Images"])
    
    sub_t1.markdown("### 4.1 Alluvial River Basins & Agricultural Hubs")
    sub_t1.write("Punjab sits in northwestern India and is famously known as the land of five rivers. Its plains make it the primary agricultural heartland of the country.")
    sub_t1.image("https://unsplash.com", caption="Figure 4.1: The Golden Temple Complex of Amritsar", use_container_width=True)

    sub_t2.markdown("### 4.2 Tandoori Roasts & Rich Dairy Delicacies")
    sub_t2.write("Punjabi cooking is celebrated for its bold, hearty flavors, heavy use of fresh butter and cream, and traditional clay-oven (*tandoor*) baking methods.")
    sub_t2.write("**Iconic Dish — Sarson Ka Saag & Makki Di Roti:** A classic winter staple made from slow-simmered mustard greens (*saag*) served hot with corn flatbreads.")
    sub_t2.image("unsplash.com", caption="Figure 4.2: Robust Rich Spiced Curries and Crafted Flatbreads", use_container_width=True)
    with state_tabs[5]:
st.subheader("Chapter 5: West Bengal — The Cultural Capital")
sub_t1, sub_t2 = st.tabs(["🎨 Literary & Art Foundations", "🐟 Sea Gastronomy & Images"])
sub_t1.markdown("### 5.1 The Delta Plains & Artistic Centers")
sub_t1.write("West Bengal extends from the peaks of the high Himalayas down to the vast delta wetlands. It is known across India as a historic center for philosophy, classic literature, and fine arts.")
sub_t1.image("unsplash.com", caption="Figure 5.1: Historical Architecture and Bridges of West Bengal", use_container_width=True)
sub_t2.markdown("### 5.2 Delicate Seafood Curries & Celebrated Confections")
sub_t2.write("Bengali food focuses heavily on the perfect pairing of freshwater fish and rice. Most dishes are cooked in pungent mustard oil and use the classic five-spice blend Panch Phoron.")
sub_t2.write("The region is also famous worldwide for its delicate milk-based sweets like Rasgulla, Sandesh, and Mishti Doi.")
sub_t2.image("unsplash.com", caption="Figure 5.2: Traditional Indian Gourmet Curry Combinations", use_container_width=True)
