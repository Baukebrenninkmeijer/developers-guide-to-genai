const milestones = [
  {
    year: 2012,
    title: "AlexNet",
    description: "Deep CNN architecture that won ImageNet competition, sparking the deep learning revolution"
  },
  {
    year: 2017,
    title: "Transformers",
    description: "Google introduces 'Attention is All You Need' paper, establishing transformer architecture"
  },
  {
    year: 2018,
    title: "BERT",
    description: "Bidirectional Encoder Representations from Transformers by Google - revolutionized NLP"
  },
  {
    year: 2020,
    title: "GPT-3",
    description: "OpenAI's 175B parameter model demonstrates remarkable few-shot learning capabilities"
  },
  {
    year: 2021,
    title: "Diffusion Models",
    description: "DALL-E, Stable Diffusion and Midjourney bring text-to-image generation to the mainstream"
  },
  {
    year: 2022,
    title: "Multimodal Models",
    description: "Models like CLIP and Flamingo enable understanding across text, images, and other modalities"
  },
  {
    year: 2023,
    title: "GPT-4",
    description: "OpenAI's multimodal model demonstrates near-human performance across various tasks"
  }
];

function AITimeline() {
  return React.createElement(
    'div',
    { style: { 
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
      { style: { listStyleType: 'none', padding: 0 } },
      milestones.map((item, index) => 
        React.createElement(
          'li', 
          { key: index, style: { margin: '10px 0', padding: '10px', backgroundColor: 'rgba(50, 50, 60, 0.5)', borderRadius: '4px' } },
          React.createElement('strong', null, item.year + ': '),
          React.createElement('span', null, item.title),
          React.createElement('p', { style: { margin: '5px 0 0 0', fontSize: '0.9em', opacity: 0.8 } }, item.description)
        )
      )
    )
  );
}

export default AITimeline; 