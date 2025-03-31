function TestComponent() {
  return React.createElement(
    'div',
    {
      style: {
        padding: '20px',
        backgroundColor: 'rgba(255, 0, 0, 0.3)',
        color: 'white',
        borderRadius: '8px',
        textAlign: 'center',
        margin: '20px',
        fontSize: '24px'
      }
    },
    'This is a test component to verify React rendering works!'
  );
}

export default TestComponent; 