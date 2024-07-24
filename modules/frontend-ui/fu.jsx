import React, { useState } from 'react';

const Button = ({ onClick, children }) => (
  <button onClick={onClick}>{children}</button>
);

const Input = ({ value, onChange }) => (
  <input value={value} onChange={e => onChange(e.target.value)} />
);

const Form = () => {
  const [inputValue, setInputValue] = useState('');

  const handleSubmit = () => {
    console.log('Submitted:', inputValue);
    setInputValue('');
  };

  return (
    <div>
      <Input value={inputValue} onChange={setInputValue} />
      <Button onClick={handleSubmit}>Submit</Button>
    </div>
  );
};

export { Button, Input, Form };
