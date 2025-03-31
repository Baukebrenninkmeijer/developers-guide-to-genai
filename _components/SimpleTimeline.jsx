const milestones = [
  { year: 2012, title: "AlexNet" },
  { year: 2017, title: "Transformers" },
  { year: 2018, title: "BERT" },
  { year: 2020, title: "GPT-3" },
  { year: 2021, title: "Diffusion Models" },
  { year: 2022, title: "Multimodal Models" },
  { year: 2023, title: "GPT-4" }
];

function SimpleTimeline() {
  return React.createElement(
    'div',
    {
      style: {
        maxWidth: '800px',
        margin: '0 auto',
        padding: '20px',
        backgroundColor: 'rgba(0, 0, 0, 0.7)',
        color: 'white',
        borderRadius: '8px'
      }
    },
    React.createElement('h2', { style: { textAlign: 'center' } }, 'Key AI Milestones'),
    React.createElement(
      'ul',
      null,
      milestones.map(function(item, index) {
        return React.createElement(
          'li',
          { key: index, style: { margin: '10px 0' } },
          React.createElement('strong', null, item.year + ':'),
          ' ' + item.title
        );
      })
    )
  );
}

export default SimpleTimeline; 