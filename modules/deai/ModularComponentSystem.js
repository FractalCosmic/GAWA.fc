// ModularComponentSystem.js
import React, { useState } from 'react';

// 基本组件
const Button = ({ onClick, children }) => (
  <button onClick={onClick}>{children}</button>
);

const Input = ({ value, onChange }) => (
  <input value={value} onChange={e => onChange(e.target.value)} />
);

const Dropdown = ({ options, value, onChange }) => (
  <select value={value} onChange={e => onChange(e.target.value)}>
    {options.map(option => (
      <option key={option.value} value={option.value}>
        {option.label}
      </option>
    ))}
  </select>
);

// 组件注册表
const componentRegistry = {
  button: Button,
  input: Input,
  dropdown: Dropdown,
};

// 动态组件渲染器
const DynamicComponent = ({ type, props }) => {
  const Component = componentRegistry[type];
  return Component ? <Component {...props} /> : null;
};

// 应用构建器
const AppBuilder = () => {
  const [components, setComponents] = useState([]);
  const [selectedType, setSelectedType] = useState('');

  const addComponent = () => {
    if (selectedType) {
      setComponents([...components, { type: selectedType, props: {} }]);
    }
  };

  return (
    <div>
      <select value={selectedType} onChange={e => setSelectedType(e.target.value)}>
        <option value="">Select component type</option>
        {Object.keys(componentRegistry).map(type => (
          <option key={type} value={type}>
            {type}
          </option>
        ))}
      </select>
      <button onClick={addComponent}>Add Component</button>
      <div>
        {components.map((component, index) => (
          <DynamicComponent key={index} {...component} />
        ))}
      </div>
    </div>
  );
};

export default AppBuilder;
