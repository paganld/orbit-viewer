// src/app/page.tsx
import React from 'react';

// We will eventually replace this with a dynamic, server-side component
// that loads the map component only on the client.
import MapViewer from '../components/MapViewer'; 

const Home = () => {
  return (
    <main style={{ display: 'flex', height: '100vh', width: '100vw', margin: 0, padding: 0, backgroundColor: '#1a1a1a', fontFamily: 'sans-serif' }}>
      
      {/* Left Panel: Layer controls, filters, etc. */}
      <div style={{ width: '300px', backgroundColor: '#242424', color: 'white', padding: '1rem', overflowY: 'auto' }}>
        <h2 style={{ margin: 0, marginBottom: '1rem' }}>Orbitviewer</h2>
        <p>Controls and layers will be here.</p>
        {/* Placeholder for layer toggles and other controls */}
      </div>

      {/* Main Content: The Map */}
      <div style={{ flex: 1, position: 'relative' }}>
        <MapViewer />
      </div>

      {/* Right Panel: SIGINT feeds, entity details, etc. */}
      <div style={{ width: '350px', backgroundColor: '#242424', color: 'white', padding: '1rem', overflowY: 'auto' }}>
        <h3 style={{ margin: 0 }}>Intelligence Feed</h3>
        {/* Placeholder for news feeds, dossier info, etc. */}
      </div>

    </main>
  );
};

export default Home;
