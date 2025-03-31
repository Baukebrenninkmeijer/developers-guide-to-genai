function VisibleTest() {
  return React.createElement(
    'div',
    {
      style: {
        width: '100%',
        height: '300px',
        padding: '30px',
        backgroundColor: 'red',
        color: 'white',
        fontSize: '36px',
        fontWeight: 'bold',
        textAlign: 'center',
        border: '10px solid yellow',
        position: 'relative',
        zIndex: 9999,
        display: 'block',
        opacity: 1,
        visibility: 'visible',
        transform: 'none'
      }
    },
    'THIS TEXT SHOULD BE VISIBLE',
    React.createElement(
      'p',
      {
        style: {
          margin: '20px 0',
          fontSize: '24px'
        }
      },
      'If you can see this, React is working!'
    )
  );
}

export default VisibleTest; 