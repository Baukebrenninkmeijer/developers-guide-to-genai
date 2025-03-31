import React from 'react';
import { milestones } from './timelineData';

export default function AITimeline() {
  return (
    <div style={{
      maxWidth: '100%',
      margin: '0 auto',
      padding: '10px',
      fontFamily: 'Segoe UI, Tahoma, Geneva, Verdana, sans-serif',
      color: '#e0e0e0'
    }}>
      <h2 style={{
        textAlign: 'center',
        marginBottom: '30px',
        color: '#fff',
        fontWeight: 600
      }}>Key Milestones in AI History (2012-2023)</h2>
      
      <div style={{
        position: 'relative',
        padding: '10px 0'
      }}>
        {milestones.map((milestone, index) => (
          <div key={index} style={{
            position: 'relative',
            marginBottom: '30px',
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'flex-start'
          }}>
            <div style={{
              position: 'absolute',
              width: '20px',
              height: '20px',
              left: '50%',
              transform: 'translateX(-50%)',
              borderRadius: '50%',
              zIndex: 2,
              backgroundColor: milestone.color
            }}></div>
            
            <div style={{
              position: 'absolute',
              width: '80px',
              textAlign: index % 2 === 0 ? 'right' : 'left',
              right: index % 2 === 0 ? 'calc(50% + 30px)' : 'auto',
              left: index % 2 === 1 ? 'calc(50% + 30px)' : 'auto',
              top: 0,
              fontWeight: 'bold',
              fontSize: '1.1rem',
              color: 'rgba(255, 255, 255, 0.8)'
            }}>{milestone.year}</div>
            
            <div style={{
              width: 'calc(50% - 50px)',
              padding: '15px',
              backgroundColor: 'rgba(30, 30, 40, 0.7)',
              borderRadius: '6px',
              boxShadow: '0 3px 10px rgba(0, 0, 0, 0.2)',
              marginLeft: index % 2 === 0 ? '80px' : 0,
              marginRight: index % 2 === 1 ? '80px' : 0,
              borderLeft: index % 2 === 0 ? `4px solid ${milestone.color}` : 'none',
              borderRight: index % 2 === 1 ? `4px solid ${milestone.color}` : 'none',
              textAlign: index % 2 === 1 ? 'right' : 'left'
            }}>
              <h3 style={{
                marginTop: 0,
                marginBottom: '8px',
                fontSize: '1.2rem',
                color: '#fff'
              }}>{milestone.title}</h3>
              <p style={{
                margin: 0,
                color: 'rgba(255, 255, 255, 0.7)',
                lineHeight: 1.4,
                fontSize: '0.9rem'
              }}>{milestone.description}</p>
            </div>
          </div>
        ))}
        
        <div style={{
          position: 'absolute',
          top: 0,
          bottom: 0,
          left: '50%',
          width: '4px',
          backgroundColor: 'rgba(255, 255, 255, 0.3)',
          transform: 'translateX(-50%)',
          zIndex: -1
        }}></div>
      </div>
    </div>
  );
} 