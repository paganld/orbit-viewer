# Project Orbitviewer: Initial Proposal

**Project Name:** Orbitviewer
**Mandate:** Create a GEOINT platform inspired by `Shadowbroker`, but with a unique value proposition leveraging advanced AI models.

### **Analysis of `Shadowbroker`**

*   **Mission:** A real-time, multi-domain OSINT (Open-Source Intelligence) dashboard that aggregates dozens of public data feeds onto a single map.
*   **Core Technologies:**
    *   **Frontend:** Next.js with MapLibre GL (a high-performance map renderer).
    *   **Backend:** FastAPI (a modern Python web framework).
    *   **Deployment:** Fully containerized with Docker/Podman and supports Helm for Kubernetes.
*   **Data Sources:** It's a masterclass in data aggregation, pulling from OpenSky (flights), aisstream.io (ships), CelesTrak (satellites), USGS (earthquakes), GDELT (conflict events), NASA, NOAA, and many more.
*   **Key Features:** It tracks aircraft (commercial, private, military), ships, satellites, conflict zones, CCTV networks, GPS jamming, and even has a live radio tuner for public SDR receivers.

### **Proposed Differentiators for Orbitviewer**

`Shadowbroker` is a comprehensive data visualization tool. Our opportunity is to build an AI-native intelligence *analysis* tool.

**Recommendation: The "Why" Engine**

This approach plays to our strengths (access to powerful LLMs like Gemini 2.5 Pro) and offers a truly unique value proposition.

*   **Concept:** Instead of just showing *what* is happening, Orbitviewer will focus on *why* it might be happening. The system will ingest not just telemetry data, but also unstructured text from global news feeds, aviation/maritime alerts (NOTAMs/HYDROPACs), and even curated social media channels.
*   **Unique Feature:** An AI-powered correlation engine. A user could click on an asset (e.g., an aircraft, a ship) and get a real-time, LLM-generated intelligence summary.
    *   *Example 1:* User clicks a military tanker that has diverted. The panel shows: *"This KC-135 Stratotanker diverted towards the Black Sea 25 minutes ago. This coincides with a NOTAM for a drone exercise in the area and increased chatter from naval observers on Twitter."*
    *   *Example 2:* User clicks on a cluster of cargo ships stopped outside a port. The panel shows: *"Five container ships are anchored outside the Port of Singapore. This follows a report from Lloyd's List 2 hours ago detailing a temporary channel blockage due to a grounded vessel."*
*   **What's Different:** We move from being a data visualizer to an AI-powered intelligence analyst.

**Other Ideas Considered:**
*   **"Pattern of Life" Analyzer:** Focus on historical data to automatically flag anomalies. (Strong second choice, could be a future feature).
*   **Immersive 3D Globe (CesiumJS):** Compete on UI/UX with a true 3D interface. (Higher development cost, less unique from a data perspective).

### **Next Steps**

1.  Review this proposal.
2.  Finalize the core concept.
3.  Resolve the GitHub token write-permission issue.
4.  Begin creating the high-level architecture for the AI correlation engine.
