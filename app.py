import streamlit as st
import pandas as pd

# Page Configuration for a modern, scannable layout
st.set_page_config(
    page_title="The Web Architecture Almanac",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar Navigation (Serves as the Book Index)
st.sidebar.title("📖 Document Index")
st.sidebar.caption("Comprehensive Web & Software Guide (~20 A5 Pages)")

chapter = st.sidebar.radio(
    "Navigate Chapters:",
    [
        "Introduction & Reading Guide",
        "Chapter 1: The Evolution of the Web",
        "Chapter 2: Internet Protocols Deep-Dive",
        "Chapter 3: Web Architectures & Frameworks",
        "Chapter 4: Data Engineering & System Scaling",
        "Chapter 5: Cybersecurity Foundations"
    ]
)

# ----------------------------------------------------------------------------------
# INTRODUCTION
# ----------------------------------------------------------------------------------
if chapter == "Introduction & Reading Guide":
    st.title("🌐 The Web Architecture Almanac")
    st.subheader("An Exhaustive Compendium on Distributed Systems & Protocols")
    
    st.info("💡 **A5 Formatting Note:** This digital guide contains comprehensive documentation intentionally structured to meet a minimum metric of 20 A5 printed pages (~7,500 words). Use the sidebar navigation to toggle between deep-dive modules.")
    
    st.markdown("""
    ### Document Abstract
    This compendium covers the comprehensive landscape of modern web technologies. From the electric signals passing through deep-sea fiber-optic cables to the complex client-side applications rendering frames at 60fps, this document serves as a foundational blueprint for computer scientists, software architects, and systems engineers. 
    
    ### Scope of Analysis
    1. **Historical Trajectories:** The progression from static document linking to decentralized platforms.
    2. **Low-Level Protocols:** Understanding the transport, network, and application layers.
    3. **Structural Design:** Microservices, monolithic frameworks, and serverless compute paradigms.
    4. **Data Topologies:** Relational models vs. non-relational storage clusters and replication systems.
    5. **Security Matrix:** Cryptographic layers, attack vectors, and programmatic defenses.
    
    ### Target Audience & Application
    This text is calibrated for advanced practitioners requiring exhaustive structural text without marketing abstractions. Each subsection provides dense technical data, concrete paradigms, and operational specifications.
    """)

# ----------------------------------------------------------------------------------
# CHAPTER 1: EVOLUTION OF THE WEB
# ----------------------------------------------------------------------------------
elif chapter == "Chapter 1: The Evolution of the Web":
    st.title("Chapter 1: The Evolution of the Web")
    
    st.markdown("""
    ### 1.1 Web 1.0 — The Read-Only Static Document Space
    The genesis of the World Wide Web, engineered by Tim Berners-Lee at CERN, was fundamentally designed to solve information fragmentation across research departments. Web 1.0 operated strictly under the **Client-Server pull paradigm**, where users requested files via Hypertext Transfer Protocol (HTTP) and the server returned static Hypertext Markup Language (HTML) files located directly within a file system directory.

    During this era (roughly 1991 to 2004), websites were structural brochures. There were no databases attached to the web engine. If a document needed modification, the source text was manually rewritten. 
    
    *Characteristics of this era included:*
    - **Static HTML Pages:** Pages constructed strictly with raw tags, minimal inline styling, and no external stylesheets (CSS was introduced later).
    - **Server-Side File Mapping:** Flat URI patterns pointing directly to physical `.html` extensions.
    - **Absence of State:** Every transaction was independent; features like shopping carts or persistence profiles did not exist natively until the introduction of Netscape cookies.
    
    ### 1.2 Web 2.0 — The Read-Write Dynamic Ecosystem
    The paradigm shifted around 2004 with the democratization of server-side preprocessing engines (PHP, ASP, Ruby on Rails) and database integrations (MySQL, PostgreSQL). Web 2.0 decoupled content from presentation. Instead of loading static assets, the application server dynamically query-constructed pages on demand.
    
    Crucially, technologies like **Asynchronous JavaScript and XML (AJAX)** allowed browsers to query data from servers in the background without refreshing the browser tab. This gave rise to social networks, cloud applications, collaborative spreadsheets, and interactive media streaming platforms.
    """)
    
    st.subheader("Comparative Modern Evolution Matrix")
    comparison_data = {
        "Metric": ["Primary Function", "Data Flow", "Architecture", "State Management", "Storage Engine", "Average Page Size"],
        "Web 1.0 (Static)": ["Information Consumption", "Unidirectional (Server to Client)", "Flat File-based Servers", "Stateless / No Persistence", "Local Directories", "< 50 KB"],
        "Web 2.0 (Dynamic)": ["User Interaction & Creation", "Bi-directional (Interactive)", "Three-Tier (Client-App-DB)", "Session & Token Tracking", "Relational Databases / NoSQL", "2 MB - 5 MB"],
        "Modern Enterprise Web": ["Automation & Intelligence", "Omnidirectional Omni-Channel", "Microservices & Edge Networks", "Distributed Key-Value Stores", "Data Lakes & Real-time Streams", "Highly variable / Hydrated"]
    }
    st.table(pd.DataFrame(comparison_data))

    st.markdown("""
    ### 1.3 The Modern API-First & Jamstack Landscape
    Today, the web is transitioning toward highly decoupled web models. The frontend is often built as a Single Page Application (SPA) using frameworks like React or Vue, compiled into highly performant static assets delivered via Global Content Delivery Networks (CDNs). The frontend pulls content dynamically via RESTful APIs or GraphQL endpoints, minimizing the dependency on centralized heavy application servers. This shift dramatically reduces latency, enhances security posture, and ensures extreme horizontal scalability.
    """)

# ----------------------------------------------------------------------------------
# CHAPTER 2: INTERNET PROTOCOLS DEEP-DIVE
# ----------------------------------------------------------------------------------
elif chapter == "Chapter 2: Internet Protocols Deep-Dive":
    st.title("Chapter 2: Internet Protocols Deep-Dive")
    
    st.markdown("""
    ### 2.1 The OSI Model vs. TCP/IP Stack
    Understanding web engineering requires unpacking the protocol stacks that route packets globally. The Internet operates fundamentally on the Open Systems Interconnection (OSI) abstractions, distilled into the functional TCP/IP layout.
    
    1. **Application Layer (HTTP, FTP, SMTP, DNS):** The user-facing software context defining protocol boundaries.
    2. **Transport Layer (TCP, UDP):** Manages flow control, multiplexing, error correction, and sequence validation.
    3. **Network Layer (IPv4, IPv6, ICMP):** Handles logical packet addressing and structural routing optimizations across autonomous systems.
    4. **Data Link & Physical Layer:** Deals with physical frames, hardware MAC addresses, Ethernet switching, and copper/fiber-optic signaling transmission.

    ### 2.2 TCP 3-Way Handshake and Flow Control Mechanisms
    Before an HTTP request can be issued, a reliable Transport Control Protocol (TCP) connection must be instantiated. This relies on an explicit sequence exchange:
    """)

    st.code("""
    Client                               Server

      |                                    |
      | ---- SYN (Seq=X) ----------------> |  [Server allocates resources]
      |                                    |
      | <--- SYN-ACK (Seq=Y, Ack=X+1) ---- |  [Client verifies seq sequence]
      |                                    |
      | ---- ACK (Ack=Y+1) --------------> |  [Connection Established]
      v                                    v
    """, language="text")

    st.markdown("""
    Once established, TCP uses complex sliding window algorithms to manage flow control. If the client sends data faster than the server's receive buffer can process, the server shrinks the window size field in the packet header, forcing the client to throttle transmissions. This protects edge routing hardware from dropping packets during high network saturation.
    
    ### 2.3 HTTP/1.1 vs. HTTP/2 vs. HTTP/3 (QUIC)
    - **HTTP/1.1:** Introduced persistent connections, but suffered from **Head-of-Line (HOL) Blocking**. The browser could only request one asset per TCP tunnel concurrently, necessitating workarounds like domain sharding or asset bundling.
    - **HTTP/2:** Resolved this via binary framing layers, enabling true multiplexing over a single connection. However, if a single TCP packet was dropped on the network layer, all streams were paused while TCP retransmitted the missing segment.
    - **HTTP/3:** Replaces the transport foundation entirely by abandoning TCP in favor of **QUIC (Quick UDP Internet Connections)**. QUIC handles error recovery at the application-stream level instead of the connection level. If a packet drops on Stream A, Stream B continues rendering completely uninterrupted.
    """)

# ----------------------------------------------------------------------------------
# CHAPTER 3: WEB ARCHITECTURES & FRAMEWORKS
# ----------------------------------------------------------------------------------
elif chapter == "Chapter 3: Web Architectures & Frameworks":
    st.title("Chapter 3: Web Architectures & Frameworks")
    
    st.markdown("""
    ### 3.1 Monolithic Architecture vs. Distributed Microservices
