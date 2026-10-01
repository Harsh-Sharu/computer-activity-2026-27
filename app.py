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
    st.info("📊 Digital Archive Notice: This digital guide contains deeply detailed documentation intentionally structured to meet dense, multi-page layout requirements, complete with structured column systems and graphic assets.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### The Culinary and Geographical Landscape")
        st.write("India's cultural layout is incredibly diverse, shaped by distinct climates, historical trajectories, and deep local traditions across its regions. This encyclopedia isolates five major Indian states, exploring their unique geography, historical markers, architectural wonders, and signature multi-course cuisines.")
        st.markdown("### Intentional Core Focus Areas")
        st.write("1. **Regional Geography:** Exploring climates ranging from the arid Thar Desert to the lush tropical Western Ghats backwaters.")
        st.write("2. **Historical Milestones:** Tracking legacies from independent princely kingdoms to early maritime colonial ports.")
        st.write("3. **Culinary Architecture:** Analyzing unique flavor styles, signature crop harvests, native spice profiles, and distinct cooking methods.")
        st.write("4. **Iconic Staples:** Highlighting essential local food variations, like slow-cooked flatbreads, slow-simmered curries, and unique costal fish dishes.")
    with col2:
        st.subheader("🖼️ Cultural Overview Map")
        st.image("https://placehold.co", caption="Figure 0.1: Conceptual Map of India's Dynamic Cultural Zones", use_container_width=True)

# ----------------------------------------------------------------------------------
# MODULE 1: RAJASTHAN
# ----------------------------------------------------------------------------------
elif state_selection == "1. Rajasthan: Land of Kings":
    st.title("👑 Chapter 1: Rajasthan — The Land of Kings")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 1.1 Architectural and Historical Legacies")
        st.write("Rajasthan, located in northwestern India, is defined by the vast Thar Desert and the ancient Aravalli mountain range. It is famous around the world for its grand historical architecture, featuring massive sandstone citadels, ornate royal palaces, and beautifully decorated stepwells.")
        st.markdown("### 1.2 Signature Desert Cuisine Profiles")
        st.write("Because the hot, dry desert climate severely limits fresh water and green vegetables, traditional Rajasthani cooking adapted in fascinating ways. Chefs rely heavily on robust, long-lasting ingredients like milk, clarified butter (ghee), buttermilk, lentils, and unique wild desert beans.")
        st.write("**Iconic Dish — Dal Baati Churma:** The ultimate local meal features dense, round wheat balls cooked over open fire pits (*baati*), dipped in rich ghee, served with a spiced multi-lentil stew (*dal*), and paired with a sweet, crumbled wheat dessert (*churma*).")
    with col2:
        st.subheader("🖼️ Traditional Rajasthani Thali")
        st.image("https://placehold.co", caption="Figure 1.1: Multi-course traditional desert meal presentation", use_container_width=True)

# ----------------------------------------------------------------------------------
# MODULE 2: KERALA
# ----------------------------------------------------------------------------------
elif state_selection == "2. Kerala: God's Own Country":
    st.title("🌴 Chapter 2: Kerala — God's Own Country")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 2.1 Tropical Geographies & Coastal Ecosystems")
        st.write("Kerala rests along the southwestern Malabar Coast of India. It features a stunning tropical landscape of winding interconnected backwaters, lush high-altitude tea plantations, and dense palm trees that run right down to the ocean shore.")
        st.markdown("### 2.2 Coastal Culinary Frameworks")
        st.write("Kerala's cooking style is driven by its massive natural harvests of fresh coconut and aromatic spices like black pepper, cardamom, and cinnamon. Rice serves as the main food staple across the region.")
        st.write("**Iconic Feast — The Kerala Sadya:** A magnificent, all-vegetarian banquet served traditionally on a large, fresh green banana leaf. It includes up to 28 distinct small dishes, featuring items like Avial (a thick mixed vegetable stew with coconut paste), Olan, and sweet Payasam puddings.")
    with col2:
        st.subheader("🖼️ The Traditional Sadya Banquet")
        st.image("https://placehold.co", caption="Figure 2.1: Multi-course vegetarian feast served traditionally on a banana leaf", use_container_width=True)

# ----------------------------------------------------------------------------------
# MODULE 3: MAHARASHTRA
# ----------------------------------------------------------------------------------
elif state_selection == "3. Maharashtra: The Gateway of India":
    st.title("🦁 Chapter 3: Maharashtra — The Gateway of India")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 3.1 Industrial Valleys & High-Plateau History")
        st.write("Maharashtra stretches across a massive part of central-western India, spanning from the bustling coastline of Mumbai up through the vast Deccan plateau. Its history features legendary stories of fortified mountain strongholds built by the historic Maratha Empire.")
        st.markdown("### 3.2 Dynamic Street Food and Spiced Curries")
        st.write("The local food changes dramatically from region to region. The Konkan coast features fiery coconut-seafood curries, while the interior plateau uses intense, slow-simmered peanut and chili spice mixes.")
        st.write("**Iconic Staple — Misal Pav:** A widely popular, high-spice breakfast dish made of a rich curry of sprouted moth beans (*misal*). The curry is topped with crispy chickpea noodles (*farsan*), fresh chopped onions, and squeezed lime juice, all scooped up using soft, buttered bread rolls (*pav*).")
    with col2:
        st.subheader("🖼️ Maharashtrian Spice Assembly")
        st.image("https://placehold.co", caption="Figure 3.1: Spiced bean sprouts curry paired with local leavened bread", use_container_width=True)

# ----------------------------------------------------------------------------------
# MODULE 4: PUNJAB
# ----------------------------------------------------------------------------------
elif state_selection == "4. Punjab: The Granary of India":
    st.title("🌾 Chapter 4: Punjab — The Granary of India")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 4.1 Alluvial River Basins & Agricultural Hubs")
        st.write("Punjab sits in northwestern India and is famously known as the land of five rivers. Its incredibly fertile river plains make it the primary agricultural heartland of the country, responsible for massive yearly harvests of wheat, sugarcane, and fresh dairy products.")
        st.markdown("### 4.2 Tandoori Roasts & Rich Dairy Delicacies")
        st.write("Punjabi cooking is celebrated for its bold, hearty flavors, heavy use of fresh butter and cream, and traditional clay-oven (*tandoor*) baking methods.")
        st.write("**Iconic Dish — Sarson Ka Saag & Makki Di Roti:** A classic winter staple made from slow-simmered mustard greens (*saag*) cooked down with warming winter spices. It is served hot with a big dollop of fresh white butter, and paired with flatbreads made from yellow corn flour (*makki di roti*).")
    with col2:
        st.subheader("🖼️ Authentic Punjabi Farm Platter")
        st.image("https://placehold.co", caption="Figure 4.1: Slow-cooked winter mustard greens served with local corn flatbreads", use_container_width=True)

# ----------------------------------------------------------------------------------
# MODULE 5: WEST BENGAL
# ----------------------------------------------------------------------------------
elif state_selection == "5. West Bengal: The Cultural Capital":
    st.title("🎨 Chapter 5: West Bengal — The Cultural Capital")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 5.1 The Delta Plains & Artistic Centers")
        st.write("West Bengal extends from the peaks of the high Himalayas down to the vast delta wetlands of the Bay of Bengal. It is known across India as a historic center for philosophy, classic literature, fine arts, and grand festival celebrations.")
        st.markdown("### 5.2 Delicate Seafood Curries & Celebrated Confections")
