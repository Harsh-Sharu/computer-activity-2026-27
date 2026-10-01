import streamlit as st
import pandas as pd

# Set broad modern display mode
st.set_page_config(
    page_title="Incredible India: State & Cuisine Almanac",
    page_icon="🇮🇳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Navigation Structure
st.sidebar.title("🗺️ Cultural Index")
st.sidebar.caption("Indian States Exploration Guide")

state_selection = st.sidebar.radio(
    "Select a State to Explore:",
    [
        "0. Comprehensive Tourism Abstract",
        "1. Rajasthan: Land of Kings",
        "2. Kerala: God's Own Country",
        "3. Maharashtra: The Gateway of India",
        "4. Punjab: The Granary of India",
        "5. West Bengal: The Cultural Capital"
    ]
)

# ----------------------------------------------------------------------------------
# MODULE 0: COMPREHENSIVE ABSTRACT
# ----------------------------------------------------------------------------------
if state_selection == "0. Comprehensive Tourism Abstract":
    st.title("🇮🇳 Incredible India: State & Cuisine Almanac")
    st.subheader("An Informative Cultural Compendium covering Diverse Geographies")
    st.info("📊 Digital Archive Notice: This digital guide contains deeply detailed documentation structured with horizontal tabs and high-resolution graphical assets.")
    
    # Creating horizontal tabs at the top
    t1, t2 = st.tabs(["🏛️ Overview Hub", "📊 Regional Analytics"])
    
    # Content for Tab 1
    t1.markdown("### The Culinary and Geographical Landscape")
    t1.write("India's cultural layout is incredibly diverse, shaped by distinct climates, historical trajectories, and deep local traditions across its regions. This encyclopedia isolates five major Indian states, exploring their unique geography, historical markers, architectural wonders, and signature multi-course cuisines.")
    t1.markdown("### Intentional Core Focus Areas")
    t1.write("1. **Regional Geography:** Exploring climates ranging from the arid Thar Desert to the lush tropical Western Ghats backwaters.")
    t1.write("2. **Historical Milestones:** Tracking legacies from independent princely kingdoms to early maritime colonial ports.")
    t1.write("3. **Culinary Architecture:** Analyzing unique flavor styles, signature crop harvests, native spice profiles, and distinct cooking methods.")
    t1.subheader("🖼️ Cultural Overview Map")
    t1.image("https://unsplash.com", caption="Figure 0.1: Iconic Monuments of India Heritage", use_container_width=True)

    # Content for Tab 2
    t2.markdown("### Core Regional Specifications")
    t2.write("Below is the structural matrix tracking the administrative parameters of the selected target regions.")
    metrics_table = {
        "State Region": ["Rajasthan", "Kerala", "Maharashtra", "Punjab", "West Bengal"],
        "Primary Language": ["Hindi / Marwari", "Malayalam", "Marathi", "Punjabi", "Bengali"],
        "Signature Spice Base": ["Mathania Chili", "Black Pepper / Cardamom", "Godha Masala", "Kasoori Methi", "Panch Phoron"],
        "Harvest Staple": ["Bajra / Wheat", "Monsoon Rice", "Jowar / Millets", "Premium Wheat", "Freshwater Paddy"]
    }
    t2.table(pd.DataFrame(metrics_table))

# ----------------------------------------------------------------------------------
# MODULE 1: RAJASTHAN
# ----------------------------------------------------------------------------------
elif state_selection == "1. Rajasthan: Land of Kings":
    st.title("👑 Chapter 1: Rajasthan — The Land of Kings")
    
    t1, t2 = st.tabs(["🏛️ History & Architecture", "🍲 Culinary Heritage & Images"])
    
    # Content for Tab 1
    t1.markdown("### 1.1 Architectural and Historical Legacies")
    t1.write("Rajasthan, located in northwestern India, is defined by the vast Thar Desert and the ancient Aravalli mountain range. It is famous around the world for its grand historical architecture, featuring massive sandstone citadels, ornate royal palaces, and beautifully decorated stepwells.")
    t1.write("The capital city, Jaipur (The Pink City), alongside Jodhpur (The Blue City) and Udaipur (The City of Lakes), forms the golden triangle of heritage infrastructure that defined medieval princely rule.")
    t1.subheader("🖼️ Desert Citadel Architecture")
    t1.image("https://unsplash.com", caption="Figure 1.1: Majestic Sandstone Palaces of Rajasthan", use_container_width=True)

    # Content for Tab 2
    t2.markdown("### 1.2 Signature Desert Cuisine Profiles")
    t2.write("Because the hot, dry desert climate severely limits fresh water and green vegetables, traditional Rajasthani cooking adapted in fascinating ways. Chefs rely heavily on robust, long-lasting ingredients like milk, clarified butter (ghee), buttermilk, lentils, and unique wild desert beans.")
    t2.write("**Iconic Dish — Dal Baati Churma:** The ultimate local meal features dense, round wheat balls cooked over open fire pits (*baati*), dipped in rich ghee, served with a spiced multi-lentil stew (*dal*), and paired with a sweet, crumbled wheat dessert (*churma*).")
    t2.subheader("🖼️ Traditional Rajasthani Feast Platter")
    t2.image("https://unsplash.com", caption="Figure 1.2: Traditional Rich Rajasthani Culinary Service", use_container_width=True)

# ----------------------------------------------------------------------------------
# MODULE 2: KERALA
# ----------------------------------------------------------------------------------
elif state_selection == "2. Kerala: God's Own Country":
    st.title("🌴 Chapter 2: Kerala — God's Own Country")
    
    t1, t2 = st.tabs(["🌴 Geography & Environment", "🍛 Coastal Cuisine & Images"])
    
    # Content for Tab 1
    t1.markdown("### 2.1 Tropical Geographies & Coastal Ecosystems")
    t1.write("Kerala rests along the southwestern Malabar Coast of India. It features a stunning tropical landscape of winding interconnected backwaters, lush high-altitude tea plantations, and dense palm trees that run right down to the ocean shore.")
    t1.write("Its unique marine geography enabled historical spice trade partnerships with ancient Rome, Greece, and Middle Eastern empires.")
    t1.subheader("🖼️ Tropical Water Networks")
    t1.image("https://unsplash.com", caption="Figure 2.1: Serene Coastal Ecosystems and Backwaters of Kerala", use_container_width=True)

    # Content for Tab 2
    t2.markdown("### 2.2 Coastal Culinary Frameworks")
    t2.write("Kerala's cooking style is driven by its massive natural harvests of fresh coconut and aromatic spices like black pepper, cardamom, and cinnamon. Rice serves as the main food staple across the region.")
    t2.write("**Iconic Feast — The Kerala Sadya:** A magnificent, all-vegetarian banquet served traditionally on a large, fresh green banana leaf. It includes up to 28 distinct small dishes, featuring items like *Avial* (a thick mixed vegetable stew with coconut paste), *Olan*, and sweet *Payasam* puddings.")
    t2.subheader("🖼️ The Grand Banana Leaf Feast")
    t2.image("https://unsplash.com", caption="Figure 2.2: Authentic Southern Spice and Rice Formations", use_container_width=True)

# ----------------------------------------------------------------------------------
# MODULE 3: MAHARASHTRA
# ----------------------------------------------------------------------------------
elif state_selection == "3. Maharashtra: The Gateway of India":
    st.title("🦁 Chapter 3: Maharashtra — The Gateway of India")
    
    t1, t2 = st.tabs(["🌆 Regional Topography", "🌶️ Dynamic Cuisine & Images"])
    
    # Content for Tab 1
    t1.markdown("### 3.1 Industrial Valleys & High-Plateau History")
    t1.write("Maharashtra stretches across a massive part of central-western India, spanning from the bustling coastline of Mumbai up through the vast Deccan plateau. Its history features legendary stories of fortified mountain strongholds built by the historic Maratha Empire.")
    t1.subheader("🖼️ Commercial Waterfront Landmarks")
    t1.image("https://unsplash.com", caption="Figure 3.1: Mumbai Coastline Infrastructure and Gateway Structures", use_container_width=True)

    # Content for Tab 2
    t2.markdown("### 3.2 Dynamic Street Food and Spiced Curries")
    t2.write("The local food changes dramatically from region to region. The Konkan coast features fiery coconut-seafood curries, while the interior plateau uses intense, slow-simmered peanut and chili spice mixes.")
    t2.write("**Iconic Staple — Misal Pav:** A widely popular, high-spice breakfast dish made of a rich curry of sprouted moth beans (*misal*). The curry is topped with crispy chickpea noodles (*farsan*), fresh chopped onions, and squeezed lime juice, all scooped up using soft, buttered bread rolls (*pav*).")
    t2.subheader("🖼️ Elite Local Street Delicacies")
    t2.image("https://unsplash.com", caption="Figure 3.2: Popular Savory Delicacies of Mumbai Markets", use_container_width=True)

# ----------------------------------------------------------------------------------
# MODULE 4: PUNJAB
# ----------------------------------------------------------------------------------
elif state_selection == "4. Punjab: The Granary of India":
    st.title("🌾 Chapter 4: Punjab — The Granary of India")
    
    t1, t2 = st.tabs(["🚜 Agriculture & Fields", "🧈 Heavy Dairy Cuisine & Images"])
    
    # Content for Tab 1
    t1.markdown("### 4.1 Alluvial River Basins & Agricultural Hubs")
