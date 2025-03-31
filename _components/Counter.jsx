function Counter() {
  // Use React's useState hook with proper variable declaration
  const countState = React.useState(0);
  const count = countState[0];
  const setCount = countState[1];

  return React.createElement(
    'div',
    {
      style: {
        padding: '20px',
        backgroundColor: 'rgba(0, 100, 200, 0.3)',
        color: 'white',
        borderRadius: '8px',
        textAlign: 'center',
        margin: '20px'
      }
    },
    React.createElement('h3', null, 'React Counter Test'),
    React.createElement('p', null, 'Count: ' + count),
    React.createElement(
      'button',
      {
        onClick: function() { setCount(count + 1); },
        style: {
          padding: '8px 16px',
          margin: '10px',
          backgroundColor: '#4CAF50',
          color: 'white',
          border: 'none',
          borderRadius: '4px',
          cursor: 'pointer'
        }
      },
      'Increment'
    )
  );
}

export default Counter; 