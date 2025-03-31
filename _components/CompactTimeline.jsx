import React from 'react';

const milestones = [
  { year: 2012, title: "AlexNet", color: "#4285F4" },
  { year: 2017, title: "Transformers", color: "#EA4335" },
  { year: 2018, title: "BERT", color: "#FBBC05" },
  { year: 2020, title: "GPT-3", color: "#34A853" },
  { year: 2021, title: "Diffusion", color: "#4285F4" },
  { year: 2022, title: "Multimodal", color: "#EA4335" },
  { year: 2023, title: "GPT-4", color: "#FBBC05" }
];

export default function CompactTimeline() {
  return (
    <div style={{
      display: 'flex',
      justifyContent: 'space-between',
      padding: '0 20px',
      position: 'relative',
      maxWidth: '100%',
      margin: '0 auto',
      color: '#ffffff',
      fontFamily: 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif'
    }}>
      {/* Horizontal line */}
      <div style={{
        position: 'absolute',
        top: '20px',
        left: '2%',
        right: '2%',
        height: '4px',
        background: 'rgba(255, 255, 255, 0.2)',
        zIndex: 0
      }}></div>
      
      {milestones.map((milestone, index) => (
        <div key={index} style={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          position: 'relative',
          zIndex: 1,
          width: '12%',
          transition: 'transform 0.3s ease'
        }}>
          <div style={{
            width: '20px',
            height: '20px',
            borderRadius: '50%',
            marginBottom: '10px',
            backgroundColor: milestone.color
          }}></div>
          <div style={{
            fontWeight: 'bold',
            fontSize: '1rem',
            marginBottom: '5px',
            color: 'rgba(255, 255, 255, 0.9)'
          }}>{milestone.year}</div>
          <div style={{
            fontSize: '0.9rem',
            fontWeight: 600,
            marginBottom: '5px',
            textAlign: 'center',
            color: 'rgba(255, 255, 255, 0.9)'
          }}>{milestone.title}</div>
        </div>
      ))}
    </div>
  );
} 