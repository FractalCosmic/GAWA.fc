// components/Button.js
import React from 'react';
import styled from 'styled-components';

const StyledButton = styled.button`
  padding: 10px 20px;
  font-size: ${props => props.theme.fontSize.medium};
  color: ${props => props.theme.colors.text};
  background-color: ${props => props.theme.colors.primary};
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;

  &:hover {
    background-color: ${props => props.theme.colors.primaryHover};
  }

  @media (max-width: ${props => props.theme.breakpoints.mobile}) {
    width: 100%;
  }
`;

const Button = ({ children, onClick }) => (
  <StyledButton onClick={onClick}>{children}</StyledButton>
);

export default Button;

// components/Input.js
import React from 'react';
import styled from 'styled-components';

const StyledInput = styled.input`
  padding: 10px;
  font-size: ${props => props.theme.fontSize.medium};
  color: ${props => props.theme.colors.text};
  background-color: ${props => props.theme.colors.background};
  border: 1px solid ${props => props.theme.colors.border};
  border-radius: 4px;
  width: 100%;
  box-sizing: border-box;

  &:focus {
    outline: none;
    border-color: ${props => props.theme.colors.primary};
  }
`;

const Input = ({ type = 'text', placeholder, value, onChange }) => (
  <StyledInput 
    type={type} 
    placeholder={placeholder} 
    value={value} 
    onChange={onChange} 
  />
);

export default Input;

// components/Card.js
import React from 'react';
import styled from 'styled-components';

const StyledCard = styled.div`
  background-color: ${props => props.theme.colors.background};
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 20px;
  margin-bottom: 20px;

  @media (max-width: ${props => props.theme.breakpoints.mobile}) {
    padding: 15px;
  }
`;

const Card = ({ children }) => (
  <StyledCard>{children}</StyledCard>
);

export default Card;
